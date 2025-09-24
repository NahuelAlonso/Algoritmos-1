{--Implementar una funci´on sumaRacionales :: Integer ->Integer ->Float que dados dos naturales n, m
sume todos los n´umeros racionales de la forma p/q con 1 ≤ p ≤ n y 1 ≤ q ≤ m--}
sumaRacionales :: Integer ->Integer ->Float 
sumaRacionales = primerSigma

primerSigma :: Integer -> Integer -> Float
primerSigma n m | n == 0 = 0
                | otherwise = primerSigma (n-1) m + segundoSigma n m

segundoSigma :: Integer -> Integer -> Float
segundoSigma n m | m == 0 = 0
                 | otherwise = segundoSigma n (m-1) + sumando n m

sumando :: Integer -> Integer -> Float
sumando n m = fromInteger n / fromInteger m