# # # # # # CONDITIONS
# # # # # x = int(input("enter a number:"))
# # # # # if x > 0:
# # # # #     print ("entered no_is positive")
# # # # # else:
# # # # #     print("entered no_is negative:")

# # # # # x = 2 

# # # # # if x < 7:
# # # # #     print("Hello")
# # # # # else:
# # # # #     print("Good morning")

# # # # # x = 2 

# # # # # if x > 7:
# # # # #     print("siddharth")
# # # # # elif x < 3:
# # # # #     print("chethan")
# # # # # else:
# # # # #     print("good morning")

# # # # # score = int(input("enter score:"))

# # # # # if score > 90:
# # # # #     print("Grade A")
# # # # # elif score >= 80:
# # # # #     print("Grade B")
# # # # # else:
# # # # #     print("Grade C")

# # # # # weather = input("enter weather condition:")
# # # # # if weather == "rainy":
# # # # #     print("carry an umbrella")
# # # # # elif weather == "sunny":
# # # # #     print("Wear sun glasses")
# # # # # else:
# # # # #     print("dont carry an umbrella")

# # # # # age = int(input("Enter Your Age:"))

# # # # # if age >= 18:
# # # # #     print("You are major")
# # # # # else:
# # # # #     print("You are minor")

# # # # x = 5
# # # # y = 10

# # # # if x > 0:
# # # #     print("x is positive")

# # # sentence = "Hello, World!"

# # # age = 112

# # # print(sentence)
# # # print(age)

# # # a = 2 + 3j
# # # print(type(a))
# # # print(a.real)
# # # print(a.imag)

# # # num = 3.14
# # # print(type(num))
# # # print(num)

# # # sentence = "Hello, World!"
# # # age = "112"
# # # temp = 87.8
# # # print(type(sentence))
# # # print(type(age))
# # # print(type(temp))

# # # sentence = "Hello, World!"

# # # can only contain letters and numbers 

# # # ciwusydbuds_6473643_ = "Hello, World!"
# # # print(ciwusydbuds_6473643_)

# # # variable names are case sensitive 

# # # key words cannot be used as variable names
# # # for, while, if, else, elif, import, from, as, def,

# # # anif = "Hello, World!"
# # # print(anif)


# # # phone_number_of_person = "123-456-7890"
# # # print(phone_number_of_person)

# # # string
# # # word = "beautiful"
# # # print(word[0])  # b# can access only through square brackets
# # # print(word[8])  # accesing elements with positive index
# # # print(word[-1])  # l # accessing elements with negative index  

# # # SLICING
# # # word = "beautiful"
# # # print(word[:5:]) 

# # # start = 0
# # # stop = 8
# # # print(word[start:stop:])

# # # print(word[0:10]) # stop index fix with last index

# # # check string content

# # # text = "heLlo$123"

# # # text = text.upper() #HELLO$123

# # # print(text.isalnum()) 

# # # print(text.isdigit())

# # # print(text.isupper())

# # # print(text.islower())

# # # print(text.isspace())

# # #string formatting
# # # name = "John"
# # # amount = 5000
# # # sentence = f"Dear {name}, your invoice of RS.{amount} is pending"
# # # print(sentence)

# # #Dear "john", how are you?
# # # name = "Dear 'john', how are you?"
# # # print(name)


# # #using f-strings(python 3.6+)

# # # name = "John"
# # # amount = 5000

# # # sentence = "Dear {}, your invoice is of Rs.{} pending".format(name,amount)


# # # sentence = "Dear {1}, your invoice is of Rs.{0} pending".format(name,amount)

# # # print(sentence)

# # name = "John"
# # amount = 5000

# # # sentence = "Dear {}, your invoice is of Rs.{3} pending".format(name,amount)

# # sentence = "Dear {name}, your invoice is of Rs.{amount} pending".format(name="charlie",amount=2000)

# # a,b,*c = 2,4,6,8
# # a, *b, c = 2,3,4,
# # "*" can access elements except the assigned one
# # print(a,b,c) #can only have exact no of values to axis from respective variable

# # multiple starred expressions not allowed
# # mulltiline string used by triple quotes

# # sentence = "This is a rainy day"

# # email = """Dear Sanjay,
# # How are you,
# # Thanks"""

# # print(email)

# # Escape CHARACTER

# # sentence = 'It\'s a rainy day' #back slash is ignored by python
# # print(sentence)

# # print("hello", "world", sep=";")

# # a = input("Enter your name:")
# # print(f"Hello {a}")


# # a = "3"
# # b = 4

# # print(a + b) #TypeError: unsupported operand type(s) for +: 'int' and 'str'

# # a = 3/
# # b = "4"
# # c = int(b)
# # print(float(a))
# # print(float(b)) # should have only numeric values

# # print(str(a) + str(b))


# # a = int(input("Enter first number:"))
# # b = int(input("Enter your second number:"))

# # print(f"The addition of {a} & {b} is : {a + b}")
# # print(f"The multiplication of {a} & {b} is : {a * b}")
# # print(f"The subtraction of {a} & {b} is : {a - b}")
# # print(f"The division of {a} & {b} is : {a / b}")

# # ask user to enter credit card no
# # print the credit number with last four digit masked with XXXX
# output = "XXXX XXXX XXXX "
# number = input("Enter credit card number:")

# a = number[::-1]
# print(a)

