# Literary pseudocode

Each XML document is versioned data containing ordinary English. Tags identify
contracts, ports, invariants and test cases. The English describes meaning:
it is **not executable code**. Translate it into your own types and tests.

Each document has a unique `id` and `version`. `covers` and `ref` resolve existing
IDs. `status="illustrative"` reconstructs a method, not proof of a shipped feature;
`status="planned"` marks an unimplemented boundary. A contract declares inputs,
authority, preconditions, steps, commit and refusal. Tests describe given/when/then.

`make check` parses XML, resolves IDs/local Markdown links and checks the public
inventory. It does not execute English or certify a product. XML pseudocode and
the validator are MIT; editorial explanation is CC BY-SA 4.0.
