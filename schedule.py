# Name: David Weir
# Student Number: 19433086
# I acknowledge all terms of DCU's Academic Integrity Policy

from data_func import collectData
from schedule_priority import schedule_priority
from schedule_fcfs import schedule_fcfs
from schedule_sjf import schedule_sjf
from schedule_rr import round_robin
from CPU import run

def schedule(processes):
    processes = schedule_fcfs(processes) # runs fcfs scheduler on the list of tasks

    run(processes, "FCFS") # sends the sceduled list to the run function in CPU.py
    run(schedule_sjf(processes), "SJF") # runs sjf scheduler on the list of tasks and sends it to run()
    run(schedule_priority(processes), "Priority") # runs fcfs scheduler on the list of tasks and sends it to run() function

    rr_schedule, rr_wait, rr_turnaround = round_robin(processes) # runs round robin scheduler and returns the sorted tasks, average wait time and turn around times of each task
    run(rr_schedule, "Round Robin") # sends rr scheduler to the run() function

    collectData(processes, rr_schedule, rr_wait, rr_turnaround) # collects data on turnaround times and average waiting times for eash task
