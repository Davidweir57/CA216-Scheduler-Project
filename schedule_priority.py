# Name: David Weir
# Student Number: 19433086
# I acknowledge all terms of DCU's Academic Integrity Policy

def schedule_priority(processes):
    # sorts the list of tasks based on the priority value

    return sorted(processes, key=lambda x: int(x[1]))
