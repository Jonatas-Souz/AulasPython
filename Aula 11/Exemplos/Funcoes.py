
# #Escopo de Variavel
# def funcao_local():
#     variavel_local = 10
#     print(variavel_local)
    
# funcao_local() #10
# # print(variavel_local) #5


#################################################

# variavel_global = 5 

# def funcao_global():
#     variavel_global = 10
#     print(variavel_global)
    
# funcao_global() #10
# print(variavel_global) #5

#################################################

# variavel_global = 5 

# def funcao_global():
#     global variavel_global
#     variavel_global = 10
#     print(variavel_global)
    
# funcao_global() #10
# print(variavel_global) #10

#################################################

# def tabuada(numero):
#     print(f"Tabuada do {numero}: ")
#     for i in range(1, 11):
#         resultado = numero * i
#         print(f"{numero} x {i} = {resultado}")
        
# tabuada(7)

#################################################

# def tabuada(numero,h,j): #Define Função
#     print(f"Tabuada do {numero}: ")
#     for i in range(h,j): #Loop de 'h' até 'j'
#         resultado = numero * i
#         print(f"{numero} x {i} = {resultado}")
        
# tab = int(input("Digite o numero da tabuada: "))
# inicio = int(input("Digite o inicio da tabuada: "))
# fim = int(input("Digite o fim da tabuada: "))

# tabuada(tab,inicio,fim+1)

#################################################

# def contador(*num):
#     print(num)
    
# contador(1,2,3)
# contador(3,88,54,85,45,8,4,5)
# contador("casa","casa","casa","casa")


import operacoesTabuada

operacoesTabuada.tabuada(7)
operacoesTabuada.soma(8)
operacoesTabuada.subtracao(10)