valores = input().split(' ')

pi = 3.14159

triangulo = (float(valores[0]) * float(valores[2])) / 2  # <- Área do triângulo retângulo.
circulo = (float(valores[2]) ** 2) * pi  # <- Área do circulo
trapezio = ((float(valores[0]) + float(valores[1])) * float(valores[2])) / 2  # <- Área do trapézio.
quadrado = float(valores[1]) * float(valores[1])  # <- Área do quadrado.
retangulo = float(valores[0]) * float(valores[1])

print('TRIANGULO: {:.3f}'.format(triangulo))
print('CIRCULO: {:.3f}'.format(circulo))
print('TRAPEZIO: {:.3f}'.format(trapezio))
print('QUADRADO: {:.3f}'.format(quadrado))
print('RETANGULO: {:.3f}'.format(retangulo))
