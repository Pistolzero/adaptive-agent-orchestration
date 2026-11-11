# Routing matrix — general-purpose, evidence-driven

Read only when planning delegation. This is an adaptive policy, not a mandatory roster.

| Workstream | Default ownership | Example delegate/effort (if supported) | Why / caution |
|---|---|---|---|
| Very small one-step task; simple local edit | Main agent | None | No spawn overhead |
| Thousands of uniform records; dedupe; label by fixed rubric | Mechanical delegate | `gpt-6-luna`, medium or high | Exact rules + samples; do not let it invent rules |
| Read several source files to create a map | Scout delegate | `gpt-6-luna`, high | Return paths, quotes, counts, uncertainties; no silent conclusions |
| Bounded technical documentation / independent research | Research delegate | `gpt-6.1-sol`, medium | Verify version and primary sources; escalate if contradictory |
| Multi-file implementation with clear spec and tests | Builder delegate | `gpt-6.1-sol`, medium/high | Single writer, no scope creep; tests essential |
| Complex debugging, difficult algorithms, domain ambiguities | Main or high-tier technical delegate | `gpt-6.1-sol`, high; main if genuinely hard | Don't under-specify; verify hard edges |
| Strategic tradeoffs, architecture, safety, uncertain root cause | Main agent | User-selected model/effort, e.g. Astra xhigh | Own the final decision |
| Independent quality, security, reproducibility review | Separate reviewer only if useful | `gpt-6.1-sol`, high | Reviewer should not certify own work |
| External actions: deployment, purchases, system changes, outreach | Main agent approval flow | Usually no delegate action | Review permissions, reversibility, user approval |

## Routing procedure

1. Rate **complexity** (routine / bounded / ambiguous), **criticality** (low / medium / high), **parallel independence**, and **data volume**.
2. Choose a clear owner and a model that is known to be available, capable and permitted.
3. Prefer inexpensive delegates for *bounded deterministic work*; don't push complex risk decisions to a weak tier.
4. Prefer fewer delegates with coherent tasks over many tiny delegates.
5. If a model is inaccessible or the effort is unsupported, use an allowed alternative and disclose it. Never silently inherit the expensive main model just to keep a spawn count.
6. A failed cheap attempt may cost more than a correct medium-tier attempt. Use a single targeted retry, then escalate if warranted.
7. Explicit user choice of model, collaboration pattern, quality threshold and time/budget takes precedence.

## Standard execution pattern

**Small:** main alone → deliver.

**Medium, separable:** main briefs 1–2 delegates → delegates return short evidence → main verifies and produces output.

**Large:** main plans dependencies → independent discovery/verification delegates → main decides design → one controlled builder or disjoint writers → conditional separate reviewer → main integrates and delivers.

**High-risk:** main owns analysis and approval; delegates may gather evidence only unless explicitly authorized.

## Model configuration caveats

- The user might choose `gpt-6-astra` with `xhigh` as the main model. This need **not** apply to delegates when explicit supported model/effort is configured.
- A Skill describes routing behavior. Per-delegate overrides are implemented by **Codex custom-agent TOML files** or explicit supported spawn configuration; a Skill does not set runtime models by itself.
- Suggested model names and supported levels may change. Verify actual installed Codex client/account capabilities before invoking.
- Never assume a tier called `ultra`, `xhigh` or `max` is supported by every model.
