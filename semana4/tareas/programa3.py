################################################
# File name: Tarea semana #4, Programa #3      #
# Author:    Jorge Castro                      #
# Submission: October 22, 2018                 #
# Instructor: Pedro Guzman                     #
################################################

numero_evaluar = int(input("Por favor digite el numero entero positivo a evaluar: "))

def entero_es_positivo(num):
    if num > 0:
        return True
    return False

def es_num_perfecto(num):
    suma_total = 0
    for i in range(1, num):
        if (num % i == 0):
            suma_total += i
    if num == suma_total:
        return True
    return False

if entero_es_positivo(numero_evaluar):
    #El numero entero ingresado, sí es positivo
    if es_num_perfecto(numero_evaluar):
        print("El número {} sí es perfecto".format(numero_evaluar))
    else:
        print("El número {} NO es perfecto".format(numero_evaluar))
else:
    print("Lo sentimos, el numero digitado debe ser un número entero mayor o igual a cero")

