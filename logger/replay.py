from dataclasses import dataclass, field
from html import escape


@dataclass
class ReplayLogger:
    steps: list[dict] = field(default_factory=list)

    def log(self, step: int, action: str, result: str) -> None:
        self.steps.append({"step": step, "action": action, "result": result})

    def to_html(self) -> str:
        rows = "".join(
            f"<tr><td>{entry['step']}</td><td>{escape(entry['action'])}</td><td>{escape(entry['result'])}</td></tr>"
            for entry in self.steps
        )
        return (
            "<html><body><h1>Dungeon Replay</h1>"
            "<table border='1'><tr><th>Step</th><th>Action</th><th>Result</th></tr>"
            f"{rows}</table></body></html>"
        )
