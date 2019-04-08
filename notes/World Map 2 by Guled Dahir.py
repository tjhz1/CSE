class Room(object):
    # This is a constructor
    def __init__(self, name, description, north=None, south=None, west=None, east=None):
        self.name = name
        self.north = north
        self.south = south
        self.west = west
        self.east = east
        self.description = description

#  These are the instances of the rooms (Instantiation)


Prison_cell = Room("The prison Cell", "Where the prisoners sleep")
Cafeteria = Room("Cafeteria","Where the prisoners eat",None, None, "The gym", None)
The_gym = Room("The gym","Where the prisoners plan an escape",None, None, None,"The dungeon")
The_dungeon = Room("The dungeon", "Where the worst prisoners live" ,None, None,"The office",None)
The_office = Room("The office", "Where the boss of the prison is", None, None,None, "bathroom")
Bathroom = Room("Bathroom", "Where the prisoners do there business","The women area", None, None, None)
The_women_area = Room("The_women area", "Where the women prisoner are", None, None, None, "The power factory")
the_power_factory = Room('The power factory', "Where the prisoner do their punishments", None, None, "the arena")
the_arena = Room("the arena", "WHere prisoner battle each other", None, "The weapons shop", None, None,)
the_weapons_shop = Room("the weapons shop", "Where the prisoners get the their weapons for battle", None, None, None, "The medical area")
the_medical_area = Room("The medical area", "Where the prisoners get fix after the fight in the arena","The boss office", None, None, None)
the_boss_office = Room("the boss office", "Where the prisoners go to the", None, None, None, "The coal mine")
the_coal_mine = Room("the coal mine", "Where the prisoner work for time", None, None, None,"the court")
the_court = Room("the court", "Where the prisoner get judge","The exits", None, None, None)
the_exit = Room("the exit", "Where the prisoner get released")