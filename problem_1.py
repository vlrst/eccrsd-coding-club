from math import sqrt

a = 6
b = 8
c = 12
s = (a+b+c)/2
area = sqrt(s*(s-a)*(s-b)*(s-c))

print((area // 0.01) / 100)
