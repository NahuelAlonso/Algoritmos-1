def resultadoMateria(notas:list)->int:
    todos_mayores_4:bool = mayores_a_4(notas)
    promedio:float = calcular_promedio(notas)
    if(not todos_mayores_4):
        return 3
    elif promedio >=7:
        return 1
    elif promedio >=4:
        return 2
    else:
        return 3
    
def mayores_a_4(notas:list)->bool:
    for nota in notas:
        if(nota < 4):
            return False
    return True

def calcular_promedio(notas:list)->float:
    suma = 0
    for nota in notas:
        suma +=nota
    return suma/len(notas)

