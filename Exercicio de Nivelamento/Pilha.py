class Pilha:
    __pilha = []

    def adicionar(self, valor):
        self.__pilha.append(valor)
        print(self.__pilha,"\n")

    def imprimir(self):
        print(self.__pilha,"\n")

    def remover(self):
        self.__pilha.pop()
        print(self.__pilha,"\n")

p = Pilha()
while True:
    print("Menu")
    print("1 - Adicionar na Pilha")
    print("2 - Remover da Pilha")
    print("3 - Imprimir a Pilha")
    print("4 - Exit")
    a = int(input("Digite sua escolha: "))
    if a == 1:
        p.adicionar(input("Digite o valor que deseja adicionar: "))
    if a == 2:
        p.remover()
    if a == 3:
        p.imprimir()
    if a == 4:
        break