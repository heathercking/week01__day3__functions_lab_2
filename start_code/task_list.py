tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

#task 1

def uncompleted_tasks(list):
    task_list = []
    index = 0
    for item in list:
        if list[index]["completed"] == False:
            task_list.append(list[index]["description"])
        index += 1
    
    print(task_list)

uncompleted_tasks(tasks)

#task 2

def completed_tasks(list):
    task_list = []
    index = 0

    for task in list:
        if list[index]["completed"] == True:
            task_list.append(list[index]["description"])
        index += 1
    
    print(task_list)

completed_tasks(tasks)


# # 3. Print a list of all task descriptions

def task_descriptions(list):
    index = 0

    for item in list:
        print(list[index]["description"])
        index += 1

task_descriptions(tasks)

# # 4. Print a list of tasks where time_taken is at least a given time


def time_taken(list, min_time):
    index = 0

    for item in list:
        if list[index]["time_taken"] >= min_time:
            print(list[index]["description"])
        index += 1

time_taken(tasks, 15)

# 5. Print any task with a given description

def given_description(list, description):
    index = 0

    for item in list:
        if list[index]["description"] == description:
           print(list[index]) 
        index += 1

given_description(tasks, "Feed Cat")

#6. Given a description update that task to mark it as complete.

def status_update(list, description):
    index = 0

    for item in list:
        if list[index]["description"] == description:
            list[index]["completed"] = True
        index += 1

print(status_update(tasks, "Feed Cat"))
