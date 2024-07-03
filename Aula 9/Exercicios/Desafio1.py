# DESAFIO 01

# Faça um programa que leia 5 valores numéricos e guarde-os
# em uma lista.

# No final, mostre qual foi o maior e o menor valor digitado e as
# suas respectivas posições na lista.

Valor = []
print("Digite 5 valores")
for i in range(0,5):
    ValorNum = int(input(f"Digite {i+1}º Valor\n "))
    Valor.append(ValorNum)
print(Valor)
print(f"Menor valor digitado: {min(Valor)}")
print(f"Maior valor digitado: {max(Valor)}")

posicaomin = Valor.index(min(Valor))
print(f"Posição do Menor valor {posicaomin}")
posicaomax = Valor.index(max(Valor))
print(f"Posição do Maior valor {posicaomax}")
