# Name: David Weir
# Student Number: 19433086
# I acknowledge all terms of DCU's Academic Integrity Policy

def run(tasks, scheduler):

    print(f"{scheduler}:") # prints scheduler that was used

    for task in tasks:
        name, priority, burst = task[0], task[1], task[2] # assigns name priority and burst to variables for formattings

        print(f"Running task = {name} {priority} {burst} for {len(tasks)} units.")

    print()