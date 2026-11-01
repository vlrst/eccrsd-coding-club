
x = int(input())

for j in range(1, 10+1):
    if j % 2 == 0:
        print(int(str(x*j)[::-1]))
    else:print(x*j)
