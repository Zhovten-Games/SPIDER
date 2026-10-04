# Inherit and specialize

A consumer pins an exact SPIDER commit and the universal Constitution revision.
It keeps its own `governance/PROFILE.md`, specification and domain model.
There is no mandatory base class or giant framework object.

| Layer | Source | Consumer action |
| --- | --- | --- |
| Universal Constitution | Pinned upstream normative text | Preserve attribution and adoption status |
| Method and contracts | Pinned SPIDER revision | Implement the boundaries; record changed contracts |
| Portable C++ helpers | SPIDER include tree | Use directly or a verified vendored snapshot |
| Project profile | Consumer repository | Name jurisdiction, roles, stack and evidence |
| Domain rules/content | Consumer repository and attributed sources | Compile and test actual project behavior |
| Projections | Consumer adapters | Render one shared session |

Changing C++ to another language is an ordinary project override. Replacing a
build tool, naming convention or serialization library is also local when its
effect stays inside the declared boundary. State ownership, provenance,
human authority and a shared public contract cannot be silently discarded.

Each override records `id`, `source_rule`, `scope`, `reason`, `replacement`,
`check` and `status`. Update a pin with a reviewed diff, rebuild consumers and
retain the previous pin for rollback. Never treat upstream `main` as a release.

Private consumers may vendor the three small helper headers with SHA-256
verification, in addition to a pinned git submodule. This makes an offline
bootstrap and CI possible without a cross-repository credential. The vendored
copy is external-derived, carries its source commit/license and is regenerated
from that commit; it must not be edited independently.
