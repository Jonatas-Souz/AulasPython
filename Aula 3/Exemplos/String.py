texto = "Curso de Python"

print(texto)
print(texto[6]) # "[]" imprime a letra da posição indicada, no caso a 6
print(texto[9:15]) # Vai imprimir "de" [;] "até"
print(texto[9:15:2]) #Imprime pulando Letras "Pto"
print(texto[:5]) #Para trás da aposição 5
print(texto[6:]) #Adiante da posição 6

print(len(texto)) #Conta tamanho do string

print(f"Letras o: {texto.count('o')}") #Conta quantas vezes a letra selecionada aparece, obs, não usar ("")

print(f"Existe Pythin?: {texto.find(' Python')}") #Obs "espaço" também é caracter, posisão 8
print(f"Existe Pythin?: {texto.find('Python')}") # Posisão 9
print(f"Existe Pythin?: {texto.find('um')}") #-1 Quando não encontrar

print(f"Existe Python na frase? {'Python' in texto}") #Diz se é falso ou verdadeiro, se tem certa palavra numa frase, no caso True
print(f"Existe 1Python na frase? {'1Python' in texto}") #False