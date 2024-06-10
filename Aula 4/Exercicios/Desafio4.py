
# DESAFIO 04

# Faça um programa que leia três números e mostre qual é o
# maior e qual é o menor.

numero1 = float(input("Digite o primeiro numero: "))
numero2 = float(input("Digite o segundo numero: "))
numero3 = float(input("Digite o terceiro numero: "))

# Numero Maior
if numero1 > numero2 and numero1 > numero3:
    print(f"Numero Maior: {numero1}")
if numero2 > numero3 and numero2 > numero1:
    print(f"Numero Maior: {numero2}")
if numero3 > numero1 and numero3 > numero2:
    print(f"Numero Maior: {numero3}")

# Numero Menor       
if numero1 < numero2 and numero1 < numero3:
    print(f"Numero Menor: {numero1}")
if numero2 < numero3 and numero2 < numero1:
    print(f"Numero Menor: {numero2}")
if numero3 < numero1 and numero3 < numero2:
    print(f"Numero Menor: {numero3}")

#Numero restante
if numero1 < numero2 and numero1 > numero3:
    print(f"Numero entre maior e menor: {numero1}")
if numero2 < numero3 and numero2 > numero1:
    print(f"Numero entre maior e menor: {numero2}")
if numero3 < numero1 and numero3 > numero2:
    print(f"Numero entre maior e menor: {numero3}")
print("obrigado!")