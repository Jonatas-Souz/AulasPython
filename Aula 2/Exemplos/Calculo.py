# print("Senai")

# nome = "Jonatas" # OBS - Váriaveis inician comçetras minusculas

# salario = 1200.50
# salarioBruto = 2050.33 #camelCase
# salario_bruto = 3300.25 #snake_case

# print("Salario = R$", salario)
# salario = salario+ 150 # Soma 1200.50 + 150 = 1350.5 

# print("Salario Atualziado = R$", salario) #Imprimir salário corrigido \ Trocou o '+' pela ','

# #Obs; (Ctrl) + (;) marca a linha como comentario 

# n1 = 20
# n2 = 30
# print("n1 =", n1)
# print("n2 =", n2)

# print("************** Calculos 1 ***************")

# soma = n1 + n2
# print("Soma =", soma) 
# print(n1 + n2) #Só exibe o resultado ao usuario
# print("Soma =",str(n1 + n2)) #Não precisa de variavel / str = string (tranfoma em texto) 

# subtracao = n1 - n2 
# print("Subtracao =", subtracao)
# print(f"Subtracao = {subtracao}")
# print(f"Subtracao = {n1-n2}") #Usar o "f" na frente

# multiplicacao = n1 * n2
# print("Multiplicacao =", multiplicacao)
# print(f"Multiplicacao = {n1*n2}")
# print(f"Multiplicacao = {multiplicacao}")

# divisao = n1 / n2 
# print("Divisao =", divisao)
# print(f"Divisao = {divisao}")
# print(f"Divisao = {n1/n2}")

# print("************** Calculos 2, Teste ***************")

# n3 = 1.2
# n4 = 2.3

# divisaoInteira = n3 // n4
# print("Divisao inteira 1.2 // 2.3 =", divisaoInteira) #Mostra número quebrado

# potencia = n3 ** n4
# print("Potencia 1.2 ** 2.3 =", potencia) #Potencia

# restoDaDivisao = n1 % n2
# print("Resto da divisao 1.2 % 2.3 = ", restoDaDivisao) #Mostra o Resto
# print(f"Resto da divisao = {8 % 2}")

# print("************** Leitura ***************")

# #Atribui dados pelo usuario e converte em Numero
# numeroInteiro = int(input("Digite um numero inteiro:"))
# print(f"Numero digitado = {numeroInteiro}")

# #Atribui dados pelo usuario e converte em Numero
# numeroReal = float(input("Digite um numero Decimal:"))
# print(f"Numero digitado = {numeroReal}")

# #Atribui dados pelo usuario e converte em Bool // Se existe valor = True, se não existe = False
# boolano = bool(input("Digite um valor Boolaeano:"))
# print(f"Valor digitado = {boolano}")

# #Atribui dados pelo usuario e converte em Texto
# string = str(input("Digite um texto:"))
# print(f"Texto digitado = {string}")

# print("************** Tipo ***************")

# print(type(3)) #Mostra o tipo da variavel 
# print(type(2.3))
# print(type(True))
# print(type("Word"))

variavelMisterio = 10/2<10 # "<" Comparação, se o resultado da conta é menor que 10
print(type(variavelMisterio)) #"variavelMisterio" tipo bool, booleano, True ou False
 
texto ="123" 
print(texto.isnumeric())
print(texto.isalpha())

texto2 ="jon"
print(texto2.islower())
print(texto2.isupper())

texto3 = "12.0"
print(texto3.isdecimal())

texto4 = "12"
print(texto4.isdecimal())
