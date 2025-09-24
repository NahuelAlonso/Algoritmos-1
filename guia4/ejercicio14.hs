{--Especificar e implementar una funci´on sumaPotencias :: Integer ->Integer ->Integer ->Integer que
dados tres naturales q, n, m sume todas las potencias de la forma q**(a+b)
con 1 ≤ a ≤ n y 1 ≤ b ≤ m.
--}
sumaPotencias :: Integer ->Integer ->Integer ->Integer
sumaPotencias = primerSigma 

primerSigma :: Integer -> Integer -> Integer -> Integer
primerSigma q n m | n == 0 = 0
                  | otherwise = primerSigma q (n-1) m + segundoSigma q n m

segundoSigma :: Integer -> Integer -> Integer -> Integer
segundoSigma q n m | m == 0 = 0
                   | otherwise = segundoSigma q n (m-1) + sumando q n m

sumando :: Integer -> Integer -> Integer -> Integer
sumando q n m = q ^ (n+m)