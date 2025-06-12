
#question 1
list = [['jack','apple'],['orange', 'kiwi'],['dragon', 'grape']]

print(list[2][0])

#question2
a = ((0,1),(2,3),(4,5))

print(a[2][1])

#question 3

list_students = [('Alist',23),('Bob',21)]

print(list_students[1][1])

#question 4

list1 = ([10,20],[30,40])

print(list1[1][1])

#question 5 

students = {
    "name1" : "siddharth",
    "name2" : "abhi"
    ""
    }
print(students["name1"])

#question 6

subject_marks = {
    "maths" : "90",
    "english" : "80",
    "science" : "85"
}
print(int(subject_marks["maths"][1]))

#question 7

dict_person = {
    "name" : "siddharth",
    "details" : {
        "age" : 23,
        "city" : "bangalore",
        "mail" : "sidd@gmail.com" }
}

print(dict_person["details"])

#question 8
billing_history = {
    "customer1" : [100, 200, 300],
    "customer2" : [150, 250, 350]
}
print(billing_history["customer1"])

#question 9
billing_dict =(
    {"user1" : "siddharth" , "age" : "23", "ammount" : "1000"},
    {"user2" : "abhi" , "age" : "21", "amount" : "2000"},
)
print(billing_dict[0]["ammount"])

#question 10

list_temp_city = [("hyderabad",30),("bangalore",25),("chennai",35)]
print(list_temp_city[2][1])

#question 11

list_students_scores = {
    "user_1" : "45",
    "user_2" : "50",
    "user_3" : "55"
}

print(list_students_scores["user_3"])

#question 12

products = [{
    "product1" : "laptop",
    "price" : 50000,},
    {
    "product2" : "mobile",
    "price2" : 20000    
}]
print(products[0]["product1"])

#question 13

list_subject_marks = [("subject1", 90), ("subject2", 80),]

print(list_subject_marks[1][1])

#question 14    

weekly_tasks= {
    "monday" : ("task1", "task2"),
    "tuesday" : ("task3", "task4"),
    "wednesday" : ("task5", "task6"),
    "thursday" : ("task7", "task8"),   
    "friday" : ("task9", "task10"),
    "saturday" : ("task11", "task12"),
    "sunday" : ("task13", "task14")
}

print(weekly_tasks["monday"][0])

#question 15

students = [
    {
        "name": "siddharth",
        "marks": {
            "Math": 78,
            "Science": 92,
            "English": 30
        }
    },
    {
        "name": "chethan",
        "marks": {
            "Math": 98,
            "Science": 96,
            "English": 95
        }
    }
]

print(students[1]["marks"]["Math"])

