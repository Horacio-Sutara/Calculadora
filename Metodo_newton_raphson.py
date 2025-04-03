import Ecuacion_procesar

class Metodo_Newton_Raphson:
    def __init__(self,x0, error):
        self.ecuacion = Ecuacion_procesar.Ecuacion_procesar()
        self.derivada = self.ecuacion.derivar()
        self.derivada_segunda = self.ecuacion.derivar()
        self.x0 = x0
        self.error_max=error
    
    def calculo(self):
        error=100
        xn=self.x0
        cont=0
        if self.ecuacion.resultado(xn,self.derivada)==0:
            print("No se puede aplicar el metodo de Newton-Raphson")
            return None
        elif -1<self.ecuacion.resultado(xn,self.derivada_segunda)<1:
            xn+=0.1
        while error>self.error_max:
            cont+=1
            f_xn=self.ecuacion.resultado(xn)
            f_derivada=self.ecuacion.resultado(xn,self.derivada)
            xn_1=xn-(f_xn/f_derivada)
            error=abs(xn_1-xn)
            xn=xn_1

        print("Bucles: ",cont," Resultado: ",xn_1)
    
    def calculo_raices_multiples(self):
        error=100
        xn=self.x0
        cont=0
        if self.ecuacion.resultado(xn,self.derivada)==0:
            print("No se puede aplicar el metodo de Newton-Raphson para raices multiples")
            return None
        elif -1<self.ecuacion.resultado(xn,self.derivada_segunda)<1:
            xn+=0.1
        while error>self.error_max:
            cont+=1
            f_xn=self.ecuacion.resultado(xn)
            f_derivada=self.ecuacion.resultado(xn,self.derivada)
            f_derivada_segunda=self.ecuacion.resultado(xn,self.derivada_segunda)
            f_derivada_elevada=f_derivada**2
            xn_1=xn-(f_xn*f_derivada)/(f_derivada_elevada-f_xn*f_derivada_segunda)
            error=abs(xn_1-xn)
            xn=xn_1

        print("Bucles: ",cont," Resultado: ",xn_1)
if __name__ == "__main__":
    ecuacion=Metodo_Newton_Raphson(1.1,1e-4)
    ecuacion.calculo()
    ecuacion.calculo_raices_multiples()