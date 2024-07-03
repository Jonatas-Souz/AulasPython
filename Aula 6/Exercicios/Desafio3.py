# DESAFIO 03

# Faça um programa que calcule a soma entre todos os números
# ímpares que são múltiplos de três e que se encontram no
# intervalo de 1 até 500.
soma = 0
for i in range(3,501,3): #Conta de 1 em 1 do 1 ao 5
    if i % 3 == 0: #multiplo de 3
        soma = soma+i
print(soma)