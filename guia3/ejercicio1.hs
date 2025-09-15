f:: Int -> Int --problema f (n : Z) : Z {
                -- requiere: {n = 1 ∨ n = 4 ∨ n = 16}
                -- asegura: {(n = 1 → res = 8) ∧ (n = 4 → res = 131) ∧ (n = 16 → res = 16)}
                -- }
f 1 = 8
f 4 = 131
f 16 = 16

g:: Int -> Int --g(8) = 16
                -- g(16) = 4
                -- g(131) = 1


g 8 = 16
g 16 = 4
g 131 = 1

--c) A partir de las funciones definidas en los ´ıtems a) y b), implementar las funciones parciales h = f ◦ g y k = g ◦ f

h:: Int -> Int
h x = f (g x)

k:: Int -> Int
k x = g (f x)