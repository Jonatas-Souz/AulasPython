# Crie um programa que leia vários números inteiros pelo
# teclado. O programa só vai parar quando o usuário digitar o
# valor 999, que é a condição de parada. No final, mostre
# quantos números foram digitados e qual foi a soma entre eles
# (desconsiderando o 999)

quantidade_digitada = 0
total = 0
while True:
    numeros = int(input("Digite qualquer numero inteiro: "))
    quantidade_digitada = quantidade_digitada + 1
    if numeros == 999:
        print("Você saiu")
        break #Sai do loop
    else:
        print("Continue digitando!!")
        total = total + numeros
print(f"Você digitou: {quantidade_digitada} números")
print(f"Total da soma dos números digitados: {total}")
print("Continua o jogo")