{--
agregarATodos :: Integer -> Set (Set Integer) -> Set (Set Integer) que dado un n ́umero n y un conjunto
de conjuntos de enteros cls agrega a n en cada conjunto de cls.
--}

agregarATodos :: Integer -> [[Integer]] -> [[Integer]]
agregarATodos _ [] = []
agregarATodos num (cabeza : cola) =
    agregarATodosRecursiva num cabeza : agregarATodos num cola

agregarATodosRecursiva :: Integer -> [Integer] -> [Integer]
agregarATodosRecursiva _ [] = []
agregarATodosRecursiva num (cabeza : cola) = cabeza + num : agregarATodosRecursiva num cola

{--
partes :: Integer -> Set (Set Integer) que genere todos los subconjuntos del conjunto {1, 2, . . . , n}.
--}

partes :: Integer -> [[Integer]]