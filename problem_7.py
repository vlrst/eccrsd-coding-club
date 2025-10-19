arr = input("Enter the array ")
arr = arr.split()
unsort = list(arr)

arr.sort()

print(arr)
print(unsort)



value = 0
sorted_x = 0
original_x = 0
print(unsort.index("3"))
for x in range(len(arr)):
    
    print(f"{arr[x]} has a distance of {unsort.index(arr[x])}")
    print(f"unsort.index(arr[x]) - {unsort.index(arr[x])} and that is equal to {unsort[(int(arr[x-1]))]}")
        
    
    
    
print(value)
