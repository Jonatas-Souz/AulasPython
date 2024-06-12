# DESAFIO 06

# Crie um programa que faça o computador jogar Jokenpô com
# você:

import random

usuario = str(input("Escolha e digite Pedra, Papel ou Tesoura: "))
usuarioMai = usuario.upper()
opcoes =["PEDRA","PAPEL","TESOURA"]

gera_numero= random.randint(0,2)
escolha_pc= opcoes[gera_numero]
print(f"Você escolheu: {usuarioMai}")
print(f"computador escolheu: {escolha_pc}")

if usuarioMai=="PEDRA" and escolha_pc=="TESOURA":
    print("Você ganhou!")
if usuarioMai=="PAPEL" and escolha_pc=="PEDRA":
    print("Você ganhou!")
if usuarioMai=="TESOURA" and escolha_pc=="PAPEL":
    print("Você ganhou!")
    
if usuarioMai=="TESOURA" and escolha_pc=="PEDRA":
    print("Você perdeu!")
if usuarioMai=="PEDRA" and escolha_pc=="PAPEL":
    print("Você perdeu!")
if usuarioMai=="PAPEL" and escolha_pc=="TESOURA":
    print("Você perdeu!")
    
if usuarioMai == escolha_pc:
    print("Empate")



