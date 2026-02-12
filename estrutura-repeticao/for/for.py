# nome_alunos = ["Seu Antonio", "Idalguinho", "Fefe", "Uilian", "Eztêfãnia", "Luzkinha", "Rapaizinho de rosa", "Didi", "Lendrin do Gr@a", "Lele"]


# for nome in nome_alunos:
#     print(nome)


veiculos = ["Fusca","D20",  "Doublo", "Marea Turbo", "Tiggo", "Uno", "Gol bolinha", "Chevette", "Monza Tubarão", "cadete", "omega", "Veraneio"]

for carro in veiculos:
    # outros carros: nome do carro + carro legal
    # D20,  Chevette e Veraneio : nome do carro + carro classicos
    if carro == "D20" or carro == "Chevette" or carro == "Veraneio":
        print(f'{carro} Carro Clássico')
    else:
        print(f'{carro} Carro legal')
