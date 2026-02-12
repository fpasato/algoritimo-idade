'''

'''

while True: 
    n1 = int(input('Digite um número: '))
    n2= int(input('Até onde a tabuada vai: '))

    if n1 <= 0 or n2 <= 0:
        print('Números negatiivos não são permitidos!!')
        continue
    else:
        for i in range(n2):
            i+=1
            print(f'{n1} x {i} = {n1 * i}')
        

        continuar = input('Quer geraar outra tabuada? \n[S]Sim\nQualquer outra tecla para não\n').strip().lower()

        if continuar == 's':
            continue
        else:
            print('\033[4;37;41mFechando calculadora...\033[m')

            break