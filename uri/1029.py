
casos = int(input())

for i in range(casos):
    numero = int(input())

    if numero == 1:
        print(f'fib(1) = 0 calls = 1')
    elif numero == 2:
        print(f'fib(2) = 2 calls = 1')
    else:
        termo1 = 0
        termo2 = 2

        termo3 = 1
        termo4 = 1

        for j in range(numero-2):
            fib = (termo1 + termo2) + 2
            
            termo1 = termo2
            termo2 = fib

            calls = termo3 + termo4

            termo3 = termo4
            termo4 = calls
        
        print(f'fib({numero}) = {fib} calls = {calls}')    
