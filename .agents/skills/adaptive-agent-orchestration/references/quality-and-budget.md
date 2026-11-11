# Quality, time and cost measurement

Read [budget-policy.md](budget-policy.md) first for quota awareness and conservative defaults. Optimize for a *correctly accepted deliverable*, not number of spawned agents.

## Minimal ledger (only when available)
- Budget snapshot: source, captured time, applicable model/window, remaining relevant allowance, or UNKNOWN.
- User budget preference and chosen profile.
- Parent model/effort; actual child model/effort **if visible**.
- Planned and actual agents, task partitions, retry count, concurrent count.
- Time until accepted result, model tokens if surfaced, tool calls if observable.
- Evidence for acceptance: tests, citations, diffs, and unresolved failures.

If metrics cannot be observed, write **NOT OBSERVABLE** rather than inventing estimates. A percentage remaining is not a token balance. A fast parallel execution may use more tokens overall.

## Reliability beats fake thrift
- No repeated full-context distribution to several agents.
- No parallel edits of the same file.
- One targeted retry at most; after that escalate or stop with unresolved status.
- Reserve verification capacity by dropping nonessential branches first. Do not declare COMPLETE with required checks unrun.
- If budget is critical, checkpoint and end safe at the present stage; do not claim background work.

## Comparative evaluation
A claim of better cost or speed needs a genuinely comparable baseline: same input, same acceptance criteria, similar conditions, measured total consumption and elapsed time. Otherwise report observed current performance only, not percentage savings.

## Final audit checklist
1. Correctness backed by source/test evidence?
2. Completeness: all required checks passed, failed or explicitly unrun?
3. Permissions/secret-handling respected?
4. Which files did each agent touch?
5. Are model selection and quota source actually observable?
6. Did another delegate repeat the same work without reason?
7. Is the reported efficiency evidence-based?
