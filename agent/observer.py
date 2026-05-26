from world.engine import WorldState


def format_world_state(state: WorldState, last_result: str = "") -> str:
    return (
        f"Grid: {state.width}x{state.height}\n"
        f"Position: {state.position}\n"
        f"Exit: {state.exit}\n"
        f"Inventory: {', '.join(state.inventory) if state.inventory else 'empty'}\n"
        f"Key tile: {state.key_position}\n"
        f"Door tile: {state.door_position} (locked={state.door_locked})\n"
        f"Last result: {last_result or 'none'}"
    )
