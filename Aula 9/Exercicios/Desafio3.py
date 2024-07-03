# DESAFIO 03

# Crie um programa onde o usuário possa digitar cinco valores
# numéricos e cadastre-os em uma lista, já na sua posição
# correta de inserção (sem usar o sort()).

# No final mostre a lista ordenada na tela

Valor = []
for i in range(0,5):
    ValorNum = int(input("Digite um valor numerico inteiro\n "))
    Valor.append(ValorNum)

Valor.reverse
print(Valor)

