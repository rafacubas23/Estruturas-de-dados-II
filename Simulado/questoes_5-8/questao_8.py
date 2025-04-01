def atualizar_produto_binaria():
    codigo_busca = input("Digite o código do produto que deseja buscar (4 caracteres): ").strip()
    if len(codigo_busca) != 4:
        print("O código deve conter exatamente 4 caracteres.")
        return

    f = open("PRODUTOS.TXT", "r")
    linhas = f.readlines()
    f.close()

    linhas.sort()

    inicio = 0
    fim = len(linhas) - 1
    produto_encontrado = False

    while inicio <= fim:
        meio = (inicio + fim) // 2
        linha_atual = linhas[meio]
        codigo_atual = linha_atual[:4]

        if codigo_atual == codigo_busca:
            produto_encontrado = True

            nome_atual = linha_atual[4:19].strip()
            preco_atual = linha_atual[19:].strip()

            print(f"Produto encontrado: Código: {codigo_atual}, Nome: {nome_atual}, Preço: {preco_atual}")

            novo_nome = input("Digite o novo nome do produto (até 15 caracteres): ").strip()
            if len(novo_nome) > 15:
                print("O nome do produto deve ter no máximo 15 caracteres.")
                return

            novo_preco = input("Digite o novo preço do produto (no formato 00.00): ").strip()
            if len(novo_preco) > 5 or not novo_preco.replace('.', '', 1).isdigit():
                print("O preço deve ter no máximo 5 caracteres e estar no formato 00.00.")
                return

            linhas[meio] = f"{codigo_atual.ljust(4)}{novo_nome.ljust(15)}{novo_preco.rjust(5)}\n"

            print(f"Produto atualizado: Código: {codigo_atual}, Nome: {novo_nome}, Preço: {novo_preco}")
            break
        elif codigo_atual < codigo_busca:
            inicio = meio + 1
        else:
            fim = meio - 1

    if not produto_encontrado:
        print("Produto com o código informado não foi encontrado.")
        return

    f = open("PRODUTOS.TXT", "w")
    f.writelines(linhas)
    f.close()

    print("Arquivo atualizado com sucesso!")