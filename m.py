lst = []
while True:
    try:
        a = input()
        lst.append(a)
        if not a:
            break
    except EOFError:
        pass
    
