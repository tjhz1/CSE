 class Vehicle(object):
    def __init__(self, name):
        self.name = name


class Car(Vehicle):
    def __init__(self, name):
        super(Car, self).__init__(name)
        self.engine_status = False
        self.fuel = 100

    def start_engine(self):
        self.engine_status = True
        print("You turin the key and the engine starts")

    def move_forward(self):
        self.fuel -= 1
        print("You move forward")

    def turn_left(self):
        self.fuel -= 1
        print("He's Making a Left Turn")

    def turn_off(self):
        self.engine_status = False
        print("You turn the engine off")


class Viper(Car):
    def __init__(self):
        super(Viper, self).__init__("Viper")


class Tesla(Car):
    def __init__(self):
        super(Tesla, self).__init__("Tesla")

    def start_engine(self):
        self.engine_status = True
        print("You push the button and the engine starts")


guled_car = Viper()
guled_car.start_engine()
guled_car.move_forward()
guled_car.turn_left()
guled_car.move_forward()
guled_car.turn_off()
print()

guled_car = Tesla()
guled_car.start_engine()
guled_car.move_forward()