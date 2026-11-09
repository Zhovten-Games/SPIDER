# Methodology development rules

`spider-methodology-0.3.0-operative`, derived from the pinned Constitution.

| Rule | Scope and verification |
| --- | --- |
| SP-M01 | English in versioned XML; parse and resolve IDs locally. |
| SP-M02 | Explain reasoning; exclude private code, story and topology. |
| SP-M03 | Distinguish illustrative, observed and planned behavior. |
| SP-M04 | Every semantic relation needs a reason; membership creates none. |
| SP-M05 | One state authority; projections preserve permissions and versions. |
| SP-M06 | Bounded test blocks retain the complete inventory and integration gate. |
| SP-M07 | Apply scoped licensing and preserve upstream notices. |
| SP-M08 | Review historical blobs, refs and metadata before public visibility. |

This edition replaces the bootstrap C++ stack rule with XML/Markdown and a
Python-standard-library verifier. Consumer stacks/pins are unchanged. Universal
typography amendments require separate consideration.

## Verification tooling scope

`tools/warden.mjs` is the explicitly allowed repository verification orchestrator. It supplies no product implementation. `.warden/` contains generated local evidence and is excluded from the reviewed publication path inventory. Other executable product/source exclusions remain enforced by check-methodology.py.
