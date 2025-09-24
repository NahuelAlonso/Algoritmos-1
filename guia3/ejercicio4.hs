--a) productoInterno: calcula el producto interno entre dos tuplas de R × R.
productoInterno:: (Float, Float) -> (Float, Float) -> Float
productoInterno v u = fst v * fst u + snd v * snd u

--b) esParMenor: dadas dos tuplas de R × R, decide si cada coordenada de la primera tupla es menor a la coordenada correspondiente de la segunda tupla
esParMenor:: (Float, Float) -> (Float, Float) -> Bool
esParMenor v u = fst u < fst v && snd u < snd v

--c) distancia: calcula la distancia eucl´ıdea entre dos puntos de R
distancia:: (Float, Float) -> (Float, Float) -> Float
distancia v u = (fst u - fst v)**2 + (snd u - snd v)**2

--d) sumaTerna: dada una terna de enteros, calcula la suma de sus tres elementos.
sumaTerna:: (Integer, Integer, Integer) -> Integer
sumaTerna (x, y, z) = x + y + z

--e) sumarSoloMultiplos: dada una terna de n´umeros enteros y un natural, calcula la suma de los elementos de la terna que son m´ultiplos del n´umero natural.
devolverSiMultiplo :: Integer -> Integer -> Integer
devolverSiMultiplo n div | mod n div == 0 = n
                         | otherwise = 0

sumarSoloMultiplos:: (Integer, Integer, Integer) -> Integer -> Integer
sumarSoloMultiplos (n1, n2, n3) natural = devolverSiMultiplo n1 natural + devolverSiMultiplo n2 natural + devolverSiMultiplo n3 natural

--f) posPrimerPar: dada una terna de enteros, devuelve la posici´on del primer n´umero par si es que hay alguno, o devuelve 4 si son todos impares.
posPrimerPar :: (Integer, Integer, Integer) -> Integer 
posPrimerPar (n1, n2, n3) | mod n1 2 == 0 = 1
                          | mod n2 2 == 0 = 2
                          | mod n3 2 == 0 = 3
                          | otherwise = 4

--g) crearPar :: a -> b -> (a, b): a partir de dos componentes, crea un par con esos valores. Debe funcionar para elementos de cualquier tipo.
crearPar :: a -> a -> (a, a)
crearPar n m = (n, m)

--h) invertir :: (a, b) -> (b, a): invierte los elementos del par pasado como par´ametro. Debe funcionar para elementos de cualquier tipo.

invertir :: (a, a) -> (a, a)
invertir tupla = (snd tupla, fst tupla)

--i) Reescribir los ejercicios productoInterno, esParMenor y distancia usando el siguiente renombre de tipos: type Punto2D = (Float, Float)
type Punto2D = (Float, Float)

productoInterno2:: Punto2D -> Punto2D -> Float
productoInterno2 v u = fst v * fst u + snd v * snd u

esParMenor2:: Punto2D -> Punto2D -> Bool
esParMenor2 v u = fst u < fst v && snd u < snd v

distancia2:: Punto2D -> Punto2D -> Float
distancia2 v u = (fst u - fst v)**2 + (snd u - snd v)**2