
x = float(input('Digite a coordenada X: '))

y = float(input('Digite a coordenada Y: '))

if (x > 0) and (y > 0):
   print('O ponto está no 1º Quadrante.')

elif (x < 0) and (y > 0):
   print('O ponto está no 2º Quadrante.') 

elif (x < 0) and (y < 0):
   print('O ponto está no 3º Quadrante.')

elif (x > 0) and (y < 0):
   print('O ponto está no 4º Quadrante.')

elif (x == 0) and (y == 0):
   print('O ponto está na origem (0,0).')

elif (y == 0):
   print('O ponto está sobre o eixo X.')

else:
   print('O ponto está sobre o eixo Y.')