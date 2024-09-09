# Función para calcular el área de un rectángulo
def AreaRectangulo(alturarectangulo, baserectangulo):
    arearect = alturarectangulo * baserectangulo
    return arearect

# Función para calcular el área de un triángulo

def AreaTriangulo(basetriangulo, alturatriangulo):
    areatrian = 0.5 * basetriangulo * alturatriangulo
    return areatrian

# Función principal

if __name__ == "__main__":
    alturarectangulo = float(input('Altura del rectangulo: '))
    baserectangulo = float(input('Base del rectangulo: '))
    basetriangulo = float(input('Base del triangulo: '))
    alturatriangulo = float(input('Altura del triangulo: '))
    arearect = AreaRectangulo(alturarectangulo, baserectangulo)
    areatrian = AreaTriangulo(alturatriangulo, basetriangulo)
    print(f"{alturarectangulo} * {baserectangulo} = {arearect}")
    print(f"{0.5} * {basetriangulo} * {alturatriangulo} = {areatrian}")
