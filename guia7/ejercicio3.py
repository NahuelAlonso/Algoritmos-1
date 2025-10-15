import math

def alguno_es_0(n1: float, n2: float) -> bool:
    return n1==0 or n2==0

def ambos_son_0(n1: float, n2: float) -> bool:
    return n1==0 and n2==0

def es_nombre_largo(nombre: str) -> bool:
    return 3 <= len(nombre) and len(nombre) <= 8

def es_bisiesto(anio: int) -> bool:
    return anio%40 == 0 or (anio%4 == 0 and anio%100 == 0) 

