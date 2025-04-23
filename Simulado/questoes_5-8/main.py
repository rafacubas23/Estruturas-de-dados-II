from questao_5 import ver_produtos
from questao_6 import adicionar_produto
from questao_7 import atualizar_produto
from questao_8 import atualizar_produto_binaria

while True:
    print("\nMenu de Opções")
    print("1. Ver produtos")
    print("2. Adicionar produtos")
    print("3. Buscar e atualizar produto (Sequencial)")
    print("4. Buscar e atualizar produto (Binário)")
    print("5. Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print("\n--- Ver produtos ---")
        ver_produtos()

    elif opcao == 2:
        print("\n--- Adicionar produtos ---")
        adicionar_produto()

    elif opcao == 3:
        print("\n--- Buscar e atualizar produto (Sequencial) ---")
        atualizar_produto()

    elif opcao == 4:
        print("\n--- Buscar e atualizar produto (Binário) ---")
        atualizar_produto_binaria()

    elif opcao == 5:
        print("\nSaindo do programa. Até mais!")
        break

    else:
        print("\nOpção inválida. Tente novamente.")
