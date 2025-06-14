from ecsdif import rungekutta1, rungekutta4

def Metodos_edos(funcion, x0, y0, xn, n, h, modo, metodo):
    print("Datos recibidos para calcular la solución:")
    print(f"Función: {funcion}, x0: {x0}, y0: {y0}, xn: {xn}, n: {n}, h: {h}, modo: {modo}, metodo: {metodo}")

    if metodo == 'rk1':
        resultado = rungekutta1(funcion, x0, y0, xn, h, n)
    elif metodo == 'rk4':
        resultado = rungekutta4(f, x0, y0, xn, h, n)
    else:
        return {'error': 'Modo no reconocido.'}

    return {'resultado': resultado}