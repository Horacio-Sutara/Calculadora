import Ecuacion_procesar

class Metodo_Newton_Raphson:
    def __init__(self,x0, error,ecuacion="ecuacion.txt", iteracciones=100):
        self.ecuacion = Ecuacion_procesar.Ecuacion_procesar(ecuacion)
        self.derivada = self.ecuacion.derivar()
        self.derivada_segunda = self.ecuacion.derivar()
        self.x0 = x0
        self.error_max=error
        self.iteracciones=iteracciones
    
    def calculo(self):
        error=100
        xn=self.x0
        cont=0
        if self.ecuacion.resultado(xn,self.derivada)==0:
            print("No se puede aplicar el metodo de Newton-Raphson")
            return 0, False
        elif -1<self.ecuacion.resultado(xn,self.derivada_segunda)<1:
            print("No se puede aplicar el metodo de Newton-Raphson")
            return 0, False
        while error>self.error_max:
            if cont>self.iteracciones:
                print("Se ha alcanzado el numero maximo de iteraciones")
                return 0, False
            if -1<self.ecuacion.resultado(xn,self.derivada_segunda)<1:
                print("No se puede aplicar el metodo de Newton-Raphson")
                return 0, False
            cont+=1
            f_xn=self.ecuacion.resultado(xn)
            f_derivada=self.ecuacion.resultado(xn,self.derivada)
            xn_1=xn-(f_xn/f_derivada)
            error=abs(xn_1-xn)
            #print("error: ", error, "\tf_xn ",f_xn, "\tderivada",self.derivada,"\tf_derivada ",f_derivada, "\txn_1 ",xn_1,"\txn ",xn)# Buscar error
            xn=xn_1
        #print("Bucles: ",cont," Resultado: ",xn_1)
        error=self.error_max
        while error<1:
            error*=10
            cont+=1
            #print("error: ", error, "\tcont: ",cont)
        return self.ecuacion.truncar_sympy(xn_1,cont),True
    
    def calculo_raices_multiples(self):
        error=100
        xn=self.x0
        cont=0
        if self.ecuacion.resultado(xn,self.derivada)==0:
            print("No se puede aplicar el metodo de Newton-Raphson para raices multiples")
            return 0, False
        if -1<self.ecuacion.resultado(xn,self.derivada_segunda)<1:
                print("No se puede aplicar el metodo de Newton-Raphson")
                return 0, False
        while error>self.error_max:
            if cont>self.iteracciones:
                print("Se ha alcanzado el numero maximo de iteraciones ")
                return 0, False
            if -1<self.ecuacion.resultado(xn,self.derivada_segunda)<1:
                print("No se puede aplicar el metodo de Newton-Raphson")
                return 0, False
            cont+=1
            f_xn=self.ecuacion.resultado(xn)
            f_derivada=self.ecuacion.resultado(xn,self.derivada)
            f_derivada_segunda=self.ecuacion.resultado(xn,self.derivada_segunda)
            f_derivada_elevada=f_derivada**2
            xn_1=xn-(f_xn*f_derivada)/(f_derivada_elevada-f_xn*f_derivada_segunda)
            error=abs(xn_1-xn)
            xn=xn_1

        #print("Bucles: ",cont," Resultado: ",xn_1)
        cont=0
        error=self.error_max
        while error<1:
            error*=10
            cont+=1
            #print("error: ", error, "\tcont: ",cont)
        return self.ecuacion.truncar_sympy(xn_1,cont),True
if __name__ == "__main__":
    ecuacion=Metodo_Newton_Raphson(-0.4,1e-7)
    res,valido=ecuacion.calculo()
    ecuacion.calculo_raices_multiples()
