import Metodo_biseccion

class Metodo_regula_falsi():
    def __init__(self,a=0.1,b=1,error=0.001,ecuacion=None):
        self.error_maximo=error
        if ecuacion is None:
            self.ecuacion=Metodo_biseccion.Metodo_biseccion(a,b,50)
        else:
            self.ecuacion=Metodo_biseccion.Metodo_biseccion(a,b,50,ecuacion)
        self.a,self.b=self.ecuacion.calcular()
    def __comprobar_signo(self):
        derivada=self.ecuacion.ecuacion.derivar()
        derivada_segunda=self.ecuacion.ecuacion.derivar(derivada)
        derivada=self.ecuacion.ecuacion.procesar_ecuacion(derivada,self.a)
        derivada_segunda=self.ecuacion.ecuacion.procesar_ecuacion(derivada_segunda,self.a)
        #print(derivada,derivada_segunda)
        if derivada*derivada_segunda>0:
            print("Punto fijo B",self.a,self.b)
            return True
        else:
            print("Punto fijo A ", self.a,self.b)
            return False
    
    def calcular(self):
        ef=0
        f_ef=0
        error=100
        xn_1=0
        f_xn=0
        if self.__comprobar_signo():
            ef=self.b
            f_ef=self.ecuacion.ecuacion.procesar_ecuacion(valor_x=self.b)
            xn=self.a
            f_xn=self.ecuacion.ecuacion.procesar_ecuacion(valor_x=xn)
            #print("funcion B: ",f_ef)
        else:
            ef=self.a
            f_ef=self.ecuacion.ecuacion.procesar_ecuacion(valor_x=self.a)
            xn=self.b 
            f_xn=self.ecuacion.ecuacion.procesar_ecuacion(valor_x=xn)
            #print("funcion A ", f_ef)
        cont=0
        while (error>self.error_maximo):
            cont+=1
            if xn_1!=0:
                xn=xn_1
            f_xn=self.ecuacion.ecuacion.procesar_ecuacion(valor_x=xn) 
            xn_1=ef-((f_ef*(ef-xn))/(f_ef-f_xn))
            error=abs(xn_1-xn)

        print(f"Bucles: {cont} xn: ",xn, "xn+1= ",xn_1, "Resultado: ",(xn_1+xn)/2)

if __name__=="__main__":    
    ecuacion=Metodo_regula_falsi(a=1,b=2,error=1e-4)
    ecuacion.calcular()