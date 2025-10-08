from sys import exit
from math import sqrt

a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))
c = int(input('Digite o valor de c: '))
s = (b**2)-4*a*c
d1 = ((-b)+sqrt(s))/2
d2 = ((-b)-sqrt(s))/2
if (a==0):
    exit('Não é uma equação de segundo grau.')
elif s<0:
    exit('A equação não apresenta raizes reais.')
elif s==0:
    print(f'o valor x1= {d1}')
else:
        print(f'o valor x1= {d1}, x2= {d2}')