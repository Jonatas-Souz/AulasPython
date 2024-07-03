pessoa1 ={
    "Nome": "Chico",
    "Sobrenome": "Bento",
    "Idade": 18
    }

pessoas=[
    {
    "Nome": "Bob",
    "Sobrenome": "Esponja",   #Keys = Nome, Sobrenome, 
    "Idade": 13
    },
    {
    "Nome": "Chico",
    "Sobrenome": "Bento",
    "Idade": 18
    },
    {
    "Nome": "Sid",
    "Sobrenome": "Moreira",
    "Idade": 40
    }
]
print(pessoas)
print(f"O personagem: {pessoas[0]['Nome']} {pessoas[0]['Sobrenome']} tem {pessoas[0]['Idade']} anos")

# print(pessoa1)
# print(pessoa1.items())
# print(pessoas.values())
# print(pessoa1.keys())
# for k,v in pessoas[1].items():
#     print(f'O {k} e {v}')

print("---------------------------------")

pos = 0

for pos in range(0, len(pessoas)):
    for k, v in pessoas[pos].items():
        print(f'O {k} e {v}')
        pos = pos + 1
    print("-------")


