# Adaptive Agent Orchestration for Codex

**A reusable, budget-aware multi-agent policy for Codex**. It helps a strong coordinator decide **whether** to delegate, **which model/effort** to use, **how many simultaneous agents** to spawn, **how to brief them**, and **how to audit failures** before declaring success.

> Status: v1.1.0 — instruction-first, no dependencies, no hidden quota access. Not affiliated with OpenAI or the author of any third-party orchestration skill.

## What it actually does

- Dynamically recommends 0–3 concurrent delegates (normally fewer) based on independent work and **usage-budget profiles**.
- Supports the *same agent role* repeated on disjoint file sets.
- Routes mechanical tasks to lightweight options, bounded technical work to mid-tier options, and critical judgments to the user's chosen main agent.
- Requires exact task briefs, failure/attempt logs, acceptance checks, and main-agent verification.
- Defaults to **conservative** when remaining quota is unknown; does **not** pretend it can automatically read everyone's account limits.
- Never grants permissions, installs tools, charges credits, or launches agents merely by existing.

## Quick install (Windows / Codex)

1. Download or clone this repository.
2. Copy `.agents/skills/adaptive-agent-orchestration/` into `%USERPROFILE%\.agents\skills\adaptive-agent-orchestration\` (retain the `references` directory).
3. Open a fresh Codex session. Ask: `Use adaptive-agent-orchestration for this task. If usage is unknown, default to CONSERVE and report uncertainties.`
4. Optional: copy `agents/*.toml` **selectively** into `%USERPROFILE%\.codex\agents\`; check model access. Merge `examples/config-snippet.toml` into your existing `config.toml` rather than overwriting it. Back up before editing.

To publish the repository, see [GitHub publishing guide (TR)](docs/PUBLISH_TR.md).

For a single project only, Codex can discover `.agents/skills/` in the repository; there is no need for a global install. See [Installation guide](docs/INSTALL_TR.md).

## Usage-budget behavior

| Relevant remaining usage (when reliably known) | Policy | Default concurrent subagents |
|---|---|---|
| >= 60% | QUALITY | 0–3 |
| 30–59% | BALANCED | 0–2 |
| 10–29% | CONSERVE | 0–1 |
| < 10% or near/exhausted | CRITICAL | 0 new |
| Unknown/stale | UNKNOWN / CONSERVE | 0–1 |

These are **user-configurable policy heuristics**, *not official OpenAI thresholds*. Percentage is not a token balance. Some limits are model- or window-specific. The skill can use a fresh **official status supplied by the user/host**, but does **not** have a universal live quota API. Never read credentials or purchase credit overages.

## Use in a prompt

```text
Use the adaptive-agent-orchestration skill for this task.
Choose the smallest effective team for quality, elapsed time, and usage budget.
My budget preference is BALANCED. If you cannot verify remaining usage,
use UNKNOWN/CONSERVE and do not invent numbers.
Brief every delegate precisely and require the complete failure/evidence report.
Verify key claims from original evidence, not just agent summaries.
Do not make external or destructive changes without my approval.
```

## Structure

- `.agents/skills/adaptive-agent-orchestration/SKILL.md`: entrypoint policy
- `references/budget-policy.md`: quota-aware staffing, fallback rules
- `references/brief-templates.md`: task-specific prompts for smaller models
- `references/failure-and-evidence-report.md`: mandatory error and evidence disclosure
- `references/dynamic-team-sizing.md`: independent partitioning and same-role clones
- `agents/`: **optional** custom Codex role TOMLs, including distinct Balanced/Deep variants because pinned TOML settings take precedence (not auto-installed)
- `docs/`: detailed setup, security, limitations
- `tests/`: validation tests for package structure and TOML

## Important limitations

- Codex subagents require the host runtime to support delegation. A Skill does not implement a fleet by itself.
- User-selected xhigh for the parent **does not force** all child agents to xhigh if explicit supported role settings are applied, but unsupported combinations may fall back or fail.
- More agents can be faster in elapsed time yet cost more total tokens. No savings guarantee without measurement.
- Role files cannot override the parent approval/sandbox policy. Protect high-impact actions with real approvals.
- This is an **independently written project**. No third-party `fable-orchestration` files or `codex-fleet` dependency are distributed.

## License and contributions

MIT for the original material in this repository. See [LICENSE](LICENSE), [CONTRIBUTING](CONTRIBUTING.md) and [SECURITY](SECURITY.md). If adapting others' content, check their licenses separately.
