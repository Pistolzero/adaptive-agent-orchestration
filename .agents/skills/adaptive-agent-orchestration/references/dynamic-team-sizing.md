# Dynamic team sizing

Choose whether to delegate at all. The skill proposes staffing; it does not itself create or schedule agents. Apply [budget-policy.md](budget-policy.md) **before** each wave.

1. Enumerate only independent, ready units with distinct deliverables, input scopes, acceptance checks and output files.
2. Compute candidates = minimum of ready units, observed available concurrency, and budget-profile cap. If concurrency is unknown, do not exceed one new delegate by default.
3. Reduce candidates if brief creation, duplicated context and verification likely exceed the work saved. Zero is a valid answer.
4. You may instantiate the **same role** multiple times for disjoint partitions, each with a unique task ID and report. Never grant overlapping write scope. A second opinion on the same evidence is allowed only when intentionally requested or justified by high risk.
5. Start with <= 2 when profile permits, review outputs, then decide if another wave is worthwhile.
6. If tasks depend on each other, finish prerequisites first. Cancel superseded branches if runtime supports safe cancellation.
7. Honor system/user limits. Never try to bypass provider quotas or hide actual usage.

| Situation | Suggested plan |
|---|---|
| Single clear modification | Main agent, no subagent |
| Five unrelated research questions, BALANCED | 1–2 focused researchers, then another wave if needed |
| Thirty independent files, QUALITY | Up to 3 scoped same-role analysis instances, one partition per instance |
| Sensitive production deployment | Main controls approval; subagents evidence-only |
| UNKNOWN budget | 0–1 delegate, no speculative large parallel team |
| CRITICAL | No new delegates; checkpoint |

For the final answer, record **how many actually ran** and which were blocked; do not confuse planned with completed.
