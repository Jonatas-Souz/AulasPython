# # Lista

#lista = [4,5,3,6,8,6,12]
# print(lista) 
# print(lista[3]) #Posição 3
# print(lista[-1]) #Imprime Ultima posição

# lista.append(101)#Adicionar no Final
# print(lista)

# lista.insert(7, 8)#Posisão e novo valor e realoca o restante
# print(lista)

# lista.remove(6)#Apaga o primeiro numero da lista indicado no comando
# print



# lista = [4,5,3,6,8,6,12]

# lista.sort()
# print(lista) #Crescente

# lista.reverse()
# print(lista)#Decrescente

# print(lista.count(6))

# excluido = lista.pop()
# print(f"REMOVIDO= {excluido}")
# print(lista)

compra = [10.2, 3.35, 16.3,["tomate","sabone","arroz"]]
print(compra)
produtos = compra[3]
print(produtos)
total = compra[0]+compra[1]+compra[2]#Soma os valores
print(total)

letra = ["a","b","c"]
num = [2,4,6]
tudo = [num,letra] #[[2, 4, 6], ['a', 'b', 'c']]
print(tudo)
tudo1 = [num+letra] #[[2, 4, 6, 'a', 'b', 'c']]
print(tudo1)

