# How we work

For both teammates. Nothing here requires Claude Code: if you work without it, follow the same
loop and write the WORKLOG entry yourself.

## Which tool for what

| Use | For | Why |
| --- | --- | --- |
| **claude.ai Project chat** | Understanding a concept before a task (images vs containers, what a runner is); asking "why" about a diff; design choices; the report and viva prep | No repo needed; explanation-first; the Project keeps the context |
| **Claude Code, in the repo** | Anything that edits or runs repo files: code, Dockerfile, workflow YAML, `check.sh`, debugging a failed CI run | It runs the command, reads the error and fixes it in one loop. Chat can only guess at your error |
| **Your own hands** | Writing the tests; reading every diff; merging PRs; anything you'd be asked about in the viva | The grade, and the resume claim, are yours |

Rule of thumb: if you're asking *what* or *why*, use chat. If you're asking *do*, use Claude Code.

## The session loop (one task per session)

1. Pick the next task in `docs/ROADMAP.md`. If its concept is new to you, spend 10 minutes in chat first.
2. Open Claude Code in the repo. CLAUDE.md, the worklog and decisions load automatically.
3. Say the task number. Use plan mode: read the plan, push back, approve.
4. Claude implements and runs `scripts/check.sh` until it passes (`docs/CHECKS.md`).
5. Ask Claude to walk you through the diff. Don't commit a line you can't explain.
6. Commit on the task branch, open a PR, and let CI decide.
7. Claude adds the WORKLOG entry. Start the next task in a fresh session (`/clear`).

## Habits worth keeping

- Write the test before the code, by hand. It's the part the project is about.
- When CI fails, paste the failing log into Claude Code rather than describing it.
- Screenshot each stage the first time it goes green. The README needs them.
- If `CLAUDE.md` didn't stop a repeated mistake, add one concrete line to it, not a paragraph.
