#Bloco de código
#Estrutura Condicional
    
nota = float(input("digite sua media: "))

if nota>= 5: #Se nota é maior ou igual a 5
    print("voce passou de ano!") #Verdade
else:
    print("Repetiu ;)")#Se a nota é menor
print("Fim")

# E = &&
# OU = ||

# Media escola
#Aprovado acima de 6
#Reprovado a baixo de 3

media = float(input("Media: "))

if media>6:
    print("Aprovado")
else:
    if media<3:
        print("reprovado")
    else:
        print("recuperação")
        
################ OU #################

media = float(input("Media: "))

if media>6:
    print("Aprovado")
elif media<3: ## OBS 
    print("reprovado")
else:
    print("recuperação")
    

############### Outro Exemplo ################

media = 9
falta = 11

if media >7 and falta <=10:
    print("Aprovado")
else:
    print("Reprovado")


# # Aprovado se  media maior ou igual a 7
# # faltas até 10

from datetime import datetime

anoNascimento=int(input('Digite seu ano de nascimento:'))

# anoAtual=2024
anoAtual= datetime.now().year
print(anoAtual)
idade=anoAtual-anoNascimento

if idade<=5:
    print("Você não pode se inscrever")
    input()
elif idade<=9:
    categoria="MIRIM"
elif idade<=14:
    categoria="INFANTIL"
elif idade<=19:
    categoria="JUNIOR"
elif idade<=24:
    categoria="SÊNIOR"
else:
    categoria="MASTER"

print(F"Você está na categoria: {categoria}")

# input(


