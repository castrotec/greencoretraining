class Persona (object):

    # -------------------------
    # ATRIBUTOS
    # -------------------------
    '''
    nombre = ""
    apellido = ""
    edad = 0
    cedula = ""
    '''

    # -------------------------
    # METODO
    # -------------------------

    # Metodo constructor
    # La responsabilidad de un constructor en un objeto
    # es realizar la inicializacion. self es una referencia hacia la instancia

    def __init__(self, nombre, apellido, cedula, edad = None, *args, **kwargs):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.cedula = cedula
        if "profesion" in kwargs:
            self.profesion = kwargs["profesion"]

persona = Persona(
    "Jorge",
    "Castro",
    "11111111",
    None,
    12, "hola", ["h", "m"],
    profesion = "ingenieria"
)

# Por tanto *args es una lista, mientras que **kwargs es un diccionario

print(persona.profesion)