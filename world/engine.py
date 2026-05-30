from world.maps import MAPS

class GameEngine:
    def __init__(self):
        self.map = MAPS["default"]
        self.current_room = self.map["rooms"][self.map["start"]]
        self.inventory = []
        self.goal = self.map["goal"]
        self.goal_achieved = False
        self.visited_rooms = []

    def move(self, direction):
        if direction in self.current_room['exits']:
            next_room_id = self.current_room['exits'][direction]
            self.current_room = self.map["rooms"][next_room_id]
            return True ,f"You move {direction} to the {self.current_room['name']}."
        elif direction in self.current_room['doors']:
            door = self.current_room['doors'][direction]
            if door['locked'] and door['key_id'] in [item['id'] for item in self.inventory]:
                door['locked'] = False
                self.current_room = self.map["rooms"][door['leads_to']]
                return True, "You unlock the door, and moved through it."
            elif door['locked']:
                return False, "The door is locked."
            else:
                next_room_id = door['leads_to']
                self.current_room = self.map["rooms"][next_room_id]
                return True ,f"You move {direction} through the door to the {self.current_room['name']}."
        else:
            return False, "You can't go that way."

    def take(self, item_name):
        item_name = item_name.strip("[]")
        for item in self.current_room['items']:
            if item['name'] == item_name:
                self.inventory.append(item)
                self.current_room['items'].remove(item)
                return True, f"You have taken the {item_name}."
        return False, "That item is not here."


    def check_goal(self):
        if self.current_room ==self.map["rooms"][self.goal]:
            self.goal_achieved = True
            return True, "Congratulations! You have achieved your goal!"
        else:
            return False, "You have not achieved your goal yet."
        

    def get_current_state(self):
        if self.current_room['name'] not in self.visited_rooms:
            self.visited_rooms.append(self.current_room['name'])
        state = {
            "current_room": self.current_room['name'],
            "description": self.current_room['description'],
            "exits": list(self.current_room['exits'].keys()),
            "doors": {direction: {"locked": door['locked']}for direction, door in self.current_room['doors'].items()},
            "items": [item['name'] for item in self.current_room['items']],
            "inventory": [item['name'] for item in self.inventory],
            "visited": self.visited_rooms
        }
        return state
