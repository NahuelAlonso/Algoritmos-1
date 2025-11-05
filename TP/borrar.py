
from batallaNaval import *
from typing import List as list #Tuve que añadirlo para que me compile en mi computadora


grillaUnoLocal = [[AGUA, AGUA, AGUA, VACÍO],
                    [BARCO, VACÍO, VACÍO]]

grillaUnoOponente = [[AGUA, AGUA, AGUA, BARCO],
                        [VACÍO, VACÍO, VACÍO]]

grillaDosLocal = [[AGUA, AGUA, AGUA, BARCO],
                    [VACÍO, VACÍO, VACÍO, VACÍO]]

grillaDosOponente = [[AGUA, AGUA, AGUA, VACÍO],
                        [VACÍO, VACÍO, VACÍO, VACÍO]]

estado = ((2,4), [1], [UNO], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente))

print(tableroValidoEnJuego((grillaUnoLocal, grillaUnoOponente), estado))
#print(esEstadoDeJuegoVálido(estado))