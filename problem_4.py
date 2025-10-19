'''

A per on is hopping for water bottle and wants to buy a pack where each bottle cost $0.75 or
le . Write a program that read the total price of the pack of water bottle a11d the number of
bottles it contains. The program should calculate the price of one bottle and determine whether
the person will purcha e the pack. Additionally, the program should print the price per bottle.

'''


price = float(input("price of bottles: "))
bottles = int(input("enter bottles: "))

if price/bottles >= 0.75:
    print(f"{round(price/bottles, 2)} YES")
else:
    print(f"{round(price/bottles, 2)} NO")
