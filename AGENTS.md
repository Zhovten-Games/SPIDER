# Working in SPIDER

Read `governance/PROFILE.md`, `governance/legislation/DEVELOPMENT-CXX.md`,
`docs/METHOD.md` and `docs/PROJECT-INHERITANCE.md` before changing contracts.
The pinned universal text is `.code-constitution/locales/ru/CONSTITUTION_CODE.md`.

Keep portable components independent of domain rules, host I/O and wall clocks.
Record source/generated/fixture/external/report status in the artifact manifest.
Run `make check` for a meaningful change and report its actual scope.
Do not manually edit generated outputs or advance normative/dependency pins
without an explicit provenance update. Preserve the distinction between a
technical check and a human decision.

Project overrides are expected. Do not force the upstream TypeScript/Node stack
onto C++ consumers. A local override names the rule, scope, reason and check.
The current bootstrap profile is a candidate; do not fabricate ratification,
approvers, independence of consent or adoption dates.
