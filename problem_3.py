'''

You are running a grocery tore and need to calculate the total price ba ed on the number of
item bought and whether the customer has a di count card. If the cu to mer ha a discount card,
they get a 20% di count on the total price.

'''


items = int(input("Enter your total number of items: "))
discount = bool(input("Discount? "))
price = float(input("What is the price of the items: "))

if discount:
    print(round(0.8*(items*price), 2))
else:
    print(round(items*price, 2))
