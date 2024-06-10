# DESAFIO 01

# Escreva um programa que faça o computador “pensar” em um
# número inteiro entre 5 e 0 e peça para o usuário tentar descobrir
# qual foi o número escolhido pelo computador.

# O programa deverá escrever na tela se o usuário venceu ou
# perdeu.

import random #Importar biblioteca que escolhe aleatóriamente

print("Jogo do adivinhe o numero!")
numeroUsuario = int(input("Digite um numero entre 0 e 5:"))

numeroComputador = random.randint(1,5)
print(f"Numero da sorte: {numeroComputador}")

if numeroUsuario == numeroComputador:
    print("Parabens, voce venceu")
else:
    print("Que pena, voce perdeu")