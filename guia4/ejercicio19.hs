{--
Implementar la funci´on esSumaInicialDePrimos :: Integer ->Bool seg´un la siguiente especificaci´on:
problema esSumaInicialDePrimos (n: Z) : B {
requiere: { n ≥ 0 }
asegura: { resultado = true ↔ n es igual a la suma de los m primeros n´umeros primos, para alg´un m.}
}
--}
menorDivisor :: Integer -> Integer
menorDivisor num = menorDivisorRecursiva num 2

menorDivisorRecursiva :: Integer -> Integer -> Integer
menorDivisorRecursiva num divisor | mod num divisor == 0 = divisor
                                  | otherwise = menorDivisorRecursiva num (divisor + 1)

esPrimo :: Integer -> Bool
esPrimo num = menorDivisor num == num


esSumaInicialDePrimos :: Integer -> Bool
esSumaInicialDePrimos numero = sumaPrimerosPrimos numero 0 2

sumaPrimerosPrimos :: Integer -> Integer -> Integer -> Bool
sumaPrimerosPrimos maximo sumaActual numeroEvaluado | maximo < sumaActual = False
                                                    | maximo == sumaActual = True
                                                    | esPrimo numeroEvaluado = sumaPrimerosPrimos maximo (sumaActual + numeroEvaluado) (numeroEvaluado+1)
                                                    | otherwise = sumaPrimerosPrimos maximo sumaActual (numeroEvaluado+1)