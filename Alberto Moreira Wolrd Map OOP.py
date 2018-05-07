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


north_military_base = Room("North Military Base", "Four_locked_doors", None, "east_military_base",
                           "west_military_base", None, None, "You have been teleported to a island you are "
                           "being chased by the unknown your only way to leave is to make it to the other end."
                           " Good Luck.")

south_military_base = Room("South Military Base",)
west_military_base = Room("West Military Base", "North Military Base", )
east_military_base = Room("East Military Base")
first_door = Room("First Door", "")
second_door = Room()
third_door = Room()
fourth_door = Room()
underground = Room("Underground")
two_giant_rocks = Room("two giant rocks")
