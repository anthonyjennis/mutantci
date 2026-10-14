# MutantCI

A CI/CD pipeline whose signature stage is a mutation-testing gate: a pull request cannot merge if
mutmut's mutation score on `core/` falls below the threshold. The app is deliberately tiny. The
pipeline is the product.

This is a graded university project (DevOps Lab CA) that will also go on a resume. The two humans
on it are new to Docker and GitHub Actions, and must be able to explain every line in a viva.

## Current state

@WORKLOG.md
@docs/DECISIONS.md

Task list (core 1–13, stretch S1–S6, later): `docs/ROADMAP.md`. Definition of done: `docs/CHECKS.md`.

## Layout

Some of these are created by core tasks 1–10. If something below doesn't exist yet, say so rather
than inventing a substitute.

```
core/rules.py              pricing rules under test. Keep under ~80 lines: every line adds mutants
tests/strong/              boundary-focused tests; must keep the mutation score at or above threshold
tests/weak/                DELIBERATELY weak tests used in the demo. Never edit
app/main.py                FastAPI app, one endpoint
scripts/check.sh           the one command that decides whether work is done
scripts/mutation_gate.py   reads mutmut results, exits non-zero below the threshold
.mutation-threshold        the gate threshold (single source for local runs and CI). Never edit
Dockerfile
.github/workflows/ci.yml
```

## Commands

```
./scripts/check.sh                                      # everything; must pass before "done"
pytest tests/strong --cov=core --cov-report=term-missing
docker build -t mutantci . && docker run --rm -p 8000:8000 mutantci
```

mutmut runs inside the Docker image or WSL, never on native Windows.

## Hard rules

- Never edit `tests/weak/` or `.mutation-threshold`. Both are also blocked in `.claude/settings.json`.
  If a task seems to need it, stop and ask.
- Never make a gate pass by lowering the threshold, excluding files from mutation, adding
  no-mutate pragmas, skipping or xfail-ing tests, or deleting assertions. Fix the code, or ask.
- Tests come from the spec, before the code. Never change an existing test to make code pass; if a test looks wrong, stop and ask.
- No secrets in the repo. Registry and deploy credentials live only in GitHub Actions secrets.

## How to work

- One task per session, from `docs/ROADMAP.md`. Start in plan mode: name the task, the files you
  will touch, and how you will verify it. Wait for approval before editing.
- Explain step by step with the reasoning, especially for Docker and GitHub Actions. No large
  silent diffs. After implementing, walk through the diff so the human can explain every line.
- Keep diffs small and limited to the files the task needs.
- Done means: `scripts/check.sh` passes, the task's "done when" is met, and the review list in
  `docs/CHECKS.md` is answered. Report the actual command output, not a claim.
- If a check fails, fix and rerun. After three failed attempts on the same error, stop and
  summarise what you tried and what you suspect.
- End of session: add a `WORKLOG.md` entry (format at the top of that file). Add a
  `docs/DECISIONS.md` entry for any choice someone might later ask "why?" about.
- Git: one branch per task (`task-07-score-script`), conventional commits (`feat:`, `fix:`,
  `test:`, `ci:`, `docs:`, `chore:`), PR into `main`. Don't push or open PRs unless asked.
