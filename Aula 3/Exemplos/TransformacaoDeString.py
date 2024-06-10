texto = "Curso de Python"

trocaTexto = texto.replace("Python" , "JavaScript")
print(trocaTexto)
print(texto)
print(f"Temos {texto} e {trocaTexto}, venha estudar conosco")

textoMinusculo = texto.upper() #Deixa o texto em caixa alta
print(textoMinusculo)

textoMaiusculo = texto.lower() #Deixa o texto minusculo
print(textoMaiusculo)

textoCaptalize = texto.capitalize() #
print(textoCaptalize)

fraseTitle = texto.title() #Deixa as iniciais de cada paavra maiuscila
print(fraseTitle)




print("****Como Tirar Espaco****")

texto2 = " com espaco "
removeEspaco = texto2.strip() #
print(" com espaco ")
print(removeEspaco)



print("****Divisao****")

juntaFrase = '-'.join(texto) #Junta as letas, no caso, c-u-r-s-o- -d-e- -P-y-t-h-o-h-
print(juntaFrase)

divideFrase = texto.split() #Separa as palavras, no caso, ['Curso', 'de', 'Python'] 
print(divideFrase)