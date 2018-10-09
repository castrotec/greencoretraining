#Jorge Castro

#Programa 1

numero1 = 2000
numero2 = 3200

def es_divisible(num_entrada, num_divisor) -> bool:
    return num_entrada%num_divisor == 0

#es_divisible_entre(30, 4)
def extraer_numeros_divisibles_por_7_no_por_5 (min, max):
    los_que_cumplen_la_condicion = [] #Creamos una lista vacia
    for numero in range(min, max+1):
        if es_divisible(numero,7) and not es_divisible(numero, 5):
            los_que_cumplen_la_condicion.append(numero)
    return los_que_cumplen_la_condicion

print (extraer_numeros_divisibles_por_7_no_por_5(2000, 3200))
