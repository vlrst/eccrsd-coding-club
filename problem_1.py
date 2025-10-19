'''

You are give11 the length of three sides of a triangle: a, b, and c. Your ta k is to calculate the
area of the triangle using Heron' formula written below.

'''


from math import sqrt

a = 6
b = 8
c = 12
s = (a+b+c)/2
area = sqrt(s*(s-a)*(s-b)*(s-c))

print((area // 0.01) / 100)
