# DESAFIO 02

# Crie um programa onde 4 jogadores joguem um dado e
# tenham resultado aleatórios. Guarde esses resultados em um
# dicionário . No final, coloque esse dicionário em ordem,
# sabendo que o vencedor tirou o maior numero no dado.

import random
Lista = list()
Jogador = {}
pos = 1

for pos in range(1,5):
    Jogador[f'Player {pos}'] = str(input(f"Player {pos} "))
    Jogador['Dado'] = random.randint(1,6)
    Lista.append(Jogador.copy())
    
    print(Jogador)
    pos = pos+1
print(Lista)