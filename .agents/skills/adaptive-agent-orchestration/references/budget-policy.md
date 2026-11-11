# Budget-aware routing and usage limits

This policy answers **how to adjust delegation in light of the available usage allowance**. It does not provide a guaranteed way to read another user's current usage. Codex quota is not a universal wallet of tokens: the relevant allowance may differ by model, time window, product, credit balance, organization setting or rate limit.

## 1. Trustworthy budget inputs

Accept (in priority order):

1. A **fresh official usage indicator** exposed by the active session/host, including which model/window it covers; do not assume programmatic access exists.
2. An explicitly user-supplied official usage snapshot (`/status` or dashboard), with time and applicability.
3. A user-chosen spending policy: `QUALITY`, `BALANCED`, `CONSERVE`, or `CRITICAL`, including optional cap on active agents or total task effort.
4. Otherwise: `UNKNOWN`, default to **CONSERVE** for optional fan-out.

Never infer remaining usage from account plan name, model name, UI screenshot of a different model/window, or approximate number of messages. Do not secretly query private usage APIs, inspect authentication files or scrape cookies. Avoid saving raw account identifiers in reports.

Recheck the applicability and freshness at the start of each **new wave** of delegates. Do not repeatedly poll a usage interface or ask users for status unless it materially changes what can be done. A stale snapshot must not be treated as live quota.

## 2. Optional heuristic tiers (not official quota thresholds)

If the user supplies a reliable *remaining percentage of the relevant allowance*, these are **local policy heuristics**, not OpenAI limits or predicted token capacity:

| Profile | Remaining relevant allowance | Concurrent delegates | New work policy |
|---|---|---:|---|
| QUALITY | >= 60% | 0–3 | Up to 2 initially; 3rd only if independent and useful; optional reviewer if stakes justify |
| BALANCED | 30–59% | 0–2 | Targeted workstreams, optional review only when material risk |
| CONSERVE | 10–29% | 0–1 | Prefer single-agent or one bounded delegate; main verifies, no speculative branches |
| CRITICAL | < 10%, exhausted, or explicit near-limit alert | 0 | No new delegates; checkpoint and finish only safe essential work within allowance |
| UNKNOWN | No fresh/usable figure | 0–1 | Conservative default; do not claim precise cost optimization |

These bands can be overridden by a *stricter* explicit user instruction. If the user specifically chooses a higher budget profile, allow it within available entitlements and existing approval constraints; never invent entitlement or bypass a provider limit. If several model-specific buckets apply, use the **most restrictive relevant** one; do not convert percentages across unrelated quota windows.

## 3. How budget affects model and job design

- **QUALITY:** Use a strong main coordinator on complex questions; route repeatable work to cheaper verified models. Do not spawn more than independent ready work just to fill slots.
- **BALANCED:** Choose the smallest team predicted to save meaningful elapsed time; reuse a delegate for related follow-up where possible.
- **CONSERVE/UNKNOWN:** Consolidate small bounded subtasks when cost of setting up separate agents dominates. Prefer one adequate mid-tier delegate for a large mechanical read, with a short validated report. Main agent handles only key judgments and final checking.
- **CRITICAL:** No new delegate. Preserve outputs and report which checks are not complete. Only essential user-approved work, and don't promise automatic resumption.

A cheap model that fails repeatedly can cost *more* than a mid-tier success. One targeted retry at most, then escalate to main or mark unresolved. An important safety check is never silently skipped; if affordable verification isn't possible, explicitly state that the result is unverified.

## 4. Translating the profile into actual Codex models

**Important:** A configured custom-agent TOML that pins `model_reasoning_effort` takes precedence for that role. Merely saying "run this agent at medium" may **not** override its own `high` setting. Select the matching preset or a supported unpinned built-in agent instead.

| Goal | Optional role | Example model/effort (only if supported) |
|---|---|---|
| Fast mechanical reading | `aao_bulk_analyst` | Luna / medium |
| Budget-oriented bounded research | `aao_researcher_balanced` | Sol / medium |
| Difficult research with edge cases | `aao_researcher` | Sol / high |
| Scoped implementation | `aao_builder` | Sol / medium |
| Complex implementation | `aao_builder_deep` | Sol / high |
| Independent high-impact review | `aao_reviewer` | Sol / high |

A profile does not require opening a delegate. Under `CONSERVE`, zero agents may be cheapest. Under `CRITICAL`, no new delegates. For unsupported model/effort combinations use a supported alternative with disclosure, not an invented fallback.

## 5. Accountability

Before spawn, record `chosen_profile`, `source`, `time`, `model/window applicability`, `active_cap`, `reasoning`, and `why this work merits delegation`.

After work, record observed tokens/time if actually reported, distinct task count, failures and corrections, and whether acceptance checks passed. If metrics are not surfaced, label **NOT OBSERVABLE**. Never promise “<= one normal-level run” or assert savings without a measured, comparable baseline.

Never enable paid credit overages, buy tokens, change account plan, or switch the user's chosen main model/effort without specific user authorization.
