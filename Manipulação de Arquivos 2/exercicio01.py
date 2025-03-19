def contar_palavra(nome_arquivo, palavra):
    contador = 0
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            contador += linha.lower().count(palavra.lower())
    return contador

nome_arquivo = "arquivo_grande.txt"
palavra = input("Digite a palavra que deseja contar: ")
ocorrencias = contar_palavra(nome_arquivo, palavra)
print(f"A palavra '{palavra}' aparece {ocorrencias} vezes no arquivo.")