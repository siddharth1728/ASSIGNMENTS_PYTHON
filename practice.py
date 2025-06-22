# # # # CONDITIONS
# # # x = int(input("enter a number:"))
# # # if x > 0:
# # #     print ("entered no_is positive")
# # # else:
# # #     print("entered no_is negative:")

# # # x = 2 

# # # if x < 7:
# # #     print("Hello")
# # # else:
# # #     print("Good morning")

# # # x = 2 

# # # if x > 7:
# # #     print("siddharth")
# # # elif x < 3:
# # #     print("chethan")
# # # else:
# # #     print("good morning")

# # # score = int(input("enter score:"))

# # # if score > 90:
# # #     print("Grade A")
# # # elif score >= 80:
# # #     print("Grade B")
# # # else:
# # #     print("Grade C")

# # # weather = input("enter weather condition:")
# # # if weather == "rainy":
# # #     print("carry an umbrella")
# # # elif weather == "sunny":
# # #     print("Wear sun glasses")
# # # else:
# # #     print("dont carry an umbrella")

# # # age = int(input("Enter Your Age:"))

# # # if age >= 18:
# # #     print("You are major")
# # # else:
# # #     print("You are minor")

# # x = 5
# # y = 10

# # if x > 0:
# #     print("x is positive")

# sentence = "Hello, World!"

# age = 112

# print(sentence)
# print(age)

# a = 2 + 3j
# print(type(a))
# print(a.real)
# print(a.imag)

# num = 3.14
# print(type(num))
# print(num)

# sentence = "Hello, World!"
# age = "112"
# temp = 87.8
# print(type(sentence))
# print(type(age))
# print(type(temp))

# sentence = "Hello, World!"

# can only contain letters and numbers 

# ciwusydbuds_6473643_ = "Hello, World!"
# print(ciwusydbuds_6473643_)

# variable names are case sensitive 

# key words cannot be used as variable names
# for, while, if, else, elif, import, from, as, def,

# anif = "Hello, World!"
# print(anif)


# phone_number_of_person = "123-456-7890"
# print(phone_number_of_person)

# string
# word = "beautiful"
# print(word[0])  # b# can access only through square brackets
# print(word[8])  # accesing elements with positive index
# print(word[-1])  # l # accessing elements with negative index  

# SLICING
# word = "beautiful"
# print(word[:5:]) 

# start = 0
# stop = 8
# print(word[start:stop:])

# print(word[0:10]) # stop index fix with last index

# check string content

# text = "heLlo$123"

# text = text.upper() #HELLO$123

# print(text.isalnum()) 

# print(text.isdigit())

# print(text.isupper())

# print(text.islower())

# print(text.isspace())

#string formatting
# name = "John"
# amount = 5000
# sentence = f"Dear {name}, your invoice of RS.{amount} is pending"
# print(sentence)

#Dear "john", how are you?
# name = "Dear 'john', how are you?"
# print(name)


#using f-strings(python 3.6+)

# name = "John"
# amount = 5000

# sentence = "Dear {}, your invoice is of Rs.{} pending".format(name,amount)


# sentence = "Dear {1}, your invoice is of Rs.{0} pending".format(name,amount)

# print(sentence)

name = "John"
amount = 5000

# sentence = "Dear {}, your invoice is of Rs.{3} pending".format(name,amount)

sentence = "Dear {}, your invoice is of Rs.{3} pending".format(name="charlie",amount=2000)