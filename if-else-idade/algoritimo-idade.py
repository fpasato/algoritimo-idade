

idade = int(input('Digite uma idade: '))

if idade < 13:
    print(F"Criança")
elif idade < 18:
    print(F"Adolescente")
elif idade < 60:
    print(F"Adulto")
else:
    print(F"Idoso")