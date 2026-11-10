# Custom Operations Workspaces

A team already has documents, repositories, payments, build tools and provider
permissions. The useful workspace connects their workflow in one interface:
find the authoritative object, understand its relationships, perform an allowed
operation, and see whether it actually completed.

The owner-supplied Halloween 2026 overview, **Custom Operations Workspaces —
From Internal Production to Client Infrastructure**, grounds this summary. It
identifies two October implementations behind the IRONCREED service. The
reusable result is a dedicated operational application around existing
infrastructure, with identity, authority, recovery and verifiable outcomes.

The transferable idea is the operational boundary, not a universal dashboard.
Keep provider originals authoritative. Keep a typed, versioned project model.
Project that model for an operator without duplicating business or game rules.
A different project gets its own vocabulary, connectors and access policy.

| Case | Original authority | Workspace responsibility |
| --- | --- | --- |
| [InterDead](examples/interdead/README.md) | Author documents, Git game sources and the portable core | Sources, explicit relations, graph/document views and build review |
| [EMBO](examples/embo/README.md) | WooCommerce orders/entitlements and approved releases | Order projection, durable export/retry and release provenance |

The [shared pseudocode](method.xml) describes the boundary. [Typography](typography.xml)
explains shared roles, local palettes and system fonts. Both examples are original
literary descriptions, not source exports or deployment templates.

## The integration problem

Source authority, identity, permissions, artifact integrity, synchronization,
recovery and audit are separate engineering responsibilities. A connected API
alone does not solve them. Event IDs, durable deduplication, reconciliation,
operation state and controlled retries matter when a provider fails halfway.

A workspace can connect document production, build coordination, plugin
catalogues, licensing, synchronization and operational workflows. Scope and
access follow the team's actual operations. This methodology is portable across
those domains; it is not a prebuilt universal dashboard or a commercial quote.

## A small relation system inspired by VOX

The [public VOX semantic-core contract](https://github.com/IRONCREED/VOX/blob/9a79a8fd18133dea4e3f333d6fab7b482610838f/governance/legislation/SEMANTIC_CORE_AND_ENTITY_INDEX_2026-08-11.md)
provides a useful reference: stable entities, explicit semantic relationships and
separate derived views. Its private editorial tools are not available here.
InterDead adapts those principles to a D1 production registry, not a second
literary canon.

**“Palantir on a shoestring” / «Палантир на минималках»** is our informal analogy
for a typed object/relation model with operational views. It is inspired by the
ontology-to-operations idea associated with Palantir, not an implementation of
its software, an affiliation or a claim of equivalent scale/capability.

The earlier promotional name VOICE is clarified by the owner as **VOX**.

An assistant may resolve explicit instructions into a typed relation package.
Ambiguity stays a proposal. An already authorized package can be previewed and
applied without another ceremonial approval. The server checks identity, role,
revision, IDs and digest; one atomic transaction creates the links and receipt.
Graph exposure is explicit: interface or system-only. System-only is presentation,
not an access-control or secrecy boundary.
