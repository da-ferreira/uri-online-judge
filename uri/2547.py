
while True:
    try:
        visitantes, altura_min, altura_max = map(int, input().split())
        quantidade = 0

        for i in range(visitantes):
            altura = int(input())
            if altura >= altura_min and altura <= altura_max:
                quantidade +=1
        
        print(quantidade)
    except EOFError:
        break
