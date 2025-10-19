cost = 0
items = input("Enter the items ")
for x in range(len(items)):
    if items[x] == "g":
        cost += 1
    elif items[x] == "y":
        cost += 2
    elif items[x] == "r":
        cost += 3
        
print(cost)
