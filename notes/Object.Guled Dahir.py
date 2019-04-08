class Plane(object):
    def __init__(self, colour):
        # Thing that the plane has.
        # Everything in the list should be relevant to the program.
        self.engine: "Turbo pop"
        self.passengers = 20
        self.fuel = 100
        self.color = colour
        self.functioning = True

    def fly(self):
        if self.functioning:
            # Plane all fueled up
            if self.fuel >= 100:
                print("The plane fuels up quickly")
                return

            # Plane is all fuel up
            if self.fuel >= 100:
                print("The plane is already fuel up")
                self.fuel = 100

        # Plane is out of fuel
            else:
                print("The plane is now at %d%%" % self.fuel)

        else:
            print("It crashed. Good job")

    def crash(self):
        self.functioning = False
        print("I went to go fly the plane")
        print()
        print()
        print()
        print(".....AND I CRASHED IT")

    def use(self, time):
        self.fuel -= time
        print("You use the plane for $s minutes" % time)


my_plane = Plane("Red")

my_plane.use(40)
my_plane.use(20)
my_plane.use(1000)
my_plane.use()
my_plane.use(20)