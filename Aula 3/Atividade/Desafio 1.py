# DESAFIO 01

# Crie um programa que leia o nome completo de uma pessoas
# e mostre
# O nome com todas as letras maiúsculas
# O nome com todas as letras minúsculas
# Quantas letras ao todo (sem considerar espaços)
# Quantas letras tem o primeiro nome

texto = str(input("Digite um texto:"))
print(f"Texto digitado = {texto}")

textoMaiusculo = texto.lower() #Deixa o texto minusculo
print(f"Minusculo {textoMaiusculo}")

textoMinusculo = texto.upper() #Deixa o texto em caixa alta
print(f"Maiusculo {textoMinusculo}")

semEspaco = texto.replace(" " , "") #Apagar todos os espaços
print(f"Quantidade de Letras: {len(semEspaco)}")

arrayNome = texto.split() #["silas","bastianelli"]
primeiroNome = arrayNome[0]
print(f"Seu Primeiro Nome possui: {len(primeiroNome)}")