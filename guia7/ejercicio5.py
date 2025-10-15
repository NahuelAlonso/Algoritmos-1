

def devolver_el_doble_si_es_par(num: float) -> float:
    if num % 2 == 0:
        return 2*num
    return num

def devolver_valor_si_es_par_sino_el_que_sigue(num:float) -> float:
    if num %2==0:
        return num
    return num+1
