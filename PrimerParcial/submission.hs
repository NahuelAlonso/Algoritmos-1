{--
Yo: COMPLETE SU NOMBRE ACÁ
Certifico que el siguiente archivo fue elaborado únicamente por mí, sin ayuda de otras personas o herramientas.
--}


module SolucionT2 where

-- Ejercicio 1: Encontrar el mayor número de Fibonacci en un rango
mayorFibonacciEnRango :: Integer -> Integer -> Integer
mayorFibonacciEnRango desde hasta
    | esFibo hasta 0 = hasta
    | otherwise = mayorFibonacciEnRango desde (hasta-1)

nesimoFibo :: Integer -> Integer
nesimoFibo 0 = 1
nesimoFibo 1 = 1
nesimoFibo num = nesimoFibo (num-1) + nesimoFibo (num-2)


esFibo :: Integer -> Integer -> Bool
esFibo num desde
    | num > nesimoFibo desde = esFibo num (desde+1)
    | num == nesimoFibo desde = True
    | otherwise = False




-- Ejercicio 2: Verificar si una secuencia es montaña rusa
esMontaniaRusa :: [Integer] -> Bool
esMontaniaRusa lista = 
    esMontaniaRusaRecursiva lista True || esMontaniaRusaRecursiva lista False 

esMontaniaRusaRecursiva :: [Integer] -> Bool -> Bool
esMontaniaRusaRecursiva [] _ = True
esMontaniaRusaRecursiva [ultimoNum] _ = True
esMontaniaRusaRecursiva (num1 : num2 : cola) debeSerPos
    | num1 - num2 < 0 && not debeSerPos = esMontaniaRusaRecursiva (num2 : cola) (not debeSerPos)
    | num1 - num2 > 0 && debeSerPos = esMontaniaRusaRecursiva (num2 : cola) (not debeSerPos)
    | otherwise = False


-- Ejercicio 3: Crear catálogo de libros por autores
catalogoPorAutores :: [(String, String)] -> [(String, [String])]
catalogoPorAutores [] = []
catalogoPorAutores (cabeza : cola) =
    (fst cabeza, obtenerLibros (fst cabeza) (cabeza: cola)) :
        catalogoPorAutores (quitarAutor (fst cabeza) (cabeza: cola) )

obtenerLibros :: String -> [(String, String)] -> [String]
obtenerLibros _ [] = []
obtenerLibros autorBuscado ((autor, libro) : cola)
    | autor == autorBuscado = libro : obtenerLibros autorBuscado cola
    | otherwise = obtenerLibros autorBuscado cola

quitarAutor :: String -> [(String, String)] -> [(String, String)]
quitarAutor _ [] = []
quitarAutor autorBuscado ((autor, libro):cola) 
    | autor == autorBuscado = quitarAutor autorBuscado cola
    | otherwise = (autor,libro) : quitarAutor autorBuscado cola




-- Ejercicio 4: Encontrar la fila que contiene el valor máximo de una matriz
filaDelMaximo :: [[Integer]] -> Integer
filaDelMaximo matriz = fst (obtenerMaximoDeTuplas (filaConMaximo matriz 1))

obtenerMaximoDeTuplas :: [(Integer, Integer)] -> (Integer, Integer)
obtenerMaximoDeTuplas [tupla] = tupla
obtenerMaximoDeTuplas ((fila, maximo) : cola)
    | maximo < snd (obtenerMaximoDeTuplas cola) = obtenerMaximoDeTuplas cola
    | otherwise = (fila, maximo)

filaConMaximo :: [[Integer]] -> Integer -> [(Integer, Integer)]
filaConMaximo [fila] indice = [(indice, maximoFila fila)]
filaConMaximo (cabeza : cola) indice =
    (indice, maximoFila cabeza) : filaConMaximo cola (indice+1)

maximoFila :: [Integer] -> Integer
maximoFila [elemento] = elemento
maximoFila (num1 : num2 : cola)
    | num1 < num2 = maximoFila (num2 : cola) 
    | otherwise = maximoFila (num1 : cola) 

{--
Siendo la última modificación con la solución final:
COMPLETE FECHA y HORA DE ULTIMA MODIFICACIÓN ACA
1/10 14:42
--}
