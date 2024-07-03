# DESAFIO 03

# Crie um programa que leia duas notas entre 0 a 10 de um aluno
# e calcule sua média, mostrando uma mensagem no final, de
# acordo com a média atingida.
# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 a 6.9: RECUPERAÇÃO
# Média igual ou superior a 7.0: APROVADO

nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))

media = (nota1 + nota2) / 2

if media < 5.0: # Média maior que 5
    print("Reprovado")
if media == 5.0 or media == 6.9: # Média igual a 5 ou 6,9 
    print("Recuperação")
if media >= 7: # Média maior ou igual a 7
    print("Aprovado")