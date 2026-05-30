from llm.gemini import ask
from agent.actions import VALID_VERBS
from agent.observer import format_observe
from world.engine import GameEngine
from logger.logger import logger


class AgentHarness:
    def __init__(self):
        self.game_engine = GameEngine()
        self.goal = self.game_engine.goal
        self.goal_achieved = False
        self.max_steps = 20
        self.steps = 0
        self.logger = logger()

    def run(self):
        while not self.goal_achieved and self.steps < self.max_steps:
            self.steps += 1
            observation = format_observe(self.game_engine.get_current_state(), self.goal)
            print("\n--- STEP", self.steps, "---")
            print(observation)
            action = ask(observation).strip().lower()
            for direction in ["north", "south", "east", "west"]:
                if action == direction:
                    action = "move " + direction
            print("ACTION", action)
            if any(action.startswith(verb) for verb in VALID_VERBS):
                if action == "look":
                    print(self.game_engine.current_room['description'])
                elif action.startswith("move"):
                    direction = action.split()[1]
                    success, message = self.game_engine.move(direction)
                    print(message)
                elif action.startswith("take"):
                    item_name = action.split(' ', 1)[1]
                    success, message = self.game_engine.take(item_name)
                    print(message)
                self.logger.log_step(self.steps, observation, action, message)
                self.goal_achieved, goal_message = self.game_engine.check_goal()
                if self.goal_achieved:
                    print(goal_message)
            else:
                print(message)
            self.logger.save_json()
            self.logger.save_html()

if __name__ == "__main__":
    harness = AgentHarness()
    harness.run()