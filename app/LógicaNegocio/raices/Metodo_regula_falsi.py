from .Ecuacion_procesar import Ecuacion_procesar
import numpy as np
class Metodo_regula_falsi():
    def __init__(self,ecuacion,error=0.001, iteraciones=50):
        self.error_maximo=error
        self.iteracciones=iteraciones
        self.ecuacion=Ecuacion_procesar(ecuacion)
        self.derivada=self.ecuacion.derivar()
        self.derivada_segunda=self.ecuacion.derivar(self.derivada)

    def __comprobar_signo(self,x):
        return self.ecuacion.procesar_ecuacion(self.derivada, x) * self.ecuacion.procesar_ecuacion(self.derivada_segunda, x) > 0
    
    def buscar_raiz(self,a, b):
        # Determinar extremo fijo
        if self.__comprobar_signo( a):
            ef = b
            mov = a
        else:
            ef = a
            mov = b

        f_ef = self.ecuacion.procesar_ecuacion(valor_x=ef)
        error = float("inf")
        cont = 0

        while error > self.error_maximo and cont < self.iteracciones:
            f_mov = self.ecuacion.procesar_ecuacion(valor_x=mov)
            denominador = f_ef - f_mov
            if denominador == 0:
                return 0, False

            xn = ef - (f_ef * (ef - mov)) / denominador
            error = abs(xn - mov)
            mov = xn
            cont += 1

        if cont >= self.iteracciones:
            return 0, False

        decimales = max(0, -int(np.floor(np.log10(self.error_maximo))))
        return self.ecuacion.truncar_sympy(mov, decimales), True
if __name__=="__main__":    
    ecuacion=Metodo_regula_falsi("10*cos(x)+x**2",error=1e-7)
    res=ecuacion.buscar_raiz(1,2)
    print(res)