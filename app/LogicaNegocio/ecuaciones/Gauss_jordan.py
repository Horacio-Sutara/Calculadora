import numpy as np

def GaussJordan(matriz):
    longitud = len(matriz)  # Cantidad de filas
    columnas = len(matriz[0])  # Cantidad total de columnas
    resultados = []
    exito = False

    for i in range(longitud):
        # Elemento de la diagonal principal
        pivote = matriz[i][i]
        print(f"Pivote inicial en ({i},{i}): {pivote}")
        band = True

        # Si el pivote es cero, buscar una fila más abajo para intercambiar
        if pivote == 0:
            band = False
            for j in range(i+1, longitud):
                if matriz[j][i] != 0:
                    matriz[[i, j]] = matriz[[j, i]]  # Intercambio de filas
                    pivote = matriz[i][i]
                    band = True
                    break
        if not band:
            print("No se puede resolver. El sistema tiene una fila sin pivote.")
            return resultados, exito

        # Normalizar la fila actual (hacer que el pivote valga 1)
        matriz[i] = matriz[i] / pivote
        print(f"Fila {i} normalizada: {matriz[i]}")

        # Hacer cero todos los elementos por encima y por debajo del pivote
        for j in range(longitud):
            if j != i:
                factor = matriz[j][i]
                print(f"factor {factor}")
                matriz[j] = matriz[j] - factor * matriz[i]
                print(f"Fila {j} actualizada con respecto a la fila {i}: {matriz[j]}")

    # Extraer los resultados que están en la última columna
    for i in range(longitud):
        resultados.append(round(matriz[i][-1], 7))

    exito = True
    print("Resultado final:", resultados)
    return resultados, exito


matriz = [
        [2, 1, -1, 8],
        [-3, -1, 2, -11],
        [-2, 1, 2, -3]
    ]
matriz = np.array(matriz, dtype=float)

result = GaussJordan(matriz)

print(result)

# if __name__ == '__main__':
#     # Ejemplo de prueba
#     matriz = [
#         [2, 1, -1, 8],
#         [-3, -1, 2, -11],
#         [-2, 1, 2, -3]
#     ]
#     matriz = np.array(matriz, dtype=float)
#     GaussJordan(matriz)
