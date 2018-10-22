################################################
# File name: Tarea semana #4, Programa #1      #
# Author:    Jorge Castro                      #
# Submission: October 22, 2018                 #
# Instructor: Pedro Guzman                     #
################################################

print("A continuacion se le solicitaran 3 numeros")

num1 = float(input("Por favor digite el primer numero: "))
num2 = float(input("Por favor digite el segundo numero: "))
num3 = float(input("Por favor digite el tercer numero: "))

def DevuelveMayor(num1, num2, num3):
    mayor = num1
    if num2 > mayor:
        mayor = num2
    if num3 > mayor:
        mayor = num3

    return mayor * 1

print("El numero mayor es: {}".format(DevuelveMayor(num1, num2, num3)))
