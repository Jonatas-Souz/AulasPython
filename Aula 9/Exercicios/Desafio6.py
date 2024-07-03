# DESAFIO 06

# Crie um programa onde o usuário possa digitar sete valores
# numéricos e cadastre-os em uma lista única que mantenha
# separados os valores pares e impares. No final mostre os
# valores pares e impares e ordem crescente.

Lista = []
ListaPar = []
ListaImpar = []
print("Digite 7 valores Numericos")
for i in range(0,7):
    valor = int(input(f"Digite o {i+1}° Valor \n"))
    calculo = valor % 2
    if calculo==0:
        ListaPar.append(valor)
    else:
        ListaImpar.append(valor)
ListaImpar.sort()
ListaPar.sort()
print(ListaPar, ListaImpar)
