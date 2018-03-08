world_map = {
    'PARKING LOT': {
        'NAME': "Parking Lot",
        'DESCRIPTION': "You are west of the house",
        'PATHS': {
            'NORTH': 'HOSPITAL'
        }
    },
    'HOSPITAL': {
        'NAME': "Hospital Waiting Room",
        'DESCRIPTION': "Description here",
        'PATHS': {
            'WEST': 'RESTROOM',
            'EAST': 'ELEVATOR1'
        }
    },
    "RESTROOM": {
        'NAME': 'The boy\'s room',
        'DESCRIPTION': '',
        'PATHS': {
            'EAST': "HOSPITAL"
        }
    },
    "ELEVATOR1": {
        'NAME': 'Elevator',
        'DESCRIPTION': 'You are on the 1st floor',
        'PATHS': {
            'WEST': "HOSPITAL",
            'UP': "ELEVATOR2"
        }
    },
    "ELEVATOR2": {
        'NAME': 'Elevator',
        'DESCRIPTION': 'You are on the 2nd floor',
        'PATHS': {
            'DOWN': 'ELEVATOR1'
        }
    },
    "ELEVATOR3": {
        'NAME': 'Elevator',
        'DESCRIPTION': 'You are on the 2nd floor',
        'PATHS': {
            'DOWN': 'ELEVATOR1'
        }
    }
}
current_node = world_map['PARKING LOT']
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST', 'UP', 'DOWN']
while True:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input('>_')
    if command == 'quit':
        quit(0)
    if command in directions:
        try:
            name_of_node = current_node['PATHS'][command]
            current_node = world_map[name_of_node]
        except KeyError:
            print("you cant go this way")
    else:
        print('Command not Recognized')
