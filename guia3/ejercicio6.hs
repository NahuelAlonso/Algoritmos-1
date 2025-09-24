{--
    Ejercicio 6. Usando los siguientes tipos:
    type Anio = Integer
    type EsBisiesto = Bool
    Programar la funci´on bisiesto :: Anio -> EsBisiesto seg´un la siguiente especificaci´on:
    problema bisiesto (a˜no : Z) : Bool {
    requiere: {T rue}
    asegura: {(res = f alse) ↔ (a˜no no es m´ultiplo de 4, o bien, a˜no es m´ultiplo de 100 pero no de 400)}
    }
    Por ejemplo:
    bisiesto 1901 ⇝ False bisiesto 1904 ⇝ True
    bisiesto 1900 ⇝ False bisiesto 2000 ⇝ True
--}
type Anio = Integer
type EsBisiesto = Bool

bisiesto :: Anio -> EsBisiesto
bisiesto anio = not (mod anio 4 /= 0 || (mod anio 100 == 0 && mod anio 400 /= 0 )) 