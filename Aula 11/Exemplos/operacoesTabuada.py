#Função tabuada
def tabuada(numero):
    print(f"Tabuada do {numero}: ")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")  
        
def soma(numero):
    print(f"Soma do {numero}: ")
    for i in range(1, 11):
        resultado = numero + i
        print(f"{numero} + {i} = {resultado}")  
        
def subtracao(numero):
    print(f"Subtracao do {numero}: ")
    for i in range(1, 11):
        resultado = numero - i
        print(f"{numero} - {i} = {resultado}")
