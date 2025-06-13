#managing tasks with a dictionary
managing_tasks = {
    "task1": input("enter task1: "),
    "task2": input("enter task2: "),
    "task3": input("enter task3: "),
}

managing_tasks["task2"] = input("update task2: ")
del managing_tasks["task3"]
print(managing_tasks)