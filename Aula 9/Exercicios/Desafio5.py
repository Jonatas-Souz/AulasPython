# DESAFIO 05

# Faça um programa que leia nome e peso de varias pessoas,
# guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Um listagem com as pessoas mais leves

cadastradas = 0

print("Digite o Nome e o peso do paciente")
while True:
    nomePaciente = str(input("Digite o nome do paciente:\n "))
    peso = float(input("Digite o peso do paciente:\n "))
    cadastradas = cadastradas + 1
    print(f"Nome do Paciente: {nomePaciente}................Peso: {peso}")   
    print(f"Quantidade de cadastrados: {cadastradas}")
    if peso  
    