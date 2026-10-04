# Several projections, one session

| Boundary | Owns | Must not own |
| --- | --- | --- |
| Domain session | Facts, logical time, command legality, events, knowledge | Filesystem, browser DOM, rendering, wall clock |
| Content compiler | IDs, source status, references, localization completeness | Authorial approval or invented unresolved scenes |
| Player projection | Permitted text, visible state, semantic actions | Hidden transcript or new gameplay rules |
| Inspection | Named values, versions, guards and diagnostics for development | Player knowledge or arbitrary production state mutation |
| Host adapter | Resources, devices, layout, delivery and technical pauses | Independent stress, story or permission calculations |
| Warden | Scenario orchestration and explicit assertions | A second implementation of domain transitions |

Commands carry a stable ID, expected revision and typed payload. A retry with
the same ID and payload returns the prior receipt; reusing an ID for a different
payload is an error. Revision checks apply to new commands. Ordered logical
time is injected, and technical pauses freeze it.

Player text resolution records requested locale, served locale and fallback.
An unknown key fails explicitly. Locale fallback is an authored policy;
localization does not silently reveal hidden information.

Native, WASM and Unreal projections must compare semantic events and state
using the same content/rules versions. Pixel geometry and device inputs can
differ. A graph check alone does not prove executable guards or finished text.
