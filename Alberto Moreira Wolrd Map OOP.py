class Room(object):
    def __init__(self, name, north, south, east, west, up, down, description):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.description = description
        self.up = up
        self.down = down

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


park = Room("Parking Lot", None, None, None, None, None, None, 'locked cars')
hospital = Room("waiting room", None, "Parking lot", "restroom", None, None, "elevator")
elevator1 = Room()
elevator2 = Room()
elevator3 = Room("Elevator", None, None, None,  None, None, 'elevator4','elevator2',"You are on the third floor")
elevator4 = Room("Elevator", None, None, None, None, 'elevator5', 'elevator3', "You are on the fourth floor.")
elevator5 = Room("Elevator", None, None, None, None, None, 'elevator4', "You are on the fifth floor.")