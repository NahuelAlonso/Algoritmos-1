{--
pertenece :: (Eq t) => t -> [t] -> Bool seg ́un la siguiente especificaci ́on:
problema pertenece (e: T, s: seq⟨T⟩) : B {
requiere: { T rue }
asegura: { resultado = true ↔ e ∈ s }
}
--}
pertenece :: (Eq t) => t -> [t] -> Bool
pertenece _ [] = False
pertenece elemento (primero: lista) | primero == elemento = True
                                    | otherwise = pertenece elemento lista

{--2. todosIguales :: (Eq t) => [t] -> Bool, que dada una lista devuelve verdadero s ́ı y solamente s ́ı todos sus ele-
mentos son iguales.--}

longitud :: [t] -> Int
longitud [] = 0
longitud (_: lista) = 1 + longitud lista

todosIguales :: (Eq t) => [t] -> Bool
todosIguales lista | longitud lista == 1 = True
                   | head lista == segundo = todosIguales (tail lista)
                   | otherwise = False
                   where segundo = head (tail lista)

{-- 
todosDistintos :: (Eq t) => [t] -> Bool seg ́un la siguiente especificaci ́on:
problema todosDistintos (s: seq⟨T⟩) : B {
    requiere: { T rue }
    asegura: { resultado = f alse ↔ (∃i, j : Z)(0 ≤ i < |s| ∧ 0 ≤ j < |s| ∧ i ̸= j ∧ s[i] = s[j] }
}
--}

todosDistintos :: (Eq t) => [t] -> Bool
todosDistintos lista | longitud lista == 1 = True
todosDistintos (primero: cola) = not (pertenece primero cola) && todosDistintos cola

{--
hayRepetidos :: (Eq t) => [t] -> Bool seg ́un la siguiente especificaci ́on:
problema hayRepetidos (s: seq⟨T⟩) : B {
requiere: { T rue }
asegura: {resultado = true ↔ (∃i, j : Z)(0 ≤ i < |s| ∧ 0 ≤ j < |s| ∧ i ̸= i ∧ s[i] = s[j])}
}
--}

hayRepetidos :: (Eq t) => [t] -> Bool
hayRepetidos lista = not (todosDistintos lista)

{--
quitar :: (Eq t) => t -> [t] -> [t], que dada una lista xs y un elemento x, elimina la primera aparici ́on de x
en la lista xs (de haberla).
--}

quitar :: (Eq t) => t -> [t] -> [t]
quitar _ [] = []
quitar elemento (cabeza: cola) | cabeza == elemento = cola
                               | otherwise = cabeza : quitar elemento cola

{--
quitarTodos :: (Eq t ) => t -> [t] -> [t], que dada una lista xs y un elemento x, elimina todas las apariciones
de x en la lista xs (de haberlas). Es decir:
problema quitarTodos (e: T, s: seq⟨T⟩) : seq⟨T⟩ {
requiere: { T rue }
asegura: { resultado es igual a s pero sin el elemento e. }
}
--}

quitarTodos :: (Eq t ) => t -> [t] -> [t]
quitarTodos _ [] = []
quitarTodos elemento (cabeza: cola) | cabeza == elemento = quitarTodos elemento cola
                                    | otherwise = cabeza : quitarTodos elemento cola

{--
eliminarRepetidos :: (Eq t) => [t] -> [t] que deja en la lista una  ́unica aparici ́on de cada elemento, eliminando
las repeticiones adicionales.
--}

eliminarRepetidos :: (Eq t) => [t] -> [t]
eliminarRepetidos [] = []
eliminarRepetidos (cabeza: cola) = cabeza : eliminarRepetidos (quitarTodos cabeza cola)

{--
mismosElementos :: (Eq t) => [t] -> [t] -> Bool, que dadas dos listas devuelve verdadero s ́ı y solamente s ́ı
ambas listas contienen los mismos elementos, sin tener en cuenta repeticiones, es decir:
problema mismosElementos (s: seq⟨T⟩, r: seq⟨T⟩) : B {
requiere: { T rue }
asegura: { resultado = true ↔ (∀e : T)(e ∈ s ↔ e ∈ r) }
}
--}

mismosElementos :: (Eq t) => [t] -> [t] -> Bool
mismosElementos lista0 lista1 = esSubconjunto lista0 lista1 && esSubconjunto lista1 lista0

esSubconjunto :: (Eq t) => [t] -> [t] -> Bool
esSubconjunto [] _ = True
esSubconjunto (cabeza: cola) conjunto = pertenece cabeza conjunto && esSubconjunto cola conjunto

{--
capicua :: (Eq t) => [t] -> Bool seg ́un la siguiente especificaci ́on:
problema capicua (s: seq⟨T⟩) : B {
requiere: { T rue }
asegura: { resultado = true ↔ (∀i : Z)(0 ≤ i < ⌊s/2⌋ → s[i] = s[|s| − 1 − i]) }

}
--}

reverso :: [t] -> [t]
reverso [] = []
reverso (primero: lista) = reverso lista ++ [primero]

capicua :: (Eq t) => [t] -> Bool
capicua [] = True
capicua [elemento] = True
capicua (cabeza: cola) = cabeza == ultimo && capicua medio
    where
        ultimo = head (reverso cola)
        medio = reverso (tail (reverso cola))

