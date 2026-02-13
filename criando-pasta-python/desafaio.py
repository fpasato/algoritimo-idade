import os

while True:

    nome = input('Digite o nome da pasta: ').strip().lower()
    print()
    if os.path.exists(nome):

        print(f'A pasta com nome {nome} já existe')
        print()
    else:
        os.mkdir(nome)
        print("Pasta criada com sucesso!!")
         
    continuar = input('Deseja Criar uma nova pasta? \n[S]sim \nQualquer outra tecla para não\n ')
    if continuar == 's':
        continue
    else:
        print('fechando...')
        break