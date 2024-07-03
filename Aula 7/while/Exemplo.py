# x=1

# while x<10: # Enquanto 'X' for menor do que 10 temos o loop
#     print(x)
#     x=x+1 #Soma 1 a X || ou x+1 = x ou x*=2(que é igual a x=x*2) 
# else:
#     print("Acabou!")
    
    
###############################################################
# numero = 0 

# while numero < 5:
#     numero += 1 #Numero + 1
    
#     if numero == 3: #É igual a 3?
#         print("Vamos pular a interação para", numero)
#         continue # Sai do loop 
    
#     print("Numero:", numero)
    
# print("Fim do loop")

##################################################################

# while True:
#     resposta = input("Deseja sair? (n/s): ")
#     if resposta.lower() == 's': #Transforma texto em minusculo
#         print("Saindo do loop.")
#         break#Sai do loop
#     print("Continua o loop...")

#################################################################

#Desafio 6 Jokenpô

import random

while True:
    op_jogador = int(input("Digite sua escolha: \n1-Pedra \n2-papel  \n3-Tesoura \n digite: "))
    print(op_jogador)

    if op_jogador ==1:
        tx_jogador="PEDRA"
        img_jogador="🧱"
    elif op_jogador ==2:
        tx_jogador="PAPEL"
        img_jogador ="🧻"
    elif op_jogador ==3:
        tx_jogador="TESOURA"
        img_jogador ="✂"
    else:
        print("Opção invalida")

    print(tx_jogador)
    
    opcoes =["PEDRA","PAPEL","TESOURA"]
    op_computador =random.choice(opcoes)

    print(f"Esolha jogador: {tx_jogador} - {img_jogador}")
    print(f"Esolha PC: {op_computador}")

    #VITORIA
    if (
            (tx_jogador=="PEDRA" and op_computador=="TESOURA")or
            (tx_jogador=="TESOURA" and op_computador=="PAPEL")or
            (tx_jogador=="PAPEL" and op_computador=="PEDRA")    
        ):
        print("Você venceu! 😎")
    #Derrota
    elif (
            (tx_jogador=="PEDRA" and op_computador=="PAPEL")or
            (tx_jogador=="TESOURA" and op_computador=="PEDRA")or
            (tx_jogador=="PAPEL" and op_computador=="TESOURA")    
        ):
        print("Você perdeu! 😵")
    else:
        print("EMPATE!! 😐")
        
    resposta = input("Deseja sair? (n/s): ")
    if resposta.lower() == 's': #Transforma texto em minusculo
        print("Saindo do jogo.")
        break #Sai do loop
    
    print("Continua o jogo")