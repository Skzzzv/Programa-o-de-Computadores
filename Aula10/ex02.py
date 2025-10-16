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
    if l1 <= 0 or l2 <= 0 or l3 <= 0:
        sys.exit('ERRO: Os lados do triângulo devem ser números positivos.')

    elif l1 + l2 < l3 and l2 + l3 < l1 and l1 + l3 < l1:
        sys.exit('Não é um triângulo')

    cosa = (l2**2 + l3**2 - l1**2) / 2*l2*l3
    cosb = (l1**2 + l3**2 - l2**2) / 2*l1*l3
    anga = math.acos(cosa)
    angb = math.acos(cosb)
    # anga = math.degrees(anga)
    # angb = math.degrees(angb)
    print(f'{anga}')
    print(f'{anga}')