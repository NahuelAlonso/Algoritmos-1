module Test where

import Test.HUnit
import Parcial

ejercicio1Test = runTestTT testSet1

testSet1 = test [
        "Primeros 11 " ~: cantidadNumerosAbundantes 1 11 ~?= 0,
        "Primeros 12 " ~: cantidadNumerosAbundantes 1 12 ~?= 1,
        "Sólo abundante " ~: cantidadNumerosAbundantes 12 12 ~?= 1,
        "Sólo no abundante " ~: cantidadNumerosAbundantes 11 11 ~?= 0,
        "Dado " ~: cantidadNumerosAbundantes 12 24 ~?= 4
    ]

