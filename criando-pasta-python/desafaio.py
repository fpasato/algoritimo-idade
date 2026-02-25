import os

while True:
    nome = input('Digite o nome da pasta: ').strip().lower()

    if nome == '':
        print("\033[0;30;41mNome invalido, tente novamente\033[m")
        continue

    if os.path.exists(nome):
        print(f"\033[0;30;43mA pasta com nome {nome} já existe\033[m")

    else:
        os.mkdir(nome)
        print("\033[0;30;42mPasta criada com sucesso!!\033[m")

         
    continuar = input('Deseja Criar uma nova pasta? \n[S]sim \nQualquer outra tecla para não\n ')
    if continuar == 's':
        continue
    else:
        print('fechando...')
        break