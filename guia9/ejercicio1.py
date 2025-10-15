from typing import List, Tuple
from queue import LifoQueue as Pila
import numpy as np
import random

def generar_nros_al_azar(cantidad:int, desde:int, hasta:int)-> Pila[int]:
    pila: Pila[int] = Pila()
    for i in range(cantidad):
        pila.put(random.randint(desde, hasta))
    return pila

def cantidad_de_elementos(p: Pila[int])->int:
    cant:int = 0
    pila_aux: Pila[int] = Pila()
    while(not p.empty()):
        cant+=1
        pila_aux.put(p.get())
    while not pila_aux.empty():
        p.put(pila_aux.get())
    return cant

def buscar_maximo(p: Pila[int])->int:
    max:int = 0
    pila_aux: Pila[int] = Pila()
    while(not p.empty()):
        aux=p.get()
        if(aux > max):
            max = aux
        pila_aux.put(aux)
    while not pila_aux.empty():
        p.put(pila_aux.get())
    return max

def buscar_nota_maxima(pila:Pila[Tuple[str, int]])->Tuple[str, int]:
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

def esta_bien_balanceada(expresion:str)->bool:
    


pila = generar_nros_al_azar(5,1,10)
print(pila.queue)
print(buscar_nota_maxima(pila))
print(pila.queue)