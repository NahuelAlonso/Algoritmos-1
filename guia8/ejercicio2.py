def CerosEnPosicionesPares(lista:list)->None:
    for i in range(len(lista)):
        if(i%2==0):
            lista[i]=0

def CerosEnPosicionesPares(lista:list)->list:
    nueva_lista:list = []
    for i in range(len(lista)):
        if(i%2==0):
            nueva_lista.append(0)
        else:
            nueva_lista.append(lista[i])
    return nueva_lista

def sin_vocales(original:str)->str:
    nuevo:str=""
    for c in original:
        if(not (c in "aeiou")):
            nuevo = nuevo + c
    return nuevo

def reemplaza_vocales(original:str)->str:
    nuevo:str=""
    for c in original:
        if(not (c in "aeiou")):
            nuevo += c
        else:
            nuevo += "_"
    return nuevo

def da_vuelta_str(original:str)->str:
    nuevo = ""
    for i in range(len(original)):
        nuevo += original[len(original)-1-i]
    return nuevo

def eliminar_repetidos(original:str)->str:
    nuevo = ""
    for idx, c in enumerate(original):
        if(not c in original[idx+1:]):#No se puede hacer con a[i:f]
            nuevo += c
    return nuevo
