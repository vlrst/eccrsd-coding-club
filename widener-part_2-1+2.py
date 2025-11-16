'''inputs = list(map(int, input("Enter an input\n").split()))
a, b, c = inputs[0], inputs[1], inputs[2]

if a + b + c == 180:
    if a == 60 and b == 60 and c == 60:
        result = "Equilateral"

    elif (a != b) and (b != c) and (a!=c):
        result = "Scalene"

    elif ((a!=b)  and (a!=c) and (b==c)) or ((b!=a)  and (b!=c) and (a==c)) or ((c!=a) or (c!=b) and (b==a)):
        result = "Isoceles"

else:
    result = "Error"

print(result)'''



counter = 1

num = '9780921418' + input("Enter a num\n")
inputs = list(map(int, num))

print(inputs)
total = 0

for x in range(len(inputs)):
 
    if counter % 2 == 1:
        total += inputs[x]*1
        print(f"{inputs[x]}*1")
    elif counter % 2 == 0:
        total += inputs[x]*3
        print(f"{inputs[x]}*3")
    
    counter += 1


if total % 10 == 0:
    print(f"{total} YES")
else:
    print(f"{total} NO")
