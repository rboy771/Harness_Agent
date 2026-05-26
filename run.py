import argparse

from agent.harness import DungeonHarness


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the dungeon agent loop.")
    parser.add_argument("--steps", type=int, default=20, help="Maximum number of steps")
    parser.add_argument("--model", default="claude-3-5-haiku-latest", help="Claude model name")
    args = parser.parse_args()

    harness = DungeonHarness(max_steps=args.steps, model=args.model)
    output = harness.run()
    status = "escaped" if output["completed"] else "stuck"
    print(f"Dungeon run finished: {status} in {output['steps']} step(s)")


if __name__ == "__main__":
    main()
