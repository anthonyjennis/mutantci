# Roadmap

Now: the 15-hour core (graded). Next: 10 hours of stretch, in order, only once the core is merged
and deployed. Later: after grading, toward a portfolio-grade project.

## Core — 15 h, target Oct 14–21

| # | Task | Owner | h | Done when |
| --- | --- | --- | --- | --- |
| 1 | Repo, protected `main`, Docker installed on both laptops | Both | 1 | Both push a branch; `docker run hello-world` works |
| 2 | Strong + weak tests (humans, first), then `core/rules.py`: free shipping, GST slab, discount tier | P1 | 2 | Both suites at 100% coverage |
| 3 | Run mutmut on both suites | P1 | 1 | Weak ~40–50%, strong ≥ 80%; scores in README |
| 4 | FastAPI app, one endpoint (fee, tax, discount for an order total) + one API test | P1 | 1 | Works locally |
| 5 | Dockerfile (python-slim, non-root) + local build and run | P2 | 1.5 | Container serves the endpoint |
| 6 | Workflow: ruff + pytest with coverage | P2 | 1.5 | Green on a PR; required by branch protection |
| 7 | `scripts/mutation_gate.py` reading `.mutation-threshold` | P1 | 1 | Fails on weak suite, passes on strong |
| 8 | Workflow: mutation gate job inside the Docker image | P2 | 1 | Runs on every PR after tests |
| 9 | Build and push image to ghcr.io, tagged with commit SHA | P2 | 1 | Image under the repo's Packages |
| 10 | Deploy to Render on merge to `main` | P2 | 1.5 | Merged PR updates the live URL |
| 11 | Demo PR: swap a strong test for a lazy one | Both | 0.5 | Merge blocked; screenshot saved |
| 12 | README: problem, each stage, rubric mapping, screenshots | P1 | 1 | Every rubric item points to a section |
| 13 | Record demo video | Both | 1 | Linked in README |

## Stretch — 10 h, in priority order

| # | Task | Owner | h |
| --- | --- | --- | --- |
| S1 | Surviving mutants in the job summary; full report as an artifact | P2 | 1.5 |
| S2 | Architecture and pipeline diagram | P1 | 1 |
| S3 | Mutation lab lite: static page of source, mutants, score vs coverage, from a CI-produced JSON | P1 | 3.5 |
| S4 | pip and Docker layer caching in the workflow | P2 | 1 |
| S5 | Trivy image scan, fail on critical vulnerabilities | P2 | 1 |
| S6 | Move deployment from Render to Azure | P2 | 2 |

## Later — after grading (from the original 84 h scope; not estimated yet)

- Live mutation lab: run mutmut on demand from the UI, highlight each mutant's changed line
- Weak/strong suite toggle in the UI; precomputed-results fallback for slow servers
- Larger, more realistic rules module
- Mutation score history across PRs (a trend, not just a gate)
- Write-up for the portfolio: problem, design decisions (from DECISIONS.md), results
