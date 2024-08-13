anoNasc = input("Insira ano nascimento: ")

try:
    anoNasc = int(anoNasc)
    if anoNasc > 2024 or anoNasc < 1900:
        print("Data Invalida")
    else:
        print(f"Idade: {2024-anoNasc}")

except ValueError:
    print("Apenas numeros inteiros")

except:
    print("Insira apenas numeros")