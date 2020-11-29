import sys
#Check if functions exist.
def check_func(word):
    #Commands
    commands = ['LOG']
    #Get word in lowercase; follow DRY.
    #Check if word exists.
    if word in commands:
        return word
    #If word doesn't exist(nothing returns), return None.
    return None

def exec(cmd, words, line):
    #Link command with function, then execute function. 
    commands = {'LOG' : say, None : none}
    #Run function linked with command.
    commands[cmd](words, line)

#For Say function
def say(words, line):
    #Variables
    string = ""
    inString = False
    markdown = False
    
    #Get characters
    chars = splitWord(line)
    for char in chars:
        #Quote found. Start/end string.
        if char == '"':
            if not inString:
                inString = True
            else:
                inString = False
        elif char == '\\':
            if markdown:
                string += char
                markdown = False
            else:
                markdown = True
        elif markdown:
            if char == 'n':
                string += "\n"
                markdown = False
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
