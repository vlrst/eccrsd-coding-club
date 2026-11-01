num = int(input())
high = 1
for x in range(1, num+1):
    total =0
    counter =0 
    #print("the x is", str(x))
    for i in range(x, num+1):
        total += i
        counter+=1;
        if total == num:
            #print(f"Counter: {counter}")
            if counter > high:
                high = counter;
            break
        if total > num:
            break
        #print("Total: " + str(total))

print("IMPOSSIBLE" if high == 1 else high)
