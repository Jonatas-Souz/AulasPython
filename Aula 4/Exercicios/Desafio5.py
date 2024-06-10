
# DESAFIO 05
# Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo.
# Condições Necessárias:
# a + b > c
# a + c > b
# b + c > a

reta1 = float(input("Digite a primeira reta: ")) #Entrada de numero Real
reta2 = float(input("Digite a segunda reta: "))
reta3 = float(input("Digite a terceira reta: "))

if reta1 + reta2 > reta3 and reta2 + reta3 > reta1 and reta3 + reta1 > reta2: #Compara se a soma de duas retas é maior que a terceira 
    print(f"As retas {reta1}, {reta2} e {reta3} 'PODEM' formar um triangulo, pois...")
    if reta1 + reta2 > reta3:
        print(f"A soma das retas {reta1} e {reta2} é igual a {reta1 + reta2}, que é maior que {reta3}")
    if reta2 + reta3 > reta1:
        print(f"A soma das retas {reta2} e {reta3} é igual a {reta2 + reta3}, que é maior que {reta1}")
    if reta3 + reta1 > reta2:
        print(f"A soma das retas {reta3} e {reta1} é igual a {reta3 + reta1}, que é maior que {reta2}")

else:
    print(f"As retas {reta1}, {reta2} e {reta3} 'NAO' podem formar um triangulo, pois...") #Se a soma de duas retas for menor que a terceira 
    if reta1 + reta2 < reta3:
        print(f"A soma das retas {reta1} e {reta2} é igual a {reta1 + reta2}, que é menor que {reta3}")
    if reta2 + reta3 < reta1:
        print(f"A soma das retas {reta2} e {reta3} é igual a {reta2 + reta3}, que é menor que {reta1}")
    if reta3 + reta1 < reta2:
        print(f"A soma das retas {reta3} e {reta1} é igual a {reta3 + reta1}, que é menor que {reta2}")

print("obrigado!")