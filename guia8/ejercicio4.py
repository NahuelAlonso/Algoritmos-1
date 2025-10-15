from typing import List, Tuple
def saldoActual(movimientos:List[Tuple[str,int]])->int:
    saldo = 0
    for mov in movimientos:
        if(mov[0]=='I'):
            saldo += mov[1]
        else:
            saldo -= mov[1]
    return saldo

print(saldoActual([("I",2000), ("R", 20),("R", 1000),("I", 300)]))
