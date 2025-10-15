import math

def peso_pino(long: float) -> float:#long en metros
    if(long <= 3):
        return long*100*3
    else:
        return 3*100*3+(long-3)*100*2

def es_peso_util(peso: float) -> bool:
    return peso>400 and peso<1000

def sirve_pino(altura: float) -> bool:
    return es_peso_util(peso_pino(altura))
