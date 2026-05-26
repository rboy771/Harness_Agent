from __future__ import annotations

from dataclasses import dataclass, field

from world.maps import DEFAULT_MAP
from world.objects import Door, Key


MOVES = {
    "north": (0, -1),
    "south": (0, 1),
    "west": (-1, 0),
    "east": (1, 0),
}


@dataclass
class WorldState:
    width: int
    height: int
    position: tuple[int, int]
    exit: tuple[int, int]
    key_position: tuple[int, int] | None
    inventory: list[str] = field(default_factory=list)
    door_position: tuple[int, int] | None = None
    door_locked: bool = True


class WorldEngine:
    def __init__(self, level: dict | None = None) -> None:
        config = level or DEFAULT_MAP
        self.state = WorldState(
            width=config["width"],
            height=config["height"],
            position=config["start"],
            exit=config["exit"],
            key_position=config.get("key"),
            door_position=config.get("door"),
        )
        self._key = Key() if self.state.key_position else None
        self._door = Door(locked=bool(self.state.door_position))

    def _can_enter(self, target: tuple[int, int]) -> bool:
        if self.state.door_position == target and self._door.locked:
            return False
        return 0 <= target[0] < self.state.width and 0 <= target[1] < self.state.height

    def apply_action(self, action: str) -> str:
        if action in MOVES:
            dx, dy = MOVES[action]
            target = (self.state.position[0] + dx, self.state.position[1] + dy)
            if not self._can_enter(target):
                return "You cannot move there."
            self.state.position = target
            return "You move " + action + "."

        if action == "look":
            return "You inspect your surroundings."

        if action == "pickup":
            if self.state.key_position == self.state.position and self._key:
                self.state.inventory.append(self._key.name)
                self.state.key_position = None
                self._key = None
                return "You pick up the brass key."
            return "There is nothing to pick up."

        if action == "unlock":
            if self.state.door_position != self.state.position:
                return "There is no door here."
            key = Key() if "brass key" in self.state.inventory else None
            if self._door.unlock(key):
                self.state.door_locked = False
                return "You unlock the door."
            return "The door is locked and you need a key."

        return "Unknown action."

    def is_complete(self) -> bool:
        return self.state.position == self.state.exit and not self._door.locked
