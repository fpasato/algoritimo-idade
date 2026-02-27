

alunos = ['fer - aprovado']


# escolha = input('Menu de opções:\n[1] - Cadastrar aluno\n[2] - Listar alunos\n[3] - Sair')


while True:
    print("Sistema Escolar".center(30, '='))
    print('''
        Menu de opções:\n[1] - Cadastrar aluno\n[2] - Listar alunos\n[3] - Sair
          ''')
    escolha = input('Escolha a ação: ')


    match escolha:
        case '1':
            nome =  input('Digite o nome do aluno: ')
            nota1 =  int(input('Digite a primeira nota: '))
            nota2 =  int(input('Digite a segunda nota: '))

            media = (nota1 + nota2) / 2 
            
            if media > 6:
                alunos.append(f'{nome} - Aprovado')
            else:
                alunos.append(f'{nome} - Reprovado')

        case '2':
            print()
            for aluno in alunos:
                print(aluno)
            print()
            
        case '3':
            print("Fechando programa")
            break
        case _:
            print("Opção inválida, Tente novamente")
            continue
    
    
    





    
        # ┌───────┐
        # │       │
        # └───────┘