from typing import Any
from biblioteca import *
from queue import Queue as Cola
from typing import List as list

## Ejercicio 1

def cantidadDeBarcosDeTamaño(barcos: list[BarcoEnGrilla], tamaño: int) -> int:
    """ Indica la cantidad de barcos en *barcos* de tamaño *tamaño*
        PRE: sonBarcosVálidos(barcos)
    """
    res: int = 0
    for barco in barcos:
        if tamañoBarco(barco) == tamaño:
            res = res + 1
        else:
            pass

    return res

## Ejercicio 2

def nuevoJuego(
        cantidadDeFilas: int,
        cantidadDeColumnas: int,
        barcosDisponibles: list[Barco]
    ) -> EstadoJuego:
    """ Genera un estado de juego con dimensiones *cantidadDeFilas* de alto y *cantidadDeColumnas* de ancho,
        barcos disponibles *barcosDisponibles* y dos tableros vacíos de la dimensión correspondiente.
        PRE: cantidadDeFilasVálida
        PRE: cantidadDeColumnasVálida
        PRE: cantidadDeBarcosVálida
    """
    return (
        (cantidadDeFilas, cantidadDeColumnas),
        barcosDisponibles,
        [UNO],
        nuevoTablero(cantidadDeFilas, cantidadDeColumnas),
        nuevoTablero(cantidadDeFilas, cantidadDeColumnas)
    )

def nuevoTablero(cantidadDeFilas: int, cantidadDeColumnas: int) -> Tablero:
    res:Grilla = grillaVacia(cantidadDeFilas, cantidadDeColumnas)
    return (res, res)

def grillaVacia(cantidadDeFilas: int, cantidadDeColumnas: int) -> Grilla:
    res:Grilla = []
    for _ in range(cantidadDeFilas):
        listaAuxiliar:list[Celda] = []
        for _ in range(cantidadDeColumnas):
            listaAuxiliar.append(VACÍO)
        res.append(listaAuxiliar)
    return res

## Ejercicio 3

def esEstadoDeJuegoVálido(estadoDeJuego: EstadoJuego) -> bool:
    """ Indica si el estado de juego *estadoDeJuego* es válido.
        Para ser un estado de juego válido debe tener cantidad de filas, columnas y barcos válidas,
            debe ser el turno de un jugador, deben coincidir las posiciones atacadas y ambos tableros deben cumplir
            tableroValidoEnJuego(tablero)
    """
    
    cantidadDeFilas:int = cantidadDeFilasEstadoJuego(estadoDeJuego)
    cantidadDeColumnas:int = cantidadDeColumnasEstadoJuego(estadoDeJuego)
    barcosDisponiblesSegunEstado:list[Barco] = barcosDisponibles(estadoDeJuego)
    listaJugadorActual:list[Jugador] = estadoDeJuego[2]
    tableroUNO:Tablero = tableroDeJugador(estadoDeJuego, UNO)
    tableroDOS:Tablero = tableroDeJugador(estadoDeJuego, DOS)
    tableroValidoUNO:bool = tableroValidoEnJuego(tableroUNO, estadoDeJuego)
    tableroValidoDOS:bool = tableroValidoEnJuego(tableroDOS, estadoDeJuego)
    verificaCoincidenPosicionesAtacadas:bool = False

    
    if tableroValidoDOS and tableroValidoUNO:
        #Si no son todas las grillas matrices, o tienen diferentes dimensiones,
        #   coincidenPosicionesAtacadas tiraría error
        verificaCoincidenPosicionesAtacadas = coincidenPosicionesAtacadas(tableroUNO, tableroDOS)
    else:
        pass
    
    return (
        cantidadDeFilas >= 1 and
        cantidadDeFilas <= 26 and
        cantidadDeColumnas > 0 and
        len(listaJugadorActual) == 1 and
        len(barcosDisponiblesSegunEstado) > 0 and
        tableroValidoUNO and
        tableroValidoDOS and
        verificaCoincidenPosicionesAtacadas
    )
    
def tableroValidoEnJuego (tablero:Tablero, estadoDeJuego:EstadoJuego) -> bool:
    '''Indica si *tablero* es un tablero válido.
        Para esto, debe cumplir que ambas grillas sean matrices, cumplan grillaVálidaEnJuego y que las posiciones atacadas coincidan
    '''
    dimensionesGrillas:Dimensiones = dimensionesEstadoJuego(estadoDeJuego)
    return (
        dimensionesGrillas == dimensionesGrilla(grillaLocal(tablero)) and
        dimensionesGrillas == dimensionesGrilla(grillaOponente(tablero)) and
        esMatrizVálida(grillaLocal(tablero)) and
        esMatrizVálida(grillaOponente(tablero)) and
        grillaVálidaEnJuego(grillaLocal(tablero), estadoDeJuego) and
        grillaVálidaEnJuego(grillaOponente(tablero), estadoDeJuego) and
        coincidenBarcosEnGrilla(barcosDisponibles(estadoDeJuego), grillaLocal(tablero))
    )
    
def coincidenBarcosEnGrilla(barcos:list[Barco], grilla:Grilla) -> bool:
    return mismosElementos(barcos, tamaños(barcosEnGrilla(grilla)))

def tamaños(barcos: list[BarcoEnGrilla]) -> list[int]:#TODO:Probar si consigna se interpretó bien
    listaConTamaños: list[int] = []
    for barco in barcos:
        listaConTamaños.append(tamañoBarco(barco))
    return listaConTamaños

def mismosElementos(lista1: list[Any], lista2: list[Any]) -> bool:#TODO: Probar
    lista2ContieneLista1: bool = True
    lista1ContieneLista2: bool = True
    for elementoEnLista1 in lista1:
        if elementoEnLista1 not in lista2:
            lista2ContieneLista1 = False
        else:
            pass
    for elementoEnLista2 in lista2:
        if elementoEnLista2 not in lista1:
            lista1ContieneLista2 = False
        else:
            pass
    return lista2ContieneLista1 and lista1ContieneLista2
    
def coincidenPosicionesAtacadas(tablero:Tablero, tableroOponente:Tablero) -> bool:
    tableroUnoGrillaLocal:Grilla = grillaLocal(tablero)
    tableroUnoGrillaOponente:Grilla = grillaOponente(tablero)
    tableroDosGrillaLocal:Grilla = grillaLocal(tableroOponente)
    tableroDosGrillaOponente:Grilla = grillaOponente(tableroOponente)
    discrepanciaTableroUnoGrillaOponente:bool = False#Si no está vacía la celda p del tableroUnoGrillaOponente, la celda p del tableroDosGrillaLocal debe tener igual valor
    discrepanciaTableroDosGrillaOponente:bool = False#Si no está vacía la celda p del tableroDosGrillaOponente, la celda p del tableroUnoGrillaLocal debe tener igual valor
    cantidadDeNoVaciosUno:int = 0
    cantidadDeNoVaciosDos:int = 0
    dimensionesGrillas:Dimensiones = dimensionesGrilla(tableroUnoGrillaOponente)#Las cuatro grillas tienen las mismas dimensiones
    alto = altoDimensiones(dimensionesGrillas)
    ancho = anchoDimensiones(dimensionesGrillas)


    for fila in range(alto):
        for columna in range(ancho):
            #posición:Posición = ()TODO: Preguntar, debo usar posición o está bien de esta forma?
            celdaTableroUnoGrillaOponente:Celda = tableroUnoGrillaOponente[fila][columna]
            celdaTableroDosGrillaLocal:Celda = tableroDosGrillaLocal[fila][columna]
            if celdaTableroUnoGrillaOponente != VACÍO and celdaTableroUnoGrillaOponente != celdaTableroDosGrillaLocal:
                discrepanciaTableroUnoGrillaOponente = True
            else:
                pass

            if celdaTableroUnoGrillaOponente != VACÍO:#Lo podría poner en el else del if anterior, pero de esta forma es más claro y prolijo
                cantidadDeNoVaciosUno += 1
            else:
                pass

            celdaTableroDosGrillaOponente:Celda = tableroDosGrillaOponente[fila][columna]
            celdaTableroUnoGrillaLocal:Celda = tableroUnoGrillaLocal[fila][columna]
            if celdaTableroDosGrillaOponente != VACÍO and celdaTableroDosGrillaOponente != celdaTableroUnoGrillaLocal:
                discrepanciaTableroDosGrillaOponente = True
            else:
                pass
            
            if celdaTableroDosGrillaOponente != VACÍO:
                cantidadDeNoVaciosDos += 1
            else:
                pass

    return(
        not discrepanciaTableroUnoGrillaOponente and
        not discrepanciaTableroDosGrillaOponente and
        0 <= cantidadDeNoVaciosUno - cantidadDeNoVaciosDos and
        cantidadDeNoVaciosUno - cantidadDeNoVaciosDos <= 1
    )

    
## Ejercicio 4

def dispararEnPosición(estado_juego: EstadoJuego, posición: Posición) -> ResultadoDisparo:
    """ 
    Genera el estado del juego *estado_juego* luego de haber efectuado un disparo a la posición *posición*
        PRE: juegoVálido
        PRE: laPosiciónEsVálidaEnLaGrilla
        PRE: posiciónNoAtacada
    """
    atacante:Jugador = turno(estado_juego)
    tableroAtacante:Tablero = tableroDeJugador(estado_juego, atacante)
    tableroAtacanteGrillaOponente:Grilla = grillaOponente(tableroAtacante)
    cambiarTurno(estado_juego)
    atacado:Jugador = turno(estado_juego)
    tableroAtacado:Tablero = tableroDeJugador(estado_juego, atacado)
    tableroAtacadoGrillaLocal:Grilla = grillaLocal(tableroAtacado)
    resultado:ResultadoDisparo
    if celdaEnPosición(tableroAtacadoGrillaLocal, posición) == VACÍO:
        resultado = NADA
        cambiarCeldaGrilla(tableroAtacadoGrillaLocal, posición, AGUA)
        cambiarCeldaGrilla(tableroAtacanteGrillaOponente, posición, AGUA)
    else:
        # celdaEnPosición(tableroAtacadoGrillaLocal, posición) == BARCO: #Porque no pudo haber atacado a AGUA
        resultado = TOCADO
        cambiarCeldaGrilla(tableroAtacadoGrillaLocal, posición, BARCO)#Redundante
        cambiarCeldaGrilla(tableroAtacanteGrillaOponente, posición, BARCO)
    return resultado


## Ejercicio 5

def barcosEnGrilla(grilla: Grilla) -> list[BarcoEnGrilla]:
    """ Indica los barcos ubicados en la grilla *grilla*
        PRE: laGrillaEsVálida
        PRE: hayUnaÚnicaFormaDeConstruirBarcos
    """
    
    posición:Posición = primeraPosiciónEnGrilla(grilla)
    colaPosicionesConBarcos:Cola[Posición] = Cola()
    barcos:list[BarcoEnGrilla] = []

    if(celdaEnPosición(grilla, posición) == BARCO):
        colaPosicionesConBarcos.put(posición)
    else:
        pass

    while(not esLaÚltimaPosiciónEnGrilla(posición, grilla)):
        posición = posiciónSiguienteEnGrilla(posición, grilla)
        if(celdaEnPosición(grilla, posición) == BARCO):
            colaPosicionesConBarcos.put(posición)
        else:
            pass
    
    while not colaPosicionesConBarcos.empty():
        unirPosiciónABarcos(colaPosicionesConBarcos.get(), barcos)
    
    return barcos
    
def unirPosiciónABarcos(posición: Posición, barcos:list[BarcoEnGrilla]) -> None:
    '''Si la posición *posición* es adyacente a algún barco en *barcos*, lo une a esta lista.
    Si no, crea un nuevo barco en grilla
    '''
    seUnióABarco = False
    for barco in barcos:
        if hayPosiciónAdyacenteEn(posición, barco):
            barco.append(posición)
            seUnióABarco = True
        else:
            pass

    if seUnióABarco == False:
        barcos.append([posición])

    return None
