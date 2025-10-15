
def pertenece0(lista:list, elemento:int) -> bool:
    for e in lista:
        if elemento == e:
            return True
    return False

def pertenece1(lista:list, elemento:int) -> bool:
    return elemento in lista

def pertenece2(lista:list, elemento:int) -> bool:
    for i in range(len(lista)):
        if elemento == lista[i]:
            return True
    return False


def divide_a_todos(lista:list, elemento:int) -> bool:
    for i in lista:
        if i%elemento != 0:
            return False
    return True

def suma_total(lista:list)->int:
    suma:int = 0
    for i in lista:
        suma+=i
    return suma

def maximo(lista:list)->int:
    aux:int = lista[0]
    for i in lista:
        if(aux < i):
            aux = i
    return aux

def minimo(lista:list)->int:
    aux:int = lista[0]
    for i in lista:
        if(aux > i):
            aux = i
    return aux

def ordenados(lista:list)->bool:
    for i in range(len(lista)-2):
        if(lista[i] > lista[i+1]):
            return False
    return True

def pos_maximo(lista: list) -> int:
    if len(lista)==0:
        return -1
    pos = 0
    max = lista[0]
    for index, i in lista:
        if (max < i):
            pos = index
            max = i
    return pos

def long_mayor_a_siete(lista:list) -> bool:
    for i in lista:
        if(len(i) > 7):
            return True
    return False

def es_palindroma(lista:list) -> bool:
    long = len(lista)
    for i in range(long):
        if(lista[i] != lista[long-i-1]):
            return False
    return True

def iguales_consecutivos(lista:list) -> bool:
    num = lista[0]
    repeticiones = 0
    for i in lista:
        if repeticiones == 3:
            return True
        if num == i:
            repeticiones += 1
        else:
            repeticiones = 1
            num = i
    return False

def vocales_distintas(string: str) -> bool:
    vocales:list = ['a','e','i','o','u']
    conteo = 0
    for vocal in vocales:
        if vocal in string:
            conteo += 1
    return conteo >=3


def pos_secuencia_ordenada_mas_larga(lista:list) -> int:
    maxima_long = 1
    posicion = 0
    sublista_actual = 1
    posicion_actual = 0
    for i in range(len(lista)-2):
        if(lista[i] <= lista[i+1]):
            sublista_actual += 1
        else:
            posicion_actual = i+1
            sublista_actual = 1
        if (sublista_actual > maxima_long):
            maxima_long = sublista_actual
            posicion = posicion_actual
    return posicion

def cantidad_digitos_impares(lista:list) -> int:
    acc = 0
    for i in lista:
        for j in descomponer_en_digitos(i):
            if(j%2==1):
                acc += 1
    return acc
                
def descomponer_en_digitos(num: int) -> list:
    res = []
    while num != 0:
        res.append(num%10)
        num //= 10
    return res

print(cantidad_digitos_impares([12345, 15,33,7897,1]))