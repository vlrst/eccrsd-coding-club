import math
x = input()
chars = len(x);

total = 0

for i in range(chars):
    total += math.pow(int(list(x)[i]), i+1)
   # print(f" {chars} I { i+1} ")


print("YES" if int(x) == total else "NO")
