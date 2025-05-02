import numpy as np

def gauss_seidel(A, b, x0=None, tol=1e-10, max_iter=1000):
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    n = len(A)

    # Verificación de tipo de sistema
    rango_A = np.linalg.matrix_rank(A)
    A_ampliada = np.column_stack((A, b))
    rango_ampliada = np.linalg.matrix_rank(A_ampliada)

    if rango_A < n:
        if rango_A == rango_ampliada:
            print("⚠️ Sistema con infinitas soluciones")
        else:
            print("❌ Sistema incompatible (sin solución)")
        return [], 0, [], False

    for i in range(n):
        if A[i][i] == 0:
            print("❌ Cero en la diagonal, no se puede aplicar Seidel directamente.")
            return [], 0, [], False

    resultado = x0 or [0.0 for _ in range(n)]
    historial = []  # Ahora es una lista vacía, como en Jacobi

    for iteraciones in range(1, max_iter + 1):
        x_new = resultado.copy()
        for i in range(n):
            sum1 = sum(A[i][j] * x_new[j] for j in range(i))
            sum2 = sum(A[i][j] * resultado[j] for j in range(i + 1, n))
            x_new[i] = (b[i] - sum1 - sum2) / A[i][i]

            historial.append(float(x_new[i]))  # Agregamos cada valor suelto al historial

        error = max(abs(x_new[i] - resultado[i]) for i in range(n))
        if error < tol:
            return [float(val) for val in x_new], iteraciones, historial, True

        resultado = x_new

    return [float(val) for val in resultado], max_iter, historial, False
