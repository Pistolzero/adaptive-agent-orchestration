# Design notes and known limitations

The root agent is responsible for architecture, user approvals, and integration. Delegates own bounded evidence and implementation streams; a separate reviewer is optional. Decisions about child model selection are constrained by actual availability and relevant quota, not brand status.

**No magic quota API:** usage snapshots shown in a product UI are not an authorized programmable endpoint. Never automate web scraping of a private dashboard, parse credentials, or claim access to another user's quota. Offer conservative behavior when unavailable.

**No guarantee of efficiency:** delegation may increase tokens. Measure before claiming improvements. Budget heuristics control fan-out, not actual consumption as a hard quota enforcement mechanism.

**Model names and config evolve:** optional TOML models are examples. Check Codex support before installing. The user keeps control of parent model/effort. Custom agents cannot override the parent's permissions.

**No hidden failure guarantee:** delegate reports are necessary but not sufficient; deterministic tests, tool logs and diffs must corroborate significant claims. If a check is unrun, report it, don't fabricate evidence.

**Licensing:** this project is independently written using general delegation concepts; do not add other authors' Skill files unless their license permits redistribution.
