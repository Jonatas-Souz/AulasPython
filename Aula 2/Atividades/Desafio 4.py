# DESAFIO 04

# Desenvolva um programa que leia as duas notas de um aluno,
# calcule e mostra a sua média.

nota1 = int(input("Digite um numero:"))
print(f"Primeira nota = {nota1}")

nota2 = int(input("Digite outro numero:"))
print(f"Segunda nota = {nota2}")

soma = nota1 + nota2
media = soma / 2

print("Media =", media)
