

class AC: #class decleration is done
    def __init__(self,brand, color, ):
        self.brand = brand
        self.color = color


    def turn_on(self):
        print("turning on ac")

    def turn_off(self):
        print("turning off acc")

# print(type(AC))

ac = AC('samsung', 'white')

ac2 = AC("HAIER", "white")
ac2.brand()
# AC.color = "blue"
# # ac2 = AC()
# print(type(ac))

# print(ac.brand)

# print(ac is ac2) #not pointed to same memory location hence gives false

# print(ac.turn_on())

# whenever we initialise we have one actual object
# if you initialise again it has an other object which  has different memory location 

