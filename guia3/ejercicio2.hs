absoluto:: Integer -> Integer
absoluto n | n < 0 = -n
           | n >= 0 = n

maximo:: Integer -> Integer -> Integer
maximo n m | n > m = n
           | otherwise = m

maximoAbsoluto:: Integer -> Integer -> Integer
maximoAbsoluto n m | absoluto n > absoluto m = n
                   | otherwise = m


maximo3:: Integer -> Integer -> Integer -> Integer
maximo3 n m p = maximo (maximo n m) p

algunoEsCero:: Float -> Float -> Bool
algunoEsCero n m = n*m == 0

ambosSonCero:: Float -> Float -> Bool
ambosSonCero n m = (n == 0) && (m == 0)

encontrarIntervalo:: Float -> Int
encontrarIntervalo n | n > 7 = 3
                     | n <= 3 = 1
                     | otherwise = 2

enMismoIntervalo:: Float -> Float -> Bool
enMismoIntervalo n m = encontrarIntervalo n == encontrarIntervalo m

sumaDistintos:: Integer -> Integer -> Integer -> Integer
sumaDistintos n m p | (n == m) && (n == p) = n
                    | n == m = n + p
                    | n == p = n + m
                    | m == p = n + m
                    | otherwise = n + m + p

esMultiploDe:: Integer -> Integer -> Bool
esMultiploDe posibleMult divisor = mod posibleMult divisor == 0

digitoUnidades:: Integer -> Integer
digitoUnidades n = mod (absoluto n) 10

digitoDecenas:: Integer -> Integer
digitoDecenas n = mod (absoluto n) 100 - digitoUnidades n

