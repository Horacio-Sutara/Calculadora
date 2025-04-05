import Ecuacion_procesar

class MetodoSecante:
    def __init__(self, x0,x1, error, ecuacion=None, iteracciones=50):
        if ecuacion is None:
            self.ecuacion = Ecuacion_procesar.Ecuacion_procesar()
        else:
            self.ecuacion = Ecuacion_procesar.Ecuacion_procesar(ecuacion)
        self.x0 = x0
        self.x1 = x1
        self.error_maximo = error
        self.iteracciones=iteracciones

    def calcular(self):
        error=100
        cont=0
        while error>self.error_maximo:
            if cont>self.iteracciones:
                print("No se puede resolver")
                return 0,False
            cont+=1
            try:
                xn_1 = self.x1 - (self.ecuacion.resultado(self.x1)*(self.x1-self.x0))/(self.ecuacion.resultado(self.x1)-self.ecuacion.resultado(self.x0))
            except:
                print("Division por cero")
                return 0,False
            error=abs(xn_1-self.x1)
            self.x0=self.x1
            self.x1=xn_1
        #print("Bucles: ",cont," Resultado: ",xn_1)
        error=self.error_maximo
        cont=0
        while error<1:
            error*=10
            cont+=1
        return self.ecuacion.truncar_sympy(xn_1,cont),True
if __name__=="__main__":
    ecuacion=MetodoSecante(x0=-2,x1=-1.5,error=1e-7)
    ecuacion.calcular()