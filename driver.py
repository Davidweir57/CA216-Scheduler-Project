#!/usr/bin/env python3

# tasks is in the format
#
# [name] [priority] [CPU burst]
#

# Name: David Weir
# Student Number: 19433086
# I acknowledge all terms of DCU's Academic Integrity Policy

import sys
from error import *
from files import file_handle
from schedule import schedule

def main():

    error = 0

    processes = [] # stores all tasks in the text file as a list of lists with their name priority and CPU burst
    
    # opens the text file with the tasks
    processes = file_handle(sys.argv[1])

    # error handling
    error = error + task_validate(processes) # checks that the task list contain only name, priority and burst
    error = error + buffer_validate(processes) # checks that the buffer is a valid number input
    error = error + priority_validate(processes) # checks that priority is a valid number input

    # if an error is found exit the program. Error is printed in the function
    if error != 0:
        exit()

    else:
        schedule(processes) # runs schedule function on the process

if __name__ == '__main__':
    main()