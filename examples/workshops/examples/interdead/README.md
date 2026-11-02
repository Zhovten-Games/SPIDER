# InterDead Workshop

[InterDead](https://github.com/Zhovten-Games/InterDead) combines author documents,
technical content, repositories and build review in one production interface.
It remains separate from the game's portable state authority.

| Element | Responsibility |
| --- | --- |
| Cloudflare Access | Admission to the workspace; server roles govern mutations |
| Google Drive/Docs | Authoritative originals read by a bounded provider adapter |
| Workshop D1 | Source registrations, typed relations/groups and user preferences |
| Project Graph / Document Center | Two views of the same project references |
| GitHub and Build Center | Exact game revision, immutable artifacts and preview review |
| Three.js / Unreal | Planned spatial tooling and engine presentation boundaries |

See [operations](workspace.xml), [assistant relation packages](relations.xml),
[shared method](../../README.md) and the [game architecture](../../../interdead/README.md).
No provider originals, permissions or gameplay state are replaced by this metadata.

A natural-language instruction is the starting point. The assistant resolves
registered IDs, records the instruction reference and creates a bounded package.
Preview exposes updates/deletes and prior values. Apply uses a checked digest,
expected revision and stable package ID. Every operation commits together with
one audit/receipt; an exact retry returns that receipt. Manual editing remains
available through the same registry and revision boundary.

Newly registered and already indexed documents use the same endpoint contract.
Unresolved or inaccessible endpoints are refused rather than guessed. A relation
can appear on the graph or remain system-only; both remain inspectable as data.
Group membership does not generate pairwise links. The current implementation
bounds receipt retention without automatic eviction: capacity requires a reviewed
storage extension, not silent loss of deduplication evidence.

Typography follows the EMBO native sans-serif approach with InterDead's own
palette. Labels name an object, action or state. Decorative slogans do not replace
useful status. The shared roles are portable; a project owns its specific palette.

## Spatial and artifact boundaries

The supplied Halloween overview emphasizes traceability from authorial material
through executable rules, exact build inputs and delivered bytes. Build version
labels alone are insufficient; source revision, content identity, toolchain and
verification manifests accompany each artifact. Playable execution uses an
isolated protected origin rather than the administrative workspace origin.

Three.js location previews and Unreal-facing APIs belong to the developing spatial
workflow. This example keeps them [explicitly planned](spatial.xml): object IDs,
transforms and location meanings must survive adapter conversion. A planned
projection is not evidence of an accepted engine integration.
