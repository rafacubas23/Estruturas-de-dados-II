with open("dados2.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Rafael Cubas\n")

with open("dados2.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
    print("Conteúdo usando read():\n", conteudo)

with open("dados2.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write("23/07/2003\n")
    arquivo.write("São Bento do Sul\n")
    arquivo.write("21\n")

with open("dados2.txt", "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()
    print("\nConteúdo usando readlines():")
    print(linhas)

with open("dados2.txt", "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()
    print("\nConteúdo linha por linha com numeração:")
    for i, linha in enumerate(linhas, start=1):
        print(f"Linha {i}: {linha.strip()}")
