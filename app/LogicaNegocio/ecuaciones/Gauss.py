import numpy as np

def Gauss(matriz, constante, tol=None, max_iter=None):
    constante = np.array(constante, dtype=float)
    matriz = np.array(matriz, dtype=float)
    longitud = len(matriz)
    resultados = []
    historial = []
    iteraciones = 0
    exito = False

    # Eliminación hacia adelante (triangulación)
    for i in range(longitud):
        if matriz[i][i] == 0:
            # Evitar división por cero
            for k in range(i+1, longitud):
                if matriz[k][i] != 0:
                    matriz[[i, k]] = matriz[[k, i]]
                    constante[[i, k]] = constante[[k, i]]
                    break

        for j in range(i+1, longitud):
            if matriz[i][i] == 0:
                continue  # saltar si sigue siendo 0
            multiplicador = -matriz[j][i] / matriz[i][i]
            matriz[j] += multiplicador * matriz[i]
            constante[j] += multiplicador * constante[i]
            iteraciones += 1
            historial.append(matriz.copy().tolist())

    # Verificar si el sistema es compatible determinado
    rango_matriz = np.linalg.matrix_rank(matriz)
    matriz_ampliada = np.column_stack((matriz, constante))
    rango_ampliada = np.linalg.matrix_rank(matriz_ampliada)

    if rango_matriz < longitud:
        if rango_matriz == rango_ampliada:
            print("⚠️ Sistema con infinitas soluciones")
        else:
            print("❌ Sistema incompatible (sin solución)")
        return resultados, iteraciones, historial, exito  # exito sigue en False

    # Sustitución hacia atrás
    resultados = np.zeros(longitud)
    for i in range(longitud - 1, -1, -1):
        suma = sum(matriz[i][j] * resultados[j] for j in range(i + 1, longitud))
        resultados[i] = (constante[i] - suma) / matriz[i][i]
        iteraciones += 1
        historial.append(matriz.copy().tolist())

    exito = True
    return resultados.tolist(), iteraciones, historial, exito


# 🚀 Ejemplo para probar
if __name__ == '__main__':
    matriz = [
        [1, 1],
        [1, 1]
    ]
    constante = [3, 3]

    resultados, iteraciones, historial, funciono = Gauss(matriz, constante)
    print("Resultado:", resultados)
    print("Iteraciones:", iteraciones)
    print("Historial de matrices:", historial)
    print("Función terminó con éxito:", funciono)



