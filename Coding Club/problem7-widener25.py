hours, minutes = map(int, input().split())

stack = [(0,0)]
counter = 0

while stack:
   h,m = stack.pop()
   if h>= hours:
       continue
   if m>= minutes:
       stack.append((h+1, 0))
       continue
   time = (h, m)
   print(time)

