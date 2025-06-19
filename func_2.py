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

# question 9

count = 10
while count >= 1:
    if count == 5:
        count -= 1
        continue
    print(count)
    count -= 1






