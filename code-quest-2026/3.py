
x = input()
split = x.replace("-", " ").split()
if len(split) > 1:
    for word in split:
        print(word[0].upper(), end='')


