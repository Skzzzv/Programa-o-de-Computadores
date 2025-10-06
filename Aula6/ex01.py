import sys
try:
    raio = float(input('Informe o raio: '))
except Exception as strErro:
    sys.exit(f'EXCEÇÃO: {sys.exc_info()[0]} -> {strErro}')
else:
    if raio <= 0:
        sys.exit('ERRO: O Raio deve ser positivo...')
    area = 3.1416 * raio ** 2
    print(f'A área do círculo de raio = {raio} é {area:.2f}')