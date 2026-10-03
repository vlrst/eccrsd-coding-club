x = input()

flag =False


if x[0] == '"' and x[len(x)-1] == '"':


    try: 
        val = (x[::-1][1]) # [1] because [0] is always a "
    except Exception as e:
        print("No Letter Found")
        flag = True


    if not flag:
        print(val)




