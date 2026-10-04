# SPIDER

Signal Preserved in Deep Echo Runtime.

SPIDER defines a reusable method for turning an attributed source into a
versioned state transition and several consistent projections. A project owns
its domain rules; SPIDER owns the shared contracts and their provenance.

Start with [the method](docs/METHOD.md), [projection contract](docs/PROJECTIONS.md)
and [project inheritance](docs/PROJECT-INHERITANCE.md). The small C++20 library
provides command context, localization resolution and named check results.
It contains no InterDead story or gameplay rules.

The [Code Constitution](https://github.com/FOP-Oksana-Dubinetska/code-constitution)
is pinned in `.code-constitution`. [PROFILE](governance/PROFILE.md) and
[development rules](governance/legislation/DEVELOPMENT-CXX.md) describe the local
implementation. Project overrides, including a different language or build
system, are normal: record their scope, source, reason and evidence.

```sh
git clone --recurse-submodules https://github.com/Zhovten-Games/SPIDER.git
cd SPIDER
make check
```

Verified bootstrap toolchain: GCC 13.3.0, GNU Make 4.3, Python 3.12.14 on Linux.
The library needs C++20; the check command also needs Python 3.10 or newer.
Build outputs stay in `build/`. CMake is an optional integration definition,
not a separately verified toolchain in this bootstrap.

The constitutional profile is a published candidate. Technical checks implement
the requested foundation; they do not claim formal ratification or complete
constitutional conformity. Adoption requires the separate human record described
in the upstream Constitution. New domain projects must make their own profile.

First consumer: [InterDead](https://github.com/Zhovten-Games/InterDead).
