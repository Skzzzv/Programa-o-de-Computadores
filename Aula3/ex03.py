x1 = int(input('Informe a nota da ETAPA 1:'))
x2 = int(input('Informe a nota da ETAPA 2:'))

r = round( (x1*2 + x2*3) / 5)

print(f'Nota da Etapa 1: {x1}')
print(f'Nota da Etapa 2: {x2}')
print(f'Média: {r}')

if (r >= 60):
   print('Aprovado')
elif (r >= 20):
   print('Prova Final')
else:
   print('Reprovado')