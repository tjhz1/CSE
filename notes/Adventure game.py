class Room(object):
    # This is a constructor
    def __init__(self, name, north=None, south=None, east=None, west=None, description=""):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.description = description





class Items(object):
    def __init__(self, name):
        self.name = name


class Weapons(object):
    def __init__(self, name, damage):
        super(Weapons, self).__init__(name)
        self.damage = damage


class Bow(Weapons):
    def __init__(self, name, arrow, kills):
        super(Bow, self).__init__(name)
        self.arrows = 50
        self.kills = 10


class Potion(object):
    def __init__(self, name):
        self.name = name


class Growth(Potion):
    def __init__(self, name):
        super(Potion, self).__init__(name)
        self.size = 40


class Axe(Weapons):
    def __init__(self, name):
        super(Weapons, self).__init__(name)
        self.damage = 40


class Shrink(Potion):
    def __init__(self):
        super(Shrink, self).__init__("Shrink")


class Knife(Weapons):
    def __init__(self):
        super(Knife, self).__init__("Knife")
        self.damage = 20


class Speed(Potion):
    def __init__(self):
        super(Speed, self).__init__("Speed")


class Strength(Potion):
    def __init__(self):
        super(Strength, self).__init__("Strength")


class Sword(Weapons):
    def __init__(self):
        super(Sword, self).__init__("Sword")
        self.damage = damage


class Tools(Items):
    def __init__(self, name):
        super(Tools, self).__init__()
        self.name = name


class Drill(Tools):
    def __init__(self):
        super(Drill, self).__init__("Drill")


class Pickaxe(Tools):
    def __init__(self):
        super(Pickaxe, self).__init__("Pickaxe")


class Shovel(Tools):
    def __init__(self):
        super(Shovel, self).__init__("Shovel")
        self.shovel_amt = shovel_amt


class Food(Items):
    def __init__(self, name):
        super(Food, self).__init__()
        self.name = name


class Soup(Food):
    def __init__(self, name):
        super(Soup, self).__init__("Soup")


class Fish(Food):
    def __init__(self, name):
        super(Fish, self).__init__("Fish")


class Armor(Items):
    def __init__(self, name, armor_amt):
        super(Armor, self).__init__(name)
        self.armor_amt = armor_amt


class Healing(Potion):
    def __init__(self, name):
        super(Healing, self).__init__("Healing")
        self.health = 100


class Character(object):
    def __init__(self, name, health, weapons, armor):
        self.name = name
        self.health = health
        self.weapons = weapons
        self.armor = armor

class Player(Character):
    def __init__(self, weapons, potions, items, name, armor):
        super(Player, self).__inti__(name, weapons, armor)
        self.inventory = []


    def take_damage(self, damage):
        if damage < self.armor.armor_amt:
            print("No damage is done because of some Fabulous armor")
        else:
            self.health -= damage - self.armor.armor_amt
            if self.health < 0:
                self.health = 0
                print("%s ahs fallen" % self.name)
            print("%s has %d health left" % (self.name, self.health))

        def attack(self, target):
            print("%d attacks %s for %d damage" %
                  (self.name, target.name, self, weapon.damage))
            target.take_damgae(self.weapon.damage)


class Player(object):
    def __init__(self, starting_location):
        self.health = 100
        self.inventor = []
        self.current_location = starting_location

    def move(self, new_location):
        """This method moves a player to a new location

        :param new_location: The room object that we move to
        """
        self.current_location = new_location

    def find_room(self, direction):
        """This method takes a direction, and finds the variable of the room.

        :param direction: A String (all lowercase), with cardinal direction
        :return: A room object if it exists, None if it does not
        """
        name_of_room = getattr(self.current_location, direction)
        return globals()[name_of_room]


# These are the instances of the rooms (Instantiation)

# Option 1 - Use the Variables, but fix later
R19A = Room("Mr. Wiebe's Room")
parking_lot = Room("The Parking Lot", None, R19A)

R19A.north = parking_lot

# Option 2 - Use Strings, but more difficult controller
R19A = Room("Mr. Wiebe room", 'parking_lot', None, None, None, "This is your computer science class.")
parking_lot = Room("The Parking Lot", None, "R19A", None, None, "There are a few cars parked here")

player = Player(R19A)

directions = ['north', 'south', 'east', 'west', 'up', 'down']
short_directions = ['n', 's', 'e', 'w', 'u', 'd']
playing = True

# Controller
while playing:
    print(player.current_location.name)
    print(player.current_location.description)A

    command = input(">_")

    if command in short_directions:
        pos = short_directions.index(command)
        command = directions[pos]

    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command in directions:
        try:
            next_room = player.find_room(command)
            player.move(next_room)
        except KeyError:
             print("I can't go that way")

# Items
sword = Weapons("Sword", 10)
canoe = Weapons("Canoe", 84)
wiebe_armor = Armor("Armor of the Gods", 1000000000)

# Characters
prisnoner = Character("Prisoners", 100, sword, Armor("Generic Armor", 2))
wiebe = Character("Wiebe", 1000000000,canoe ,wiebe_armor)

prisnoner.attack(wiebe)
wiebe.attack(prisnoner)
wiebe.attack(prisnoner)

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



Prison_cell = Room("The Prison Cell", "Where the prisoners sleep")
Cafeteria = Room("Cafeteria","Where the prisoners eat",None, None, "The gym", None)
The_gym = Room("The gym","Where the prisoners plan an escape",None, None, None,"The dungeon")
The_dungeon = Room("The dungeon", "Where the worst prisoners live" ,None, None,"The office",None)
The_office = Room("The office","Where the boss of the prison is", None, None,None, "bathroom")
Bathroom = Room("Bathroom", "Where the prisoners do there business","The women area", None, None, None)
The_womenarea = Room("The_women area", "Where the women prisoner are", None, None, None, "The power factory")
the_powerfactory = Room('The power factory', "Where the prisoner do their punishments", None, None, "the arena")
the_arena = Room("the arena", "WHere prisoner battle each other", None, "The weapons shop", None, None,)
the_weaponsshop = Room("the weapons shop", "Where the prisoners get the their weapons for battle", None, None, None, "The medical area")
the_medicalarea = Room("The medical area", "Where the prisoners get fix after the fight in the arena","The boss office", None, None, None)
the_bossoffice = Room("the boss office", "Where the prisoners go to the", None, None, None, "The coal mine")
the_coalmine = Room("the coal mine", "Where the prisoner work for time", None, "the court", None, None)
the_court = Room("the court", "Where the prisoner get judge", "The exits", None, None, None)
the_exit = Room("the exit", "Where the prisoner get released")

class Player(object):
    def __init__(self, starting_location):
        self.health = 100
        self.inventor = []
        self.current_location = starting_location




    else:
        print("Command not recognized.")


