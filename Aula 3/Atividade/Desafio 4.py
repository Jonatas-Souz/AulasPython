
# DESAFIO 04

# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A"
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece a ultima vez

frase = str(input("Digite uma frase:"))
print(f"Frase digitada;{frase}")
maiusculo = frase.count('A')
minusculo = frase.count('a')
total = maiusculo + minusculo

print(f"Quantidade de letras maiuscula (A): {maiusculo}")
print(f"Quantidade de letras minuscula (a): {minusculo}")
print(f"Total de maiusculos e minusculos: {total}")
