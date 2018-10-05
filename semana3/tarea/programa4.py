################################################
# File name: Tarea semana #3, Programa #4      #
# Author:    Jorge Castro                      #
# Submission: October 5, 2018                  #
# Instructor: Pedro Guzman                     #
################################################

aVocales = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
strNombres = ["", "", ""]

strNombres[0] = input("Por favor digite un primer nombre: ")
strNombres[1] = input("Por favor digite un segundo nombre: ")
strNombres[2] = input("Por favor digite un tercer nombre: ")
print("\n\rLa cantidad de vocales por nombre es la siguiente:\n\r")

for iName in range(0, 3):
    iTotVocales = 0
    for j in range(0, len(strNombres[iName])):
        for i in aVocales:

            #print(strNombres[0][j])
            if strNombres[iName][j] == i:
                iTotVocales += 1
    print("El nombre \"{}\" tiene un total de {} vocales.".format(strNombres[iName], iTotVocales))
