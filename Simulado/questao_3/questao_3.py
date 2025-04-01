f = open("arquivo1.txt", "r")

reg = f.readlines()
c1 = reg[3][:3]
c2 = reg[3][3:10]
c3 = reg[3][10:]
print(c2, c1, c3)

# resposta correta:
# A saída será MFJ2527 004 2011:
