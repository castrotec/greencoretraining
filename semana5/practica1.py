#Practica

def suma(x,y):
    return x + y

lista = ["jorge", 21, 213.5, False, suma]

#for elemento in lista: print(type(elemento))

#print(type(lista[-1]))

#texto = "Hola Jorge!"
#print(texto[0:2])

mi_lista = []
mi_lista_de_listas = []

for numero in range (0, 8):
    #mi_lista.append(numero)
    mi_lista_de_listas.append([])
    for num in range (0, 3):
        mi_lista_de_listas[numero].append(num)

#print(mi_lista_de_listas)

def print_matrix_impura(matrix):
    for fila in matrix:
        print (fila)

#print_matrix_impura(mi_lista_de_listas)

#import pprint
#pprint.pprint(mi_lista_de_listas)