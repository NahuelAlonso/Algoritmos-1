import math

def imprimir_saludo(nombre: str) -> None:
    print('Hola ' + nombre)

def raiz_cuadrada_de(num: float) -> float:
    return math.sqrt(num)

def fahrenheit_a_celsius(far: float) -> float:
    return (far-32)*5/9

def imprimir_dos_veces(est: str) -> None:
    print((est+'\n')*2)

def es_multiplo_de(n:float, m:float) -> bool:
    return n % m == 0

def es_par(num:int) -> bool:
    return es_multiplo_de(num, 2)

def cantidad_de_pizzas(personas: int, min_cant: int) -> int:
    return math.ceil((personas*min_cant)/8)


