# LLM Agent in a Virtual World — Bank Heist

## What is this?

A text-based game where an AI agent is placed into a virtual bank and must
complete a heist. Starting from the entrance, the agent must explore rooms,
find a vault key card, unlock a door, and reach the vault — all autonomously,
powered by Google Gemini.

## How to run it

1. Clone the repo
2. Install dependencies:
   pip install google-generativeai python-dotenv

3. Create a `.env` file in the root folder:
   GEMINI_API_KEY="your_key_here"

4. Run:
   python run.py

A log of the run will be saved as `log.html` and `log.json` in the root folder.

## Project structure

agent/ — observer, harness, actions
world/ — game engine, maps, objects  
llm/ — Gemini API wrapper
logger/ — step logger and HTML replay

## Design decisions

### Why text-based?

Text is the most natural format for an LLM to reason in. Gemini thinks in
text, so giving it a text observation requires no conversion. It also kept
complexity focused on the agent harness design rather than rendering.

### Observation design

Each step the agent receives: current room and description, available exits,
locked door status, items in the room, current inventory, goal, and a list of
previously visited rooms.

I designed this by putting myself in the agent's shoes — what would I need
to know to make a good decision, without being given too much? The visited
rooms list was added after the agent kept wandering in circles with no memory
of where it had already been.

### The agent harness

The harness is the interface between Gemini and the world. Each step it: gets
the current world state, formats it into a prompt, sends it to Gemini, parses
the response, executes the action on the game engine, and checks if the goal
is achieved. A step limit of 20 prevents infinite loops.

## What didn't work at first

- The agent had no memory of visited rooms so it wandered endlessly — fixed
  by adding a visited rooms list to the observation
- The agent couldn't see its inventory so it didn't know it had picked up
  the key — fixed by including inventory in every observation
- Gemini returned bare directions like `south` instead of `move south` —
  fixed by auto-prefixing bare directions in the harness
- Gemini wrapped item names in brackets: `take [vault key card]` which
  didn't match — fixed by stripping brackets before searching
- The locked door wasn't shown in the observation so the agent kept trying
  to walk through it — fixed by adding locked door status to the prompt
- The move method returned inconsistent formats causing crashes — fixed by
  making all returns consistent tuples

## What I'd add with more time

- More rooms, more items, more complex multi-step puzzles
- A full bank heist storyline with multiple floors
- Upgrade to a 2D grid world with visual rendering
- Eventually progress to a 3D environment
- A better memory system so the agent reasons across more steps
