'''
   Este programa pede ao usuário as coordenadas (x e y) de um ponto
   e informa sua localização em um plano cartesiano.
'''

# Pede a coordenada X e guarda o número digitado.
fltCoordX = float(input('Digite a coordenada X: '))

# Pede a coordenada Y e guarda o número digitado.
fltCoordY = float(input('Digite a coordenada Y: '))

# A partir daqui, o programa verifica várias condições em ordem.

# Se X e Y forem positivos, o ponto está no 1º Quadrante.
if (fltCoordX > 0) and (fltCoordY > 0):
   print('O ponto está no 1º Quadrante.')

# Se X for negativo e Y positivo, o ponto está no 2º Quadrante.
elif (fltCoordX < 0) and (fltCoordY > 0):
   print('O ponto está no 2º Quadrante.') 

# Se X e Y forem negativos, o ponto está no 3º Quadrante.
elif (fltCoordX < 0) and (fltCoordY < 0):
   print('O ponto está no 3º Quadrante.')

# Se X for positivo e Y negativo, o ponto está no 4º Quadrante.
elif (fltCoordX > 0) and (fltCoordY < 0):
   print('O ponto está no 4º Quadrante.')

# Se X e Y forem zero, o ponto está na origem.
elif (fltCoordX == 0) and (fltCoordY == 0):
   print('O ponto está na origem (0,0).')

# Se apenas Y for zero, o ponto está sobre o eixo X.
elif (fltCoordY == 0):
   print('O ponto está sobre o eixo X.')

# Se nenhuma das condições acima for verdade, só resta uma opção:
# O ponto está sobre o eixo Y (quando X é zero).
else:
   print('O ponto está sobre o eixo Y.')