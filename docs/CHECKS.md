# Checks — the definition of done

A task is done only when all three levels pass. Level 1 is a machine verdict, so it comes first:
nobody, human or Claude, gets to grade their own work by opinion when a command can do it.

## Level 1 — `scripts/check.sh` (automated, must exit 0)

Built during core tasks 2–8. Until a step exists, the script prints `SKIP <step>` for it.

| Step | Passes when |
| --- | --- |
| Lint | `ruff check .` reports nothing |
| Strong tests | all pass |
| Coverage | `core/` has 100% line coverage under the strong suite **and** under the weak suite |
| Mutation gate | strong-suite score ≥ the value in `.mutation-threshold` |
| Demo still works | weak-suite score is **below** the threshold. If the weak suite ever passes, the demo is broken |
| Docker build | image builds |
| Smoke test | container starts and the endpoint returns 200 with the expected JSON |

CI runs the same steps except the weak-suite run (it doubles mutation time).

## Level 2 — the task's "done when"

Each task in `docs/ROADMAP.md` has one observable result (a red PR, a live URL, a package on
ghcr.io). Show it: command output, a screenshot path, or a link.

## Level 3 — review (Claude answers first, a human has the final say)

- [ ] Did the diff touch only files this task needs?
- [ ] Did any change weaken a gate? (threshold, skipped tests, mutation exclusions, deleted assertions)
- [ ] Any secret, token or personal path committed?
- [ ] Is anything in README or docs now wrong because of this change?
- [ ] WORKLOG entry added; DECISIONS entry added if a choice was made?
- [ ] **Human only:** can I explain every changed line, and why it's there, without notes?

## Assignment rubric (tick as each is demonstrable)

- [ ] Version control with Git/GitHub (branches, PRs, protected `main`)
- [ ] Application build
- [ ] Automated testing (unit tests, coverage, mutation gate)
- [ ] Containerisation with Docker
- [ ] CI/CD pipeline with GitHub Actions
- [ ] Deployment to a suitable environment
- [ ] Project documentation
- [ ] Working pipeline demonstrated (demo video)
