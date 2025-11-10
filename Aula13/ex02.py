s = 'ekkocaipira' 
entrada = input('digite a senha:')
#se colocar s.lower == entrada.lower vai jogar 
# tudo pra minusculo e fazer a comparação lá. .upper tbm funciona
#para maiusculo
if s == entrada:
    print('Acesso permitido.')
else:
    print('Acesso negado')