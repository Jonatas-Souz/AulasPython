# DESAFIO 05

# Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o ultimo nome
# separadamente
# Exemplo: Ana Maria De Souza
# Primeiro: Ana
# Ultimo: Souza

nomeCompleto = str(input("Digite seu nome: "))

divideNome = nomeCompleto.split() #Inicia cada palavra dentro de um array
tamanhoArray = len(divideNome)
inicioNome = divideNome[0]
fimNome = divideNome[tamanhoArray - 1]

print(f"Primeiro Nome: {inicioNome}")
print(f"Ultimo Nome: {fimNome}")