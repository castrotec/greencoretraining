#Bullet 4

num1 = int(input("Digite el primer numero: "))
num2 = int(input("Digite el segundo numero: "))

if(num1 < num2):
    suma = 0
    for i in range(num1, num2+1):

        if(i%2 != 0):
            suma += i

    print("El total de numeros impares en el rango dado es: {}".format(suma))
else:
    print("Lo sentimos, el primer numero debe ser menor que el segundo")
