phrase = input("Enter a phrase")

phrase = list(phrase.split())

newstr = ""
space = None
wordsinPhrases = list[len(phrase)]

for x in range(len(phrase)):

    string = list(phrase[x])

    '''
    How to decide whether to put a space or not
    If there is an abbrv and the next one is also an abbrv, put no space
    else: space = False
    
    '''
    space = False
    beforeElement = string[0] 
    if string[0] == string[0].upper():
        newstr += string[0]
        
    if string[0] == string[0].lower():

        newstr += phrase[x]


