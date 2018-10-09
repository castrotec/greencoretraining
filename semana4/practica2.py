#Jorge Castro
#Practica 2

# Q = raiz cuadrada de (2*C*D/H) con C=50 y H=30

def eleva_pot(base, exponente):
    return base ** exponente

def getFormulaRaiz(C, D, H):
    return eleva_pot(base = (2*C*D/H), exponente=1/2)

print(getFormulaRaiz(50, 20, 30))