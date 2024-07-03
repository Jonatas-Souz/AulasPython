# DESAFIO 04

# Crie um programa que vai ler vários números e colocar em
# uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os
# valores pares e os valores impares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

Lista = []
ListaImpar = []
ListaPar = []
while True:
    ValorNum = int(input("Digite um valor numerico inteiro e (0) para sair:\n "))
    calculo = ValorNum % 2 
    if calculo==0:
        ListaPar.append(ValorNum)
        Lista.append(ValorNum)
    else:
        ListaImpar.append(ValorNum)
        Lista.append(ValorNum)
    if ValorNum==0:
        break
        
print(f"Numeros digitados {Lista}")  
print(f"Lista par {ListaPar}")
print(f"Lista impar {ListaImpar}")