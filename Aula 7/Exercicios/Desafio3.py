# DESAFIO 03

# Crie um programa que leia vários números inteiros pelo
# teclado. No final da execução, mostre a média entre todos os
# valores e qual foi o maior e o menor valores lidos. O programa
# deve perguntar ao usuário se ele quer ou não continuar a
# digitar valores

quantidade_digitada = 0
total = 0
media = 0
registro = 0

while True:
    numeros = int(input("Digite qualquer numero inteiro: "))
    quantidade_digitada = quantidade_digitada + 1
    
    if numeros > registro:
        registro = 0 #Zerar registro
        registro = registro + numeros #Somar com ultimo maior
        total = total + numeros
        media = total / quantidade_digitada
        print(" ")
        print(f"Numero Maior {registro}")
        print(f"Total = {total}")
        print(f"Media = {media}")
        print(f"Quantidade de números digitados: {quantidade_digitada}")
    else:
        print("Continue digitando!!")
        total = total + numeros
        media = total / quantidade_digitada
        print(" ")
        print(f"Numero Maior {registro}")
        print(f"Total = {total}")
        print(f"Media = {media}")
        print(f"Quantidade de números digitados: {quantidade_digitada}")
        
    resposta = input("Deseja sair? (n/s): ")
    if resposta.lower() == 's': #Transforma texto em minusculo
        print("Fim")
        break #Sai do loop
print("Até mais!")