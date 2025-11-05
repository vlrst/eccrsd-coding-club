value = 0
arr = input().split()
unsort = list(arr)
arr.sort()
for x in range(len(unsort)):
    for y in range(len(arr)):
        if unsort[x] == arr[y]:
            value += abs(x-y)
print(F"This is the value {value}")
