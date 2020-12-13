
joias = set()
while True:
    try:
        joias.add(input())
    except EOFError:
        print(len(joias))
        break
