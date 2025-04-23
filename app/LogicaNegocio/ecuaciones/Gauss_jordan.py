import numpy as np

def GaussJordan(matriz,constante,tol=None,max_iter=None):
    longitud = len(matriz)  # Cantidad de filas
    iteraciones=0
    resultados = []
    exito = False
    historial=[]
    matriz=matriz.copy()
    const=constante.copy()
    matriz = np.array(matriz, dtype=float)
    
    for i in range(longitud):
        # Elemento de la diagonal principal
        pivote = matriz[i][i]
        #print(f"Pivote inicial en ({i},{i}): {pivote}")
        band = True

        # Si el pivote es cero, buscar una fila más abajo para intercambiar
        if pivote == 0:
            band = False
            for j in range(i+1, longitud):
                if matriz[j][i] != 0:
                    matriz[[i, j]] = matriz[[j, i]]  # Intercambio de filas
                    const[i,j]=const[j,i]
                    pivote = matriz[i][i]
                    band = True
                    iteraciones+=1
                    historial.append(matriz.tolist())
                    break
        if not band:
            #print("No se puede resolver. El sistema tiene una fila sin pivote.")
            exito = False
            return resultados,iteraciones,historial, exito

        # Normalizar la fila actual (hacer que el pivote valga 1)
        matriz[i] = matriz[i] / pivote
        const[i]=const[i]/pivote
        historial.append(matriz.tolist())
        #print(f"Fila {i} normalizada: {matriz[i]}")

        # Hacer cero todos los elementos por encima y por debajo del pivote
        for j in range(longitud):
            if j != i:
                factor = matriz[j][i]
                #print(f"factor {factor}")
                #print(matriz,[float(const[k]) for k in range(longitud)]," antes")
                matriz[j] = matriz[j] - factor * matriz[i]
                const[j]=const[j]-factor*const[i]
                #print(matriz,[float(const[k]) for k in range(longitud)])
                historial.append(matriz.tolist())
                #print(f"Fila {j} actualizada con respecto a la fila {i}: {matriz[j]}")

    # Extraer los resultados que están en la última columna
    for i in range(longitud):
        const[i]=float(const[i])

    exito = True
    return const,iteraciones,historial, exito

if __name__=='__main__':
        
    """matriz = [
            [2, 1, -1, 8],
            [-3, -1, 2, -11],
            [-2, 1, 2, -3]
    ]"""
    matriz=[
        [1,2,5],
        [2,1,4]
    ]
    res=[5,4]
    result,iteraciones,historial,exito = GaussJordan(matriz,res)

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
