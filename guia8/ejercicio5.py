from typing import List
def pertenece_a_cada_uno_version_3(matriz: List[List[int]], ele:int)->List[bool]:
    res = []
    for row in matriz:
        res.append(ele in row)
    return res

