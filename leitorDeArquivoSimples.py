try:
    open('Arquivos.txt', 'r', encoding="utf-8").readlines()
    print("Leitura Feita")
except FileNotFoundError:
    open('Arquivos.txt', 'a+')
except PermissionError:
    print("Permissão Insuficiente")
except ValueError:
    print("Arquivo Vazio")
except UnicodeEncodeError:
    print("Erro ao Codificar Arquivo")
