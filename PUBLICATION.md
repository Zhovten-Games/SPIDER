# Publication boundary

This edition contains original English doctrine, literary pseudocode, a small
validator and governance/licensing pointers. Examples use synthetic identifiers:
no game dialogue, private Drive IDs, live graph, credentials, client orders or
provider payloads. InterDead and EMBO may remain private; links identify source
projects rather than export their code. VOX is a reviewed public projection.

[Dependency pins](manifest/dependencies.json) retain provenance. InterDead keeps
the old MIT C++ bootstrap at `3c67103c1456f5b1dd5ce88204be658d0bbce3bd`.
Removing C++ from main changes neither that object nor the consumer pin. Do not
point a C++ consumer at methodology main.

Before public visibility, review all advertised refs, reachable commits,
historical blobs, messages and identity metadata. The original repository has
two commits and one main branch; the first tree contains only a short README.
Preserve clean history. If sensitive data is found, keep visibility private,
sanitize affected history and review every remaining ref before publication.

`manifest/publication.json` inventories public paths. The checker rejects
unlisted paths and common private-locator/secret forms. It supports human source
review; it does not prove every possible secret is recognizable.
