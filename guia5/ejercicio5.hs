{--
nat2bin :: Integer -> [Integer], que recibe un n ́umero no negativo y lo transforma en una lista de bits corres-
pondiente a su representaci ́on binaria. Por ejemplo nat2bin 8 devuelve [1, 0, 0, 0].
--}

nat2bin :: Integer -> [Integer]
nat2bin 0 = []--nat2bin 0 me devuelve [], esta bien?
nat2bin num = nat2bin (div num 2) ++ [mod num 2]

{--
bin2nat :: [Integer] -> Integer seg ́un la siguiente especificaci ́on:
problema bin2nat (s: seq⟨Z⟩) : Z {
requiere: { s es una lista de 0’s y 1’s}
asegura: { resultado es el n ́umero entero no negativo cuya representaci ́on binaria es s.}
}
--}
longitud :: [Integer] -> Integer
longitud [] = 0
longitud (cabeza : cola) = 1 + longitud cola

bin2nat :: [Integer] -> Integer
bin2nat [] = 0
bin2nat (cabeza : cola) = cabeza * (2 ^ longitud cola) + bin2nat cola

{--
nat2hex :: Integer -> [Char], que recibe un n ́umero no negativo y lo transforma en una lista de caracteres corres-
pondiente a su representaci ́on hexadecimal. Por ejemplo nat2hex 45 devuelve [’2’, ’D’].
--}
nat2hexChicos :: Integer -> Char
nat2hexChicos 0 = '0'
nat2hexChicos 1 = '1'
nat2hexChicos 2 = '2'
nat2hexChicos 3 = '3'
nat2hexChicos 4 = '4'
nat2hexChicos 5 = '5'
nat2hexChicos 6 = '6'
nat2hexChicos 7 = '7'
nat2hexChicos 8 = '8'
nat2hexChicos 9 = '9'
nat2hexChicos 10 = 'A'
nat2hexChicos 11 = 'B'
nat2hexChicos 12 = 'C'
nat2hexChicos 13 = 'D'
nat2hexChicos 14 = 'E'
nat2hexChicos 15 = 'F'


nat2hex :: Integer -> [Char]
nat2hex 0 = []--nat2hex 0 me devuelve [], esta bien?
nat2hex num = nat2hex (div num 16) ++ [nat2hexChicos (mod num 16)]

sumaAcumulada :: (Num t) => [t] -> [t]
sumaAcumulada lista = sumaAcumuladaRecursiva lista 0

sumaAcumuladaRecursiva :: (Num t) => [t] -> t -> [t]
sumaAcumuladaRecursiva [] _ = []
sumaAcumuladaRecursiva (cabeza : cola) suma = cabeza + suma : sumaAcumuladaRecursiva cola (cabeza + suma)

descomponerEnPrimos :: [Integer] -> [[Integer]]
descomponerEnPrimos [] = []
descomponerEnPrimos (cabeza : cola) = descomponerEnPrimosRecursiva cabeza : descomponerEnPrimos cola


menorDivisor :: Integer -> Integer
menorDivisor num = menorDivisorRecursiva num 2

menorDivisorRecursiva :: Integer -> Integer -> Integer
menorDivisorRecursiva num divisor | mod num divisor == 0 = divisor
                                  | otherwise = menorDivisorRecursiva num (divisor + 1)

descomponerEnPrimosRecursiva :: Integer -> [Integer]
descomponerEnPrimosRecursiva 1 = []
descomponerEnPrimosRecursiva num = menorDivisor num : descomponerEnPrimosRecursiva (div num (menorDivisor num))
