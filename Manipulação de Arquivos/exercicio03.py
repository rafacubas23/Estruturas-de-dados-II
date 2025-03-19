with open("contatos.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Nome: Celular:\n")
    arquivo.write("Guilherme (41) 9 9123-4567\n")
    arquivo.write("Rafaela (47) 9 2002-2222\n")
    arquivo.write("Eduardo (48) 9 9876-5432\n")
    arquivo.write("Mercado (47) 3003-1010\n")

def buscar_contato():
    with open("contatos.txt", "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
        contatos = {linha.split()[0]: linha.split(" ", 1)[1].strip() for linha in linhas[1:]}

    while True:
        nome = input("Digite o nome do contato (ou 'sair' para encerrar): ")
        if nome.lower() == "sair":
            break
        print(contatos.get(nome, "Contato não encontrado."))

buscar_contato()
