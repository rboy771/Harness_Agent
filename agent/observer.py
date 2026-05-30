
def format_observe(state, goal):
        items = ', '.join(state['items']) if state['items'] else 'none'
        inventory = ', '.join(state['inventory']) if state['inventory'] else 'empty'
        
        door_info = ', '.join([f"{direction} (locked - needs key)" if details['locked'] else f"{direction} (unlocked)"
        for direction, details in state['doors'].items()
    ]) if state['doors'] else 'none'
        
        observation = f"""you are currenly in the {state['current_room']}.
        {state['description']}
        Exits: {', '.join(state['exits'])}.
        locked doors: {door_info}.
        Items in the room: {items}.
        Your inventory: {inventory}.
        Your goal is to {goal}.
        Rooms already visited: {', '.join(state['visited'])}.
        Do not revisit rooms you have already been to unless necessary.
        Go back to the entrance to use the key on the locked door.
        Respond with only a single word action: move north / move south / move east / move west / take [item name]"""
        
        


        return observation


