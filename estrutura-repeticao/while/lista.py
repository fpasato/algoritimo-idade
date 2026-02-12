lista = [1,2,3,-4,5,-6,-7,-8,-9]

lista_nova = []

for n in lista:
    if n <=0:
        lista_nova.append(0)
    else:
        lista_nova.append(n)


print(lista)
print(lista_nova)
