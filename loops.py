#question1
for numbers in range(1,6):
    print(numbers)

#question2

for numbers in range (10,20,2):
    print(numbers)

#question3
names = [input("Enter a name: ") for _ in range(2)]
for name in names:
    print(name)

#question4

numbers = [1, 2, 3, 4, 5]
for squares in numbers:
    print(squares ** 2)

#question5

details = [{
    "name": "Alice",
    "age": 30
}, {
    "name": "Bob",
    "age": 25
}, {
    "name": "Charlie",
    "age": 35
}] 

for detail in details:
    print(f"{detail["name"]}, {detail["age"]}")

# #question 6

list_fruits = [["apple", "banana", ],["grape","mango"]]
for fruit in list_fruits:
    for item in fruit:
        print(item)

# question 7
a = input("Enter a string: ")
for char_ in a:
    print(char_)
    
# question 8

for i in range(5,0,-1):
    print(i)

# question 9

details = [{
    "subject": input("Enter subject: "),
    "marks": int(input("Enter marks: "))
   }
    for _ in range(3)]
for detail in details:
    print(f"{detail['subject']}: {detail['marks']}")

# question 10

products = [("apple", 10), ("banana", 20), ("orange", 30)]
for product in products:
    name, price = product
    print(f"Product: {name}, Price: {price}")
