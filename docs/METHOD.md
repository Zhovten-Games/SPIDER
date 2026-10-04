# The SPIDER method

The same method applies to a game, simulator or other stateful project:

1. **Attribute** the source, revision, authorial status and adopted requirement.
2. **Translate** it into an explicit contract: inputs, permitted commands,
   preconditions, effects, errors, time, knowledge and invariants.
3. **Compile** immutable definitions. Preserve input hashes and compiler version.
   Unresolved authorial choices remain draft and block a release.
4. **Execute** a command against one authoritative session. Check its identity
   and expected revision, create a candidate, verify invariants, then commit
   state and events together. A rejected command changes neither.
5. **Project** committed state for an audience. A projection supplies semantic
   content and actions; the host supplies layout, input devices and transport.
6. **Observe** the same session through a separate inspection port. Warden
   scenarios call the actual command boundary and compare named values.
7. **Carry** versions, state and attributed history to the next host or release.
   Unknown versions require an explicit migration or refusal.

Pseudocode describes the extension points; it does not implement domain rules:

```text
dispatch(context, command):
  previous = session.snapshot()
  resolve_duplicate_or_validate_context(context, command)
  candidate, events = project_domain_rule(previous, command, definitions)
  validate(candidate, events, definitions)
  commit(candidate, events, context)
  return player_projection(candidate), accepted_receipt
```

The host never reimplements `project_domain_rule`. It can request a command
or advance injected logical time, but it cannot change a state field directly.
Localized text is a versioned definition, not a UI-only afterthought.

An event proving an action occurred is distinct from a requirement permitting
that action. A test proving a defined result is distinct from approval of the
result. Keep both chains available and contestable.
