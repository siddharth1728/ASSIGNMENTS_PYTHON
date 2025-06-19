# #question1

def greet_user(name):
    return f"Hello, {name}!"
a = greet_user("John")
print(a)



# #question 2

def check_temperature(temp):

    if temp > 99:
        return "Fever"
    elif temp < 99:
        return "Normal"
    else:
        return "None"

    
a = check_temperature(143)
print(a)

# #question 3

fruits = ["apple", "banana", "cherry"]
def get_list_fruits(fruits):
    return fruits[-1]

a = get_list_fruits(fruits)

print(a)

#question4

def get_price_tag(price):
    if price > 1000:
        return "Expensive"
    else:
        return "Affordable" 
a = get_price_tag(1000)

print(a)

#question 5
def format_user_info(name,age):
    return f"Name: {name}, Age: {age}"

a = format_user_info("Alice", 30)
print(a)   

# question 6

def uppercase_if_string(value):
    if  isinstance(value, str):
        return value.upper()
    else :
        return "invalid input"
    
a = uppercase_if_string("shddciusd")
print(a)

# question 7
def safe_divide(num,den):
    result = num/den
    if den != 0:
        return result
    else:
        return "cannot divide"

a = safe_divide(5,2.5)
print(float(a))

#question 8

def check_login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == "admin" and password == "2468":
        return "Login successful"
    else:
        return "Login failed"
a = check_login()
print(a)

#question 9

def get_full_name(first_name, last_name):
    return f"{first_name} {last_name}"

a = get_full_name("john", "doe")
print(a.title())

#question 10

def get_discounted_price(price, is_memeber):
    if is_memeber:
        return price * 0.9
    else:
        return price
a = get_discounted_price(100, True)
print(a)

#june 17
 #question1

def accept_numbers(*args):
    return sum(args)
a = accept_numbers(1, 2)

print(a)
# question 2

def arguments(**kwargs):
    return kwargs
a = arguments(name="Alice", age=30, city="New York")
print(a)

#question 3

while True:
    a  = input("Enter a word: ")
    if a == "exit":
        print(a)
        break

# question 4
a = 1
while True:
    print(a)
    if a == 5:
        break
    a += 1

#question5



while True:
    a = int(input(("enter a number:")))
    if a < 0:
        break

# question 6

# question 7
names = []
while True:
    name = input("Enter a name (or press Enter to stop): ")
    if name == "":
        break
    names.append(name)
    
print("Names entered:", names)



