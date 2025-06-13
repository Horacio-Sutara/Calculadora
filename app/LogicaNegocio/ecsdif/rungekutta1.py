from .ecdif import FuncionXYProcesar

def rungekutta1(f, x0, y0, xn, h=None, n=None):

    ecuacion = FuncionXYProcesar(f)
    if not ecuacion.reconocer():
        raise ValueError("La función no es válida o contiene variables no permitidas.")
    if x0 >= xn:
        raise ValueError("El valor inicial x0 debe ser menor que el valor final xn.")
    if y0 is None:
        raise ValueError("El valor inicial y0 no puede ser None.")
    if n:
        if not isinstance(n, int):
            raise ValueError("El número de pasos n debe ser un entero.")
        if n <= 0:
            raise ValueError("El número de pasos n debe ser un entero positivo mayor que cero.")
    if h is None and n is None:
        n = 100
    if h is None:
        h = (xn - x0) / n #Tamaño del paso
    if h <= 0:
        raise ValueError("El paso h debe ser positivo y mayor que cero.")
    points = [(x0, y0)]  # Lista para almacenar los puntos (x, y)
    while x0 < xn:
        y0 = y0 + h * ecuacion.resultado(x0, y0)
        y0 = round(y0, 10)
        x0 = x0 + h
        x0 = round(x0, 10)
        print(f"El valor de {x0} y el de h{h}")
        points.append((x0, y0))
    return points

if __name__ == "__main__":
    # Ejemplo de uso
    f = "1*x+2*x*y" # Definir la función
    x0 = 0.5  # Valor inicial de x
    y0 = 1  # Valor inicial de y
    xn = 1  # Valor final de x
    n = 5  # Número de pasos

    resultado = rungekutta1(f, x0, y0, xn, n)
    print(resultado)  # Imprimir los puntos generados