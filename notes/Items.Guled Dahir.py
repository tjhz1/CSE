class Items(object):
    def __init__(self, name):
        self.name = name


class Weapons(object):
    def __init__(self, name, damage):
        super(Weapons, self).__init__(name)
        self.damage = damage

class Bow(Weapons):
    def __init__(self, name):
        super(Bow, self).__init__("Bow", 20)
        self.arrows = 50
        self.kills = 10

    def numbers_kills(self):
        self.kills = True

    def shot_arrow(self):
        self.arrows = 50

class Potion(object):
    def __init__(self, name):
        self.name = name
        self.change = change

    def change_time(self):
        self.change = True
        print("Your have change due to the potion")


class Growth(Potion):
    def __init__(self, name):
        super(Potion, self).__init__(name)
        self.size = 40

    def over_time(self):
        self.change = True
        print("You have grown due to the potion")


class Axe(Weapons):
    def __init__(self, name):
        super(Weapons, self).__init__(name)
        self.damage = 40


class Shrink(Potion):
    def __init__(self):
        super(Shrink, self).__init__("Shrink")

    def over_time(self):
        self.change = True
        print("You have shrunk due to the potion")


class Knife(Weapons):
    def __init__(self):
        super(Knife, self).__init__("Knife", 20)
        self.damage = 20


class Speed(Potion):
    def __init__(self):
        super(Speed, self).__init__("Speed")

    def over_time(self):
        self.change = True
        print("You have gotten faster due to the potion")


class Strength(Potion):
    def __init__(self):
        super(Strength, self).__init__("Strength")


class Sword(Weapons):
    def __init__(self):
        super(Sword, self).__init__("Sword", 50)
        self.damage = damage


class Tools(Items):
    def __init__(self, name):
        super(Tools, self).__init__("Tools")
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

class Pizza(Food):
    def __init__(self, name):
        super(Pizza, self).__init__("Pizza")


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

def take_damage(self, damage):
    if damage < self.armor.armor_amt:
        print("No damage is done because of some Fabulous armor")
    else:
        self.health -= damage - self.armor.armor_amt
        if self.health <0:
            self.health = 0
            print("%s ahs fallen" % self.name)
        print("%s has %d health left" % (self.name, self.health))

    def attack(self, target):
        print("%d attacks %s for %d damage" %
            (self.name, target.name, self,weapon.damage))
        target.take_damgae(self.weapon.damage)


# Items
sword = Weapons("Sword", 10)
canoe = Weapons("Canoe", 84)
wiebe_armor = Armor("Armor of the Gods", 1000000000)

# Characters
prisnoner = Character("Prisoners", 100, sword, Armor("Generic Armor", 2))
Boss = Character("Boss", 1000000000, canoe, wiebe_armor)

Victor.weapons = Bow, Sword, knife, potion
Victor.damgae()
Victor.change()