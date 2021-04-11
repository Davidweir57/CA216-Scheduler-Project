# Name: David Weir
# Student Number: 19433086
# I acknowledge all terms of DCU's Academic Integrity Policy

# 10 ms quantum

import copy

def round_robin(tasks):
    finished = [] # finished list of tasks in the correct order
    done = 0 # counter of how many tasks have been completed
    quantum = 10

    wait, turnaround = 0, [] # total wait time variables and list of turnaround times of the tasks

    editable = copy.deepcopy(tasks) # creates a copy list of tasks that can be edited when subtracting the quantum from burst time
    # the list is created as a deepcopy to allow for editing so that elements in the 2 lists do not share the same space in memory

    # loop while the number of finished tasks is less than the number of tasks
    while done < len(editable):
        i = 0

        # loops through the tasks in the list of tasks
        while i < len(editable):

            # if the burst value is greater than the quantum
            if int(editable[i][2]) > quantum:
                editable[i][2] = int(editable[i][2]) - quantum # subtract the quantum from the burst time
                wait = wait + quantum # increase the total wait time by the quantum
           
            else:

                # if this task is not already in finished tasks
                if tasks[i] not in finished:
                    done = done + 1 # increment done
                    wait = wait + int(editable[i][2]) # add the burst value to the total wait
                    turnaround.append(wait) # add the current value of wait to turnaround times list
                    finished.append(tasks[i]) # add the task to the list of finished tasks

            i = i + 1

    # dont include the last tasks burst time / quantum
    if int(finished[-1][2]) > quantum: # if burst is greater than quantum subtract the quantum
        wait = wait - quantum

    # else subtract the last tasks burst time
    else:
        wait = wait - int(finished[-1][2])

    return finished, wait / len(tasks), turnaround
