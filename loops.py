
for numbers in range(1,6):
    print(numbers)

#question2

for numbers in range (10,20,2):
    print(numbers)

#question3
# names = [input("Enter a name: ") for _ in range(2)]
# for name in names:
#     print(name)

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