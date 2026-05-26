from __future__ import annotations

import os


class ClaudeClient:
    def __init__(self, model: str = "claude-3-5-haiku-latest") -> None:
        self.model = model
        self.api_key = os.getenv("ANTHROPIC_API_KEY", "")
        self._client = None
        if self.api_key:
            try:
                from anthropic import Anthropic

                self._client = Anthropic(api_key=self.api_key)
            except Exception:
                self._client = None

    def choose_action(self, prompt: str, valid_actions: list[str]) -> str:
        if not self._client:
            return "look"

        message = self._client.messages.create(
            model=self.model,
            max_tokens=20,
            messages=[
                {
                    "role": "user",
                    "content": (
                        "Return exactly one action from this list: "
                        + ", ".join(valid_actions)
                        + "\n\n"
                        + prompt
                    ),
                }
            ],
        )
        text = "".join(
            block.text for block in message.content if getattr(block, "type", "") == "text"
        ).strip()
        return text
