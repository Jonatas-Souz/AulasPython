# DESAFIO 04

# A confederação Nacional de Natação precisa de uma programa
# que leia o ano de nascimento de uma atleta e mostre sua
# categoria, de acordo com a idade.
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JUNIOR
# Até 24 anos: SÊNIOR
# Acima: MASTER

idade = int(input("Digite sua idade: "))

if idade <= 9:
    print("Sua categoria é a Mirim")
if idade > 9 and idade <= 14:
    print("Sua categoria é a Infantil")
if idade > 14 and idade <= 19:
    print("Sua categoria é a Junior")
if idade > 19 and idade <= 24:
    print("Sua categoria é a Sênior")
if idade > 24:
    print("Sua categoria é a Master")
print("Fim")