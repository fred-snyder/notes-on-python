"""
Description:
1. Ask user for a string of text.
2. Ask user for a character.
3. Replace every occurance of that character in the string of text from step 1.
"""

# TODO: Check if this needs python34

from tkinter import Tk
r = Tk()
r.withdraw()

# ask user for input
print("Replace character by spaces: ")
print("============================")
print(" ")

str_var = r.selection_get(selection = "CLIPBOARD") 
char_var = input("Character: ")

# process user input
# replace every occurence of char_var in str_var
output = str_var.replace(char_var, " ")
print(" ")
print(output + "   >>>   Copy-ed to clipboard")
print(" ")

r.clipboard_append(output)

# wait for user input to exit the program
# input("Press Enter to continue..")
