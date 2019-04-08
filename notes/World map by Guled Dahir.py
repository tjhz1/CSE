world_map = {
    'The dungeon':{
        'Name': "The prison",
        'Description': "Where you were sent to",
        'Paths': {
            'North': "Your prison cell",
        }
    },
    'Prison cell': {
        'Name': "Prison cell",
        'Description': "Where you are sleeping",
        'Paths': {
            'West': "The cafeteria",
        }
    }
    'The cafeteria': {
        'Name': "The cafeteria",
        'Description': "Where you get hardly any food and get bullied ",
        'Paths': {
            'West': "The gym"
        }
    }
    'The gym': {
        'Name': "The gym",
        'Description': "Where you plan an escape and work out",
        'Path': {
            'North': "The bosses office"
        }
    }
    'The bosses office': {
        'Name': "The bosses office",
        'Description': "Where the guy who look and makes us for his dirty work is",
        'Paths': {
            'West': "the weapons shop"
        }
    }
        'The weapons shop': {
        'Name': "The weapons shop",
        'Description': "where the prisoner get the weapons for the arena",
        'Paths': {
            'South': "The arena"
        }
    'The arena': {
        'Name': "The arena",
        'Description': "Where the prisoner fight each other",
        'Paths': {
            'East': "the healing area"
        }
    'The Healing area': {
        'Name': "The healing area",
        'Description': "Where the prisoner get healed after the fights",
        'Paths':
            'South' : "the arena"
        }
    'The arena': {
        'Name': "The arena",
        'Description': "Where the prisoner fight each other",
        'Paths': {
            'South':"The Power factory"
        }
    'The Power factory': {
        'Name': "The Power factory",
        'Description': "Where the prisoners do the punishment work time",
        'Paths':
            'West':"The woman area"
        }
    'The woman area': {
        'Name': "The woman area",
        'Descrition': "Where the woman prisoners are",
        'Path': {
            'North':"The coal mine"
        }
    'The coal mine': {
        'Name': "The coal mine",
        'Description': "Where the prisoners work for their crimes",
        'Paths':{
            'East':"the court"
        }
    'The court': {
        'Name': "the court",
        'Description': "Where the prisoners get judge",
        'Paths': {
            'North': "The exit"
        }
    'The exits':
        'Name': "The exit",
        'Description': "Where the prisoners get released for their time"
    }
}
# Controller
while playing:
    print(player.current_location.name)
    print(player.current_location.description)

    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command in directions:
        try:
            next_room = player.find_room(command)
            player.move(next_room)
        except KeyError:
            print("I can't go that way")
    else:
        print("Command not recognized.")
