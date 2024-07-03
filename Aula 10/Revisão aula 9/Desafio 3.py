# DESAFIO 03

# Crie um programa onde o usuário possa digitar cinco valores
# numéricos e cadastre-os em uma lista, já na sua posição
# correta de inserção (sem usar o sort()).

# No final mostre a lista ordenada na tela


lista = []

for contador in range(0,5):   #contador =5
    num = int(input("Digite um valor: ")) # 3,8,6,5,-2
   
    if contador == 0 or num > lista[-1]:
        lista.append(num)
        print('Adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(lista):  # pos =0 e len=4 → 0<4?
            if num <= lista[pos]: # -2<= 3?
                lista.insert(pos,num)
                print(f"Adicionado na posição {pos} da lista")
                break
            pos += 1
 
#lista [-2,3,5,6,8]  
print(f"Os valores digitados em ordem foram {lista}")