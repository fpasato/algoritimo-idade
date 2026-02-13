import os


nome_pasta = "meus_alunos"

# os.mkdir(nome_pasta)

arquivo = os.path.join(nome_pasta,'arquivo.txt')

with open(arquivo, 'w', encoding='utf-8') as f:
    f.write('Hello World')
