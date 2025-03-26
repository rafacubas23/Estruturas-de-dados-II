arquivo = "VEICULOS.TXT"

#Exercicio1
def exibir_registros():
    try:
        with open(arquivo, "r", encoding="utf-8") as file:
            print("\nRegistros do arquivo 'VEICULOS.TXT':\n")
            for linha in file:
                linha = linha.strip()
                if len(linha) == 14:
                    codigo = linha[0:3]
                    placa = linha[3:10]
                    ano = linha[10:14]
                    print(f"CÓDIGO: {codigo}, PLACA: {placa}, ANO: {ano}")
                else:
                    print("Erro: Registro fora do padrão esperado.")
    except FileNotFoundError:
        print(f"O arquivo '{arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo: {e}")

#Exercicio2
def inserir_registro():
    try:
        codigo = input("Digite o CÓDIGO (3 dígitos): ").zfill(3)
        placa = input("Digite a PLACA (7 caracteres, ex: ABC1234): ").upper()
        ano = input("Digite o ANO (4 dígitos): ")

        if len(codigo) != 3 or not codigo.isdigit():
            print("Erro: O CÓDIGO deve conter exatamente 3 dígitos.")
            return

        if len(placa) != 7 or not placa.isalnum():
            print("Erro: A PLACA deve conter exatamente 7 caracteres alfanuméricos.")
            return

        if len(ano) != 4 or not ano.isdigit():
            print("Erro: O ANO deve conter exatamente 4 dígitos.")
            return

        novo_registro = f"{codigo}{placa}{ano}\n"

        with open(arquivo, "a", encoding="utf-8") as file:
            file.write(novo_registro)

        print("Novo registro inserido com sucesso!")

    except Exception as e:
        print(f"Ocorreu um erro ao inserir o registro: {e}")

#Exercicio3
def alterar_registro():
    """Altera os atributos de PLACA e ANO do veículo com base no código fornecido."""
    try:
        codigo_busca = input("Digite o CÓDIGO do veículo que deseja alterar (3 dígitos): ").zfill(3)

        # Ler todo o conteúdo do arquivo
        with open(arquivo, "r", encoding="utf-8") as file:
            linhas = file.readlines()

        encontrado = False

        novo_conteudo = []

        for linha in linhas:
            linha = linha.strip()
            if linha[:3] == codigo_busca:  # Compara os primeiros 3 caracteres com o código buscado
                print(f"Registro encontrado: CÓDIGO: {linha[:3]}, PLACA: {linha[3:10]}, ANO: {linha[10:14]}")
                placa_nova = input("Digite a nova PLACA (7 caracteres, ex: ABC1234): ").upper()
                ano_novo = input("Digite o novo ANO (4 dígitos): ")

                if len(placa_nova) != 7 or not placa_nova.isalnum():
                    print("Erro: A PLACA deve conter exatamente 7 caracteres alfanuméricos.")
                    return

                if len(ano_novo) != 4 or not ano_novo.isdigit():
                    print("Erro: O ANO deve conter exatamente 4 dígitos.")
                    return

                novo_registro = f"{codigo_busca}{placa_nova}{ano_novo}\n"
                novo_conteudo.append(novo_registro)
                encontrado = True
            else:
                novo_conteudo.append(linha + "\n")

        if not encontrado:
            print(f"Código {codigo_busca} não encontrado no arquivo.")

        with open(arquivo, "w", encoding="utf-8") as file:
            file.writelines(novo_conteudo)

        if encontrado:
            print("Registro alterado com sucesso!")

    except FileNotFoundError:
        print(f"O arquivo '{arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao alterar o registro: {e}")

#Exercicio4
def excluir_registro_por_codigo():
    try:
        codigo_busca = input("Digite o CÓDIGO do veículo que deseja excluir (3 dígitos): ").zfill(3)


        with open(arquivo, "r", encoding="utf-8") as file:
            linhas = file.readlines()

        linhas.sort(key=lambda x: x[:3])

        inicio, fim = 0, len(linhas) - 1
        encontrado = False

        while inicio <= fim:
            meio = (inicio + fim) // 2
            codigo_atual = linhas[meio][:3]

            if codigo_atual == codigo_busca:
                encontrado = True
                print(f"Registro encontrado: {linhas[meio].strip()}")
                del linhas[meio]
                break
            elif codigo_atual < codigo_busca:
                inicio = meio + 1
            else:
                fim = meio - 1

        if not encontrado:
            print(f"Código {codigo_busca} não encontrado no arquivo.")
        else:
            with open(arquivo, "w", encoding="utf-8") as file:
                file.writelines(linhas)
            print("Registro excluído com sucesso!")

    except FileNotFoundError:
        print(f"O arquivo '{arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao excluir o registro: {e}")

# Menu principal
while True:
    print("\n=== MENU ===")
    print("1. Exibir registros")
    print("2. Inserir novo registro")
    print("3. Alterar registro")
    print("4. Excluir registro")
    print("5. Sair")
    try:
        opcao = int(input("Escolha uma opção: "))
        if opcao == 1:
            exibir_registros()
        elif opcao == 2:
            inserir_registro()
        elif opcao == 3:
            alterar_registro()
        elif opcao == 4:
            excluir_registro_por_codigo()
        elif opcao == 5:
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")
    except ValueError:
        print("Por favor, insira um número válido.")