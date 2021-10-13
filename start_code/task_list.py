tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

#task 1
task_list = []
index = 0

for task in tasks:
    if tasks[index]["completed"] == False:
        task_list.append(tasks[index]["description"])
    index += 1
    
print(task_list)

#task 2
task_list = []
index = 0

for task in tasks:
    if tasks[index]["completed"] == True:
        task_list.append(tasks[index]["description"])
    index += 1
    
print(task_list)
