import math

def imprimir_saludo(nombre)->None:
    print("Hola " + nombre)

def raiz_cuadrada_de(num)->float:
    return math.sqrt(num)

def fahrenheit_a_celcius(temp_far)->float:
    return (temp_far-32)*5/9

def imprimir_dos_veces(estribillo)->None:
    print((estribillo+"\n")*2)

def es_multiplo_de(n, m)->float:
    return n%m==0

def es_par(n)->float:
    return (n%2)==0

def cantidad_de_pizzas(comensales, min_cant_por)->float:
    return (math.ceil((comensales*min_cant_por)/8))