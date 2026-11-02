# EMBO Workshop: a different domain

This case is an independent literary description of the private
[EMBO Workshop](https://github.com/EMBO-Studio-develop/embo-workshop).
It uses synthetic order concepts; no client data or GPL implementation is copied.
The reference repository is read-only for this work.

WooCommerce owns payments and entitlements. Workshop keeps an order projection,
durable deduplication, fixed spreadsheet-row ownership and an export outbox.
An operator can observe/retry allowed work; retry never creates a second payment
or a second owner of the same row. Approved add-on releases retain source and
artifact provenance. See [the boundary](commerce.xml).

The reference uses a native Segoe UI / Arial sans-serif stack, restrained headings,
clear active navigation and an inspector. InterDead adopts the typography approach
while retaining its own palette. No font binaries, provider identifiers, customer
records or styling source are redistributed. EMBO itself is not changed.

## Operational chain and authority

The owner's October overview supplies the broader example:

| Object | Authority / responsibility |
| --- | --- |
| Release | GitHub/CI source revision and verified package identity |
| Private package | Cloudflare R2 distribution with artifact-integrity checks |
| Purchase and entitlement | WooCommerce commerce/licensing authority |
| Operational projection/outbox | Cloudflare D1 event state and recovery |
| Exported record | Google Sheets projection with reconciliation |
| Installation | The individual WordPress site and its administrator |

Site Commander, Connect and Store are separate client/commerce responsibilities;
paid add-ons are distributed independently. The workspace coordinates them without
moving purchase authority into its dashboard. See [distribution and cancellation](distribution.xml).

The supplied account describes a synthetic staging lifecycle: catalogue → purchase
→ license activation → verified ZIP → installation, followed by order cancellation,
revoked future download and a reconciled sheet. The installed plugin remains
installed. This is attributed source evidence, not a new staging test performed
by this methodology checker. Real payments, production acceptance and public
distribution remain separate milestones.
