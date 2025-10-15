module Parcial where

cantidadNumerosAbundantes :: Integer -> Integer -> Integer
cantidadNumerosAbundantes desde hasta
    | desde > hasta = 0
    | esNumeroAbundante desde = 1 + cantidadNumerosAbundantes (desde+1) hasta
    | otherwise = cantidadNumerosAbundantes (desde+1) hasta


esNumeroAbundante :: Integer -> Bool
esNumeroAbundante num = sumarLista (divisoresPropiosDesde num 1) > num

sumarLista :: [Integer] -> Integer
sumarLista [] = 0
sumarLista (cabeza : cola) = cabeza + sumarLista cola

divisoresPropiosDesde :: Integer -> Integer -> [Integer]
divisoresPropiosDesde num divisorPosible
    | num == divisorPosible = []
    | mod num divisorPosible == 0 = divisorPosible : divisoresPropiosDesde num (divisorPosible+1)
    | otherwise = divisoresPropiosDesde num (divisorPosible+1)

--Ejercicio 2
cursadasVencidas :: [(String, Integer, Integer)] -> [String]
cursadasVencidas [] = []
cursadasVencidas ((nombre, anio, periodo) : cola)
    | anio < 2021 = nombre : cursadasVencidas cola
    | periodo < 1 && anio == 2021 = nombre : cursadasVencidas cola
    | otherwise = cursadasVencidas cola

--Ejercicio 3
saturarEnUmbralHastaNegativo :: [Integer] -> Integer -> [Integer]
saturarEnUmbralHastaNegativo [] _ = []
saturarEnUmbralHastaNegativo (cabeza : cola) umbral
    | cabeza > umbral = umbral : saturarEnUmbralHastaNegativo cola umbral
    | cabeza < 0 = []
    | otherwise = cabeza : saturarEnUmbralHastaNegativo cola umbral

--Ejercicio 4
cantidadParesColumna :: [[Integer]] -> Integer -> Integer
cantidadParesColumna [] _ = 0
cantidadParesColumna (cabeza : cola) columna = mod (1 + hallarNesimoElemento cabeza columna) 2 + cantidadParesColumna cola columna

hallarNesimoElemento :: [Integer] -> Integer -> Integer
hallarNesimoElemento (cabeza : _) 1 = cabeza
hallarNesimoElemento (_ : cola) indice = hallarNesimoElemento cola (indice-1)
