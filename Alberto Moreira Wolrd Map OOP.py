class Room(object):
    def __init__(self, name, north, south, east, west, southeast, southwest, climb_up, climb_down,
                 northeast, northwest, description):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.southeast = southeast
        self.southwest = southwest
        self.climb_up = climb_up
        self.climb_down = climb_down
        self.northeast = northeast
        self.northwest = northwest
        self.description = description

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


front_of_base = Room("Front of Base", None, "First Door", None, None, None, None, None, None, None, None,
                     "The First Door room is south")
first_door = Room("First Door", "Front of base", "First Base Room", None, "West of Base", "East of Base",
                  "Mystery Room", None, None, None, None, "The Front of Base is North, "
                  "the First Base Room is south,"
                  "the West of Base room is west, the East of Base room is east, and the mystery room is"
                  "southwest")
west_of_base = Room("West of Base", None, "Mystery Room", "First Door", None, None, None, None, None,
                    None, None, "The mystery room is south and the first door is east")
east_of_base = Room("East of Base", None, "Weapon Vault", None, None, None, None, None, None,
                    None, "First Door", "The Weapon Vault is south and the First Door is northwest")
mystery_room = Room("Mystery Room", "West of Base", "Cellar", "Second Door", None, None, None, None, None, None,
                    None, "The west of base room is north, the cellar is south, and the second door is east")
cellar = Room("Cellar", "Mystery room", None, None, None, None, None, None, None, None, None, "The mystery room"
                                                                                              "is north")
weapon_vault = Room("Weapon Vault", "East of Base", None, None, None, None, None, None, None, None, None,
                    "The east of base is north")
first_base = Room("First Base", "First Door", "Second Door", None, None, None, None, None, None, None, None,
                  "The First Door is north and the Second Door is south")
second_door = Room("Second Door", "First Base", "Hallway", None, "Mystery Room", "East Hall", "West Hall",
                   None, None, None, None, "The first base is north, the hallway is south, the mystery room is west,"
                                           "the east hall is southeast, and the west hall is southwest")
hallway = Room("Hallway", "Second Door", "Back of Base", "East Hall", "West Hall", None, None, None, None, None, None,
               "The second door is north, the Back of Base room is south, the east hall is east, and the west hall"
               "is west")
east_hall = Room("East of Hall", None, None, None, "Hallway", None, None, None, None, None, None, "The hallway is west")
west_hall = Room("West of Hall", None, None, "Hallway", None, None, None, None, None, None, None, "The hallway is east")
underground = Room("Underground", "Back of Base", "start of maze")
back_of_base = Room("Back of base",)
the_end = Room()
