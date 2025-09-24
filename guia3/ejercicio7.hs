{--
a) Implementar la funci´on:
distanciaManhattan:: (Float, Float, Float) -> (Float, Float, Float) -> Float
problema distanciaManhattan (p : R × R × R, q : R × R × R) : R {
requiere: {T rue}
asegura: {res =
P2
i=0 |pi − qi
|}
}
Por ejemplo:
distanciaManhattan (2, 3, 4) (7, 3, 8) ⇝ 9
distanciaManhattan ((-1), 0, (-8.5)) (3.3, 4, (-4)) ⇝ 12.8
b) Reimplementar la funci´on teniendo en cuenta el siguiente tipo: type Punto3D = (Float, Float, Float)
--}
absoluto :: Float -> Float
absoluto n | n<0 = -n
           | otherwise = n

distanciaManhattan:: (Float, Float, Float) -> (Float, Float, Float) -> Float
distanciaManhattan (x0, y0, z0) (x1, y1, z1) = absoluto (x0 - x1) + absoluto (y0 - y1) + absoluto (z0 - z1)

type Punto3D = (Float, Float, Float)

distanciaManhattan2:: Punto3D -> Punto3D -> Float
distanciaManhattan2 (x0, y0, z0) (x1, y1, z1) = absoluto (x0 - x1) + absoluto (y0 - y1) + absoluto (z0 - z1)