import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


import numpy as np
import sympy as sp
from raices import Metodo_newton_raphson
from raices import Metodo_biseccion
from raices import Metodo_regula_falsi
from raices import Metodo_secante
from raices import Metodo_punto_fijo

class Metodos_raices:
    def __init__(self,expr_str, intervalo=(-10, 10), subintervalos=None, tol=1e-7):
        if subintervalos is None:
            rango=abs(intervalo[1]-intervalo[0])
            subintervalos=int(rango/0.025)
        self.x = sp.symbols('x')
        self.expr = sp.sympify(expr_str, locals={'sin': sp.sin, 'cos': sp.cos, 'tan': sp.tan,
                                            'asin': sp.asin, 'acos': sp.acos, 'atan': sp.atan,
                                            'exp': sp.exp, 'ln': sp.ln})
        self.func = sp.lambdify(self.x, self.expr, modules=['numpy'])
        if expr_str=="exp(x)":
            intervalo=(-7,intervalo[1])
        self.a, self.b = intervalo 

        self.puntos = self.detectar_cambios_signo(self.func,self.a, self.b, subintervalos + 1)
        self.Metodos={ "Newton Raphson" : Metodo_newton_raphson.Metodo_Newton_Raphson(expr_str, error=1e-9,iteracciones=30).buscar_raiz
                ,"Secante": Metodo_secante.MetodoSecante(expr_str, error=tol*0.001,iteracciones=40).buscar_raiz
                ,"Regula Falsi" : Metodo_regula_falsi.Metodo_regula_falsi(expr_str, error=tol*0.001,iteraciones=50).buscar_raiz
                ,"Punto Fijo" : Metodo_punto_fijo.Metodo_punto_fijo(expr_str, error=tol*0.001,iteracion=50).buscar_raiz, 
                "Biseccion": Metodo_biseccion.Metodo_biseccion(expr_str, error_maximo=tol*0.001,iteraciones=50).buscar_raiz}
        self.raices = []
        
    def detectar_cambios_signo(self,f, a, b, num_subintervalos):
        """
        Divide [a,b] en subintervalos y detecta donde cambia el signo.
        Retorna lista de (xi, xi+1) donde hay posible raíz.
        """
        x_vals = np.linspace(a, b, num_subintervalos + 1)
        candidatos = []

        for i in range(len(x_vals) - 1):
            x0, x1 = x_vals[i], x_vals[i+1]
            try:
                if np.sign(f(x0)) != np.sign(f(x1)):
                    candidatos.append((x0, x1))
                elif abs(f(x1))<0.0005 and abs(f(x0))<0.0005:
                    candidatos.append((x0, x1))
            except:
                continue  # Evita problemas como división por 0
        return candidatos

    def encontrar_raices(self):
        for (xi,xi1) in self.puntos:
            #print("llego")
            #print("xi:", xi, "xi1:", xi1)
            for i in self.Metodos:
                raiz, encontrada = self.Metodos[i](xi,xi1)#metodos
                if encontrada:
                    # Verificar si ya está muy cerca de una raíz encontrada
                    #print("hola")
                    if float(xi)<=raiz<=float(xi1):
                        raiz=round(raiz,7)
                        if self.raices==[]:
                            print("Raiz encontrada:", raiz, "en el intervalo:", (xi, xi1), "con el metodo:", i)
                            self.raices.append([raiz,i])
                            break
                        elif raiz not in [r[0] for r in self.raices]:
                            print("Raiz encontradasa:", raiz, "en el intervalo:", (xi, xi1), "con el metodo:", i)
                            self.raices.append([raiz,i])
                            break

        return list(sorted(self.raices))

if __name__ == "__main__":
    raices =Metodos_raices("x**2",intervalo=(-10,10),subintervalos=800,tol=1e-8).encontrar_raices()
    print("Raíces encontradas:")
    for r in raices:
        print(r[0], r[1])

