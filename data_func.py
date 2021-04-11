# Name: David Weir
# Student Number: 19433086
# I acknowledge all terms of DCU's Academic Integrity Policy

from schedule_priority import schedule_priority
from schedule_fcfs import schedule_fcfs
from schedule_sjf import schedule_sjf

# functions to find average waiting time and turnaround times for fcfs, sjf and priority scheduling
# rr scheduling is calculated in the schedule_rr.py file


# calculates the average wait time of all the tasks
def avg_wait(tasks):
    
    avg = 0

    for task in tasks[:-1]: # ignores the last tasks burst time as no task will be waiting for it to finish
        avg = avg + int(task[2]) # adds the burst time of each task to wait time

    avg = avg / len(tasks)

    return avg

# calculates turnaround time for all tasks
def turnaround(tasks):

    currWait = 0
    
    for task in tasks:
        print("{process} turn around time: {time}".format(process=task, time = currWait + int(task[2]))) # prints the turnaround time of each task

        currWait = currWait + int(task[2])

    return "\n"

def collectData(processes, rr_schedule, rr_wait, rr_turnaround):

    print("AVERAGE WAIT TIMES\n")
    # finds the average waiting time of each scheduler
    print("FCFS: " + str(avg_wait(processes)))
    print("SJF: " + str(avg_wait(schedule_sjf(processes))))
    print("Priority: " + str(avg_wait(schedule_priority(processes))))
    print("Round-Robin: " + str(rr_wait))

    # prints the turn around times of every task for each scheduler

    print("\nTURNAROUND TIMES\n")

    print("FCFS:")
    print(turnaround(processes))

    print("SJF:")
    print(turnaround(schedule_sjf(processes)))

    print("Priority:")
    print(turnaround(schedule_priority(processes)))

    print("Round Robin:")

    # loops through the list tasks sorted by round robin and prints the turnaround times of each task
    for i in range(len(rr_schedule)):
        print("{process} turn around time: {time}".format(process=rr_schedule[i], time = rr_turnaround[i]))