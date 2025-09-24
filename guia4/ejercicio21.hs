{--
Especificar e implementar una funci´on pitagoras :: Integer ->Integer ->Integer ->Integer que dados
m, n , r ∈ N≥0, cuente cu´antos pares (p, q) con 0 ≤ p ≤ m y 0 ≤ q ≤ n satisfacen que p^2+q^2<=r^2
--}

pitagoras :: Integer -> Integer -> Integer -> Integer 
pitagoras = primerSigma

primerSigma :: Integer -> Integer -> Integer -> Integer
primerSigma p q r | p == -1 = 0
                  | otherwise = primerSigma (p-1) q r + segundoSigma p q r

segundoSigma :: Integer -> Integer -> Integer ->  Integer
segundoSigma p q r | q == -1 = 0
                   | otherwise = segundoSigma p (q-1) r + sumando p q r

sumando :: Integer -> Integer -> Integer ->  Integer
sumando p q r | p ^ 2 + q ^ 2 <= r ^ 2 = 1
              | otherwise = 0