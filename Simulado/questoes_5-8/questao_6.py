def adicionar_produto():

    f = open("PRODUTOS.TXT","a")
    while True:

        codigo = input("Digite o código (4 caracteres): ").strip()
        if len(codigo) != 4:
            print("O código deve ter exatamente 4 caracteres.")
            continue

        nome_produto = input("Digite o nome do produto (até 15 caracteres): ").strip()
        if len(nome_produto) > 15:
            print("O nome do produto deve ter no máximo 15 caracteres.")
            continue

        preco = input("Digite o preço (no formato 00.00): ").strip()
        if len(preco) > 5 or not preco.replace('.', '', 1).isdigit():
            print("O preço deve ter no máximo 5 caracteres e estar no formato 00.00.")
            continue

        registro = f"{codigo.ljust(4)}{nome_produto.ljust(15)}{preco.rjust(5)}\n"
        f.write(registro)
        print(f"Produto adicionado: Código: {codigo}, Nome: {nome_produto}, Preço: {preco}")

        continuar = input("Deseja adicionar outro produto? (s/n): ").strip().lower()
        if continuar != 's':
            break

    print(f"Registros adicionados!")