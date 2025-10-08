x = int(input('Digite o valor de x: '))
y = int(input('Digite o valor de y: '))

if x>0 and y>0: 
    print(f'Você está no primeiro quadrante.')

elif x<0 and y>0:
    print(f'Você está no segundo quadrante.')

elif x<0 and y<0:
    print('Você está no terceiro quadrante.')

elif x>0 and y<0:
    print(f'Você está no quarto quadrante.')

elif x==0 and y==0: 
    print('Você está na origem.')
elif x==0:
    print('Você está no eixo x.')
else: 
    print('Você está no eixo y.')