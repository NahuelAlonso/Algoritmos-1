{--
    Ejercicio 5. Implementar la funci´on todosMenores :: (Integer, Integer, Integer) -> Bool
    problema todosMenores (t : Z × Z × Z) : Bool {
    requiere: {T rue}
    asegura: {(res = true) ↔ ((f(t0) > g(t0)) ∧ (f(t1) > g(t1)) ∧ (f(t2) > g(t2)))}
    }
    problema f (n : Z) : Z {
    requiere: {T rue}
    asegura: {(n ≤ 7 → res = n
    2
    ) ∧ (n > 7 → res = 2n − 1)}
    }
    problema g (n : Z) : Z {
    requiere: {T rue}
    asegura: {Si n es un n´umero par entonces res = n/2, en caso contrario, res = 3n + 1}
    }
--}
f :: Integer -> Integer
f n
  | n <= 7 = n * n
  | otherwise = 2 * n - 1

g :: Integer -> Integer
g n
  | mod n 2 == 0 = div n 2
  | otherwise = 3 * n + 1

todosMenores :: (Integer, Integer, Integer) -> Bool
todosMenores (t0, t1, t2) = (f t0 > g t0) && (f t1 > g t1) && (f t2 > g t2)
