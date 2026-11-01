x = int(input())


for i in range(1, x+1):
    for j in range(1, i+1):
        print(j, end="")
    
    for j in range(i-1, 0, -1): #most important line of code here
        print(j, end="")
    print()
