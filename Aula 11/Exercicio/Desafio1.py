# DESAFIO 01

# Faça um programa que tenha uma função chamada área(), que
# receba as dimensões de um terreno retangular (largura e
# comprimento) e mostre a área do terreno.

def area(l,c):
    resultado = l*c
    return resultado

largura = float(input("Digite a largura do terreno: "))
comprimento = float(input("Digite o comprimento do terreno: "))
print(f"Área do terreno igual a: {area(largura,comprimento)}")