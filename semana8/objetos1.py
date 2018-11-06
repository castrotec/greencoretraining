
#Notes
'''
__ un underscore: privado (el alcance se limita a la clase)
_ dos underscore: protected
ningun un#Herencia siempre implica polimorfismoderscore: publico

#Herencia siempre implica polimorfismo
'''
#

class Engine (object):

    #Constructor
    def __init__(self, type, hp, brand):

        self.__type = type #Diesel, Gas, Electric
        self.__hp = hp
        self.__brand = brand
        self.__is_on = False
        self.__rpm = 0 # RPM

    #@property permite convertir una funcion sin argumentos como si fuese una propiedad

    @property
    def engine_is_on(self):
        #Solo returna el valor
        return self.__is_on

    def turn_on(self):
        if not self.__is_on:
            self.__is_on = True

    def turn_off(self):
        if self.__is_on:
            self.__is_on = False


class Vehicle (object):
    def __init__(self, engine=None, color="grey",
                 make="Tata", transmission="Manual"):

        self.__engine = None
        self.__init_engine(engine)
        self.__color = None
        self.__make = None
        self.__transmission = None


    #Pero mejor tener un metodo privado para inicializar
    def __init_engine(engine):
        if engine:
            self.__engine = engine
        else:
            self.__engine = Engine("Gasolina", 50, "Hyundai")

'''
#Ejemplo inicial
small_engine = Engine("Diese", 80, "tata")
small_engine.turn_on()

result = small_engine.engine_is_on

print("Motor On: {}".format(result))
'''

