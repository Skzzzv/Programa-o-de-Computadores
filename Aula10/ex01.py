import sys
try:
    a = int(input('Digite o ano: '))
    r = a//4
except ValueError:
    sys.exit('Digite um valor algébrico')
except Exception as d:
    sys.exit(f'ERRO: {d}, {type(d)}')
else:
    if a <= 0:
        sys.exit('Esse valor não é compativel')
    elif r ==0:
        print('É um ano bissexto')  
    else:  
        print('Não é um ano bissexto')