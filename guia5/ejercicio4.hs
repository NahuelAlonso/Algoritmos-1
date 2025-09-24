{--
sacarBlancosRepetidos :: [Char] -> [Char], que reemplaza cada subsecuencia de blancos contiguos de la primera
lista por un solo blanco en la segunda lista.
--}
sacarBlancosRepetidos :: [Char] -> [Char]
sacarBlancosRepetidos [] = []
sacarBlancosRepetidos (cabeza : cola) | cabeza == ' ' = cabeza : sacarBlancosRepetidos (sacarPrimerosBlancos cola)
                                      | otherwise = cabeza : sacarBlancosRepetidos cola

sacarPrimerosBlancos :: [Char] -> [Char]
sacarPrimerosBlancos [] = []
sacarPrimerosBlancos (cabeza : cola) | cabeza == ' ' = sacarPrimerosBlancos cola
                                     | otherwise = cabeza : cola

{--
contarPalabras :: [Char] -> Integer, que dada una lista de caracteres devuelve la cantidad de palabras que tiene.
--}


contarPalabras :: [Char] -> Integer
contarPalabras oracion = 1 + contarEspaciosExceptoUltimo (normalizarOracion oracion)
--Necesito sumar uno porque cada espacio nota una palabra, excepto la primera que no tiene espacio al principio

--Normalizo la oracion, que tenga un espacio por palabra. Para esto saco todos los blancos repetidos y los blancos al principio de la oración
normalizarOracion :: [Char] -> [Char]
normalizarOracion oracion = sacarPrimerosBlancos (sacarBlancosRepetidos oracion)


contarEspaciosExceptoUltimo :: [Char] -> Integer
contarEspaciosExceptoUltimo [' '] = 0--Necesito que si termina en un espacio, que no me sume una palabra
contarEspaciosExceptoUltimo [] = 0
contarEspaciosExceptoUltimo (cabeza : cola) | cabeza == ' ' = 1 + contarEspaciosExceptoUltimo cola
                                            | otherwise = contarEspaciosExceptoUltimo cola

{--
palabraMasLarga :: [Char] -> [Char], que dada una lista de caracteres devuelve su palabra m ́as larga.
--}

palabraMasLarga :: [Char] -> [Char]
palabraMasLarga string = palabraMasLargaRecursiva (normalizarOracion string) []--Me aseguro *un* espacio entre palabra

palabraMasLargaRecursiva :: [Char] -> [Char] -> [Char]
palabraMasLargaRecursiva [] palabraMasLarga = palabraMasLarga
palabraMasLargaRecursiva string palabraMasLarga
    | longitudOracion (primeraPalabra string) > longitudOracion palabraMasLarga = palabraMasLargaRecursiva (sacarPrimeraPalabra string) (primeraPalabra string)
    | otherwise = palabraMasLargaRecursiva (sacarPrimeraPalabra string) palabraMasLarga

sacarPrimeraPalabra :: [Char] -> [Char]--No puede tener un espacio al principio
sacarPrimeraPalabra [] = []
sacarPrimeraPalabra (cabeza : cola) | cabeza == ' ' = cola
                                    | otherwise = sacarPrimeraPalabra cola

primeraPalabra :: [Char] -> [Char]--No puede tener un espacio al principio
primeraPalabra oracion = primeraPalabraRecursiva [] oracion

primeraPalabraRecursiva :: [Char] -> [Char] -> [Char]
primeraPalabraRecursiva palabra [] = palabra
primeraPalabraRecursiva palabra (cabeza : cola) | cabeza == ' ' = palabra
                                                | otherwise = primeraPalabraRecursiva (palabra ++ [cabeza]) cola

longitudOracion :: [Char] -> Integer--No cuenta a los espacios
longitudOracion [] = 0
longitudOracion (cabeza : cola) = 1 + longitudOracion cola

{--
palabras :: [Char] -> [[Char]], que dada una lista arma una nueva lista con las palabras de la lista original.
--}

palabras :: [Char] -> [[Char]]
palabras [] = []
palabras oracion | head oracion == ' ' = palabras (tail oracion)
                 | otherwise = primeraPalabra oracion : palabras (sacarPrimeraPalabra oracion)

{--
aplanar :: [[Char]] -> [Char], que a partir de una lista de palabras arma una lista de caracteres concaten ́andolas.
--}
aplanar :: [[Char]] -> [Char]
aplanar [] = []
aplanar (cabeza: cola) = cabeza ++ aplanar cola

{--
aplanarConBlancos :: [[Char]] -> [Char], que a partir de una lista de palabras, arma una lista de caracteres
concaten ́andolas e insertando un blanco entre cada palabra.
--}

aplanarConBlancos :: [[Char]] -> [Char]
aplanarConBlancos [] = []
aplanarConBlancos (cabeza: cola) = cabeza ++ [' '] ++ aplanarConBlancos cola

{--
aplanarConNBlancos :: [[Char]] -> Integer -> [Char], que a partir de una lista de palabras y un entero n,
arma una lista de caracteres concaten ́andolas e insertando n blancos entre cada palabra (n debe ser no negativo).
--}

crearNBlancos :: Integer -> [Char]
crearNBlancos 0 = []
crearNBlancos numero = ' ' : crearNBlancos (numero-1)

aplanarConNBlancos :: [[Char]] -> Integer -> [Char]
aplanarConNBlancos [] _ = []
aplanarConNBlancos (cabeza: cola) num = cabeza ++ crearNBlancos num ++ aplanarConNBlancos cola num