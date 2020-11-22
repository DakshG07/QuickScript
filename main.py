#Main Script for language.
#Accesses ".qs" files.
#(such as the test file we have here)
#TO USE: Edit the test.qs file with QuickScript code. Or, change the below variable to your QuickScript code path.
from modules import *
code_file = "test.qs"
with open(code_file) as f:
    #get code
    code_raw = f.read()

#Split code into list. Get all lines of code.
code = code_raw.split(".\n")
for line in code:
    #Split each line into it's keywords.
    words = line.split()
    #Make sure line isn't empty
    if words != [] and '#' not in line:
        #Validate function
        cmd = check_func(words[0])
        #Execute function
        exec(cmd, words, line)