# # # question_1

# # def max_of_num(a,b):
# #     if a > b:
# #         print(a)
# #     else:
# #         print(b)

# # max_of_num(2,3)

# # # question_2

# # nums = [1,44,58]

# # print(max(nums))
    
# # # question_3

# # def nature_of_num(a):
# #     if a > 0:
# #         print("Positive")
# #     elif a < 0:
# #         print("Negative")
# #     elif a == 0:
# #         print("Zero")

# # nature_of_num(4)

# # # question_4

# # def nature_of_num(a):
# #     if a%2 == 0:
# #         print("Number is even")
# #     else:
# #         print("The number is odd")

# # nature_of_num(3)

# # # question_5

# # def leap_year(a):
# #     if a%4 == 0:
# #         print("THIS IS A LEAP YEAR")
# #     else:
# #         print("NOT A LEAP YEAR")

# # leap_year(2025)

# # # question_6
# # text = input("Enter a character:")
 
# # def checking(a):
# #     if text.isalpha():
# #         print(f" {text} is an alphabet ")
# #     else:
# #         print(f"{text} is not an alphabet")

# # checking(3)
# # # question_7:


# # text = input("enter an alphabet")
# # def if_vowel_consonant():
# #     if text in 'aeiou':
# #         print("vowel")
# #     else:
# #         print("consonant")
# # if_vowel_consonant()
# # # question_8

# # text = input("Enter a character:")
 
# # def checking():
# #         if text.isalpha():
# #             print(f" {text} is an alphabet ")
# #         elif text.isdigit():
# #             print(f"{text} is a digit")
# #         else:
# #             print(f" {text} is a special character")

# # checking()

# # # question_9

# # text = input("Enter a character:")
 
# # def checking():
# #         if text.isupper():
# #             print(f" {text} is an uppercase ")
# #         elif text.isdigit():
# #             print(f"{text} is a lowercase")
        

# # checking()

# # question_10

# # # week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# # for week in range(0,8):
# #     print(week_days[int(input("Enter week number"))])

# # question_11

# def month_number():
#     month = int(input("Enter month number: "))
#     if month == 1:
#         print("January")
#     elif month == 2:
#         print("February")
#     elif month == 3:
#         print("March")
#     elif month == 4:
#         print("April")
#     elif month == 5:
#         print("May")
#     elif month == 6:
#         print("June")
#     elif month == 7:
#         print("July")
#     elif month == 8:
#         print("August")
#     elif month == 9:
#         print("September")
#     elif month == 10:
#         print("October")
#     elif month == 11:
#         print("November")
#     elif month == 12:
#         print("December")
#     else:
#         print("Invalid month number") 

# month_number()

# # question_12
# def notes_count():
#     amount = int(input("Enter the amount: "))
#     notes = [2000, 500, 100, 50, 20, 10, 5, 1]
#     note_count = {}

#     for note in notes:
#         if amount >= note:
#             count = amount // note
#             note_count[note] = count
#             amount -= count * note

#     print("Notes count:")
#     for note, count in note_count.items():
#         print(f"{note} : {count}")

# notes_count()

# # question_13

# def all_angles_of_triangle():
#     angle1 = int(input("Enter first angle: "))
#     angle2 = int(input("Enter second angle: "))
#     angle3 = int(input("Enter third angle: "))

#     if angle1 + angle2 + angle3 == 180:
#         print("The angles form a triangle")
#     else:
#         print("The angles do not form a triangle")


# all_angles_of_triangle()


# # question_14       
# def all_angles_of_triangle():
#     angle1 = int(input("Enter first angle: "))
#     angle2 = int(input("Enter second angle: "))
#     angle3 = int(input("Enter third angle: "))

#     if angle1 == angle2 == angle3:
#         print("The triangle is equilateral")
#     elif angle1 == angle2 or angle2 == angle3 or angle1 == angle3:
#         print("The triangle is isosceles")
#     else:
#         print("The triangle is scalene")

# all_angles_of_triangle()

# # question_15

# # x*2 + 4x + 4 = 0
# def roots_of_quadratic():
#     a = int(input("Enter coefficient a: "))
#     b = int(input("Enter coefficient b: "))
#     c = int(input("Enter coefficient c: "))

#     d = b**2 - 4*a*c

#     if d > 0:
#         root1 = (-b + d**0.5) / (2*a)
#         root2 = (-b - d**0.5) / (2*a)
#         print(f"The roots are real and different: {root1} and {root2}")
#     elif d == 0:
#         root = -b / (2*a)
#         print(f"The roots are real and the same: {root}")
#     else:
#         print("The roots are complex and not real")

# roots_of_quadratic()

# question_16
def add_two_numbers_without_operator():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
   
# question_17

def no_of_inputs():
    no_of_inputs = input("Enter any thing :")
    count = 0
    for char in no_of_inputs:
        count += 1
    print(f"Number of inputs: {count}")

no_of_inputs()

# question_18

def size_of_variables():
    a = 10
    b = 20.5
    c = "Hello"
    d = True

    print(f"Size of integer variable: {a.__sizeof__()} bytes")
    print(f"Size of float variable: {b.__sizeof__()} bytes")
    print(f"Size of string variable: {c.__sizeof__()} bytes")
    print(f"Size of boolean variable: {d.__sizeof__()} bytes")

size_of_variables()
        








