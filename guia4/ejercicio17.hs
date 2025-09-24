{--
Implementar la funci´on esFibonacci :: Integer ->Bool seg´un la siguiente especificaci´on:
problema esFibonacci (n: Z) : B {
    requiere: { n ≥ 0 }
    asegura: { resultado = true ↔ n es alg´un valor de la secuencia de Fibonacci definida en el ejercicio 1}
}
--}

esFibonacci :: Integer -> Bool
esFibonacci num = num == 0 || num == 1 || esFibonacciRecursivo num 1 1

esFibonacciRecursivo :: Integer -> Integer -> Integer -> Bool
esFibonacciRecursivo numero fibo0 fibo1 | numero == fibo0 + fibo1 = True
                                        | numero < fibo0 + fibo1 = False--Utilizo que es una secuencia monotona, nunca puede decrecer
                                        | otherwise = esFibonacciRecursivo numero fibo1 (fibo0 + fibo1)