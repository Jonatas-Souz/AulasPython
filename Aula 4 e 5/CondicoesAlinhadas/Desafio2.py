# DESAFIO 02

# Escreva um programa que leia dois números inteiros e
# compare- os, mostrando na tela uma mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais

numero1 = int(input("Digite um número inteiro: ")) #Digita o primeiro Número 
numero2 = int(input("Digite outro número inteiro: ")) #Digita o segundo Número
 #Compara
if numero1 > numero2: 
    print(f"O valor do primeiro número ({numero1}) é maior que o segundo ({numero2})")
if numero1 < numero2:
    print(f"O valor do segundo número ({numero2}) é maior que o primeiro ({numero1})")
else:
    print(f"Não existe valor maior, os dois são iguais")