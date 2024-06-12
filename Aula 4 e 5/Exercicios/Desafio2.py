# DESAFIO 02

# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que
# ele foi multado.
# A multa vai custar R$ 7,00 por cada Km acima do limite.

velocidade = float(input("Qual a velocidade?: "))

if velocidade > 80: #Se maior que 80
    print("voce foi multado") #Se maior
    valor = (velocidade - 80) * 7
    print(f"sua multa é de:{valor}")
else:
    print("voce nao foi multado;)")#Se menor
print("Fim")
