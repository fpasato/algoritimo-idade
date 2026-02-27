
def menu_opcao():
    print("Sistema Escolar".center(30, '='))
    print('''
        Menu de opções:\n[1] - Cadastrar aluno\n[2] - Listar alunos\n[3] - Sair\n[4] - Mostrar total de alunos cadastrados
          ''')

def cadastro_aluno():  
    nome =  input('Digite o nome do aluno: ')
    nota1 =  int(input('Digite a primeira nota: '))
    nota2 =  int(input('Digite a segunda nota: '))

    media = (nota1 + nota2) / 2 
    
    if media > 6:
        alunos.append(f'{nome} - Aprovado')
    else:
        alunos.append(f'{nome} - Reprovado')

def listar_alunos():
    if len(alunos) > 0 :
        print()
        for aluno in alunos:
            print(aluno)
        print()
    else:
        print("A lista de alunos esta vazia.")

def total_alunos():
    if len(alunos) < 1:
        print('Nenhum aluno cadastrado ainda.')
    else:
        print(f'A lista tem {len(alunos)} alunos cadastrados.')

alunos = ['fer - aprovado']

while True:
    menu_opcao()
    escolha = input('Escolha a ação: ')

    match escolha:
        case '1':
            cadastro_aluno()

        case '2':
           listar_alunos()

        case '3':
            print("Fechando programa")
            break
        case '4':
            total_alunos()
        case _:
            print("Opção inválida, Tente novamente")
            continue



