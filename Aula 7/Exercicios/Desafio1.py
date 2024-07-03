# DESAFIO 01

# Faça um jogo, onde o computador vai “pensar” em um número
# entre 0 a 10. Só que agora o jogador vai tentar adivinhar até
# acertar, mostrando no final quantos palpites foram necessários
# para vencer.

import random
tentativas = 0
while True:
    jogador = int(input("Digite um número entre 1 e 10: "))  
    op_computador =random.randint(1,10)
    print(f"O número é: {op_computador}")
    tentativas = tentativas + 1
    if jogador == op_computador:
        print("Você acertou!!")
        break #Sai do loop
    else:
        print("Você errou!!")
print(f"{tentativas} tentativas")
print("Continua o jogo")