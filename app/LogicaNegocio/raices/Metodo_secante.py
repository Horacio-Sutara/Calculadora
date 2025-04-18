from . import Ecuacion_procesar
import numpy as np

class MetodoSecante:
    def __init__(self, ecuacion, error=1e-7, iteracciones=50):
        self.ecuacion = Ecuacion_procesar.Ecuacion_procesar(ecuacion)
        self.error_maximo = error
        self.iteracciones = iteracciones

    def buscar_raiz(self, x0, x1):
        try:
            error = 100
            cont = 0
            while error > self.error_maximo and cont < self.iteracciones:
                f_x0 = self.ecuacion.resultado(x0)
                f_x1 = self.ecuacion.resultado(x1)

                denominador = f_x1 - f_x0
                if denominador == 0:
                    return 0, False

                xn_1 = x1 - (f_x1 * (x1 - x0)) / denominador
                error = abs(xn_1 - x1)

                x0, x1 = x1, xn_1
                cont += 1

            if cont >= self.iteracciones:
                return 0, False

            # Redondear según tolerancia
            decimales = max(0, -int(round(np.log10(self.error_maximo))))
            return self.ecuacion.truncar_sympy(xn_1, decimales), True

        except Exception:
            return 0, False

if __name__=="__main__":
    ecuacion=MetodoSecante("x**2-2",error=1e-7)
    res,band=ecuacion.buscar_raiz(x0=1,x1=2)
    print(res)