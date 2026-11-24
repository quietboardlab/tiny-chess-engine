# tiny-chess-engine

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/quietboardlab/tiny-chess-engine/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/quietboardlab/tiny-chess-engine/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A chess engine in 4,083 bytes of pure-stdlib Python, built for make.fun's tiny-chess-01 bounty ("Build the strongest chess engine in 4 KB of Python"). Negamax alpha-beta search (depth 3 plus capture quiescence) with a fixed 12,000-node budget per move, so it is fully deterministic: no clock, no randomness. Speaks UCI over stdin/stdout.

## Run it

```sh
python3 main.py   # UCI engine: send 'uci', 'position fen ...', 'go' on stdin
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=agfrhq8x&utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
