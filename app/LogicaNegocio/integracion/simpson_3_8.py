#metodo de integracion por simpson 3/8
from raices.Ecuacion_procesar import Ecuacion_procesar

def simpson_3_8(funcion, a, b, n):
    """
    Calcula la integral definida de una función utilizando el método de Simpson 3/8.

    :param funcion: Función a integrar.
    :param a: Límite inferior de integración.
    :param b: Límite superior de integración.
    :param n: Número de subintervalos (debe ser múltiplo de 3).
    :return: Valor aproximado de la integral definida.
    """
    h = (b - a) / n  # incremento
    puntos = [a + i * h for i in range(n + 1)]  # puntos de la integral
    ecuacion = Ecuacion_procesar(funcion)
    historial = []
    try:
        valor = ecuacion.resultado(puntos[0])  # evaluar el primer punto
        valor_final = ecuacion.resultado(puntos[-1])  # evaluar el último punto
        if valor is bool or valor_final is bool:
            return 0,False,[]
        resultado = h * (valor) * 3 / 8  # suma de los extremos
        historial.append([(puntos[0], valor), resultado])  # evaluar el primer punto
        band = False
        if len(puntos) > 25:
            band = True
            salto = len(puntos) // 25
    except Exception as e:
        # error al procesar la ecuación
        return 0,False,[]

    for i in range(1,n,3):
        valor=ecuacion.resultado(puntos[i])  # evaluar el punto impar
        valor2 = ecuacion.resultado(puntos[i + 1])
        valor3 = ecuacion.resultado(puntos[i + 2])
        if valor is bool or valor2 is bool or valor3 is bool:
            return 0,False,[]
        resultado += 9 * h * (valor + valor2) / 8
        if i + 2 < n:
            resultado += 3 * h * valor3 / 4
        else:
            resultado+= h * valor_final * 3 / 8
            
        if band is False:
            historial.append([(puntos[i+2], valor3), resultado])
        else:
            if (i + 2) % salto == 0:
                historial.append([(puntos[i+2], valor3), resultado])
    return resultado,True,historial