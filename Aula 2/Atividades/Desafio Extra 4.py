#Crie um programa para entrar com a base a altura de um retangulo e imprimir respectivamente o perimetro e a área correspondente 

base = float(input("Digite a Base:"))
print(f"Valor digitado = {base}")

altura = float(input("Digite a Altura:"))
print(f"Valor digitado = {altura}")

print(f"Area = {base * altura} e Perimetro = {2*(altura + base)}")