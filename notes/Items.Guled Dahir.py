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

    def numbers_kills(self):
        self.kills = True

    def shot_arrow(self):
        self.arrows = 50

class Potion(object):
    def __init__(self, name):
        self.name = name


class Growth(Potion):
    def __init__(self, name):
        super(Potion, self).__init__(name)
        self.size = 40

    def growth_size(self):
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

    def mile_fast(self):



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
wiebe = Character("Wiebe", 1000000000,canoe ,wiebe_armor)

prisnoner.attack(wiebe)
wiebe.attack(prisnoner)
wiebe.attack(prisnoner)

Victor.weapons = Bow
Victor.damgae()
