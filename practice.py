def say_hello():

    print("Hello, World!")
say_hello()

# 
def add_numbers(a,b):
    sum_result =  a + b
    print(sum_result)
add_numbers(5, 10)

# 

def greet(name):

    print(f"Starting the greeting function for {name}")
    result = f"Hello, {name}!"
    print("Finishing the greeting function")
    return result

print("Program starts")
message = greet("Alice")
print(f"Returned message : {message}")
print("Program ENDS")

# 

def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type} named {pet_name}.")

describe_pet("dog", "Buddy")
