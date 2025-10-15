import math
import sys
import math
try:
    l1 = int(input('Informe o valor do lado 1: '))

    l2 = int(input('Informe o valor do lado 2: '))

    l3 = int(input('Informe o valor do lado 1: '))

except ValueError:
    sys.exit('Valor inválido.')
except Exception as e:
    sys.exit(f'Erro:{e}, {type(e)}')
else:
    if l1 + l2 < l3 and l2 + l3 < l1 and l1 + l3 < l1:
        sys.exit('Não é um triângulo')