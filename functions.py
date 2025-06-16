# #question1

# def greet_user(name):
#     print(f"Hello, {name}!")



# greet_user("Alice")




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
