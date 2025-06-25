class TV:
    def __init__(self, brand):
        self.brand = brand

    def turning_on(self):
        print(f"turning on {self.brand} TV")

    def turning_off(self):
        print(f"turning off {self.brand} TV")

class Remote:
    def __init__(self):
        self.tv = tv

    def turning_on(self):
        print("turning on ...")
    
    def turning_off(self):
        print("turning off ...")

tv = TV('Samsung')
remote = Remote()
remote.tv.turning_on()
remote.tv.turning_off()

#QUESTION2

class Car:
    def __init__(self, brand):
        self.brand = brand

    def starting_engine(self):
        print(f"turning on {self.brand} ")

    def stopping_engine(self):
        print(f"turning off {self.brand} ")

class Engine:
    def __init__(self):
        self.car = car

    def starting_engine(self):
        print("turning on ...")
    
    def stopping_engine(self):
        print("turning off ...")

car = Car('Audi')
engine = Engine()
engine.car.starting_engine()
engine.car.stopping_engine()


#question3

class Classroom:
    def __init__(self, room_no):
        self.room_no = room_no

    def turning_on(self):
        print(f"turning on light in Room-{self.room_no} ")

    def turning_off(self):
        print(f"turning off light in Room-{self.room_no} ")

class Light:
    def __init__(self):
        self.classroom = classroom

    def turning_on(self):
        print("turning on ...")
    
    def turning_off(self):
        print("turning off ...")

classroom = Classroom('420')
light = Light()
light.classroom.turning_on()
light.classroom.turning_off()



class Laptop:

    def __init__(self, brand):
        self.brand = brand

    def check_charge(self):
        print(f"your laptop's charging is {self.brand}")

class Battery:

    def __init__(self, charge):
        self.charge = charge
    
    def check_charge(self):
        print(f"your laptop's charging is {self.charge}")

laptop = Laptop("LENOVO")
battery = Battery()
battery.laptop.check_charge()
    

