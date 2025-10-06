# import sys

# intNota1 = int(input('Informe a nota da ETAPA 1: '))

# if not (intNota1>=0 and intNota1<=100):
#    sys.exit('Nota 1 inválida! Deve ser entre 0 e 100.')

# intNota2 = int(input('Informe a nota da ETAPA 2: '))

# if not (intNota2>=0 and intNota2<=100):
#    sys.exit('Nota 2 inválida! Deve ser entre 0 e 100.')

# intCargaHoraria = int(input('Informe a Carga Horária da Disciplina (h/a): '))

# #TODO: Validar se a carga horária é maior que zero e menor ou igual a 360
# #if not (intCargaHoraria>0 and intCargaHoraria<=360): 
# if not (0 < intCargaHoraria <= 360):
#    sys.exit('Carga Horária inválida! Deve ser entre 1 e 360 horas/aula.')

# intFaltas = int(input('Informe a quantidade de faltas do aluno: '))

# # TODO: Validar se a quantidade de faltas é maior ou igual a zero
# # e menor ou igual a carga horária
# if not (0 <= intFaltas <= intCargaHoraria):
#    sys.exit(f'Quantidade de Faltas inválida! Deve ser entre 1 e {întCargaHoraria} horas/aula.')

# intMedia = round( (intNota1*2 + intNota2*3) / 5)

# fltFrequencia = round( (1 - (intFaltas / intCargaHoraria)) * 100, 1)

# print(f'Nota da Etapa 1: {intNota1}')
# print(f'Nota da Etapa 2: {intNota2}')
# print(f'Média..........: {intMedia}')

# print(f'Total de Aulas.: {intCargaHoraria}')
# print(f'Total de Faltas: {intFaltas}')
# print(f'Frequência.....: {fltFrequencia}%')

# # Mostrando se o aluno está APROVADO, PROVA FINAL ou REPROVADO
# # TODO: implementar a lógica para mostrar se o aluno foi 
# # reprovado por nota, por frequência ou por ambos
# if (intMedia >= 60) and (fltFrequencia>=75):
#    print('APROVADO')
# elif (intMedia >= 20) and (fltFrequencia>=75):
#    print('PROVA FINAL')
# else:
#    print('REPROVADO')
#    # Verificando motivo da reprovação
#    if intMedia < 20 and fltFrequencia < 75:
#       print('Motivo: Reprovado por nota e frequência')
#    elif intMedia < 20:
#       print('Motivo: Reprovado por nota')
#    else:
#       print('Motivo: Reprovado por frequência')