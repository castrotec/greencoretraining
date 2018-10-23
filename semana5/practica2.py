#Diccionarios

import pprint
diccionario = {}

#Agregando llave
diccionario["nombre"] = "Jorge"
diccionario["numero"] = 34.5
diccionario["subdiccionario"] = {
    "sub_color" : "rojo",
    "sub_color2" : "verde"
}

pprint.pprint(diccionario)
