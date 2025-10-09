from sys import exit

n = int(input('Digete 4 números para a soma: '))
s = n//1000
d = s % 1000
a = n//100
b = a % 100
c = n//10
d = c % 10
e = n % 10
if n < 1 or n > 9999:
    exit('Número inválido.')
else:
    print(d+b+c+e)