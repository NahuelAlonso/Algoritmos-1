{--
Implementar una funci´on mayorDigitoPar :: Integer ->Integer seg´un la siguiente especificaci´on:
problema mayorDigitoPar (n: N) : N {
    requiere: { T rue }
    asegura: { resultado es el mayor de los d´ıgitos pares de n. Si n no tiene ning´un d´ıgito par, entonces resultado es -1.
}
}--}
absoluto :: Integer -> Integer
absoluto num | num < 0 = -num
             | otherwise = num

mayorDigitoPar :: Integer ->Integer
mayorDigitoPar num = mayorDigitoParRecursiva (absoluto num) (-1)

mayorDigitoParRecursiva :: Integer -> Integer -> Integer
mayorDigitoParRecursiva num mayorDigito | num == 0 = mayorDigito
                                        | mod ultimoDigito 2 == 0 && ultimoDigito > mayorDigito = mayorDigitoParRecursiva numSinUnidades ultimoDigito
                                        | otherwise = mayorDigitoParRecursiva numSinUnidades mayorDigito
                                        where
                                            ultimoDigito = mod num 10
                                            numSinUnidades = div num 10