import sys
try:
    h = int(input('Digite o total de horas trabalhadas: '))
    s = int(input('Digite o valor de cada hora: '))
    r = h*s
    h1 = 0
except ValueError:
    input('Digite apenas valores algébricos.')
except Exception as strErro:
    sys.exit(f'ERRO: {strErro}')
if h > 40:
    h - 40 == h1
    h == 40   
elif h < 40:
    print(f'Seu salário é de {r}')
elif h > 40:
    print(f'Seu salário é de {r+(h1*1.5)}')