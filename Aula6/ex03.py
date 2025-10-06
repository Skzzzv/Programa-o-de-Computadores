import sys
try:
   intValor = int(input('Informe um valor inteiro: '))

   fltRaizQuadrada = intValor ** 0.5

except FloatingPointError:
   sys.exit('ERRO: Não há Raiz Real para números negativos...')

except ValueError:
   sys.exit('ERRO: Informe apenas números inteiros...')

else:
   print(f'A raiz quadrada de {intValor} é {fltRaizQuadrada:.2f}')
