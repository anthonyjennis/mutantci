
#!/usr/bin/env bash
# The one command that decides whether work is done.
# Runs every check in order and stops at the first failure.
set -euo pipefail
cd "$(dirname "$0")/.."

step() { printf '\n==> %s\n' "$1"; }

step "Lint"
ruff check .

step "Strong suite: tests pass, 100% coverage of core/"
pytest tests/strong -q --cov=core --cov-report=term-missing --cov-fail-under=100

step "Weak suite: tests pass, 100% coverage of core/ (demo setup)"
pytest tests/weak -q --cov=core --cov-report=term-missing --cov-fail-under=100

step "API tests"
pytest tests/api -q

step "Mutation gate: strong suite must reach the threshold"
python scripts/mutation_gate.py --suite strong

step "Demo sanity: weak suite must stay below the threshold"
python scripts/mutation_gate.py --suite weak --expect-below

if command -v docker >/dev/null 2>&1 && docker info >/dev/null 2>&1; then
  step "Docker: build image and smoke-test it"
  docker build -q -t mutantci:check . >/dev/null
  cid=$(docker run -d -p 8000:8000 mutantci:check)
  trap 'docker rm -f "$cid" >/dev/null' EXIT

  body=""
  for _ in $(seq 1 30); do
    if body=$(curl -fsS -X POST \
      -H "Content-Type: application/json" \
      -d '{"total":500}' \
      "http://localhost:8000/quote" 2>/dev/null); then
      break
    fi
    sleep 0.5
  done

  echo "${body:-no response}"

  if [ -z "$body" ]; then
    docker logs "$cid"
    echo "FAIL: Docker container did not respond"
    exit 1
  fi

  echo "$body" | grep -q '"shipping_fee":0' || {
    echo "FAIL: Docker smoke test: $body"
    exit 1
  }
else
  step "Docker: SKIP (Docker is not running)"
fi

printf '\nALL CHECKS PASSED\n'
