# Delegation brief templates

Use the smallest template that fully specifies the task. Main agent provides concrete fields; never leave placeholders to a delegate if their values are known.

## Universal brief (mandatory fields)

**Task ID and title:**
**Role / permitted model and effort:**
**Why needed:**
**Objective (single question or artifact):**
**Known facts (with supporting sources):**
**Inputs (exact files/paths/URLs/slices):**
**Excluded scope and forbidden changes:**
**Permitted tools / write permissions:**
**Steps (ordered):**
**Acceptance criteria:**
**Edge cases / failure / stop conditions:**
**Output (strict format and maximum useful length):**
**Dependencies / what the main agent will decide later:**

### Mandatory final report contract

Use the complete [failure-and-evidence-report.md](failure-and-evidence-report.md) schema. Every field is required. Failed operations, skipped steps, unrun tests and unresolved risks must be disclosed, even when a later attempt succeeds. Give per-instance IDs when parallel copies of a role are spawned.

## Small/bulk delegate — explicit and mechanical

- Give the input schema and 2–3 examples, including malformed or ambiguous records.
- Enumerate allowed normalizations, rejected inputs, tie-breaking rules and output column names.
- Process bounded batches. Return exact counts (read/accepted/rejected/ambiguous).
- Never infer missing data or invent criteria. Put ambiguous cases in a separate list.
- Run a spot check against source records; show the sample method.
- Stop if input schema deviates substantially, instead of guessing.

**Example:** "Read only files A and B. Normalize ISO dates into YYYY-MM-DD, preserve original values in `date_original`, reject ambiguous day/month formats, produce a CSV plus 10 sampled checks, and do not edit inputs."

## Bounded research delegate — precise sources and validation

- State the exact question, time/version range and required source hierarchy.
- Ask for direct evidence, authoritative URLs, dates, and reasons for confidence.
- Separate verified fact from plausible hypothesis; report contradictions and inaccessible sources.
- Set a focused search budget (e.g. 3–5 high-value searches before reassessing) rather than endless browsing.
- Explicitly prohibit making system changes or executing downloaded code.

**Example:** "For framework version X, verify whether API Y supports parameter Z. Prefer official versioned docs; provide direct quotations only when permitted, links and the exact version, plus unsupported/unknown cases."

## Builder/debugging delegate — detailed ordered implementation

- Give the user-visible behavior, scope and exact file ownership.
- Include reproduction, minimal changes, existing conventions, tests and rollback.
- Require a before/after diff, targeted tests, and report of failing or unrun tests.
- Prohibit unrelated refactoring, dependencies, hidden config changes and deleting user data.
- If a decision involves architecture, authorization, production risk or contradictory requirements, stop and hand it to the main agent.

**Example:** "Only edit `src/parser.py` and `tests/test_parser.py`. Reproduce the named failure, adjust the smallest parser branch, add both a positive and malformed-case test, run those tests, return diff summary and any failures. Do not install packages."

## Independent reviewer — skepticism and checkable findings

- Provide the actual requirement, output/diff, relevant tests and risk criteria.
- Review **what exists**; do not assume the builder succeeded or failed.
- Focus on correctness, security, regressions, missing cases and missing evidence.
- Rank by severity; reference exact files/lines; avoid generic praise or stylistic noise.
- By default do not edit; return acceptance decision plus changes needed for acceptance.

## Brief quality check before spawning

1. Can the delegate act without guessing the success condition?
2. Does it know which files it owns and which it must not touch?
3. Are exceptions and missing-source behavior specified?
4. Are sources and evidence expectations explicit?
5. Is the response short enough for the main agent to verify quickly?
6. Is the selected model capable of the requested level of independent judgment?

If any answer is no, improve the brief **before** spending delegate tokens.
