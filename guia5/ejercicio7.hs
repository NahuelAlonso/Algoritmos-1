type Identificacion = Integer
type Texto = [Char]
type Ubicacion = Texto
type Estado = (Disponibilidad, Ubicacion)
type Locker = (Identificacion, Estado)
type MapaDeLockers = [Locker]
type Disponibilidad = Bool

{--
Implementar existeElLocker :: Identificacion ->MapaDeLockers ->Bool, una funci´on para saber si un locker
existe en la facultad.
--}
existeElLocker :: Identificacion -> MapaDeLockers -> Bool
existeElLocker _ [] = False
existeElLocker id (cabeza : cola) | fst cabeza == id = True
                                  | otherwise = existeElLocker id cola
{--
Implementar ubicacionDelLocker :: Identificacion ->MapaDeLockers ->Ubicacion, una funci´on que dado un
locker que existe en la facultad, me dice la ubicaci´on del mismo.
--}

ubicacionDelLocker :: Identificacion -> MapaDeLockers -> Ubicacion--Me asegura que existe el locker
ubicacionDelLocker id (cabeza : cola) | fst cabeza == id = ubicacion
                                      | otherwise = ubicacionDelLocker id cola
    where ubicacion = snd (snd cabeza)

{--
Implementar estaDisponibleElLocker :: Identificacion ->MapaDeLockers ->Bool, una funci´on que dado un
locker que existe en la facultad, me devuelve Verdadero si esta libre.
--}

estaDisponibleElLocker :: Identificacion -> MapaDeLockers -> Bool--Me asegura que existe el locker
estaDisponibleElLocker id (cabeza : cola) | fst cabeza == id = disponibilidad
                                          | otherwise = estaDisponibleElLocker id cola
    where disponibilidad = fst (snd cabeza)

{--
Implementar ocuparLocker :: Identificacion ->MapaDeLockers ->MapaDeLockers, una funci´on que dado un loc-
ker que existe en la facultad, y est´a libre, lo ocupa
--}

ocuparLocker :: Identificacion ->MapaDeLockers ->MapaDeLockers
ocuparLocker id (cabeza : cola) | fst cabeza == id = (id, (False, ubicacion)) : cola
                                | otherwise = cabeza : ocuparLocker id cola

    where ubicacion = snd (snd cabeza)