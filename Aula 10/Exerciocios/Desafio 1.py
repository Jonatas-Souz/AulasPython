# DESAFIO 01

# Faça um programa que leia o nome e média de um aluno,
# guardando também a situação em um dicionário. No final
# mostre o conteúdo da estrutura na tela.

lista = list()
aluno = {}

aluno['Nome do Aluno'] = str(input("Digite o nome do aluno: "))
aluno['Media'] = float(input("Qual a media deste aluno? "))

if (aluno['Media']) < 5:
    aluno['Situação'] = 'Abaixo da média'
    lista.append(aluno.copy())
elif(aluno['Media']) == 5:
    aluno['Situação'] = 'Encima da Media'
    lista.append(aluno.copy())
else:
    aluno['Situação'] = 'Acima da média'
    lista.append(aluno.copy())
print(lista)