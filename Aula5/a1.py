'''
   Fazer um programa que solicite ao usuário dois números. Esses números
   correspondem as coordenadas x e y de um ponto em um plano cartesiano.

   Após receber os números, o programa deve informar em qual quadrante
   o ponto se encontra. 

   Lembrete: O plano cartesiano é dividido em quatro quadrantes:
   - Quadrante 1: Ambas as coordenadas (x e y) são positivas;
   - Quadrante 2: A coordenada x é negativa e a coordenada y é positiva;
   - Quadrante 3: Ambas as coordenadas (x e y) são negativas;
   - Quadrante 4: A coordenada x é positiva e a coordenada y é negativa;
   - Se o ponto for a origem (0,0), o programa deve informar que o ponto está 
     na origem.
   - Se o ponto estiver sobre um dos eixos (x ou y), o programa deve informar
     que o ponto está sobre o eixo correspondente:
       - Sobre o eixo x: y = 0
       - Sobre o eixo y: x = 0
'''

# Solicita ao usuário que digite a coordenada X e armazena o valor.
# A função input() lê o que o usuário digita como texto (string).
# A função float() converte esse texto para um número decimal (ponto flutuante),
# permitindo que usemos valores como 2.5, -3.0, etc.
fltCoordX = float(input('Digite a coordenada X: '))

# Faz o mesmo para a coordenada Y, solicitando o valor e convertendo para float.
fltCoordY = float(input('Digite a coordenada Y: '))

# Início da estrutura de decisão para verificar a localização do ponto.
# O programa vai testar cada condição (if/elif) em ordem, e a primeira
# que for verdadeira será executada.

# Verifica se o ponto está no 1º Quadrante.
# A condição (fltCoordX > 0) and (fltCoordY > 0) só é verdadeira se
# AMBAS as coordenadas forem positivas.
if (fltCoordX > 0) and (fltCoordY > 0):
   print('O ponto está no 1º Quadrante.')

# Se a primeira condição for falsa, esta será testada.
# Verifica se o ponto está no 2º Quadrante.
# A condição é verdadeira se X for negativo E Y for positivo.
elif (fltCoordX < 0) and (fltCoordY > 0):
   print('O ponto está no 2º Quadrante.') 

# Se as anteriores forem falsas, esta será testada.
# Verifica se o ponto está no 3º Quadrante.
# A condição é verdadeira se AMBAS as coordenadas forem negativas.
elif (fltCoordX < 0) and (fltCoordY < 0):
   print('O ponto está no 3º Quadrante.')

# Se as anteriores forem falsas, esta será testada.