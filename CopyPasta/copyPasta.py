"""
This is a simple `interpreter` for the CopyPasta esoteric
programming language. The language was made by user: BoutonIA 
on 19 April, 2018. The intended purpose is to promote copy pastas.

The language has only 4 builtin commands.
Copy : Copy the text of the following line to the clipboard
CopyFile : Copies all text from a program (the name specified on the next lie) to the clipboard. If however the
	name is not any sort of file-name, it will copy the source code of itself.
Duplicate : Duplicate the text in the clipboard as many times as the following line specifies
Pasta! : Display the clipboard and stop the program
"""
import pyperclip #So we can use the clipboard
from sys import argv #So we can get command-line arguments

def tokenizer(prog): #Takes in a program and returns a stream of tokens
	tokens = prog.split('\n') #Each line is a token
	tokens = [token + '\n' for token in tokens] #Add new line character
	return tokens #Return the stream of tokens

def file_exists(file_name): #returns True / False on if this file exists
	try: #Tries to open the file
		open(file_name, 'r')
	
	except: #If any errors occur, assume it does not exist
		return False

	else: #Otherwise, no errors occur, then the file exists
		return True

def interpreter(prog): #Interprets the given program
	raw_program = prog #Saves the raw program itself
	tokens = tokenizer(prog) #For our case we only really need tokens

	pointer = 0 #Points to current statement in program

	while pointer < len(tokens): #While there are still things to execute
		statement = tokens[pointer] #Get the statement to execute

		if statement.upper() == "PASTA!\n": #Prints whatever is on teh cipboard and stops program
			print(pyperclip.paste()) #Print out whatever is on the clipboard
			break #Exit execution loop

		elif statement.upper() == "DUPLICATE\n": #If we are duplicating whatever is on the clipboard N times
			#If there is a value in the list of statements next, and it IS a number
			if pointer + 1 < len(tokens) and tokens[pointer+1].strip().isdigit():
				#Gets the number of times we want to duplicate whatever is on the clipboard
				duplication = int(tokens[pointer+1].strip())
				#Duplicate the thing on the clipboard and save it
				pyperclip.copy(pyperclip.paste() * duplication)
				pointer += 2 #Increase pointer by 2 since we used to values (command and a number)

			else: #If there either isn't a number or just no value
				print("Expected a number on the next line after DUPLICATE!")
				print("Look around LINE: " + str(pointer + 1))
				break #Stop executing the program

		elif statement.upper() == "COPY\n": #If we are copying the next line to the clip board
			if pointer + 1 < len(tokens): #If there is a value we can copy to the clipboard
				pyperclip.copy(tokens[pointer + 1]) #Copy text to clipboard
				pointer += 2 #Increase program pointer by 2 (we used a statement and a value)

			else: #We expected some text to copy
				print("Expected some text to copy on the line after COPY!")
				print("Look around LINE: " + str(pointer + 1)) #Give line number
				break #Exit execution

		#Copies contents of the file specified on the next line
		#(Copies own source code if not a file that exists)
		elif statement.upper() == "COPYFILE\n":
			if pointer + 1 < len(tokens): #there is SOME sort of text we can copy
				file_name = tokens[pointer + 1] #gets the name of the file
				
				if file_exists(file_name.strip()) == True: #If this file exists, copy the contents
					#Copy everything from the file onto the clip board
					pyperclip.copy(open(file_name.strip(), 'r').read())

				else: #Otherwise, copy this program's own source code
					pyperclip.copy(raw_program) #Copy this program

				pointer += 2 #Progress by 2, we used a command and SOME value

			else: #Otherwise, there is no file to copy (or anything to copy)
				print("Expected some value to be able to copy after COPYFILE command")
				print("Look around LINE: " + str(pointer + 1))
				break #Exit execution

		else: #Otherwise, not a command, just go to next command
			pointer += 1

if __name__ == "__main__": #If this program is ran and not imported
	try: #test to make sure this program exists, or was even given
	#Checks to see if this program even exist
		open(argv[1], 'r')

	except IndexError: #If a program was not even given to us
		print("--No program was specified--")

	except FileNotFoundError: #IF the given prgram does not exist
		print("--Couldn't locate " + argv[1] + " in current directory--")

	else: #If the program does exist
		#Start up the interpreter
		interpreter(open(argv[1], 'r').read())
