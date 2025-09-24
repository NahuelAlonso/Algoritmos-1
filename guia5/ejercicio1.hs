-- longitud :: [t] -> Integer, que dada una lista devuelve su cantidad de elementos.
longitud :: [a] -> Integer
longitud [] = 0
--longitud (_:lista) = 1 + longitud lista
longitud lista = 1 + longitud (tail lista)

{--
ultimo :: [t] -> t seg ́un la siguiente especificaci ́on:
problema ultimo (s: seq⟨T⟩) : seq⟨T⟩ {
    requiere: { |s| > 0 }
    asegura: { resultado = s[|s| − 1] }
}
--}

ultimo :: [t] -> t
ultimo lista | longitud lista == 1 = head lista
             | otherwise = ultimo (tail lista)

{--
principio :: [t] -> [t] seg ́un la siguiente especificaci ́on:
problema principio (s: seq⟨T⟩) : seq⟨T⟩ {
requiere: { |s| > 0 }
asegura: { resultado = subseq(s, 0, |s| − 1) }
}
--}

principio :: [t] -> [t]
principio (primero: lista) | longitud lista == 0 = []
                           | otherwise = primero : principio lista

{--
reverso :: [t] -> [t] seg ́un la siguiente especificaci ́on:
problema reverso (s: seq⟨T⟩) : seq⟨T⟩ {
requiere: { T rue }
asegura: { resultado tiene los mismos elementos que s pero en orden inverso.}
}
--}

reverso :: [t] -> [t]--Lo uso después
reverso [] = []
reverso (primero: lista) = reverso lista ++ [primero]