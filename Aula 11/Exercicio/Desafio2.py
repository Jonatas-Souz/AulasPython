# DESAFIO 02

# Faça um programa que tenha uma função chamada escreva(), que
# receba um texto qualquer como parâmetro e mostre uma mensagem com
# tamanho adaptável.
# Ex:
# escreva(‘Olá, mundo!!’)
# Saída
# -----------------------------------
# Olá, mundo
# -----------------------------------

def escreva(str):
    print("--"*10)
    print("Olá, Mundo")
    print("--"*10)
    
texto = str(input("Digite um texto: "))
escreva(texto)
