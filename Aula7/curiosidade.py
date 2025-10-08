from doctest import Example
from os import strerror
import sys
try:
    r = float(input('Informe o valor de r: '))
except ValueError:
    sys.exit('Erro: ValueError. Digite valores válidos.')
except Exception as strErro:
    sys.exit(f'{sys.exc_info()[0]}, {strErro}')
