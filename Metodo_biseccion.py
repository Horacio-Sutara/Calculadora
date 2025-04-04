import Ecuacion_procesar


#ecuacion=Ecuacion_procesar.Ecuacion_procesar()
#print(ecuacion.procesar_ecuacion(2))

class Metodo_biseccion():
    def __init__(self,a=0.1,b=1,error_maximo=1,ecuacion=None,iteraciones=100):
        if ecuacion is None:
            self.ecuacion=Ecuacion_procesar.Ecuacion_procesar()
        else:
            self.ecuacion=Ecuacion_procesar.Ecuacion_procesar(ecuacion)
        self.a=a
        self.b=b
        self.xr_anterior=0
        self.xr=0
        self.umbral_error=error_maximo
        self.iteraciones=iteraciones

    def calcular(self):
        #print("!!METODO BISECCION¡¡")
        a=self.a
        b=self.b
        self.a,self.b=self.ecuacion.encontrar_intervalo(a,b)
        cont=0
        error=100
        while error>self.umbral_error:
            if cont>self.iteraciones:
                print("Se ha excedido el numero de iteraciones")
                return self.a,self.b,False
            cont+=1
            self.xr_anterior=self.xr
            self.xr=(self.a+self.b)/2
            #print("Valor de xr actual ",self.xr )
            if cont>1:
                error=abs(self.xr-self.xr_anterior)
            

            f_xr=self.ecuacion.resultado(valor=self.xr)
            f_a=self.ecuacion.resultado(valor=self.a)
            #print("producto: ",f_a*f_xr)
            if f_a*f_xr>0.00000000000000000000000001:
                self.a=self.xr
            else:
                self.b=self.xr
            
            #print(f" ciclo: {cont}, a={self.a}, b={self.b}, error={error}, xr={self.xr}, xr anterior={self.xr_anterior}, f(xr)={f_xr}, f(a)={f_a}")
        self.xr=(self.a+self.b)/2
        print(f"El punto debera estar comprendido entre los valores {self.a,self.b} , valor esperado: {self.xr}\n Con un error del {error} , Numero de intentos realizados {cont}")
        return self.a,self.b,True
if __name__=="__main__":
    ecuacion=Metodo_biseccion(a=0.8,b=1.2,error_maximo=1e-7,iteraciones=40)
    ecuacion.calcular()
    print(type(ecuacion.calcular()))
