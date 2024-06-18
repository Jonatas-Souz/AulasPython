#Desafio Temperatura

qnt_pessoas = int(input("Quantas pessoas analizadas? "))
fim = qnt_pessoas+1
somatoria = 0
print("_______________________________________________")
for i in range(1,fim):
    temperatura = float(input("Digite a teperatura: (°C)"))
    somatoria = somatoria + temperatura
    print(f"Paciente {i}")
    if temperatura <= 37.2:
        print("Temperatura Normal👍")
    elif temperatura > 37.2 and temperatura<=38:
        print("Está Febril😐")
    elif temperatura > 38 and temperatura<=39:
        print("Está com Febre😨")
    else:
        print("Está com febre alta🤯")
    print("_______________________________________________")
media = somatoria / qnt_pessoas
print(f"Média igual da Temperatura = {media}")
print("_______________________________________________")