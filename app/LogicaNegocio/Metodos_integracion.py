from integracion import trapecios,simpons_1_3

if __name__ == "__main__":
    funcion = "x**2 + 2*x + 1"  # Ejemplo de función
    a = 0  # Límite inferior
    b = 10  # Límite superior
    n = 1000  # Número de subintervalos
    resultado = trapecios.trapecios(funcion, a, b, n)
    print(f"Resultado de la integral: {resultado}")
    # resultado = simpons_1_3.simpson_1_3(funcion, a, b, n)
    resultado = simpons_1_3.simpson_1_3(funcion, a, b, n)
    print(f"Resultado de la integral: {resultado}")