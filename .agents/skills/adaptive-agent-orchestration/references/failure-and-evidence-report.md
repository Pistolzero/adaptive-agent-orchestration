# Required delegate disclosure and evidence contract

Use this report at the end of **every** delegated task. The main agent provides the concrete task-specific acceptance criteria in the brief. No unreported failures: an unsuccessful or partially successful operation belongs in the report even if later fixed. Do not include secrets or raw personal data in logs.

```text
TASK_ID: <stable ID>
ROLE_INSTANCE: <role + instance index>
MODEL_EFFORT: <actual resolved model/effort, or not observable>
STATUS: COMPLETE | PARTIAL | BLOCKED | FAILED
SCOPE: <exact task/files/allowed changes>
COMPLETED: <what was actually done; reference artifacts>
NOT_DONE: <every omitted/incomplete step; why; none if complete>
ATTEMPTS_AND_ERRORS: <attempt -> error/observed problem -> remedy -> final outcome; none if no failures>
UNRUN_OR_FAILED_CHECKS: <tests not run, failing tests, reasons and severity; none if fully passing>
EVIDENCE: <exact source/path/line/test command and result for each material claim>
MODIFICATIONS: <created/changed/deleted files; none if unchanged>
ASSUMPTIONS_AND_UNCERTAINTIES: <claims not verified; none if verified>
RISKS_OR_SIDE_EFFECTS: <including unexpected effects; none if none observed>
ACCEPTANCE_CHECKLIST: <criterion -> pass/fail/not-tested -> evidence>
NEEDS_MAIN_AGENT_DECISION: <precise question or none>
SUGGESTED_NEXT_ACTION: <one next step, or none>
```

If any required evidence or acceptance criterion is missing, STATUS may not be `COMPLETE` unless the original brief explicitly marked it optional. A successful retry does not erase an earlier failed attempt. Use `not observable` rather than invent actual model or token usage.

## Main-agent audit

1. Compare output fields to the original brief. Check counts and file ownership.
2. Inspect a relevant source sample, modified-file diff and test result. Verify key claims independently where feasible.
3. Reconcile `COMPLETED` with `NOT_DONE`, `ATTEMPTS_AND_ERRORS`, `UNRUN_OR_FAILED_CHECKS` and `ACCEPTANCE_CHECKLIST`.
4. If report is incomplete, ask a **single targeted** question of that same agent or inspect its thread; do not mark completion.
5. A report alone cannot ensure truthful disclosure. Where high confidence is required, use deterministic checks, tool logs, diffs and independent targeted review.
