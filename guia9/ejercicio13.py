from typing import List, Tuple
from queue import LifoQueue as Pila
from queue import Queue as Cola
from random import randint 

def armar_secuencia_de_bingo()->Cola[int]:
    c:Cola[int] = Cola()
    numeros:Cola[int] = Cola()
    for i in range(100):
        numeros.put(i)
    while not numeros.empty():
        c.put(obtener_elemento_random(numeros))
    return c

def obtener_elemento_random(cola:Cola[int])->int:
    tamano = tamano_de_cola(cola)
    indice = randint(0,tamano)
    return obtener_nesimo_elemento(indice, cola)

def tamano_de_cola(cola:Cola[int])->int:
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

print(armar_secuencia_de_bingo())