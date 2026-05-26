from dataclasses import dataclass


@dataclass(frozen=True)
class Key:
    name: str = "brass key"


@dataclass
class Door:
    locked: bool = True

    def unlock(self, key: Key | None) -> bool:
        if key is None:
            return False
        self.locked = False
        return True
