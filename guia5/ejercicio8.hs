sumaTotal :: [[Integer]] -> Integer --Todas las filas tienen igual longitud y no pueden ser nulas
sumaTotal = fstSigmaSumaTotal

fstSigmaSumaTotal :: [[Integer]] -> Integer
fstSigmaSumaTotal [] = 0
fstSigmaSumaTotal (cabeza : cola) = fstSigmaSumaTotal cola + sndSigmaSumaTotal cabeza

sndSigmaSumaTotal :: [Integer] -> Integer
sndSigmaSumaTotal [] = 0
sndSigmaSumaTotal (cabeza : cola) = sndSigmaSumaTotal cola + cabeza
-----------
cantidadDeApariciones :: (Eq t) => t -> [[t]] -> Integer
cantidadDeApariciones = fstSigmaApariciones

fstSigmaApariciones :: (Eq t) => t -> [[t]] -> Integer
fstSigmaApariciones _ [] = 0
fstSigmaApariciones num (cabeza : cola) = fstSigmaApariciones num cola + sndSigmaApariciones num cabeza

sndSigmaApariciones :: (Eq t) =>t -> [t] -> Integer
sndSigmaApariciones _ [] = 0
sndSigmaApariciones num (cabeza : cola) | num == cabeza = sndSigmaApariciones num cola + 1
                                        | otherwise = sndSigmaApariciones num cola
------------
contarPalabras :: String -> [[String]] -> Integer
contarPalabras = cantidadDeApariciones
------------
multiplicarPorEscalar :: Integer -> [[Integer]] -> [[Integer]]
multiplicarPorEscalar _ [] = []
multiplicarPorEscalar lambda (cabeza : cola) = multiplicarPorEscalarLista lambda cabeza : multiplicarPorEscalar lambda cola

multiplicarPorEscalarLista :: Integer -> [Integer] -> [Integer]
multiplicarPorEscalarLista _ [] = []
multiplicarPorEscalarLista lambda (cabeza : cola) = cabeza * lambda : multiplicarPorEscalarLista lambda cola
-----------
concatenarFilas :: [[String]] -> [String]
concatenarFilas [] = []
concatenarFilas (cabeza : cola) = concatenarLista cabeza : concatenarFilas cola

concatenarLista :: [String] -> String
concatenarLista [] = []
concatenarLista (cabeza : cola) = cabeza ++ concatenarLista cola
-----------
iesimaFila :: Integer -> [[a]] -> [a]
iesimaFila 0 (cabeza : cola) = cabeza
iesimaFila indice (cabeza : cola) = iesimaFila (indice-1) cola
-----------
iesimaColumna :: Integer -> [[a]] -> [a]
iesimaColumna _ [] = []
iesimaColumna numero (cabeza : cola) = iesimoElemento numero cabeza : iesimaColumna numero cola

iesimoElemento :: Integer -> [a] -> a
iesimoElemento 0 (cabeza : cola) = cabeza
iesimoElemento num (cabeza : cola) = iesimoElemento (num-1) cola
-----------
matrizIdentidad :: Integer -> [[Integer]]
matrizIdentidad dimension = generarMatrizVacia dimension dimension

generarMatrizVacia :: Integer -> Integer -> [[Integer]]
generarMatrizVacia 0 columnas = []
generarMatrizVacia filas columnas = generarListaCon0 filas columnas : generarMatrizVacia (filas-1) columnas

generarListaCon0 :: Integer -> Integer-> [Integer]
generarListaCon0 0 _ = []
generarListaCon0 longitud posicion | longitud == posicion = 0 : generarListaCon0 posicion (longitud-1)
                                   | otherwise = 1 : generarListaCon0 posicion (longitud-1)