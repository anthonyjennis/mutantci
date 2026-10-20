# Worklog

Session handoff notes, newest first. Git already records *what* changed; this records where we
stopped and what comes next, so the next session (human or Claude, either teammate) starts in
under a minute.

Rules:
- One entry per working session, at most ~6 lines.
- Link the commit or PR instead of describing the diff.
- Decisions go in `docs/DECISIONS.md`; just reference the ID here.
- Keep the last ~10 entries. Roll older ones into one line under "Earlier".

Format:

```
## YYYY-MM-DD · who · task N
Done: one line (+ commit/PR link)
Checks: check.sh pass/fail, strong score X%, weak score Y%
Decisions: D-00N (if any)
Blocked: anything stuck, or "nothing"
Next: the very next action
```

---

## 2026-10-14 · Anthony + Claude (chat) · setup
Done: added CLAUDE.md, WORKLOG.md, docs/ (ROADMAP, DECISIONS, CHECKS, WORKFLOW), .claude/settings.json, .mutation-threshold
Checks: n/a (no code yet)
Decisions: D-001 to D-007 recorded
Blocked: nothing
Next: task 1 — create the repo, protect `main`, install Docker on both laptops
