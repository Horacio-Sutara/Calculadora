#Metodo de integracion por trapecios
from raices.Ecuacion_procesar import Ecuacion_procesar

def trapecios(funcion, a, b, n):
    """
    Calcula la integral definida de una función utilizando el método del trapecio.

    :param funcion: Función a integrar.
    :param a: Límite inferior de integración.
    :param b: Límite superior de integración.
    :param n: Número de subintervalos.
    :return: Valor aproximado de la integral definida.
    """
    h = (b - a) / n  #incremento
    puntos=[ a + i * h for i in range(n + 1)]  #puntos de la integral
    ecuacion=Ecuacion_procesar(funcion)
    try:
        valor=ecuacion.resultado(puntos[0])  #evaluar el primer punto
        if valor is bool:
            return False
        resultado=h*((valor) + ecuacion.resultado(puntos[-1])) / 2  #suma de los extremos
    except Exception as e:
        #error al procesar la ecuación
        return False
    
    for i in range(1, n-1):  #suma de los puntos intermedios
        try :
            valor=ecuacion.resultado(puntos[i])  #evaluar el punto
            if valor is bool:
                return False
            resultado += h * valor
        except Exception as e:
            #error al procesar la ecuación
            return False
        
    return  resultado

if __name__ == "__main__":
    funcion = "x**2 + 2*x + 1"  # Ejemplo de función
    a = 0  # Límite inferior
    b = 10  # Límite superior
    n = 1000  # Número de subintervalos
    resultado = trapecios(funcion, a, b, n)
    print(f"Resultado de la integral: {resultado}")
