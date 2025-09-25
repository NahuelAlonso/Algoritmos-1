--Ejercicio 1

generarStock :: [String] ->[(String, Int)]
generarStock [] = []
generarStock (cabeza : cola) = (cabeza, 1 + cantidadApariciones cabeza cola) : generarStock (quitarRepetidos cabeza cola)

cantidadApariciones :: String -> [String] -> Int
cantidadApariciones _ [] = 0
cantidadApariciones mercaderia (cabeza : cola) | cabeza == mercaderia = 1 + cantidadApariciones mercaderia cola
                                               | otherwise = cantidadApariciones mercaderia cola

quitarRepetidos :: String -> [String] -> [String]
quitarRepetidos _ [] = []
quitarRepetidos mercaderia (cabeza : cola) | cabeza == mercaderia = quitarRepetidos mercaderia cola
                                           | otherwise = cabeza : quitarRepetidos mercaderia cola

--Ejercicio 2

stockDeProducto :: [(String, Int)] ->String ->Int--Si no existe, devuelve 0
stockDeProducto [] _ = 0
stockDeProducto (cabeza : cola) nombre | fst cabeza == nombre = snd cabeza
                                       | otherwise = stockDeProducto cola nombre

--Ejercicio 3

dineroEnStock :: [(String, Int)] -> [(String, Float)] ->Float
dineroEnStock [] _ = 0
dineroEnStock (cabeza : cola) precios =
    buscarPrecio (fst cabeza) precios * fromIntegral (snd cabeza) + dineroEnStock cola precios

buscarPrecio :: String -> [(String, Float)] ->Float
buscarPrecio nombre (cabeza : cola) | nombre == fst cabeza = snd cabeza
                                    | otherwise = buscarPrecio nombre cola

--Ejercicio 4
aplicarOferta :: [(String, Int)] -> [(String, Float)] ->[(String,Float)]
aplicarOferta _ [] = []
aplicarOferta stock ((nombre, precio) : cola)
    | stockDeProducto stock nombre <= 10 = (nombre, precio) : aplicarOferta stock cola
    | otherwise = (nombre, precio * 0.8) : aplicarOferta stock cola

--Ejercicio 5
type Fila = [Int]
type Tablero = [Fila]
type Posicion = (Int, Int)
type Camino = [Posicion]

maximo :: Tablero -> Int
maximo [fila] = maximoFila fila 0
maximo (primeraFila : segundaFila : cola)
    | maximoFila primeraFila 0 > maximoFila segundaFila 0 = maximo (primeraFila : cola)
    | otherwise = maximo (segundaFila : cola)

maximoFila :: Fila -> Int -> Int
maximoFila [] maximoProvisional = maximoProvisional
maximoFila (cabeza: cola) maximoProvisional
    | cabeza > maximoProvisional = maximoFila cola cabeza
    | otherwise = maximoFila cola maximoProvisional

--Ejercicio 6

matrizALista :: Tablero -> [Int]--Toma un tablero y lo aplana, lo vuelve una lista
matrizALista [] = []
matrizALista (cabeza : cola) = cabeza ++ matrizALista cola

cantidadRepetidos :: Int -> [Int] -> Int
cantidadRepetidos _ [] = 0
cantidadRepetidos numero (cabeza : cola)
    | cabeza == numero = 1 + cantidadRepetidos numero cola
    | otherwise = cantidadRepetidos numero cola

quitar :: Int -> [Int] -> [Int]
quitar _ [] = []
quitar numero (cabeza : cola)
    | numero == cabeza = quitar numero cola
    | otherwise = cabeza : quitar numero cola

listaATuplas :: [Int] -> [(Int, Int)]
listaATuplas [] = []
listaATuplas (cabeza : cola) =
    (cabeza, 1 + cantidadRepetidos cabeza cola) : listaATuplas (quitar cabeza cola)

masRepetidoTupla :: [(Int, Int)] -> (Int, Int)
masRepetidoTupla [tupla] = tupla
masRepetidoTupla (primero : segundo : cola)
    | snd primero > snd segundo = masRepetidoTupla (primero : cola)
    | otherwise = masRepetidoTupla (segundo : cola)

masRepetido :: Tablero -> Int
masRepetido tablero = fst (masRepetidoTupla (listaATuplas (matrizALista tablero)))

--Ejercicio 7
--Noto que el elemento m[i][j] en una matriz de n filas y m columnas es el elemento i*m+j de la lista
valoresDeCamino :: Tablero -> Camino ->[Int]
valoresDeCamino _ [] = []
valoresDeCamino tablero ((fila, columna) : cola) = buscarElementoNEnLista indice (matrizALista tablero) : valoresDeCamino tablero cola
    where
        indice = (fila - 1) * cantColumnas + columna
        cantColumnas = longitud (head tablero)

longitud :: [Int] -> Int
longitud [] = 0
longitud (cabeza : cola) = longitud cola + 1

buscarElementoNEnLista :: Int -> [Int] -> Int--El primero es el 1
buscarElementoNEnLista 1 (cabeza: cola) = cabeza
buscarElementoNEnLista indice (cabeza: cola) = buscarElementoNEnLista (indice - 1) cola

--Ejercicio 8
esCaminoFibo :: [Int] -> Int ->Bool
esCaminoFibo [] _ = True
esCaminoFibo (cabeza : cola) indice
    | cabeza == obtenerNesimoFibo indice = esCaminoFibo cola (indice+1)
    | otherwise = False


obtenerNesimoFibo :: Int -> Int
obtenerNesimoFibo 0 = 0
obtenerNesimoFibo 1 = 1
obtenerNesimoFibo num = obtenerNesimoFibo (num - 1) + obtenerNesimoFibo (num - 2)

--Ejercicio 9
divisoresPropios :: Int -> [Int]
divisoresPropios num = divisoresPropiosRecursiva num 1

divisoresPropiosRecursiva :: Int -> Int -> [Int]
divisoresPropiosRecursiva num divisorPosible 
    | num == divisorPosible = []
    | mod num divisorPosible == 0 = divisorPosible : divisoresPropiosRecursiva num (divisorPosible + 1)
    | otherwise = divisoresPropiosRecursiva num (divisorPosible + 1)

--Ejercicio 10
sonAmigos :: Int ->Int ->Bool
sonAmigos num1 num2 = 
    (sumarLista (divisoresPropios num1) == num2) &&
    (sumarLista (divisoresPropios num2) == num1)

sumarLista :: [Int] -> Int
sumarLista [] = 0
sumarLista (cabeza : cola) = cabeza + sumarLista cola

--Ejercicio 11
losPrimerosNPerfectos :: Int ->[Int]
losPrimerosNPerfectos num = losPrimerosNPerfectosRecursiva num 2

losPrimerosNPerfectosRecursiva :: Int -> Int -> [Int]
losPrimerosNPerfectosRecursiva 0 _ = []
losPrimerosNPerfectosRecursiva indice num
    | esPerfecto num = num : losPrimerosNPerfectosRecursiva (indice - 1) (num + 1)
    | otherwise = losPrimerosNPerfectosRecursiva indice (num + 1)


esPerfecto :: Int -> Bool
esPerfecto num = sonAmigos num num

--Ejercicio 12
tieneAmigos :: Int -> [Int] -> Bool
tieneAmigos _ [] = False
tieneAmigos num (cabeza : cola)
    | sonAmigos cabeza num = True
    | otherwise = tieneAmigos num cola

listaDeAmigos :: [Int] ->[(Int,Int)]
listaDeAmigos [] = []
listaDeAmigos (cabeza : cola)
    | tieneAmigos cabeza cola = (cabeza, sumarLista (divisoresPropios cabeza)) : listaDeAmigos cola
    | otherwise = listaDeAmigos cola