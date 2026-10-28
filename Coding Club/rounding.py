x = 5.67890


def roundX(original, x: int):
    chopper = 10**x;
    print(original*chopper)
    print(round(chopper*original))
    print(int(round(chopper*original)/chopper))



print(x*100)
print(round(x*100))
print(int(round(x*100)/100))


print(roundX(x, 2))
z = 3.99
print(int(z))
print(z-(int(z)))
if z - int(z) >= 0.99: # >= because z - int(z) == 0.990000002 
    z = round(z,0)
    print(z)
