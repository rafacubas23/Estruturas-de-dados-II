def comparar_arquivos_binarios(arquivo1, arquivo2):
    with open(arquivo1, "rb") as f1, open(arquivo2, "rb") as f2:
        posicao = 0
        while True:
            byte1 = f1.read(1)
            byte2 = f2.read(1)

            if not byte1 and not byte2:
                print("Os arquivos são idênticos.")
                return

            if byte1 != byte2:
                print(f"Os arquivos são diferentes. Primeira diferença encontrada na posição {posicao}.")
                return

            posicao += 1

comparar_arquivos_binarios("arquivo1.bin", "arquivo2.bin")
comparar_arquivos_binarios("arquivo1.bin", "arquivo3.bin")
comparar_arquivos_binarios("arquivo2.bin", "arquivo3.bin")
