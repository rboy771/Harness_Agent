class Item:
    def __init__(self,name , id):
        self.name = name
        self.id = id

class Door:
    def __init__(self, locked, id , key_id, leads_to):
        self.id = id
        self.locked = locked
        self.key_id = key_id
        self.leads_to = leads_to