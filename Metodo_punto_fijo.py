import Ecuacion_procesar

class Metodo_punto_fijo:
    def __init__(self,x0,error,funcion=None,iteracion=30):
        if funcion is not None:
            self.ecuacion=Ecuacion_procesar.Ecuacion_procesar(funcion)
        else:
            self.ecuacion=Ecuacion_procesar.Ecuacion_procesar()
        self.texto=self.ecuacion.ecuacion
        self.error_maximo=error
        self.iteracion_maxima=iteracion
        self.x0=x0

    def __funciones_en_y(self):
        ecuaciones=self.ecuacion.remplazar()
        ecuaciones_en_y=[]
        for i in ecuaciones:
            soluciones=self.ecuacion.despejar_y(i)
            ecuaciones_en_y.append(soluciones)
        return ecuaciones_en_y
    
    def calcular(self):
        print("Metodo de punto fijo")
        soluciones=self.__funciones_en_y()
        for i in soluciones:
            for j in i:
                if self.__calcular(j):
                    pass
                
    def __calcular(self,ecuacion):
        derivada=self.ecuacion.derivar(ecuacion)
        f_derivada=self.ecuacion.resultado(self.x0,derivada)
        #print("Derivada: ",derivada," en x0: ",self.x0," = ",f_derivada)
        try:
            if -1>f_derivada or f_derivada>1:
                print("No se puede aplicar el metodo de punto fijo con la funcion despejada: ",ecuacion,"\n Su modulo debe ser menor a 1\n")
                return False
        except Exception as e:
            print("No se aplico el metodo para la funcion despejada: ",ecuacion,"\nEra imaginario el resultado de la derivada\n")
            return False        
        error=100.0
        iteracion=0
        x_ant=self.x0
        while error>self.error_maximo:
            x1=self.ecuacion.resultado(self.x0,ecuacion)
            dif=abs(x1-x_ant)
            if dif<self.error_maximo/1000:
                print("Ocila entre: ",x1," y ",self.x0)
                break
            x_ant=self.x0
            self.x0=x1
            iteracion+=1
            error=abs(self.x0-x_ant)
            if iteracion>self.iteracion_maxima:
                break
        print("Bucles: ",iteracion)
        if iteracion>self.iteracion_maxima or dif <self.error_maximo/1000:
            print("El metodo no converge con la funcion despejada: ",ecuacion,"\n")
            return False
        print("Resultado: ",self.x0, "\ncon la funcion despejada: ",ecuacion,"\n")
        return True
if __name__ == "__main__":
    ecuacion=Metodo_punto_fijo(x0=1.5,error=1e-4,iteracion=40)
    ecuacion.calcular()
