from Ecuacion_procesar import Ecuacion_procesar
import numpy as np

#ecuacion=Ecuacion_procesar.Ecuacion_procesar()
#print(ecuacion.procesar_ecuacion(2))

class Metodo_biseccion():
    def __init__(self,ecuacion,error_maximo=1,iteraciones=100):
        self.ecuacion=Ecuacion_procesar(ecuacion)
        self.umbral_error=error_maximo
        self.iteraciones=iteraciones

    def buscar_raiz(self,a,b):
        #print("!!METODO BISECCION¡¡")
        cont=0
        xr=(a+b)/2
        while cont<self.iteraciones:
            cont+=1
            f_xr=self.ecuacion.resultado(valor=xr)
            if abs(f_xr)<self.umbral_error or abs((a-xr))/2<self.umbral_error:
                decimales = max(0, -int(round(np.log10(self.umbral_error))))
                return self.ecuacion.truncar_sympy(xr,decimales),True
            f_a=self.ecuacion.resultado(valor=a)
            if f_a*f_xr>self.umbral_error*0.00001:
                a=xr
                xr=b
            else:
                b=xr
            #print("cont :",abs(f_xr))
            xr=(a+xr)/2
            
        if cont==self.iteraciones:
            return 0,False
if __name__=="__main__":
    ecuacion=Metodo_biseccion("cos(x)*10+x**2",error_maximo=1e-7,iteraciones=100)
    res=ecuacion.buscar_raiz(1.5,2)
    print(res)