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
    historial=[]
    try:
        valor = ecuacion.resultado(puntos[0])  #evaluar el primer punto

        valor_final = ecuacion.resultado(puntos[-1])  #evaluar el segundo punto
        if valor is bool or valor_final is bool:
            return 0,False,[]

        resultado = h * (valor) / 3  #suma de los extremos
        band=False
        if len(puntos)>25:
            band=True
            salto=len(puntos)//25
        historial.append([(puntos[0],valor),resultado])  #evaluar el primer punto


    except Exception as e:
        #error al procesar la ecuación
        return 0,False,[]
    for i in range(1,n,2):
        valor = ecuacion.resultado(puntos[i])
        valor2 = ecuacion.resultado(puntos[i + 1])
        if valor is bool or valor2 is bool:
            return 0,False,[]
        resultado += 4 * h * valor/ 3  #suma de los puntos impares
        if i+1 < n:
            resultado += 2 * h * valor2 / 3  #suma de los puntos pares
            if band is False:
                historial.append([(puntos[i+1],valor2),resultado])
            else:
                if (i+1) % salto == 0:
                    historial.append([(puntos[i+1],valor2),resultado])
        else:
            resultado += h * valor_final / 3
            historial.append([(puntos[i+1],valor_final),resultado])
    
    #print(historial)
    
    return resultado,True,historial
