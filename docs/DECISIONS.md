# Decisions

Short records of choices someone might later ask "why?" about (the examiner, an interviewer, or
us in three months). Newest at the bottom. Status is Accepted, Proposed, or Superseded by D-00N.

---

**D-001 · 2026-10-07 · Accepted — Mutation testing tool: mutmut**
Why: Python-native, runs from the CLI, easy to wire into CI.
Considered: cosmic-ray (more setup than a 15-hour scope allows).

**D-002 · 2026-10-07 · Accepted — Core deploys to Render's free tier; Azure moves to stretch S6**
Why: the core budget for deployment is 1.5 h, and Render needs no infrastructure setup.
Watch out: free Render services sleep when idle. Open the URL a minute before any demo.
Considered: Azure for Students (more realistic, but 3–6 h for first-timers).

**D-003 · 2026-10-07 · Accepted — The live mutation lab UI is out of the core**
Why: live runs need a runner, timeouts and a slow-server fallback (about 21 h). Stretch S3 is a
static page reading results produced in CI instead.

**D-004 · 2026-10-07 · Accepted — mutmut runs inside the Docker image, locally and in CI**
Why: same environment everywhere; sidesteps mutmut's lack of native Windows support.

**D-005 · 2026-10-14 · Accepted — Gate threshold is 80%, stored once in `.mutation-threshold`**
Why: the strong suite targets 80% or more and the weak suite about 40–50%, a clear gap for the
demo. One file means local checks and CI can never disagree.

**D-006 · 2026-10-14 · Accepted — Tests are written from the spec, before the code**
Why: test quality is the subject of the project. Writing tests from the agreed spec before
`core/rules.py` exists stops them mirroring the implementation. Claude drafted the tests;
both of us review every case.

**D-007 · 2026-10-14 · Proposed — Claude Code for repo work; claude.ai Project chat for learning and review**
Why: Claude Code can run tests, Docker and git in a tight edit-run-fix loop. Chat is better for
understanding a concept before a task and for writing the report. See `docs/WORKFLOW.md`.
