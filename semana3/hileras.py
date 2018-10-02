#Tema hileras

message = input("Digite lo que quiera: ")

print (message)

# len() -> Encontrar la cantidad de caracteres que tiene una hilera

print(len(message))
print(message[0])
print(message[len(message)-1])

# Concatenacion de hileras simple
hilera = "Hilera initial "
print(hilera + " y otra hilera")
print(hilera)

hilera += " y le agregamos mas"

print(hilera)

# Inyectando texto

otra_hilera = "Hola {}! Como esta?".format("Pedro")
print(otra_hilera)

print(otra_hilera[0:1])
