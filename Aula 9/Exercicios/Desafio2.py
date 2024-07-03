# DESAFIO 02

# Crie um programa onde o usuário possa digitar vários valores
# numéricos e cadastre-os em uma lista. Caso o número já
# exista lá dentro, ele não será adicionado. No final serão
# exibidos todos os valores únicos digitados, em ordem
# crescente.

Lista = []
while True:
    ValorNum = int(input("Digite um valor numerico inteiro e (0) para sair:\n "))
    if ValorNum in Lista:
        print(f"O numero '{ValorNum}' já esta na lista")
    else:
        Lista.append(ValorNum)
    if ValorNum==0:
        break
print(Lista)
Lista.sort()
print(f"Lista ordem crescente: {Lista}")
    