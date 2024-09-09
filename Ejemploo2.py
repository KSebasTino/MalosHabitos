def calcular(valormulti1, valormulti2, sumatoria):
    respuesta = valormulti1 * valormulti2 + sumatoria
    return respuesta

if __name__ == "__main__":
    valormulti1 = float(input('Valor de multiplicacion 1: '))
    valormulti2 = float(input('Valor de multiplicacion 2: '))
    sumatoria = float(input('valor de suma: '))
    respuesta = calcular(valormulti1, valormulti2, sumatoria)
    print(f"{valormulti1}*{valormulti2}+{sumatoria}={respuesta}")


