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

