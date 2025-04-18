from . import Ecuacion_procesar
import numpy as np
class Metodo_Newton_Raphson:
    def __init__(self, ecuacion="ecuacion.txt", error=1e-7, iteracciones=100):
        self.ecuacion = Ecuacion_procesar.Ecuacion_procesar(ecuacion)
        self.derivada = self.ecuacion.derivar()
        self.derivada_segunda = self.ecuacion.derivar()
        self.error_max = error
        self.iteracciones = iteracciones

    def buscar_raiz(self, a,b):
        x0 = (a + b) / 2
        try:
            if self.ecuacion.resultado(x0, self.derivada) == 0:
                return 0, False
            if -1 < self.ecuacion.resultado(x0, self.derivada_segunda) < 1:
                return 0, False

            xn = x0
            error = 100
            iteracion = 0
            while error > self.error_max and iteracion < self.iteracciones:
                f_xn = self.ecuacion.resultado(xn)
                f_derivada = self.ecuacion.resultado(xn, self.derivada)

                if f_derivada == 0:
                    return 0, False

                xn_1 = xn - f_xn / f_derivada
                error = abs(xn_1 - xn)
                xn = xn_1
                iteracion += 1

            if iteracion >= self.iteracciones:
                return 0, False

            # Redondear según el nivel de tolerancia
            decimales = max(0, -int(round(np.log10(self.error_max))))
            return self.ecuacion.truncar_sympy(xn, decimales), True

        except Exception:
            return 0, False
if __name__ == "__main__":
    ecuacion=Metodo_Newton_Raphson("cos(x)*10+x**2",1e-7,100)
    res,valido=ecuacion.buscar_raiz(1,2)
    print(res)
