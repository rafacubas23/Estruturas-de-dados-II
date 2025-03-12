class NodeFila:
    def __init__(self, valor, proximo):
        self.valor = valor
        self.proximo = proximo

    def getValor(self):
        return self.valor

    def setValor(self, valor):
        self.valor = valor

    def getProximo(self):
        return self.proximo

    def setProximo(self, proximo):
        self.proximo = proximo

class Fila:

    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def adicionar(self, valor):
        if not self.primeiro:
            temp = NodeFila(valor, self.primeiro)
            self.primeiro = temp
            self.ultimo = temp
        else:
            temp = NodeFila(valor, None)
            self.ultimo.setProximo(temp)
            self.ultimo = temp
        self.imprimir()

    def imprimir(self):
        if not(self.primeiro):
            print("Fila Vazia...")
        else:
            temp = self.primeiro
            fila = []
            while temp:
                fila.append(temp.getValor())
                temp = temp.getProximo()
            print("\n",fila,"\n")

    def remover(self):
        self.primeiro = self.primeiro.getProximo()
        self.imprimir()

f = Fila()
while True:
    print("Menu")
    print("1 - Adicionar na Fila")
    print("2 - Remover da Fila")
    print("3 - Imprimir a Fila")
    print("4 - Exit")
    a = int(input("Digite sua escolha: "))
    if a == 1:
        f.adicionar(input("Digite o valor que deseja adicionar: "))
    if a == 2:
        f.remover()
    if a == 3:
        f.imprimir()
    if a == 4:
        break