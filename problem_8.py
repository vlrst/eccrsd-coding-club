'''

An aircraft manufacturing compa11y want to optimize boarding by minimizing the
inconvenience of seating layot1ts. Each row ha n seats and k aisles. The inconvenience is
defined a the sum of the di tances of each eat to the nearest aisle. For a layout equence
a1,a2, .. . ,ak+I (groups of eat separated by ai les), where each group i has a; seats:

• Di tance of a seat to the nearest ai le i the number of seats between them.
• The goal i to minimize the total inconvenience for a given nand k.

Ailes must be between two seats.

Input (assume the input is valid):

'''


inputs = input("Enter the input\n")
inputs = list(map(int, inputs.split()))
n = inputs[0]; k = inputs[1]

val=0
for x in range(0, k):
    val += x
    for n in range(0, n):
        val += n
        

print(val)
