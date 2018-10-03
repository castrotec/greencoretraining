################################################
# File name: Tarea semana #3, Programa #1      #
# Author:    Jorge Castro                      #
# Submission: October 5, 2018                  #
# Instructor: Pedro Guzman                     #
################################################

num1 = int(input("Por favor digite un numero positivo: "))

if( num1 > 0):
    msg = "Por favor digite otro numero que sea al menos 50 veces mayor que {}: ".format(num1)
    num2 = int(input(msg))
    if(num2-num1 >= 50):
        #Inicia el calculo de la suma de todos los numeros entre el primer y segundo numero que sean multiplos de 3 y 5
        sum_total = 0

        for i in range(num1, num2+1):
            if(i%3==0 and i%5==0):
                sum_total += i
        print("El total de todos los numeros entre el primer y segundo numero que sean multiplos de 3 y 5 es: {}".format(sum_total))

    else:
        print("Lo sentimos. {} NO es al menos 50 veces mayor que {}".format(num1, num2))
else:
    print("Lo sentimos, el primer numero debe ser positivo")