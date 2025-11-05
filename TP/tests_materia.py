import unittest
from batallaNaval import *
from typing import List as list #Tuve que añadirlo para que me compile en mi computadora

# Tests
# Tests Ejercicio 1
class cantidadDeBarcosDeTamaño_Test(unittest.TestCase):
    def test_longitud_2_hay_uno_en_el_medio(self): # Un ejemplo de test 
        barcos = [[('H',3), ('H',4), ('H',5)],
                  [('F',4), ('E',4)],
                  [('B',4), ('B',3), ('B',2)]]       
        self.assertEqual(cantidadDeBarcosDeTamaño(barcos,2),1)
        self.assertEqual(barcos, [[('H',3), ('H',4), ('H',5)],
                                  [('F',4), ('E',4)],
                                  [('B',4), ('B',3), ('B',2)]] )

    def test_no_hay_barcos(self):
        barcos:list[BarcoEnGrilla] = []
        self.assertEqual(cantidadDeBarcosDeTamaño(barcos,2),0)
        self.assertEqual(barcos, [])

    def test_un_solo_barco(self):
        barcos = [[('H',3), ('H',4), ('H',5)]]
        self.assertEqual(cantidadDeBarcosDeTamaño(barcos,3),1)
        self.assertEqual(barcos, [[('H',3), ('H',4), ('H',5)]])

    def test_barcos_de_1(self):
        barcos = [[('A',1)], [('C',4)], [('D',5)], [('B',2)]]
        self.assertEqual(cantidadDeBarcosDeTamaño(barcos,1),4)
        self.assertEqual(cantidadDeBarcosDeTamaño(barcos,2),0)
        self.assertEqual(barcos, [[('A',1)], [('C',4)], [('D',5)], [('B',2)]])
        
# Tests Ejercicio 2
class nuevoJuego_Test(unittest.TestCase):
    def test_2x2_y_un_barco_longitud_2(self):
        grillaUNO_local = [[VACÍO, VACÍO],
                           [VACÍO, VACÍO]]
        
        grillaUNO_oponente = [[VACÍO, VACÍO],
                              [VACÍO, VACÍO]]
        
        grillaDOS_local = [[VACÍO, VACÍO],
                           [VACÍO, VACÍO]]
        
        grillaDOS_oponente = [[VACÍO, VACÍO],
                              [VACÍO, VACÍO]]
        
        juego = nuevoJuego(2,2,[2])
        
        self.assertEqual(juego[0], (2,2))
        self.assertTrue(juego[1], [2])
        self.assertEqual(juego[2], [UNO])
        self.assertEqual(juego[3], (grillaUNO_local, grillaUNO_oponente))
        self.assertEqual(juego[4], (grillaDOS_local, grillaDOS_oponente))

    def test_4x3_y_tres_barcos(self):
        grillaUNO_local = [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                           [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                           [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]]
        
        grillaUNO_oponente = [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                           [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                           [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]]
        
        grillaDOS_local = [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                           [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                           [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]]
        
        grillaDOS_oponente = [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                           [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                           [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]]
        
        juego = nuevoJuego(3,5,[2,3,4])
        
        self.assertEqual(juego[0], (3,5))
        self.assertTrue(juego[1], [2,3,4])
        self.assertEqual(juego[2], [UNO])
        self.assertEqual(juego[3], (grillaUNO_local, grillaUNO_oponente))
        self.assertEqual(juego[4], (grillaDOS_local, grillaDOS_oponente))

    def test_1x1_y_un_barco_longitud_1(self):
        grillaUNO_local = [[VACÍO]]
        
        grillaUNO_oponente = [[VACÍO]]
        
        grillaDOS_local = [[VACÍO]]
        
        grillaDOS_oponente = [[VACÍO]]
        
        juego = nuevoJuego(1,1,[1])
        
        self.assertEqual(juego[0], (1,1))
        self.assertTrue(juego[1], [1])
        self.assertEqual(juego[2], [UNO])
        self.assertEqual(juego[3], (grillaUNO_local, grillaUNO_oponente))
        self.assertEqual(juego[4], (grillaDOS_local, grillaDOS_oponente))

# Tests Ejercicio 3
class esEstadoDeJuegoVálido_Test(unittest.TestCase):
    def test_grilla_DOS_local_no_coincide_con_disponibles(self): # la grillaDOSlocal tiene un solo barco de tamaño 3, en lugar de dos de tamaño 2.
        grillaUnoLocal = [[VACÍO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, BARCO, VACÍO],
                          [VACÍO, VACÍO, BARCO, VACÍO]]
        
        grillaUnoOponente = [[VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        grillaDosLocal = [[VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, BARCO, BARCO, BARCO],
                          [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        grillaDosOponente = [[VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        estado = ((4,4), [2,2], [DOS], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente))
        
        self.assertFalse(esEstadoDeJuegoVálido(estado))        
        self.assertEqual(estado, ((4,4), [2,2], [DOS], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente)))

    def test_grilla_4x4_dos_barcos_longitud_dos(self):#Está todo en orden
        grillaUnoLocal = [[AGUA, AGUA, AGUA, VACÍO],
                          [BARCO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, BARCO, VACÍO],
                          [VACÍO, VACÍO, BARCO, VACÍO]]
        
        grillaUnoOponente = [[AGUA, AGUA, AGUA, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        grillaDosLocal = [[AGUA, AGUA, AGUA, BARCO],
                          [VACÍO, VACÍO, VACÍO, BARCO],
                          [VACÍO, BARCO, BARCO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        grillaDosOponente = [[AGUA, AGUA, AGUA, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        estado = ((4,4), [2,2], [DOS], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente))
        
        self.assertTrue(esEstadoDeJuegoVálido(estado))        
        self.assertEqual(estado, ((4,4), [2,2], [DOS], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente)))

    def test_grilla_DOS_oponente_tiene_un_turno_de_mas(self): #la grillaDOSoponente tiene 5 turnos usados, mientras que las grillaUNO oponente tiene 3
        grillaUnoLocal = [[AGUA, AGUA, AGUA, VACÍO],
                          [BARCO, VACÍO, VACÍO, VACÍO]]

        
        grillaUnoOponente = [[AGUA, AGUA, AGUA, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        grillaDosLocal = [[AGUA, AGUA, AGUA, BARCO],
                          [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        grillaDosOponente = [[AGUA, AGUA, AGUA, AGUA],
                             [AGUA, VACÍO, VACÍO, VACÍO]]
        
        estado = ((2,4), [1], [DOS], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente))
        
        self.assertFalse(esEstadoDeJuegoVálido(estado))        
        self.assertEqual(estado, ((2,4), [1], [DOS], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente)))

    def test_grilla_tiene_27_filas(self): #las grillas tienen 27 filas
        grillaUnoLocal = [[VACÍO], [BARCO], [VACÍO], [VACÍO], [VACÍO], [VACÍO], [VACÍO], [VACÍO], [VACÍO], [VACÍO], [VACÍO], [VACÍO], [VACÍO], [VACÍO], [VACÍO], [VACÍO], [VACÍO], [VACÍO], [VACÍO], [VACÍO], [VACÍO], [VACÍO], [VACÍO], [VACÍO], [VACÍO], [VACÍO]]

        
        grillaUnoOponente = [[VACÍO], [VACÍO], [VACÍO], [VACÍO], [VACÍO], [VACÍO], [VACÍO], [VACÍO], [VACÍO], [VACÍO], [VACÍO], [VACÍO], [VACÍO], [VACÍO], [VACÍO], [VACÍO], [VACÍO], [VACÍO], [VACÍO], [VACÍO], [VACÍO], [VACÍO], [VACÍO], [VACÍO], [VACÍO], [VACÍO]]
        
        grillaDosLocal = [[BARCO], [VACÍO], [VACÍO], [VACÍO], [VACÍO], [VACÍO], [VACÍO], [VACÍO], [VACÍO], [VACÍO], [VACÍO], [VACÍO], [VACÍO], [VACÍO], [VACÍO], [VACÍO], [VACÍO], [VACÍO], [VACÍO], [VACÍO], [VACÍO], [VACÍO], [VACÍO], [VACÍO], [VACÍO], [VACÍO]]
        
        grillaDosOponente = [[VACÍO], [VACÍO], [VACÍO], [VACÍO], [VACÍO], [VACÍO], [VACÍO], [VACÍO], [VACÍO], [VACÍO], [VACÍO], [VACÍO], [VACÍO], [VACÍO], [VACÍO], [VACÍO], [VACÍO], [VACÍO], [VACÍO], [VACÍO], [VACÍO], [VACÍO], [VACÍO], [VACÍO], [VACÍO], [VACÍO]]
        
        estado = ((27,1), [1], [UNO], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente))
        
        self.assertFalse(esEstadoDeJuegoVálido(estado))        
        self.assertEqual(estado, ((27,1), [1], [UNO], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente)))

    def test_grilla_2x4_un_barco_longitud_uno(self): #Está todo en orden
        grillaUnoLocal = [[AGUA, AGUA, AGUA, VACÍO],
                          [BARCO, VACÍO, VACÍO, VACÍO]]

        grillaUnoOponente = [[AGUA, AGUA, AGUA, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        grillaDosLocal = [[AGUA, AGUA, AGUA, BARCO],
                          [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        grillaDosOponente = [[AGUA, AGUA, AGUA, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        estado = ((2,4), [1], [UNO], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente))
        
        self.assertTrue(esEstadoDeJuegoVálido(estado))        
        self.assertEqual(estado, ((2,4), [1], [UNO], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente)))

    def test_grilla_2x4_dimensiones_3x4(self): #La grilla es de 2x4 pero las dimensiones del estado de juego indican 3x4
        grillaUnoLocal = [[AGUA, AGUA, AGUA, VACÍO],
                          [BARCO, VACÍO, VACÍO, VACÍO]]

        grillaUnoOponente = [[AGUA, AGUA, AGUA, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        grillaDosLocal = [[AGUA, AGUA, AGUA, BARCO],
                          [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        grillaDosOponente = [[AGUA, AGUA, AGUA, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        estado = ((3,4), [1], [UNO], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente))
        
        self.assertFalse(esEstadoDeJuegoVálido(estado))        
        self.assertEqual(estado, ((3,4), [1], [UNO], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente)))

    def test_estado_de_juego_varios_elementos_en_turno(self): #La lista de jugador que determina el turno debe tener un solo elemento, pero tiene 3
        grillaUnoLocal = [[AGUA, AGUA, AGUA, VACÍO],
                          [BARCO, VACÍO, VACÍO, VACÍO]]

        grillaUnoOponente = [[AGUA, AGUA, AGUA, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        grillaDosLocal = [[AGUA, AGUA, AGUA, BARCO],
                          [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        grillaDosOponente = [[AGUA, AGUA, AGUA, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        estado = ((2,4), [1], [UNO, UNO, UNO], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente))
        
        self.assertFalse(esEstadoDeJuegoVálido(estado))        
        self.assertEqual(estado, ((2,4), [1], [UNO, UNO, UNO], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente)))

    def test_no_coinciden_posiciones_atacadas(self): #La grillaUNOlocal muestra que se atacó A1, A2 y A3, pero en la grillaDOSoponente se ve B1, B2 y B3
        grillaUnoLocal = [[AGUA, AGUA, AGUA, VACÍO],
                          [BARCO, VACÍO, VACÍO, VACÍO]]

        grillaUnoOponente = [[AGUA, AGUA, AGUA, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        grillaDosLocal = [[AGUA, AGUA, AGUA, BARCO],
                          [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        grillaDosOponente = [[VACÍO, VACÍO, VACÍO, VACÍO],
                             [AGUA, AGUA, AGUA, VACÍO]]
        
        estado = ((2,4), [1], [UNO], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente))
        
        self.assertFalse(esEstadoDeJuegoVálido(estado))        
        self.assertEqual(estado, ((2,4), [1], [UNO], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente)))
    
    def test_grilla_2x4_barcos_tocados(self): #Está todo en orden
        grillaUnoLocal = [[AGUA, AGUA, AGUA, VACÍO],
                          [BARCO, VACÍO, VACÍO, VACÍO]]

        grillaUnoOponente = [[AGUA, AGUA, AGUA, BARCO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        grillaDosLocal = [[AGUA, AGUA, AGUA, BARCO],
                          [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        grillaDosOponente = [[AGUA, AGUA, AGUA, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        estado = ((2,4), [1], [UNO], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente))
        
        self.assertTrue(esEstadoDeJuegoVálido(estado))        
        self.assertEqual(estado, ((2,4), [1], [UNO], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente)))

    def test_grilla_2x4_una_matriz_diferente_dimensión(self): #grillaUNOlocal es de 2x3 mientras que el resto es de 2x4
        grillaUnoLocal = [[AGUA, AGUA, AGUA],
                          [BARCO, VACÍO, VACÍO]]

        grillaUnoOponente = [[AGUA, AGUA, AGUA, BARCO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        grillaDosLocal = [[AGUA, AGUA, AGUA, BARCO],
                          [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        grillaDosOponente = [[AGUA, AGUA, AGUA, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        estado = ((2,4), [1], [UNO], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente))
        
        self.assertFalse(esEstadoDeJuegoVálido(estado))        
        self.assertEqual(estado, ((2,4), [1], [UNO], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente)))

    def test_grillaUnoLocal_no_es_matriz_válida(self): #La grillaUNOlocal no es una matriz
        grillaUnoLocal = [[AGUA, AGUA, AGUA, VACÍO],
                          [BARCO, VACÍO, VACÍO]]

        grillaUnoOponente = [[AGUA, AGUA, AGUA, BARCO],
                             [VACÍO, VACÍO, VACÍO]]
        
        grillaDosLocal = [[AGUA, AGUA, AGUA, BARCO],
                          [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        grillaDosOponente = [[AGUA, AGUA, AGUA, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        estado = ((2,4), [1], [UNO], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente))
        
        self.assertFalse(esEstadoDeJuegoVálido(estado))        
        self.assertEqual(estado, ((2,4), [1], [UNO], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente)))
    
    def test_barco_tamaño_negativo(self): #En la lista de barcos sólo pueden aparecer números naturales, pero tiene un -1
        grillaUnoLocal = [[AGUA, AGUA, AGUA, VACÍO],
                          [BARCO, VACÍO, VACÍO, VACÍO]]

        grillaUnoOponente = [[AGUA, AGUA, AGUA, BARCO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        grillaDosLocal = [[AGUA, AGUA, AGUA, BARCO],
                          [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        grillaDosOponente = [[AGUA, AGUA, AGUA, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        estado = ((2,4), [1, -1], [UNO], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente))
        
        self.assertFalse(esEstadoDeJuegoVálido(estado))        
        self.assertEqual(estado, ((2,4), [1, -1], [UNO], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente)))

# Tests Ejercicio 4
class DispararEnPosición_Test(unittest.TestCase):
    def test_disparo_en_posicion_vacia_UNO(self):
        estado = ((5,5), [3, 2], [UNO],
            ([[BARCO, VACÍO, VACÍO, VACÍO, VACÍO],
              [BARCO, VACÍO, VACÍO, VACÍO, VACÍO],
             [BARCO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, BARCO, BARCO]],

            [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]]),

            ([[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
              [BARCO, BARCO, BARCO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], 
            [VACÍO, VACÍO, VACÍO, BARCO, BARCO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]],

            [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]])
        )
        
        estado_esperado = ((5,5), [3, 2], [DOS],
            ([[BARCO, VACÍO, VACÍO, VACÍO, VACÍO],
              [BARCO, VACÍO, VACÍO, VACÍO, VACÍO],
             [BARCO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, BARCO, BARCO]],
            [[AGUA, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]]),
            ([[AGUA, VACÍO, VACÍO, VACÍO, VACÍO],
              [BARCO, BARCO, BARCO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, BARCO, BARCO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]],
            [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]])
        )
        resultado = dispararEnPosición(estado, ("A", 1))
        self.assertEqual(resultado, NADA)
        self.assertEqual(estado, estado_esperado)

    def test_disparo_en_posicion_barco_DOS(self):
        estado = ((5,5), [3, 2], [DOS],
            ([[BARCO, VACÍO, VACÍO, VACÍO, VACÍO],
              [BARCO, VACÍO, VACÍO, VACÍO, VACÍO],
             [BARCO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, BARCO, BARCO]],

            [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]]),

            ([[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
              [BARCO, BARCO, BARCO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, BARCO, BARCO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]],

            [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]])
        )
        
        estado_esperado = ((5,5), [3, 2], [UNO],
            ([[BARCO, VACÍO, VACÍO, VACÍO, VACÍO],
             [BARCO, VACÍO, VACÍO, VACÍO, VACÍO],
             [BARCO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, BARCO, BARCO]],

            [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]]),

            ([[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [BARCO, BARCO, BARCO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, BARCO, BARCO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]],

            [[BARCO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]])
        )
        resultado = dispararEnPosición(estado, ("A", 1))
        self.assertEqual(resultado, TOCADO)
        self.assertEqual(estado, estado_esperado)

    def test_disparo_en_posicion_barco_UNO_2x2(self):
        estado = ((2,2), [1], [UNO],
            ([[VACÍO, VACÍO],
              [BARCO, VACÍO]],

            [[VACÍO, VACÍO],
             [VACÍO, VACÍO]]),

            ([[VACÍO, VACÍO],
              [VACÍO, BARCO]],

            [[VACÍO, VACÍO],
             [VACÍO, VACÍO]]))
        
        estado_esperado = ((2,2), [1], [DOS],
            ([[VACÍO, VACÍO],
              [BARCO, VACÍO]],

            [[VACÍO, VACÍO],
             [VACÍO, BARCO]]),

            ([[VACÍO, VACÍO],
              [VACÍO, BARCO]],

            [[VACÍO, VACÍO],
             [VACÍO, VACÍO]]))
        resultado = dispararEnPosición(estado, ("B", 2))
        self.assertEqual(resultado, TOCADO)
        self.assertEqual(estado, estado_esperado)

# Tests Ejercicio 5
class barcosEnGrilla_Test(unittest.TestCase):
    def test_varios_barcos_distintos_tamaños(self): # Varios barcos de distintos tamaños en una grilla con varios barcos de distintos tamaños
        grilla: Grilla = [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, VACÍO, BARCO, BARCO, BARCO, VACÍO],
                          [BARCO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, BARCO, BARCO, VACÍO, BARCO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, BARCO, VACÍO]]
        
        barcosEsperados: list[BarcoEnGrilla] = [[('B', 1), ('C', 1), ('D', 1)], [('B', 4), ('B', 5), ('B', 6)], [('D', 3), ('D', 4)], [('D', 6), ('E', 6)]]
        
        self.assertTrue(barcosEnGrilla(grilla), barcosEsperados)
        self.assertEqual(grilla, [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                                  [BARCO, VACÍO, VACÍO, BARCO, BARCO, BARCO, VACÍO],
                                  [BARCO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                                  [BARCO, VACÍO, BARCO, BARCO, VACÍO, BARCO, VACÍO],
                                  [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, BARCO, VACÍO]])

    def test_4_barcos_en_columnas_impares(self): # Varios barcos de distintos tamaños en una grilla con varios barcos de distintos tamaños
        grilla: Grilla = [[BARCO, VACÍO, BARCO, VACÍO, BARCO, VACÍO, BARCO],
                          [BARCO, VACÍO, BARCO, VACÍO, BARCO, VACÍO, BARCO],
                          [BARCO, VACÍO, BARCO, VACÍO, BARCO, VACÍO, BARCO],
                          [BARCO, VACÍO, BARCO, VACÍO, BARCO, VACÍO, BARCO],
                          [BARCO, VACÍO, BARCO, VACÍO, BARCO, VACÍO, BARCO]]
        
        barcosEsperados: list[BarcoEnGrilla] = [
            [('A',1), ('B',1), ('C',1), ('D',1), ('E',1)],
            [('A',3), ('B',3), ('C',3), ('D',3), ('E',3)],
            [('A',5), ('B',5), ('C',5), ('D',5), ('E',5)],
            [('A',7), ('B',7), ('C',7), ('D',7), ('E',7)]]
        
        self.assertTrue(barcosEnGrilla(grilla), barcosEsperados)
        self.assertEqual(grilla, [[BARCO, VACÍO, BARCO, VACÍO, BARCO, VACÍO, BARCO],
                                [BARCO, VACÍO, BARCO, VACÍO, BARCO, VACÍO, BARCO],
                                [BARCO, VACÍO, BARCO, VACÍO, BARCO, VACÍO, BARCO],
                                [BARCO, VACÍO, BARCO, VACÍO, BARCO, VACÍO, BARCO],
                                [BARCO, VACÍO, BARCO, VACÍO, BARCO, VACÍO, BARCO]])

    def test_4_barcos_en_columnas_impares_con_diferente_orden(self): #Mismo que anterior, desordenado
        grilla: Grilla = [[BARCO, VACÍO, BARCO, VACÍO, BARCO, VACÍO, BARCO],
                          [BARCO, VACÍO, BARCO, VACÍO, BARCO, VACÍO, BARCO],
                          [BARCO, VACÍO, BARCO, VACÍO, BARCO, VACÍO, BARCO],
                          [BARCO, VACÍO, BARCO, VACÍO, BARCO, VACÍO, BARCO],
                          [BARCO, VACÍO, BARCO, VACÍO, BARCO, VACÍO, BARCO]]
        
        barcosEsperados: list[BarcoEnGrilla] = [
            [('B',1), ('C',1), ('D',1), ('A',1), ('E',1)],
            [('D',5), ('B',5), ('A',5), ('C',5), ('E',5)],
            [('A',3), ('B',3), ('C',3), ('D',3), ('E',3)],
            [('A',7), ('B',7), ('C',7), ('D',7), ('E',7)]]
        
        self.assertTrue(barcosEnGrilla(grilla), barcosEsperados)
        self.assertEqual(grilla, [[BARCO, VACÍO, BARCO, VACÍO, BARCO, VACÍO, BARCO],
                                [BARCO, VACÍO, BARCO, VACÍO, BARCO, VACÍO, BARCO],
                                [BARCO, VACÍO, BARCO, VACÍO, BARCO, VACÍO, BARCO],
                                [BARCO, VACÍO, BARCO, VACÍO, BARCO, VACÍO, BARCO],
                                [BARCO, VACÍO, BARCO, VACÍO, BARCO, VACÍO, BARCO]])

    def test_10_barcos_de_longitud_uno(self): # Diez barcos de longitud 1
        grilla: Grilla = [[BARCO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, BARCO],
                          [VACÍO, VACÍO, BARCO, VACÍO, BARCO, VACÍO, VACÍO],
                          [BARCO, VACÍO, VACÍO, VACÍO, VACÍO, BARCO, VACÍO],
                          [VACÍO, BARCO, VACÍO, BARCO, VACÍO, VACÍO, BARCO],
                          [VACÍO, VACÍO, BARCO, VACÍO, VACÍO, VACÍO, VACÍO]]
        
        barcosEsperados: list[BarcoEnGrilla] = [[('A',1)],[('A',7)],[('B',3)],[('B',5)],
                                                [('C',1)],[('C',6)],[('D',2)],[('D',4)],[('D',7)],[('D',3)]]
        
        self.assertTrue(barcosEnGrilla(grilla), barcosEsperados)
        self.assertEqual(grilla, [[BARCO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, BARCO],
                          [VACÍO, VACÍO, BARCO, VACÍO, BARCO, VACÍO, VACÍO],
                          [BARCO, VACÍO, VACÍO, VACÍO, VACÍO, BARCO, VACÍO],
                          [VACÍO, BARCO, VACÍO, BARCO, VACÍO, VACÍO, BARCO],
                          [VACÍO, VACÍO, BARCO, VACÍO, VACÍO, VACÍO, VACÍO]])
        
    def test_10_barcos_de_longitud_uno_falta_un_barco(self): # Diez barcos de longitud 1, idéntico al anterior, sin un barco en el res
        grilla: Grilla = [[BARCO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, BARCO],
                          [VACÍO, VACÍO, BARCO, VACÍO, BARCO, VACÍO, VACÍO],
                          [BARCO, VACÍO, VACÍO, VACÍO, VACÍO, BARCO, VACÍO],
                          [VACÍO, BARCO, VACÍO, BARCO, VACÍO, VACÍO, BARCO],
                          [VACÍO, VACÍO, BARCO, VACÍO, VACÍO, VACÍO, VACÍO]]
        
        barcosEsperados: list[BarcoEnGrilla] = [[('A',1)],[('A',7)],[('B',3)],[('B',5)],
                                                [('C',1)],[('C',6)],[('D',2)],[('D',4)],[('D',7)]]
        
        self.assertFalse(barcosEnGrilla(grilla), barcosEsperados)
        self.assertEqual(grilla, [[BARCO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, BARCO],
                          [VACÍO, VACÍO, BARCO, VACÍO, BARCO, VACÍO, VACÍO],
                          [BARCO, VACÍO, VACÍO, VACÍO, VACÍO, BARCO, VACÍO],
                          [VACÍO, BARCO, VACÍO, BARCO, VACÍO, VACÍO, BARCO],
                          [VACÍO, VACÍO, BARCO, VACÍO, VACÍO, VACÍO, VACÍO]])


if __name__ == '__main__':
    unittest.main(verbosity=1)
