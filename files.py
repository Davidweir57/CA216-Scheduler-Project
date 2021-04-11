# Name: David Weir
# Student Number: 19433086
# I acknowledge all terms of DCU's Academic Integrity Policy

def file_handle(file):

    processes = []

    with open(file, 'r') as file:

        # loops through each line of the file
        for line in file.readlines():
            line = line.replace(',', " ") # removes any commas "," replacing them with whitespace
            line = line.strip().split() # strips the line and splits it so each bit of information is an element

            processes.append(line) # adds the task to the processes list
    
    return processes