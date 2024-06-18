# DESAFIO 04

# Faça um programa que jogue par ou impar com o computador.
# O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitorias consecutivas que ele conquistou
# no final do jogo.

import random
vitorias = 0

while True:
    jogador = int(input("Digite (1) para impar e (2) para par "))
    if jogador ==1:
        tx_jogador="IMPAR"
    elif jogador ==2:
        tx_jogador="PAR"   

    print(F"Você escolheu: {tx_jogador}")
    
    op_computador =random.randint(1,10)
    calculo = op_computador % 2
    print(f"Número {op_computador}")
    
    if calculo == 0:
        print(f"Computador escolheu o numero {op_computador}'Par'")

    else:
        print(f"Computador escolheu o numero {op_computador}'Impar'")


    if calculo == 0 and jogador == 2:
        print("Você ganhou!")
        vitorias = +1
    elif calculo == 1 and jogador == 1:
        print("Você ganhou!")
        vitorias = +1
    else:
        print("Você perdeu!")
        print(f"Vitórias consecutivas {vitorias}")
        resposta = input("Deseja sair? (n/s): ")
        if resposta.lower() == 's': #Transforma texto em minusculo
            print("Fim")
            break 
        
