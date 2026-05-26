from __future__ import annotations

from agent.actions import VALID_ACTIONS, parse_action
from agent.observer import format_world_state
from llm.claude import ClaudeClient
from logger.replay import ReplayLogger
from world.engine import WorldEngine


class DungeonHarness:
    def __init__(self, max_steps: int = 20, model: str = "claude-3-5-haiku-latest") -> None:
        self.engine = WorldEngine()
        self.max_steps = max_steps
        self.llm = ClaudeClient(model=model)
        self.logger = ReplayLogger()

    def run(self) -> dict:
        result = "Start."
        for step in range(1, self.max_steps + 1):
            prompt = format_world_state(self.engine.state, result)
            raw_action = self.llm.choose_action(prompt, VALID_ACTIONS)
            action = parse_action(raw_action)
            result = self.engine.apply_action(action)
            self.logger.log(step, action, result)
            if self.engine.is_complete():
                return {"completed": True, "steps": step, "replay": self.logger}

        return {"completed": False, "steps": self.max_steps, "replay": self.logger}
