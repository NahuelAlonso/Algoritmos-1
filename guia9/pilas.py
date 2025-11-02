from typing import List, Tuple
from queue import LifoQueue as Pila
import numpy as np
import random

def generar_nros_al_azar(cantidad:int, desde:int, hasta:int)-> Pila:
    pila: Pila[int] = Pila()
    for i in range(cantidad):
        pila.put(random.randint(desde, hasta))
    return pila

def cantidad_de_elementos(p: Pila)->int:
    cant:int = 0
    pila_aux: Pila[int] = Pila()
    while(not p.empty()):
        cant+=1
        pila_aux.put(p.get())
    while not pila_aux.empty():
        p.put(pila_aux.get())
    return cant

def buscar_maximo(p: Pila)->int:
    pila_aux: Pila[int] = Pila()
    aux:int = p.get()
    max:int = aux
    pila_aux.put(aux)
    while(not p.empty()):
        aux=p.get()
        if(aux > max):
            max = aux
        pila_aux.put(aux)
    while not pila_aux.empty():
        p.put(pila_aux.get())
    return max

def buscar_nota_maxima(pila:Pila)->Tuple[str, int]:
    max: Tuple[str,int]=pila.get()
    pila_aux: Pila[Tuple[str,int]] = Pila()
    pila_aux.put(max)
    while not pila.empty():
        aux = pila.get()
        if(max[1] < aux[1]):
            max=aux
        pila_aux.put(aux)
    
    while not pila_aux.empty():
        pila.put(pila_aux.get())
    
    return max

def intercalar(pila1:Pila, pila2:Pila)->Pila:
    resultante = Pila()
    resultante_aux = Pila()
    pila1_aux = Pila()
    pila2_aux = Pila()

    while not pila1.empty():
        aux=pila1.get()
        resultante_aux.put(aux)
        pila1_aux.put(aux)
        aux=pila2.get()
        resultante_aux.put(aux)
        pila2_aux.put(aux)

    while not pila1_aux.empty():
        pila1.put(pila1_aux.get())

    while not pila2_aux.empty():
        pila2.put(pila2_aux.get())

    while not resultante_aux.empty():
        resultante.put(resultante_aux.get())

    return resultante


pila1 = generar_nros_al_azar(5,1,10)
pila2 = generar_nros_al_azar(5,1,10)

print(pila1.queue)
print(pila2.queue)
print(intercalar(pila1,pila2).queue)
print(pila1.queue)
print(pila2.queue)