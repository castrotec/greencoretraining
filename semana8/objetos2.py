
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
    def __init_engine(self, engine):
        if engine:
            self.__engine = engine
        else:
            self.__engine = Engine("Gasolina", 50, "Hyundai")

    def vehicle_is_on(self):
        return self.__engine.engine_is_on

    def turn_on(self):
        self.__engine.turn_on()


car = Vehicle(engine=None, color="Red", make="Audi")
car.turn_on()
print(car.vehicle_is_on())
