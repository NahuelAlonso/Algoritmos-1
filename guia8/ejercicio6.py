import numpy as np
from typing import Tuple, List

def es_matriz(matriz: List[List[int]])-> bool:
    if(len(matriz) == 0):
        return False
    dimension: int = len(matriz[0])
    for row in matriz:
        if(len(row) != dimension):
            return False
    return True

# def filas_ordenadas(matriz: List[List[int]], lista: List[bool])->None:
#     lista = []
#     for row in matriz:
#         lista.append(row == row.sort())#No se si funciona

def columna(matriz: List[List[int]], columna: int) -> List[int]:
    lista= []
    for row in matriz:
        lista.append(row[columna])
    return lista

def transponer(matriz: List[List[int]]) -> List[List[int]]:
    resultado:List[List[int]]=[]
    for idx in range(len(matriz[0])):
        resultado.append(columna(matriz, idx))
    return resultado

def quien_gana_tateti(tablero:List[List[str]])->int:
    if (gano_ver(tablero, 'O') or gano_hor(tablero, 'O') or gano_dia(tablero, 'O')):
        return 0
    if (gano_ver(tablero, 'X') or gano_hor(tablero, 'X') or gano_dia(tablero, 'X')):
        return 1
    return 2

def gano_ver(tablero:List[List[str]], c:str)->bool:
    return gano_hor(transponer(tablero), c)

def gano_hor(tablero:List[List[str]], c:str)->bool:
    for row in range(len(tablero)):
        if (tablero[row][0]==c and tablero[row][1]==c and tablero[row][2]==c):
            return True
    return False

def gano_dia(tablero:List[List[str]], str)->bool:
    return (
        (str==tablero[0][0] and str==tablero[1][1] and str==tablero[2][2])
        or
        (str==tablero[0][2] and str==tablero[1][1] and str==tablero[2][0])
    )


# print(transponer([[1,2,3,4,5],[6,7,8,9,10],[11,12,12,14,15]]))
print(quien_gana_tateti([
    ['O','','X'],
    ['X','O','X'],
    ['','X','']
    ]))

def exponenciacion_matriz(dimension:int, exponente:int)->List[List[int]]:
    matriz:List[List[int]]
    for row in range(dimension):
        matriz.append([])
        for col in range(dimension):
            matriz[row].append(np.random.random(()))
    print(matriz)