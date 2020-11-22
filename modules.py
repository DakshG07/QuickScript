import sys
#Check if functions exist.
def check_func(word):
    #Commands
    commands = ['say']
    #Get word in lowercase; follow DRY.
    lword = word.lower()
    #Check if word exists.
    if lword in commands:
        return lword
    #If word doesn't exist(nothing returns), return None.
    return None

def exec(cmd, words, line):
    #Link command with function, then execute function. 
    commands = {'say' : say, None : none}
    #Run function linked with command.
    commands[cmd](words, line)

#For Say function
def say(words, line):
    #Variables
    string = ""
    inString = False
    
    #Get characters
    chars = splitWord(line)
    for char in chars:
        #Quote found. Start/end string.
        if char == '"':
            if not inString:
                inString = True
            else:
                inString = False
        #If in string, add character to string.
        elif inString:
            string += char
    #output string.
    print(string)

#Handle no function error
def none(words, line):
    print("---\nERROR: Function was undefined.\n---")
    #Kill program
    sys.exit()

#split word into characters
def splitWord(word): 
    return [char for char in word]