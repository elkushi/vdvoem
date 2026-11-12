# Вдвоём

Two-player co-op climb. Lava rises from below, platforms generate forever
upward. **If one player falls they are not dead — they are downed**, and the
other has a few seconds to reach them. Miss it and the run ends for both.

Plays two ways:

- **One screen** — two halves of a keyboard, no setup
- **Online** — one player per phone, joined by a 4-letter room code

Single HTML file, no engine, no build toolchain, no dependencies at runtime.

## Why it is built this way

**The camera follows whoever is lower.** Neither player can climb away and
abandon the other — the screen itself enforces co-operation.

**A mistake becomes a rescue, not a blame.** Being downed is recoverable, so
falling invites the other player in instead of ending the run.

**The world is deterministic.** Both devices build an identical level from a
shared seed (mulberry32), and the lava height is a pure function of elapsed
time rather than an integration over local frames. Nothing about the world is
sent over the network — only each player's own position.

**Each device simulates only its own player.** Your character responds
instantly; only the partner is interpolated from the network. The rescue window
widens from 5s to 9s online to absorb latency.

## Controls

| | move | jump |
|---|---|---|
| player 1 | `A` `D` | `W` / `Space` |
| player 2 | `←` `→` | `↑` |

`R` restart · `M` sound. On phones: touch controls, landscape.

## Build

```bash
python3 build.py        # inlines sprites -> index.html
python3 serve.py        # local preview on :8731
```

## Online mode

Needs a Firebase Realtime Database. Put the web config in `firebase.json`
(git-ignored) next to `build.py`:

```json
{ "apiKey": "...", "authDomain": "...", "databaseURL": "...", "projectId": "..." }
```

then rebuild. Without it the online button explains itself and one-screen play
still works.

Suggested database rules — scoped to rooms, and unlike "test mode" they do not
expire:

```json
{ "rules": { "rooms": { "$code": { ".read": true, ".write": true } } } }
```
