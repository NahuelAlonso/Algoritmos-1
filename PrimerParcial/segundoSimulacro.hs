--Ejercicio 1 
cantidadNumerosAbundantes :: Integer -> Integer -> Integer
cantidadNumerosAbundantes desde hasta
    | desde > hasta = 0
    | esAbundante hasta = cantidadNumerosAbundantes desde (hasta-1) + 1
    | otherwise = cantidadNumerosAbundantes desde (hasta-1)

esAbundante :: Integer -> Bool
esAbundante num = sumarLista (divisoresPropiosDesde num 1) > num

sumarLista :: [Integer] -> Integer
sumarLista [] = 0
sumarLista (cabeza : cola) = cabeza + sumarLista cola

divisoresPropiosDesde :: Integer -> Integer -> [Integer]
divisoresPropiosDesde num divisorPosible
    | num == divisorPosible = []
    | mod num divisorPosible == 0 = divisorPosible : divisoresPropiosDesde num (divisorPosible+1)
    | otherwise = divisoresPropiosDesde num (divisorPosible+1)

--Ejercicio 2

type CursadaAprobada = (String, Integer, Integer)--Nombre materia, Año de cursada, Período lectivo
cursadasVencidas :: [CursadaAprobada] -> [String]
cursadasVencidas [] = []
cursadasVencidas ((nombre, anio, periodo) : cola)
    | anio < 2021 = cursadasVencidas cola
    | anio == 2021 && periodo == 0 = cursadasVencidas cola
    | otherwise = nombre : cursadasVencidas cola

--Ejercicio 3

saturarEnUmbralHastaNegativo :: [Integer] -> Integer -> [Integer]
saturarEnUmbralHastaNegativo (cabeza : cola) umbral
    | cabeza < 0 = []
    | cabeza < umbral = cabeza : saturarEnUmbralHastaNegativo cola umbral
    | otherwise = umbral : saturarEnUmbralHastaNegativo cola umbral

--Ejercicio 4
cantidadParesColumna :: [[Integer]] -> Integer -> Integer --devuelve cant de n pares en la iesima columna 
cantidadParesColumna [] _ = 0
cantidadParesColumna (cabeza : cola) i
    | mod (obtenerNesimoElemento cabeza i) 2 == 0 = 1 + cantidadParesColumna cola i
    | otherwise = cantidadParesColumna cola i

obtenerNesimoElemento :: [Integer] -> Integer -> Integer
obtenerNesimoElemento (cabeza : cola) 1 = cabeza
obtenerNesimoElemento (cabeza : cola) indice = obtenerNesimoElemento cola (indice - 1)