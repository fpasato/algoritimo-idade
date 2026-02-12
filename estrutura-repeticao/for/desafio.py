notas = [8,3,6,5,4,9,8,4,6,2,7,6,5,8,8,7]

aprovados = 0
acompanhamento = 0

for nota in notas:
    if nota > 6:
        print(f'Nota: {nota} Funcionário aprovado')
        aprovados +=1
    else:
        print(f'Nota: {nota} Funcionário em acompanhamento')
        acompanhamento +=1
print(f'\nFuncionários Aprovados: {aprovados}')
print(f'Funcionários em acompanhamento: {acompanhamento}')