import math, sys

try:
  # Informa os lados do triângulo
  fltLadoA = float(input('Informe o comprimento do lado A: '))
  fltLadoB = float(input('Informe o comprimento do lado B: '))
  fltLadoC = float(input('Informe o comprimento do lado C: '))

except ValueError:
  sys.exit('ERRO: Valor inválido. Informe um número real.')

except Exception as e:
  sys.exit(f'ERRO INESPERADO: {e}')

else:

  # ----------------------------------------------------------------------
  # Verificando se os lados são positivos
  if fltLadoA <= 0 or fltLadoB <= 0 or fltLadoC <= 0:
    sys.exit('ERRO: Os lados do triângulo devem ser números positivos.')

  # ----------------------------------------------------------------------
  # Verificando se os lados podem formar um triângulo
  if (fltLadoA + fltLadoB <= fltLadoC) or (fltLadoA + fltLadoC <= fltLadoB) or (fltLadoB + fltLadoC <= fltLadoA):
    sys.exit('ERRO: Os lados informados não podem formar um triângulo.') 

  # ----------------------------------------------------------------------
  # Calculando os ângulos do triângulo usando a Lei dos Cossenos e a função
  # arco-cosseno (math.acos) da biblioteca math para obter os ângulos em radianos.
  # Em seguida, converte os ângulos de radianos para graus usando a função 
  # math.degrees() e round() para evitar problemas de precisão com números 
  # de ponto flutuante.  

  # Calculando o cosseno do ângulo A e do ângulo B

  # cos(A) = (b² + c² - a²) / 2bc
  fltCossenoA = (fltLadoB**2 + fltLadoC**2 - fltLadoA**2) / (2 * fltLadoB * fltLadoC)

  # cos(B) = (a² + c² - b²) / 2ac
  fltCossenoB = (fltLadoA**2 + fltLadoC**2 - fltLadoB**2) / (2 * fltLadoA * fltLadoC)

  # Aplicando a função arco-cosseno para obter o ângulo A e o ângulo B em radianos
  fltAnguloA = math.acos(fltCossenoA)
  fltAnguloB = math.acos(fltCossenoB)

  # Convertendo os ângulos para graus e usando round() para evitar problemas
  # de precisão com números de ponto flutuante
  fltAnguloA = round( math.degrees(fltAnguloA), 3 )
  fltAnguloB = round( math.degrees(fltAnguloB), 3 )

  # Calculando o ângulo C
  fltAnguloC = round( 180 - fltAnguloA - fltAnguloB, 3)

  # ----------------------------------------------------------------------
  # Classificando o triângulo quanto aos lados
  if (fltLadoA == fltLadoB) and (fltLadoB == fltLadoC):
    strClassificacaoLados = 'Equilátero'
  elif (fltLadoA == fltLadoB) or (fltLadoA == fltLadoC) or (fltLadoB == fltLadoC):
    strClassificacaoLados = 'Isósceles'
  else:
    strClassificacaoLados = 'Escaleno'

  # ----------------------------------------------------------------------
  # Classificando o triângulo quanto aos ângulos
  if (fltAnguloA == 90) or (fltAnguloB == 90) or (fltAnguloC == 90):
    strClassificacaoAngulos = 'Retângulo'
  elif (fltAnguloA > 90) or (fltAnguloB > 90) or (fltAnguloC > 90):
    strClassificacaoAngulos = 'Obtusângulo'
  else:
    strClassificacaoAngulos = 'Acutângulo'

  # ----------------------------------------------------------------------
  # Exibindo os resultados
  print(f'\nÂngulos do triângulo:')
  print(f'Ângulo A ...........: {fltAnguloA:.5f}°')
  print(f'Ângulo B ...........: {fltAnguloB:.5f}°')
  print(f'Ângulo C ...........: {fltAnguloC:.5f}°')

  print(f'\nClassificação do triângulo:')
  print(f'Quanto aos lados ...: {strClassificacaoLados}')
  print(f'Quanto aos ângulos .: {strClassificacaoAngulos}\n')
