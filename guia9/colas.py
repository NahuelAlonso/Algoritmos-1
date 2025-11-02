from typing import List, Tuple
from queue import LifoQueue as Pila
from queue import Queue as Cola
from random import randint 

def armar_secuencia_de_bingo()->Cola:
    c:Cola[int] = Cola()
    numeros:Cola[int] = Cola()
    for i in range(100):
        numeros.put(i)
    while not numeros.empty():
        c.put(obtener_elemento_random(numeros))
    return c

def obtener_elemento_random(cola:Cola)->int:
    tamano = tamano_de_cola(cola)
    indice = randint(0,tamano)
    return obtener_nesimo_elemento(indice, cola)

def tamano_de_cola(cola:Cola)->int:
    tamanio = 0
    cola_aux = Cola()

    while not cola.empty():
        cola_aux.put(cola.get())
        tamanio += 1
    
    while not cola_aux.empty():
        cola.put(cola_aux.get())

    return tamanio

def obtener_nesimo_elemento(indice, cola):
    cola_aux = Cola()
    aux = cola.get()

    for i in range(indice-1):
        cola_aux.put(aux)
        aux = cola.get()
    
    while not cola_aux.empty():
        cola.put(cola_aux.get())

    return aux

def generar_numeros_al_azar(cantidad:int, desde:int, hasta:int)->Cola:
    cola:Cola[int]=Cola()
    for i in range(cantidad):
        cola.put(randint(desde, hasta))
    return cola

def cantidad_elementos(cola:Cola)->int:
    aux:Cola = Cola()
    cant:int=0
    while not cola.empty():
        cant+=1
        aux.put(cola.get())
    
    while not aux.empty():
        cola.put(aux.get())
    return cant

def buscar_el_maximo(cola:Cola)->int:
    cola_aux:Cola = Cola()
    aux:int = cola.get()
    mayor:int = aux
    cola_aux.put(aux)
    while not cola.empty():
        aux=cola.get()
        if(aux > mayor ):
            mayor = aux
        else:
            pass
        cola_aux.put(aux)
    
    while not cola_aux.empty():
        cola.put(cola_aux.get())
    return mayor

cola = generar_numeros_al_azar(5,-10,1)
print(cola.queue)
print(buscar_el_maximo(cola))
print(cola.queue)