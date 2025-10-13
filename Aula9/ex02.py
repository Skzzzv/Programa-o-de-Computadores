import sys
try:
    
    p = float(input('Digite seu peso: '))
    a = float(input('Digite sua altura: '))
    r = p/a**2
    20
except ValueError:
   sys.exit('ERRO: Você deve digitar um valor numérico.')
except ZeroDivisionError:
    sys.exit('O valor da alltura não pode ser 0.')
except Exception as d:
    sys.exit(f'ERRO: {d}, {type(d)}')
else:
    print('Aguarde um momento, estamos calculando o seu IMC.')
if p <= 0:
    sys.exit('O valor do peso não pode ser 0')
elif r < 1.85:
    print(f'Você está abaixo do peso')
elif r > 18.5 and r < 24.9:
    print(f'Você está no peso ideal')
elif r > 25.0 and r < 29.9:
    print(f'Você está acima do peso')
elif r > 30 and r < 34.9:
    print(f'Você está Muito acima do peso')
else:
    print(f'Você está IMENSO')