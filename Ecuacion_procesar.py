from sympy import symbols, Eq, sympify, solve,diff, sin, cos, tan,exp, asin, acos, atan,log

class Ecuacion_procesar:
    def __init__(self,nombre_archivo="ecuacion.txt"):
        if nombre_archivo=="ecuacion.txt":
            self.nombre_archivo=nombre_archivo
            with open(self.nombre_archivo, "r") as archivo:
                contenido = archivo.read().strip()
            self.ecuacion=contenido
        else:
            self.ecuacion=nombre_archivo.replace("X","x")
    def remplazar(self,x='x',y='y',excluir_anterior='e'):
        ecuaciones=[]
        cont=0
        for i in self.ecuacion:
            save=self.ecuacion
            if i == x:
                if save[cont-1]!=excluir_anterior:            
                    save=save[:cont]+y+save[(cont+1):]
                    ecuaciones.append(save)
            cont+=1
        ecuaciones.append(self.ecuacion+f"+{x}-{y}")
        return ecuaciones

    def despejar_y(self,ecuacion_str):
        # Convertir la ecuación de string a expresión simbólica
        x, y = symbols('x y')
        ecuacion = sympify(ecuacion_str)
        
        # Intentar despejar y en función de x
        solucion_y = solve(ecuacion, y)

        if len(solucion_y) == 0:
            print("No se puede despejar y en función de x.")
        elif len(solucion_y) > 1:
            aux = solucion_y[0]
            solucion_y[0] = solucion_y[1]
            solucion_y[1] = aux


        return solucion_y

    def procesar_ecuacion(self, ecuacion_txt=None,valor_x=None):
        x = symbols('x')
        if ecuacion_txt is None:
            try:
                ecuacion = sympify(self.ecuacion, locals={'sin': sin, 'cos': cos, 'tan': tan,'exp': exp,'asin': asin, 'acos': acos, 'atan': atan,'log':log})  # Permite funciones trigonométricas
            except Exception as e:
                #print(f"Error al interpretar la ecuación: {e}")
                return False
        else:
            try:
                ecuacion = sympify(ecuacion_txt, locals={'sin': sin, 'cos': cos, 'tan': tan,'exp': exp,'asin': asin, 'acos': acos, 'atan': atan,'log':log})  # Permite funciones trigonométricas
            except Exception as e:
                #print(f"Error al interpretar la ecuación: {e}")
                return False

        if "=" in self.ecuacion:  # Si hay un "=", tratamos la ecuación como una igualdad
            izquierda, derecha = self.ecuacion.split("=")
            ecuacion = Eq(sympify(izquierda, locals={'sin': sin, 'cos': cos, 'tan': tan,'exp': exp}), 
                        sympify(derecha, locals={'sin': sin, 'cos': cos, 'tan': tan,'exp': exp}))
            solucion = solve(ecuacion, x)
            #print(f"Ecuación: {ecuacion}")
            #print(f"Solución para x: {solucion}")
            return "A"
        
        else:  # Si no hay "=", la tratamos como una función matemática
            if valor_x is not None:
                resultado = ecuacion.subs(x, valor_x).evalf()  # evalf() evalúa numéricamente
                #print(f"Ecuación reconocida: {ecuacion}\nEvaluada en x={valor_x}: {resultado}")
                return resultado
            return "B"
        
    def resultado(self,valor=None,ecuacion=None):
        if valor is None:
            valor=0
        if ecuacion is None:
            tipo=self.procesar_ecuacion()
            if tipo=="B":
                #print("La ecuación es una función matemática")
                return float(self.procesar_ecuacion(valor_x=valor))
        else:
            tipo=self.procesar_ecuacion(ecuacion)
            if tipo=="B":
                #print("La ecuación es una función matemática")
                return float(self.procesar_ecuacion(ecuacion,valor_x=valor))
        return -99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999

    def derivar(self,ecuacion=None):
        if ecuacion is None:
            ecuacion=self.ecuacion
        x = symbols('x')
        # Calcular la derivada
        if self.procesar_ecuacion()=="B":
            derivada = diff(ecuacion, x)
            #print( "Derivada: ",derivada)
            return derivada
        return None

    def __intervalo_correcto__(self,a,b):
        f_a=self.resultado(a)
        f_b=self.resultado(b)

        if f_a*f_b>0:
            return True
        else:
            return False
        
    def encontrar_intervalo(self,a,b):
        while self.__intervalo_correcto__(a,b):
            a-=0.5
            b+=0.5
        #print(f"intervalo inicial encontrado ({a},{b})")
        return a,b
    def reconocer(self):
        try:
            res=int(self.resultado(1,self.ecuacion))
            if res==-99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999:
                return False
            return True
        except Exception:
            return False
        
    def reescribir(self,ecuacion):
        self.ecuacion=ecuacion

if __name__ == "__main__":
    ecuacion = Ecuacion_procesar("x**2+x-5+exp(x)")
    #print(ecuacion.resultado(1))  # Puedes cambiar el valor de x según tus necesidades
    ecua=ecuacion.remplazar()
    print("Ecuaciones a despejar: ",ecua)
    for i in ecua:
        soluciones=ecuacion.despejar_y(i)
        for j in soluciones:
            print("Despeje: ",j)
            print("Para x= 1  : ",ecuacion.resultado(1,j),"\nPara x=10  : ",ecuacion.resultado(10,j),"\n")