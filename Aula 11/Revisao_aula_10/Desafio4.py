# DESAFIO 04

# Crie um programa que gerencie o aproveitamento de um
# jogador de futebol. O programa vai ler o nome do jogador e
# quantas partidas ele jogou. Depois vai ler a quantidade de
# gols feitos em cada partida. No final, tudo isso será guardado
# em um dicionário, incluindo o total de gols feitos durante o
# campeonato.

lista = []
DicioJogador = {
    'Nome' : str(input("Nome do Jogador: ")),
    'Quantidade de Partidas' : int(input("Quantas Partidas Jogou? "))
}

contador = DicioJogador['Quantidade de Partidas']

print(DicioJogador)

if DicioJogador['Quantidade de Partidas'] >= 0:
    Gols = int(input("Quantos gols fez? "))
    lista.append(Gols)
    print(contador)
else:
        print("f")