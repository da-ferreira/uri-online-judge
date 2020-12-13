
while True:
    try:
        string = input()

        r = string[0:string.index('+')]
        l = string[string.index('+')+1:string.index('=')]
        j = string[string.index('=')+1:]

        if r.isdigit() and l.isdigit():
            print(int(r) + int(l))
        elif r.isdigit() and j.isdigit():
            print(int(j) - int(r))
        else:
            print(int(j) - int(l))

    except EOFError:
        break
