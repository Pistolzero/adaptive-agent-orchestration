# Contributing

Please open an issue describing the behavior to improve, expected result, risks and reproducible evidence. Proposals that change budgets or models should include realistic failure cases and must avoid unsupported quota access claims.

Before a PR:
1. Ensure no account tokens, device identifiers, proprietary datasets or user files are included.
2. Keep `SKILL.md` short enough for progressive loading; detailed rules belong in `references/`.
3. Check TOML syntax and internal links using `python -m unittest discover -s tests -v` (standard library).
4. Make any new scripts optional and provide clear privilege boundaries. No opaque installers.
5. Do not introduce third-party Skill content without verifying its redistribution license.

By contributing, you agree to license your contribution under MIT.
