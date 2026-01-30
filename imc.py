peso = float(input('Digite o peso: (em kg) ex: 68: '))
altura = float(input('Digite a altura: (em metros) ex: 1.75: '))


altura_metros = altura / 100
imc = peso / (altura_metros * altura_metros)

if imc < 18.5:
    print(' abaixo do peso ')
elif imc > 18.5 and imc < 24.9:
    print(' peso normal')
elif imc > 25 and imc < 29.9:
    print(' sobrepeso ')
elif imc > 30 and imc < 30.9:
    print(' obesidade ')
else:
    print('obesidade grave ')

print(imc)
