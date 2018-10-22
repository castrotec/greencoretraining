################################################
# File name: Tarea semana #4, Programa #2      #
# Author:    Jorge Castro                      #
# Submission: October 22, 2018                 #
# Instructor: Pedro Guzman                     #
################################################

RangoNumMin = float(input("Por favor digite el numero menor del rango: "))
RangoNumMax = float(input("Por favor digite el numero mayor del rango: "))
NumeroX = float(input("Por favor digite el numero a determinar si se encuentra en rango o no: "))

def RangoEsValido(NumMin, NumMax):
    if NumMin < NumMax:
        return True
    return False

def is_in_range(numero, num_min, num_max):
    if num_min <= numero <= num_max:
        return True
    return False

if RangoEsValido(RangoNumMin, RangoNumMax) == True:
    VarSiNo = "no"
    if is_in_range(NumeroX, RangoNumMin, RangoNumMax) == True:
        VarSiNo = "sí"
    print("El numero {} {} está dentro del rango de {} a {}.".format(NumeroX, VarSiNo, RangoNumMin, RangoNumMax))
else:
    print("Lo sentimos pero el segundo numero digitado ({}) no es mayor al primero ({})".format(RangoNumMin, RangoNumMax))