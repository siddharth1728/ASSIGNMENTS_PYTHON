# class device:

#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color
    
#     def turn_on(self):
#         print(f"turning on {self.brand} ")

#     def turn_of(self):
#         print(f"turning off {self.brand} ")

# bike = device('duke','orange')

# print(bike.brand)
# print(bike.color)


# class device:

#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color
    
#     def turn_on(self):
#         print(f"turning on {self.brand} ")

#     def turn_of(self):
#         print(f"turning off {self.brand} ")

# car = device('audi', 'brown')

# print(car.brand)
# print(car.color)

# class device:

#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color
    
#     def turn_on(self):
#         print(f"turning on {self.brand} ")

#     def turn_of(self):
#         print(f"turning off {self.brand} ")

# pc = device('lenovo', 'grey')

# print(pc.brand)
# print(pc.color)


# question 2

class Car:

    def __init__(self,model_no, speed, fuel_type):
        self.model_no = model_no
        self.speed = speed
        self.fuel_type = fuel_type

    def accelerate(self):
        print(f" {self.model_no} is accelerating at {self.speed}km/(hr)^2 ...")

    def stop(self):
        print(f" {self.model_no} is stopped")

    def honk(self):
        print(f" {self.model_no} Honk !!")

car = Car('audi_r8', '60', 'Petrol')

car.accelerate()
car.stop()
car.honk()


print("    ")



class Bike:

    def __init__(self,model_no, speed, fuel_type):
        self.model_no = model_no
        self.speed = speed
        self.fuel_type = fuel_type

    def accelerate(self):
        print(f" {self.model_no} is accelerating at {self.speed}km/(hr)^2 ...")

    def stop(self):
        print(f" {self.model_no} is stopped")

    def honk(self):
        print(f" {self.model_no} Honk !!")

    
bike = Bike('Royal_Enfield_classic_650', '80', 'Petrol')

bike.accelerate()
bike.stop()
bike.honk()



print(" ")



class Truck:

    def __init__(self,model_no, speed, fuel_type):
        self.model_no = model_no
        self.speed = speed
        self.fuel_type = fuel_type

    def accelerate(self):
        print(f" {self.model_no} is accelerating at {self.speed}km/(hr)^2 ...")

    def stop(self):
        print(f" {self.model_no} is stopped")

    def honk(self):
        print(f" {self.model_no} Honk !!")

truck = Truck('Ashok_Leyland', '67', 'Diesel')

truck.accelerate()
truck.stop()
truck.honk()

#Question3

class Teacher:
    def __init__(self, Name, subject):
        self.Name = Name
        self.subject = subject

    def name(self):
        print(f"{self.Name} is teaching {self.subject}")

teacher = Teacher('Kamlesh', 'Chemistry')

teacher.name()

class Student:
    def __init__(self, Name, subject):
        self.Name = Name
        self.subject = subject

    def name_stu(self):
        print(f"{self.Name} is listening to {self.subject} class")

teacher = Student('Akshar', 'Chemistry')

teacher.name_stu()

class Classroom:
    def __init__(self, classroom_no, exam):
        self.classroom_no = classroom_no
        self.exam = exam

    def students_exam(self):
        print(f"{self.classroom_no} is writing  {self.exam} mock test")

classroom = Classroom(401,'jee')

classroom.students_exam()


# question 4

class Product:
    def __init__(self,Brand, model, color ):
        self.brand = Brand
        self.model = model
        self.color = color

    def Mobile(self):
        print(f"{self.brand}_{self.model}_{self.color} is available ")

    def price(self):
        print(f"{self.brand} is 1_400_00")

mobile = Product('Iphone', '16promax', 'black')

mobile.Mobile()
mobile.price()


class Cart:
    def __init__(self,Brand, model, color ):
        self.brand = Brand
        self.model = model
        self.color = color

    def cart(self):
        print(f"{self.brand}_{self.model}_{self.color} is added in cart")

    def payment(self):
        print(f"select payment for ...{self.brand} ")

cart_ = Cart('Iphone', '16promax', 'black')

cart_.cart()
cart_.payment()

class User:
    def __init__(self,name,product, address, payment ):
        self.name = name
        self.product = product
        self.address = address
        self.payment = payment
    def payment_mode(self):
        print(f"select payment option for your product {self.product}: Google pay, phonepay, card")

    def payment_status(self):
        print(f"your paymnet is succesful for ....{self.product}")

user = User('Siddharth','Iphone', 'MIGH-Colony', 'Google Pay')

user.payment_mode()
user.payment_status()

print("-----------------Thankyou Visit Again---------------")







