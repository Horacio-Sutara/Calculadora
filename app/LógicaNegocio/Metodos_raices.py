import numpy as np
import sympy as sp
from Raices import Metodo_newton_raphson,Metodo_biseccion, Metodo_regula_falsi, Metodo_secante, Metodo_punto_fijo
class Metodos_raices:
    def __init__(self,expr_str, intervalo=(-10, 10), subintervalos=800, tol=1e-7):
        self.x = sp.symbols('x')
        self.expr = sp.sympify(expr_str, locals={'sin': sp.sin, 'cos': sp.cos, 'tan': sp.tan,
                                            'asin': sp.asin, 'acos': sp.acos, 'atan': sp.atan,
                                            'exp': sp.exp, 'ln': sp.ln})
        self.func = sp.lambdify(self.x, self.expr, modules=['numpy'])
        self.a, self.b = intervalo
        self.puntos = self.detectar_cambios_signo(self.func,self.a, self.b, subintervalos + 1)
        self.Metodos={ "Newton Raphson" : Metodo_newton_raphson.Metodo_Newton_Raphson(expr_str, error=tol,iteracciones=30).buscar_raiz
                ,"Secante": Metodo_secante.MetodoSecante(expr_str, error=tol,iteracciones=40).buscar_raiz
                ,"Regula Falsi" : Metodo_regula_falsi.Metodo_regula_falsi(expr_str, error=tol,iteraciones=50).buscar_raiz
                ,"Punto Fijo" : Metodo_punto_fijo.Metodo_punto_fijo(expr_str, error=tol,iteracion=50).buscar_raiz, 
                "Biseccion": Metodo_biseccion.Metodo_biseccion(expr_str, error_maximo=tol,iteraciones=50).buscar_raiz}
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
                    if xi<=raiz<=xi1:
                        self.raices.append([raiz,i])
                        break

        return list(sorted(self.raices))

if __name__ == "__main__":
    raices =Metodos_raices("cos(x)",intervalo=(-10,10),subintervalos=800,tol=1e-8).encontrar_raices()
    print("Raíces encontradas:")
    for r in raices:
        print(r[0], r[1])

