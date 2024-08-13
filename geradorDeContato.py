import json

open('contatos.json', 'a+').close()

contatos = {}

try:
    with open('contatos.json', 'r') as data:
        contatos = json.load(data)
except:
    print("Erro ao ler arquivo!")

formato = '####-####'
correcao = ''

numero = input("Insira o número e telefone (1234-5678): ")

if len(numero) == 8 and numero.isdigit() or len(numero) == 9 and not numero.isdigit():
    for i in numero:
        if len(correcao) == 4 and i.isdigit(): 
            correcao += '-'
        if i.isdigit():
            correcao += i
else:
    print("Numero Invalido!")

nome = input("Insira o seu nome: ")
if not correcao in contatos:
    contatos[correcao] = nome
else:
    print("Numero ja salvo!")
try:
    with open('contatos.json', 'w') as data:
        json.dump(contatos, data)
except:
    print("Erro ao escrever arquivo!")

print(contatos)