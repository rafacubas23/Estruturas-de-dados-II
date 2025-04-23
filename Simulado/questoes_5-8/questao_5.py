def ver_produtos():
    f = open("PRODUTOS.TXT", "r")
    for linha in f:
        linha = linha.strip()

        codigo = linha[:4].ljust(4)
        nome_produto = linha[4:19].ljust(15)
        preco = linha[19:].rjust(5)

        print(f"Código: {codigo} | Produto: {nome_produto} | Preço: {preco}")