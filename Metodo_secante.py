import Ecuacion_procesar

class MetodoSecante:
    def __init__(self, x0,x1, error, ecuacion=None):
        if ecuacion is None:
            self.ecuacion = Ecuacion_procesar.Ecuacion_procesar()
        else:
            self.ecuacion = Ecuacion_procesar.Ecuacion_procesar(ecuacion)
        self.x0 = x0
        self.x1 = x1
        self.error_maximo = error

    def calcular(self):
        error=100
        cont=0
        while error>self.error_maximo:
            cont+=1
            xn_1 = self.x1 - (self.ecuacion.resultado(self.x1)*(self.x1-self.x0))/(self.ecuacion.resultado(self.x1)-self.ecuacion.resultado(self.x0))
            error=abs(xn_1-self.x1)
            self.x0=self.x1
            self.x1=xn_1
        print("Bucles: ",cont," Resultado: ",xn_1)
if __name__=="__main__":
    ecuacion=MetodoSecante(x0=1.1,x1=1.3,error=1e-4)
    ecuacion.calcular()