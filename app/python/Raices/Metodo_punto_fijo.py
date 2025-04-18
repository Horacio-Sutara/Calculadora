from . import Ecuacion_procesar
import numpy as np
class Metodo_punto_fijo():
    def __init__(self, funcion, error=1e-7, iteracion=50):
        self.ecuacion = Ecuacion_procesar.Ecuacion_procesar(funcion)
        self.texto = self.ecuacion.ecuacion
        self.error_maximo = error
        self.iteracion_maxima = iteracion

    def __funciones_en_y(self):
        ecuaciones = self.ecuacion.remplazar()
        ecuaciones_en_y = []
        for i in ecuaciones:
            soluciones = self.ecuacion.despejar_y(i)
            ecuaciones_en_y.extend(soluciones)
        return ecuaciones_en_y

    def buscar_raiz(self, a,b):
        x0=(a+b)/2
        soluciones = self.__funciones_en_y()
        for i in soluciones:
            res, valido = self.__calcular(i, x0)
            if valido:
                return res, True
        return 0, False

    def __calcular(self, g, x0):
        try:
            derivada = self.ecuacion.derivar(g)
            f_derivada = self.ecuacion.resultado(x0, derivada)

            if isinstance(f_derivada, bool) or abs(f_derivada) >= 1:
                return 0, False

            iteracion = 0
            error = 100.0
            x_ant = x0

            while error > self.error_maximo and iteracion < self.iteracion_maxima:
                x1 = self.ecuacion.resultado(x0, g)
                if isinstance(x1, bool):
                    return 0, False
                dif = abs(x1 - x_ant)
                if dif < self.error_maximo / 1000:
                    return 0, False
                x_ant = x0
                x0 = x1
                iteracion += 1
                error = abs(x0 - x_ant)

            if iteracion >= self.iteracion_maxima or error > self.error_maximo:
                return 0, False

            decimales = max(0, -int(round(np.log10(self.error_maximo))))
            return self.ecuacion.truncar_sympy(x0, decimales), True
        except:
            return 0, False

if __name__ == "__main__":
    text="x**2+10*cos(x)"
    ecuacion=Metodo_punto_fijo(text,iteracion=40)
    res=ecuacion.buscar_raiz(1,2)
    print(res)