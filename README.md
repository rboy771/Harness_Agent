# Dungeon

Minimal dungeon simulation scaffold with an LLM-driven agent loop.

## File structure

```text
├── world/
│   ├── engine.py      # grid, rooms, objects, state
│   ├── maps.py        # level definitions
│   └── objects.py     # item types, doors, keys
├── agent/
│   ├── harness.py     # the main loop (core coordinator)
│   ├── observer.py    # formats world state → LLM prompt
│   └── actions.py     # action space definition + parser
├── llm/
│   └── gemini.py      # Gemini API wrapper
├── logger/
│   └── replay.py      # step logger + HTML viewer
├── run.py             # entry point
├── README.md          # setup and design notes
└── requirements.txt
```

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
python run.py --steps 20
```
