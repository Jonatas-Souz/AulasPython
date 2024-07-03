# DESAFIO 03

# Crie um programa que leia o nome de uma pessoa e diga se ela
# tem "Silva" no nome

texto = str(input("Digite um nome completo:"))
print(f"Texto digitado = {texto}")
textoMinusculo = texto.lower() #Deixa o texto Minusculo
print(textoMinusculo)
print(f"Existe (Silva) no nome? {'silva' in textoMinusculo}") 
