# DESAFIO 02

# Crie um programa que leia o nome de uma cidade e diga se ela
# começa ou não com o nome “Santo”.
texto = str(input("Digite um texto:"))
print(f"Texto digitado = {texto}")
textoMinusculo = texto.lower() #Deixa o texto Minusculo
print(textoMinusculo)
texto2 = (textoMinusculo[0:5])
print(f"Existe (Santo) na frase? {'santo' in texto2}") 
