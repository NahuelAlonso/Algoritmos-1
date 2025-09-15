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
sumarSoloMultiplos:: [Integer] -> Integer -> Integer
sumarSoloMultiplos [] natural = 0
sumarSoloMultiplos [lista] natural | mod (head lista) natural == 0 = head lista + sumarSoloMultiplos (tail lista)
                                   | otherwise = sumarSoloMultiplos (tail lista)