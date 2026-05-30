from world.maps import MAPS


def __init__(self):
    self.map = MAPS["default"]
    self.current_room = self.map["rooms"][self.map["start"]]
    self.inventory = []
    self.goal = self.map["goal"]
    self.goal_achieved = False
    self.visited_rooms = []