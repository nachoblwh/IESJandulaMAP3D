_ = False
floor_zero = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, _, _, _, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 5, _, _, _, _, _, 2, 1, 1, 1, _, _, _, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, _, 1, 1, 1, 1, _, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, _, 1, 1, 1, 1, _, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 7, _, _, _, _, _, _, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 15, 15, 1, _, 6, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 15, _, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, _, 16, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 13, _, 27, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, _, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 12, _, 12, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, _, 9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 20, _, 26, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, _, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 27, _, 19, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, _, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, _, 1, 1, 24, 24, 24, 1, 1, 22, 23, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 18, _, _, _, _, _, _, _, _, _, _, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, _, _, _, _, _, _, _, _, _, _, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, _, _, _, _, _, _, _, _, _, _, 2, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, _, _, _, _, _, _, _, _, _, _, 2, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, _, _, _, _, _, _, _, _, _, _, _, _, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, _, _, _, _, _, _, _, _, _, _, _, _, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 23, 22, 1, 17, 1, 24, 24, 24, _, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 24, _, 8, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 11, _, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, _, 14, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, _, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, _, 8, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 23, _, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 22, _, 10, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, _, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, _, 10, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 21, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

PRIMERODAM = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, 1, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, 1],
    [1, 1, 1, 1, 1, 1, 28, 1, 2, 1, 1]
]

#PRIMERODAMMOBILIARIO = [(7,4), (12,3)]

SEGUNDODAM = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, 1],
    [1, 1, 1, 1, 1, 1, 29, 1, 1]
]

SEGUNDOFPB = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, 1],
    [1, 1, 1, 1, 1, 1, 30, 1, 1]
]

PRIMEROFPB = [
    [1, 1, 1, 1, 1, 1, 1],
    [1, _, _, _, _, _, 1],
    [1, _, _, _, _, _, 1],
    [1, _, _, _, _, _, 1],
    [1, _, _, _, _, _, 1],
    [1, _, _, _, _, _, 1],
    [1, _, _, _, _, _, 1],
    [1, _, _, _, _, _, 1],
    [1, _, _, _, _, _, 1],
    [1, _, _, _, _, _, 1],
    [1, 31, 1, 1, 1, 1, 1]
]

BANIOS = [
    [1, 1, 1, 1, 1, 1, 1],
    [1, _, _, 2, _, _, 1],
    [1, 1, 1, 1, _, _, 1],
    [1, _, _, 2, _, _, 1],
    [1, 1, 1, 1, _, _, 1],
    [1, _, _, 2, _, _, 1],
    [1, 1, 1, 1, _, _, 1],
    [1, _, _, _, _, _, 1],
    [1, _, _, _, _, _, 1],
    [1, _, _, _, _, _, 1],
    [1, 1, 1, 1, 1, 32, 1]
]

BIBLIOTECA = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, 33, 33, 1, 1, 1, 1, 1, 1, 1, 34, 34, 1]
]

COCINA = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, _, _, _, _, _, _, 25, _, 1],
    [1, _, _, _, _, _, _, 25, _, 1],
    [1, _, _, _, _, _, _, 25, _, 1],
    [1, _, _, _, _, _, _, 25, _, 1],
    [1, _, _, _, _, _, _, 25, _, 1],
    [1, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, 1],
    [1, 1, 35, 1, 1, 1, 1, 1, 1, 1]
]

CONSERJERIA = [
    [1, 1, 1, 1, 1],
    [1, _, _, _, 1],
    [1, _, _, _, 1],
    [1, _, _, _, 1],
    [1, _, _, _, 1],
    [1, _, _, _, 1],
    [1, 36, 1, 1, 1]
]

DIRECCION = [
    [1, 1, 1, 1, 1],
    [1, _, _, _, 1],
    [1, _, _, _, 1],
    [1, _, _, _, 1],
    [1, _, _, _, 1],
    [1, _, _, _, 1],
    [1, _, _, _, 1],
    [1, _, _, _, 1],
    [1, _, _, _, 1],
    [1, _, _, _, 1],
    [1, 37, 1, 1, 1]
]


JEFATURA = [
    [1, 1, 1, 1, 1, 1, 1],
    [1, _, _, _, _, _, 1],
    [1, _, _, _, _, _, 1],
    [1, _, _, _, _, _, 1],
    [1, _, _, _, _, _, 1],
    [1, _, _, _, _, _, 1],
    [1, _, _, _, _, _, 1],
    [1, _, _, _, _, _, 1],
    [1, _, _, _, _, _, 1],
    [1, 38, 1, 1, 1, 1, 1]
]

LINCE = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, 39],
    [1, _, _, _, _, _, _, _, 39],
    [1, _, _, _, _, _, _, _, 39],
    [1, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1]
]

SALAPROFESORES = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, 40, 40, 1, 1, 1, 1, 1, 1, 1, 1, 41, 41, 1]
]

SALAVISITAS = [
    [1, 1, 1, 1, 1],
    [1, _, _, _, 1],
    [1, _, _, _, 1],
    [1, _, _, _, 1],
    [1, _, _, _, 1],
    [1, _, _, _, 1],
    [1, _, _, _, 1],
    [1, 1, 42, 1, 1]
]

SALONDEACTOS = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, 1, 43, 43, 1, 1, 1, 1, 2, 1, 1, 44, 44, 1, 1, 1, 1, 1]
]

SECRETARIA = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, 1],
    [1, _, _, 1, _, _, _, 1],
    [1, 45, 1, 1, 1, 1, 1, 1]
]

ORIENTACION = [
    [1, 1, 1, 1, 1],
    [1, _, _, _, 1],
    [1, _, _, _, 1],
    [1, _, _, _, 1],
    [1, _, _, _, 1],
    [1, _, _, _, 1],
    [1, _, _, _, 1],
    [1, _, _, _, 1],
    [1, _, _, _, 1],
    [1, _, _, _, 1],
    [1, 1, 1, 46, 1]
]

ALMACEN = [
    [1, 1, 1, 1],
    [1, _, _, 1],
    [1, _, _, 1],
    [1, _, _, 1],
    [1, _, _, 1],
    [1, _, _, 1],
    [1, _, _, 1],
    [1, _, _, 1],
    [1, _, _, 1],
    [1, _, _, 1],
    [1, 1, 47, 1]
]