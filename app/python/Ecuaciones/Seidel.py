def gauss_seidel(A, b, x0=None, tol=1e-10, max_iter=1000):
    # A: matriz de coeficientes
    # b: vector de términos independientes
    # x0: vector inicial (opcional)
    # tol: tolerancia para la convergencia
    # max_iter: máximo de iteraciones
    n = len(A)
    
    # verificamos si la matriz A tiene ceros en la diagonal
    for i in range(n):
        if A[i][i] == 0:
            return 0,0,0,False
    
    resultado = x0 or [0.0 for _ in range(n)]
    historial = [(0, resultado.copy())]

    #print("Historial de iteraciones:")
    #rint(f"Iteración 0: {[round(v, 6) for v in x]}")

    for iteraciones in range(1, max_iter + 1):
        x_new = resultado.copy()
        for i in range(n):
            sum1 = sum(A[i][j] * x_new[j] for j in range(i))      # valores ya actualizados
            sum2 = sum(A[i][j] * resultado[j] for j in range(i + 1, n))    # valores sin actualizar
            x_new[i] = (b[i] - sum1 - sum2) / A[i][i]

        historial.append((iteraciones, x_new.copy()))
        #print(f"Iteración {k}: {[round(v, 6) for v in x_new]}")

        # Verificamos si ya convergió
        error = max(abs(x_new[i] - resultado[i]) for i in range(n))
        if error < tol:
            #print("\nSolución aproximada:")
            #for i, valor in enumerate(x_new):
                #print(f"x{i+1} ≈ {valor:.6f}")
            #print("Iteraciones:", k)
            return x_new, iteraciones, historial,True

        resultado = x_new

    #print("\nSolución aproximada (no convergió en el máximo de iteraciones):")
    
    #for i, valor in enumerate(resultado):
        #print(f"x{i+1} ≈ {valor:.6f}")
    #print("Iteraciones:", max_iter)
    return resultado, max_iter, historial,False

if __name__ == "__main__":
    # Ejemplo 

    """A = [
        [4, 1, 2],
        [3, 5, 1],
        [1, 1, 3]
    ]

    b = [4, 7, 3]"""

    A = [
        [2,1],
        [-1,2]
    ]

    b = [1,7]

    res,iteraciones,historial,convergió = gauss_seidel(A, b)
    if convergió:
        print(res)



    A = [
        [0, 1, 2],  # Fila 0: El elemento en la diagonal es 0
        [3, 5, 1],
        [1, 1, 3]
    ]

    b = [4, 7, 3]

    gauss_seidel(A, b)  