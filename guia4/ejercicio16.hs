{--a) Implementar menorDivisor :: Integer ->Integer que calcule el menor divisor (mayor que 1) de un natural n pasado
como par´ametro--}
menorDivisor :: Integer -> Integer
menorDivisor num = menorDivisorRecursiva num 2

menorDivisorRecursiva :: Integer -> Integer -> Integer
menorDivisorRecursiva num divisor | mod num divisor == 0 = divisor
                                  | otherwise = menorDivisorRecursiva num (divisor + 1)

--Implementar la funci´on esPrimo :: Integer ->Bool que indica si un n´umero natural pasado como par´ametro es primo

esPrimo :: Integer -> Bool
esPrimo num = menorDivisor num == num

{--Implementar la funci´on sonCoprimos :: Integer ->Integer ->Bool que dados dos n´umeros naturales indica si no
tienen alg´un divisor en com´un mayor estricto que 1.--}
sonCoprimos :: Integer ->Integer -> Bool
sonCoprimos num0 num1 = sonCoprimosRecursiva num0 num1 2

sonCoprimosRecursiva :: Integer -> Integer -> Integer -> Bool
sonCoprimosRecursiva num0 num1 divisor | divisor > num0 || divisor > num1 = False
                                       | mod num0 divisor == 0 && mod num1 divisor == 0 = True
                                       | otherwise = sonCoprimosRecursiva num0 num1 (divisor + 1)

{--d) Implementar la funci´on nEsimoPrimo :: Integer ->Integer que devuelve el n-´esimo primo (n ≥ 1). Recordar que el
primer primo es el 2, el segundo es el 3, el tercero es el 5, etc.--}

nEsimoPrimo :: Integer -> Integer
nEsimoPrimo n = nEsimoPrimoRecursiva n 2

nEsimoPrimoRecursiva :: Integer -> Integer -> Integer
nEsimoPrimoRecursiva primosQueQuedan numeroEvaluado | esPrimo numeroEvaluado && primosQueQuedan == 1 = numeroEvaluado
                                                    | esPrimo numeroEvaluado = nEsimoPrimoRecursiva (primosQueQuedan-1) (numeroEvaluado+1)
                                                    | otherwise = nEsimoPrimoRecursiva primosQueQuedan (numeroEvaluado+1)