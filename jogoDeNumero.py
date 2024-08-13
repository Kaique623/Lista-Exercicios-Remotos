import json

num = 53

try:
    with open("tentativas.json", 'a+') as data:
        tentativas = data.read()
except:
    print("Erro ao ler tentativas passadas!")

tentativas = []

print("Adivinhe o numero de 1 a 100")
while True:
    chute = input("Chute: ")

    try:
        chute = int(chute)
    except:
        print("Insira apenas numeros inteiros!")
        continue

    if chute > 100 or chute < 1:
        print("Chute Fora do limite!")
        continue

    if chute == num:
        print("Você ganhou!")
        try:
            with open('tentativas.json', 'w') as data:
                json.dump('', data)
        except:
            print("Erro ao resetar data!")
        break
    else:
        tentativas.append(chute)
        print("Tente Novamente!")

    try:
        with open("tentativas.json", 'w') as data:
            json.dump(tentativas, data)
    except:
        print("erro ao salvar tentativaw")