############################ Contador em loop ##############################
# for contador in range(1,6): #Conta de 1 em 1 do 1 ao 5
#     print(contador)#+1
    
#     #contador= contador +1 - Python
#     #contador++ - outras linguagens
# print("Fim")

################################ Contador em loop com salto #############################

# for contador in range(1,6,2): #Pula de 2 em 2 indicado no ultimo número
#     print(contador)#+2

# print("Fim")

##############################################################

# numero=int(input("Digite um número: "))

# for contador in range(0,11):
#     print(f"{numero} X {contador} = {numero*contador}")
# print("fim")

###############################################################

# numero = int(input("Digite um número: "))
# inicio = int(input("Digite o número de início: "))
# fim = int(input("Digite o numero final: "))
# fim=fim+1 #Soma número digitado + 1

# for contador in range(inicio,fim):
#     print(f"{numero} X {contador} = {numero*contador}")

# print("fim")

############################# Sem Salto ######################################

# soma = 0
# for numero in range(1,5):
#     print(f"soma= {soma} + {numero}")
#     soma= soma + numero
#     print(soma)
# print(f"soma = {soma}")   
 
 
 ########################### Com Salto ########################################
 
# soma = 0
# for numero in range(1,6,2):
#     print(f"soma= {soma} + {numero}")
#     soma= soma + numero
#     print(soma)#1 4 9 
# print(f"soma = {soma}")   
 
 ############################## Com texto ###########################
# texto= "Calculo :"
# soma = 0
# for numero in range(1,6,2):
#     print(f"soma= {soma} + {numero}")
#     soma= soma + numero
#     print(soma)#1 4 9 
#     texto = texto + " " + str(numero)
# print(texto)
# print(f"soma = {soma}")   

 ###################################################################
 
# inicio = int (input("Informe o primeiro número: "))
# fim = int (input("Informe o número final: "))
# salto = int (input("Informe o salto: "))
# texto = "Cálculo: "
# soma = 0

# for numero in range(inicio , fim , salto):
#     soma = soma + numero
#     texto = texto + str(numero)
#     if numero > 50:
#         texto = texto + "\nPassou de  50"
#         break
#     if numero != fim-1:
#         texto = texto + " + "
# print(f"{texto}")
# print(f"soma : {soma}")


############################## Print Caracter em loop ########################################

# nome = "Otorrinolaringologista"

# for caractere in nome:
#     print(caractere)

############################# Print Palavras em loop ######################################

# zoo =["Zebra","Canguru","Gorila","Javali","Hiena"]
# for animal in zoo:
#     print(animal)

############################# Else do comando 'for' ################################

# numeros = [1,2,3,10,12]
# for numero in numeros:
#     if numero == 10:
#         break
#     print(f"Numero: |{numero}")
# else:
#     print("Acabou")
    
# print("fim")

############################ Passa para o próximo itém ############################

# for x in [1,10,20,30,40,50]:
#     if x == 30:
#         continue
#     print(x)

############################# Time ####################################
import time

numeros = [1,2,3,10,12]
for numero in numeros:
    if numero == 10:
        break
    print(f"Numero: |{numero}")
    time.sleep(1) #adiciona o tempo de 1 segundo
else:
    print("Acabou")
    
print("fim")