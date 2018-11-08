"""
This is a simple interpreter for the esoteric programming language Deadfish.
The commands are as follows:
    i - Incriment value stored in accumulator
    d - Decriment value stored in accumulator
    s - Squares the value stored in the asccumulator
    o - Print out the value stored in the accumulator

The value in the accumulator can only be between 0 - 255 (8 bits)
"""
from sys import argv #So we can get a program from the command line

if len(argv) == 1: #If there are no files given to execute
    print("No program was given to the Deadfish interpreter!")
    quit() #Quits the program

try: #Try to load the program for us to execute
    program = open(argv[1], 'r').read()

except FileNotFoundError: #Raise an error, program does not exist
    print("Program given does not exist in current directory!")
    quit() #Quit the program

accumulator = 0 #The multi-use ONLY variable

#Go through every character (instruction) in our program
for command in program:
    if command == 'i': #If we are incrimenting the value in the accumulator
        accumulator += 1 #Increase the value by 1

        if accumulator > 255: #If our number is too large, wrap it down to 0
            accumulator = 0

    elif command == 'd': #If we are decrimenting the value in the accumulator by 1
        accumulator -= 1 #Subtract 1 from the accumulator

        if accumulator < 0: #If the value in the accumulator is < 0, wrap it around to 255
            accumulator = 255

    elif command == 's': #If we are squaring the value stored in the accumulator
        #Squares the value in the accumulator (accumulator * accumulator)
        accumulator = accumulator ** 2

    elif command == 'o': #If we are printing out the number stored in the accumulator
        print(accumulator) #Just print out the number
