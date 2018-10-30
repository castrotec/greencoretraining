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
    # Todos los metodos al inicio deben llevar el self, incluido el constructor
    # -------------------------

    # Metodo constructor
    # La responsabilidad de un constructor en un objeto
    # es realizar la inicializacion. self es una referencia hacia la instancia

    def __init__(self, nombre, apellido, cedula, edad = None, *args, **kwargs):
        self.nombre = nombre
        self._apellido = apellido
        self.edad = edad
        self.cedula = cedula
        if "profesion" in kwargs:
            self.profesion = kwargs["profesion"]

    def get_full_name(self):
        return "{} {}".format(self.nombre, self._apellido)

    @property
    def full_name(self):
        return "{} {}".format(self.nombre, self._apellido)

persona = Persona(
    "Jorge",
    "Castro",
    "11111111",
    None,
    12, "hola", ["h", "m"],
    profesion = "ingenieria"
)

# Por tanto *args es una lista, mientras que **kwargs es un diccionario

# TODO METODO ATRIBUTO QUE INICIE CON UNDERSCORES:
#   _PROTECTED (un underscore)
#   __PRIVADO (dos underscores)

print(persona.get_full_name())
print(persona.full_name)