tempCel = input("Insira a Temperatura em celsius: ")

try:
    if ',' in tempCel:
        tempCel = tempCel.replace(",", '.')
    tempCel = float(tempCel)
    tempFarenheit = (tempCel*9/5) + 32
    print(f'Temperatura em Farenheit: {tempFarenheit}')
except:
    print("Insira apenas numeros!")