# Name: David Weir
# Student Number: 19433086
# I acknowledge all terms of DCU's Academic Integrity Policy

def task_validate(tasks):
    # if a task ([name], [priority], [CPU burst]) has too many variables or too few (i.e. missing one of the 3)
    # 
    error = 0

    # loops through each task
    for task in tasks:
        if (len(task) != 3): # if the task is missing a variable or has too many increment error
            error = error + 1
    
    if error != 0:
        print("Invalid tasks: too many/too few elements.")
        return 1
    else:
        return 0

def buffer_validate(tasks):
    # checks that the buffer is a valid number input

    error = 0

    for task in tasks:
        burst = task[2]

        if (burst.isnumeric() == False): # if the CPU burst variable is not a digit incremnent error
            error = error + 1

    if error != 0:
        print("Burst value is not a valid input.")
        return 1
    else:
        return 0

def priority_validate(tasks):
    # checks that the priority variable is a valid number input

    error = 0

    for task in tasks:
        burst = task[1]

        if (burst.isnumeric() == False): # if the priority variable is not a digit incremnent error
            error = error + 1

    if error != 0:
        print("Priority value is not a valid input.")
        return 1
    else:
        return 0

