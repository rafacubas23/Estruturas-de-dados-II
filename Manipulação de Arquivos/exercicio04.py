with open("dados.txt", "r", encoding="utf-8") as arquivo:
    # Posicionando o cursor no início da segunda linha
    arquivo.readline()  # Lê e descarta a primeira linha
    segunda_linha = arquivo.readline()  # Lê a segunda linha

    print("Segunda linha do arquivo:", segunda_linha.strip())