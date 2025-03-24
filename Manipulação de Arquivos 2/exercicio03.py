import tempfile
import os
from datetime import datetime

num_eventos = int(input("Quantos eventos deseja registrar? "))

with tempfile.NamedTemporaryFile(mode='w+', delete=False, encoding='utf-8') as temp:
    for i in range(num_eventos):
        log = f"[Evento {i + 1}] {datetime.now()}\n"
        temp.write(log)
        print(log, end='')

    temp_path = temp.name

if input("Salvar logs permanentemente? (s/n): ").lower() == 's':
    nome_arquivo = input("Nome do arquivo para salvar: ")
    with open(nome_arquivo, 'w', encoding='utf-8') as perm:
        with open(temp_path, 'r', encoding='utf-8') as t:
            perm.write(t.read())
        print(f"Logs salvos em {nome_arquivo}")

os.unlink(temp_path)
print("Arquivo temporário removido")