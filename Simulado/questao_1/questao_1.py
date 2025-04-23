f = open("arquivo2.txt", "r")
print(f.readline())
f.seek(3)
print(f.readline())

# respostas corretas:
# Para o arquivo “arq1.txt” será exibido “domingo” e “ingo”.
# Para o arquivo “arq2.txt” será exibido “Reveillon” e “eillon”.