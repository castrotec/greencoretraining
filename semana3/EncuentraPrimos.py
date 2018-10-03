#Encuentra los numeros primos en un rago
#Jorge Castro

for j in range(10, 90+1):

    ingresado = j
    divisibles = 0

    for j in range(1, ingresado):
        if(ingresado%j == 0):
            divisibles += 1

    if(divisibles == 1):
        print("El numero {} SI es primo".format(ingresado))
