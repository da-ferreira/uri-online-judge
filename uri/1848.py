
def binario(string):
    string = string.replace('-', '0')
    string = string.replace('*', '1')
    return string


piscadas = numero = 0

while piscadas != 3:
    corvo = input()

    if corvo != 'caw caw':
        numero += int(binario(corvo), 2)
    else:
        print(numero)
        piscadas += 1
        numero = 0
