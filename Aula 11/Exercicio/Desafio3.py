# DESAFIO 03

# Faça um programa que tenha uma função chamada maior(), que
# receba três parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é
# o maior.

def maior(a,b,c):
    lista = a,b,c
    print(max(lista))
    
Numero1 = int(input("Digite um numero: "))
Numero2 = int(input("Digite um numero: "))
Numero3 = int(input("Digite um numero: "))
maior(Numero1,Numero2,Numero3)