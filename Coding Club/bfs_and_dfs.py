# DEPTH FIRST SEARCH - GO DEEP BEFORE YOU GO WIDE
# usually used to preserve memory, but does not matter in competition
# *sometimes you need to be able to tell the exact path that you took



# BREADTH FIRST SEARCH - GO WIDE BEFORE YOU GO DEEP
# always finds the shortest path
# isn't always optimal to recreate your way to the answer, it makes a bunch of separte lists
# use BFS for almost always all programming competitions because they will ask you for the shortest route


# you implement these the same every time, using a Queue (data structure)


# like a line at a grocery store

# starting customers
q = [1,2]

# new people go to the back
q.append(3,4)

# when people are done, they go out from the front, assuming that nobody is in a rush
q.pop()
