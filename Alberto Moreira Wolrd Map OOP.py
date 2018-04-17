class Room(object):
    def __init__(self, name, north, south, east, west, climb_up, climb_down, description):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.description = description
        self.climb_up = climb_up
        self.climb_down = climb_down

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


north_military_base = Room("Military Base", "Four locked doors", "two_giant_rocks", None, None, "playground", None,
                           "You have been teleported to a island you are being chased by the unknown your only way "
                           "to leave is to make it to the other end Good Luck")
playground = Room("Playground", "Trees leaning on an abandoned fort", "ladder going down into a hole", None, )
two_giant_rocks = Room("two_giant_rocks",)
