from ecsdif.ecdif import FuncionXYProcesar

def rungekutta4(f, x0, y0, xn, n=100):
    ecuacion = FuncionXYProcesar(f)
    if not ecuacion.reconocer():
        raise ValueError("La función no es válida o contiene variables no permitidas.")
    if n <= 0:
        raise ValueError("El número de pasos n debe ser un entero positivo mayor que cero.")
    if x0 >= xn:
        raise ValueError("El valor inicial x0 debe ser menor que el valor final xn.")
    if y0 is None:
        raise ValueError("El valor inicial y0 no puede ser None.")
    if not isinstance(n, int):
        raise ValueError("El número de pasos n debe ser un entero.")
    
    puntos= [(x0, y0)]  # Lista para almacenar los puntos (x, y)
    h = (xn - x0) / n #Tamaño del paso
    if h <= 0:
        raise ValueError("El paso h debe ser positivo y mayor que cero.")
    
    while x0 < xn:
        k1 = h * ecuacion.resultado(x0, y0)
        k2 = h * ecuacion.resultado(x0 + h / 2, y0 + k1 / 2)
        k3 = h * ecuacion.resultado(x0 + h / 2, y0 + k2 / 2)
        k4 = h * ecuacion.resultado(x0 + h, y0 + k3)
        #print(f"Valores k1: {k1}, k2: {k2}, k3: {k3}, k4: {k4}")
        
        y0 += (k1 + 2 * k2 + 2 * k3 + k4) / 6
        y0 = round(y0, 10)
        x0 += h
        x0 = round(x0, 10)
        
        puntos.append((x0, y0))
    
    return puntos

if __name__ == "__main__":
    # Ejemplo de uso
    f = "x*sqrt(y)"  # Definir la función
    x0 = 1  # Valor inicial de x
    y0 = 4  # Valor inicial de y
    xn = 1.6  # Valor final de x
    n = 3  # Número de pasos

    resultado = rungekutta4(f, x0, y0, xn, n)
    print(resultado)  # Imprimir los puntos generados