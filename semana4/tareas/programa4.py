################################################
# File name: Tarea semana #4, Programa #4      #
# Author:    Jorge Castro                      #
# Submission: October 22, 2018                 #
# Instructor: Pedro Guzman                     #
################################################

num_1 = 14
num_2 = 94
num_3 = 15

def get_decena_cercana(num):
    return 10 * round(num / 10)

def round_num(num_a, num_b, num_c):
    return get_decena_cercana(num_a) + get_decena_cercana(num_b) + get_decena_cercana(num_c)

def calcula_y_muestra_resultado():
    print("El resultado de la suma es: {}".format(resultado))


resultado = round_num(num_1, num_2, num_3)
calcula_y_muestra_resultado()