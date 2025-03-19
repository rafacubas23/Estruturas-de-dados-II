with open("frases.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Estudando Python.\n")
    arquivo.write("Programando em Python.\n")
    arquivo.write("Manipulação de arquivos.\n")

def linhas_com_python():
    with open("frases.txt", "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
        return [linha.strip() for linha in linhas if "Python" in linha]

print("\nLinhas com 'Python':", linhas_com_python())

def linhas_com_palavra(chave):
    with open("frases.txt", "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
        return [linha.strip() for linha in linhas if chave in linha]

palavra_usuario = input("Digite uma palavra para buscar nas frases: ")
print("\nLinhas com a palavra específica:", linhas_com_palavra(palavra_usuario))