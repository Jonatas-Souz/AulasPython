# DESAFIO 05

# Crie um programa que tenha uma tupla única com nomes de produtos
# e seus respectivos preços, na sequência.

# No final, mostre uma listagem de preços, organizando os dados em
# forma tabular.

produtos = ('Sofa' , 800.00 , 'Geladeira' , 700.00,
            'Fogao' , 700.00, 'Forno' , 300.00)

tamanho = len(produtos)

#print("Produto: --------------- Preco")
#print(f"{produtos[0]} ------------------ {produtos[1]}")

for i in range(0,tamanho,2): #Faz pular de 2 em 2, além de indicar o 'i' para montar uma lista de produtos
    print(f"{produtos[i]} ------------------ {produtos[i+1]}")#Print produtos 