# DESAFIO 01

# Escreva um programa para aprovar um empréstimo bancário
# para a compra de uma casa. O programa vai perguntar o valor
# da casa, o salário do comprador e em quantos anos ele vai
# pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode
# exceder 30% do salário ou então o empréstimo será negado.

valorCasa = float(input("Qual o valor do imóvel? "))
salario = float(input("Qual o salario do comprador? "))
tempoEmAnos = float(input("Em quantos anos pretende quitar a divida? "))

tempoEmMese = tempoEmAnos * 12 #Torna a quantidade de anos em meses
prestacao = valorCasa / tempoEmMese #Encontra o valor da prestação
porcentagemSalario = (salario / 100) * 30 # 30% do salário

if (porcentagemSalario > prestacao):
    print("O imóvel 'PODE' ser adquirido") 
    print(f"Quantidade de meses {tempoEmMese}, Prestacao {prestacao} e 30% salario {porcentagemSalario}")
else:
    print("O imóvel 'NAO' pode ser adquirido")
    print(f"Quantidade de meses {tempoEmMese}, Prestacao {prestacao} e 30% salario {porcentagemSalario}")
    
    



