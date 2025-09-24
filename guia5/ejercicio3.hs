sumatoria :: [Integer] -> Integer
sumatoria [] = 0
sumatoria (cabeza: cola) = sumatoria cola + cabeza

productoria :: [Integer] -> Integer
productoria [] = 1
productoria (cabeza: cola) = productoria cola * cabeza

maximo :: [Integer] -> Integer
maximo [elemento] = elemento
maximo (cabeza: cola) | cabeza > maximo cola = cabeza
                      | otherwise = maximo cola

sumarN :: Integer -> [Integer] -> [Integer]
sumarN n [] = []
sumarN n (cabeza: cola) = (cabeza + n) : sumarN n cola

sumarElPrimero :: [Integer] -> [Integer]
sumarElPrimero (cabeza: cola) = sumarN cabeza (cabeza: cola)

ultimo :: [t] -> t
ultimo [elemento] = elemento
ultimo lista = ultimo (tail lista)

sumarElUltimo :: [Integer] -> [Integer]
sumarElUltimo lista = sumarN (ultimo lista) lista

pares :: [Integer] -> [Integer]
pares [] = []
pares (cabeza: cola) | mod cabeza 2 == 0 = cabeza : pares cola
                     | otherwise = pares cola
                     
multiplosDeN :: Integer -> [Integer] -> [Integer]
multiplosDeN _ [] = []
multiplosDeN divisor (cabeza : cola) | mod cabeza divisor == 0 = cabeza : multiplosDeN divisor cola
                                     | otherwise = multiplosDeN divisor cola


ordenar :: [Integer] -> [Integer]
ordenar [] = []
ordenar lista = maximo lista : ordenar (listaSinElemento lista (maximo lista))

listaSinElemento :: [Integer] -> Integer -> [Integer]--Encuentra la primer aparición y se la saca
listaSinElemento [] _ = []
listaSinElemento (cabeza: cola) elemento | cabeza == elemento = cola
                                         | otherwise = cabeza : listaSinElemento cola elemento
