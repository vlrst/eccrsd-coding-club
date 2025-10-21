

phrase = input("Enter a phrase")

phrase =  list(phrase.split())


newstr = ""
space = None
for x in range(len(phrase)):
    string = list(phrase[x])
    if string[0] == string[0].upper():

        newstr += string[0]

    elif string[0] == string[0].lower():
        newstr += " "
        newstr += phrase[x]
        #space = True

'''
    if space:
        newstr += " "

   

    for i in range(len(phrase) - 1):
        nextElement = phrase[i + 1]
        if nextElement[0] == nextElement[0].upper():
            space = False
        elif nextElement[0] == nextElement[0].lower():
            space = True
'''




print(newstr)

'''

if ((int)(price*100 % 100) == 99) {
    price = int(price*100)/100.0
}


    # check
'''
