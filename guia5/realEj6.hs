type Texto = [Char]
type Nombre = Texto
type Telefono = Texto
type Contacto = (Nombre, Telefono)
type ContactosTel = [Contacto]

{--
Implementar una funci´on que me diga si una persona aparece en mi lista de contactos del tel´efono: enLosContactos ::
Nombre -> ContactosTel -> Bool
--}
enLosContactos :: Nombre -> ContactosTel -> Bool
enLosContactos _ [] = False
enLosContactos nombre (cabeza : cola) | nombre == fst cabeza = True
                                      | otherwise = enLosContactos nombre cola

{--
Implementar una funci´on que agregue una nueva persona a mis contactos, si esa persona est´a ya en mis contactos entonces
actualiza el tel´efono. agregarContacto :: Contacto -> ContactosTel -> ContactosTel
--}
agregarContacto :: Contacto -> ContactosTel -> ContactosTel
agregarContacto contacto listaContactos | enLosContactos (fst contacto) listaContactos = modificarNumero contacto listaContactos
                                        | otherwise = contacto : listaContactos

modificarNumero :: Contacto -> ContactosTel -> ContactosTel
modificarNumero (nombre, numero) (cabeza : cola) | fst cabeza == nombre = (nombre, numero) : cola
                                                 | otherwise = cabeza : modificarNumero (nombre, numero) cola
{--
Implementar una funci´on que dado un nombre, elimine un contacto de mis contactos. Si esa persona no est´a no hace
nada. eliminarContacto :: Nombre -> ContactosTel -> ContactosTel
--}

eliminarContacto :: Nombre -> ContactosTel -> ContactosTel
eliminarContacto _ [] = []
eliminarContacto nombre (cabeza : cola) | fst cabeza == nombre = cola
                                        | otherwise = cabeza : eliminarContacto nombre cola

