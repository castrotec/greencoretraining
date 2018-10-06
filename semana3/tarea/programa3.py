################################################
# File name: Tarea semana #3, Programa #3      #
# Author:    Jorge Castro                      #
# Submission: October 6, 2018                  #
# Instructor: Pedro Guzman                     #
################################################

iIngresado = int(input("Por favor ingrese un numero entre 0 y 30: "))

if(iIngresado >= 0 and iIngresado <= 30):
    result = 1
    for i in range (1, iIngresado+1):
        result = result * i

    print("El factorial del numero {} es: {}".format(iIngresado, result))
else:
    print("Lo sentimos, el numero digitado debe ser mayor o igual a cero y menor o igual a 30")