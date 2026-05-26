VALID_ACTIONS = ["north", "south", "east", "west", "look", "pickup", "unlock"]


def parse_action(raw_action: str) -> str:
    action = (raw_action or "").strip().lower()
    if action in VALID_ACTIONS:
        return action
    return "look"
