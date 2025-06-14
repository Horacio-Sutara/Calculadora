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
    historial=[]
    try:
        valor=ecuacion.resultado(puntos[0])  #evaluar el primer punto
        valor_final=ecuacion.resultado(puntos[-1])  #evaluar el último punto
        band=False
        if len(puntos)>25:
            band=True
            salto=len(puntos)//25
        if valor is bool:
            return 0,False,[]
        if valor_final is bool:
            return 0,False,[]
        resultado=h*((valor)) / 2  #suma de los extremos
        
        historial.append([(puntos[0],valor),resultado])  #evaluar el primer punto tupla (x,y),resultado

        for i in range(1, n):  #suma de los puntos intermedios
            valor=ecuacion.resultado(puntos[i])  #evaluar el punto
            if valor is bool:
                return 0,False,[]
            resultado += h * valor

            if band is False:
                historial.append([(puntos[i],valor),resultado])
            else:
                if i%salto==0:
                    historial.append([(puntos[i],valor),resultado])
        resultado += valor_final*h/2  #sumar el último punto
        historial.append([(puntos[-1],valor_final),resultado])  #evaluar el último punto
    except Exception as e:
        #error al procesar la ecuación
        return 0,False,[]
        
    return  resultado,True,historial

if __name__ == "__main__":
    funcion = "x**2 + 2*x + 1"  # Ejemplo de función
    a = 0  # Límite inferior
    b = 10  # Límite superior
    n = 1000  # Número de subintervalos
    resultado = trapecios(funcion, a, b, n)
    print(f"Resultado de la integral: {resultado}")
