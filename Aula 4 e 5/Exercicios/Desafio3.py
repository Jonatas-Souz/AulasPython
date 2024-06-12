# DESAFIOS

# DESAFIO 03

# Desenvolva um programa que pergunte a distância de uma
# viagem em Km. Calcule o preço da passagem cobrando R$
# 0,50 por Km para viagens de até 200 Km e R$ 0,45 para
# viagens mais longas.

viagemKm = float(input("Qual a distancia da viagem?: "))

if viagemKm <= 200: #Se menor qu duzentos
    distacia = 0.50
    print("Sua viagem é curta")
    print(f"Sua viagem é de {viagemKm}Km, voce ira pagar R${distacia * viagemKm}")
else:
    distancialonga = 0.45
    print("Sua viagem é longa")
    print(f"Sua viagem é de {viagemKm}Km, voce ira pagar R${distancialonga * viagemKm}")
print("Obrigado!")
