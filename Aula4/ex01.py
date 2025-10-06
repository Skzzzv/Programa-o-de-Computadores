

x1 = int(input('Informe a nota da etapa 1:'))
if not (x1>=0 and x1<=100)
sys.exit('Nota 1 inválida, digite o valor entre 0 e 100')
x2 = int(input('Informe a nota da etapa 2:'))

r = round( (x1*2 + x2*3) / 5)

print(f'Nota da etapa 1: {x1}')
print(f'Nota da etapa 2: {x2}')
print(f'A média é: {r}')

y1 = int(input('Coloque a carga horária da disciplina: '))
y2 = int(input('Coloque a quantidade de faltas: '))
f  = round((1 - (y2/y1))*100)

print(f'A quantidade de carga horária é: {y1}')
print(f'A quantidade de faltas é: {y2}')
print(f'A sua frequência é: {f}%')

if (r >= 60) and (f>=75):
   print('Aprovado')
elif (r >= 20) and ((f>=75)):
   print('Prova Final')
elif (r >= 20) and (f<=75):
   print('Reprovado por falta')
elif (r <= 20) and (f>=75):
   print('Reprovado por nota')
