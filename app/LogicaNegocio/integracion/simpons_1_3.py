#metodo de integracion por simpson 1/3
from raices.Ecuacion_procesar import Ecuacion_procesar

def simpson_1_3(funcion, a, b, n):
    """
    Calcula la integral definida de una función utilizando el método de Simpson 1/3.

    :param funcion: Función a integrar.
    :param a: Límite inferior de integración.
    :param b: Límite superior de integración.
    :param n: Número de subintervalos (debe ser par).
    :return: Valor aproximado de la integral definida.
    """
    h = (b - a) / n  #incremento
    puntos=[ a + i * h for i in range(n + 1)]  #puntos de la integral
    ecuacion=Ecuacion_procesar(funcion)
    try:
        valor = ecuacion.resultado(puntos[0])  #evaluar el primer punto
        valor2 = ecuacion.resultado(puntos[-1])  #evaluar el segundo punto
        if valor is bool or valor2 is bool:
            return False
        resultado = h * (valor + valor2) / 3  #suma de los extremos
    except Exception as e:
        #error al procesar la ecuación
        return False
    
    for i in range(1,n,2):
        valor = ecuacion.resultado(puntos[i])
        valor2 = ecuacion.resultado(puntos[i + 1])
        if valor is bool or valor2 is bool:
            return False
        resultado += 4 * h * valor/ 3  #suma de los puntos impares
        resultado += 2 * h * valor2 / 3  #suma de los puntos pares
    return resultado
