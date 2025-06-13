from integracion import trapecios,simpson_1_3,simpson_3_8

def calcular_integral(funcion,metodo, a, b, n):
    metodos={
        "Trapecios": trapecios.trapecios,
        "Simpson 1/3": simpson_1_3.simpson_1_3,
        "Simpson 3/8": simpson_3_8.simpson_3_8
    }
    if metodo not in metodos:
        print("No existe ese metodo")
        return None, None, None, None,False
    resultado,funciono = metodos[metodo](funcion, a, b, n)
    return resultado,metodo, a, b, n, funciono

if __name__ == "__main__":
    funcion = "x**2 + 2*x + 1"  # Ejemplo de función
    a = 0  # Límite inferior
    b = 10  # Límite superior
    n = 1200  # Número de subintervalos
    resultado,metodo,a,b,n,funciona = calcular_integral(funcion, "Simpson 3/8", a, b, n)
    print(f"Resultado de la integral: {resultado}")