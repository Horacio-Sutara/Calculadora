import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import numpy as np
import sympy as sp

from raices import (
    Metodo_newton_raphson,
    Metodo_biseccion,
    Metodo_regula_falsi,
    Metodo_secante,
    Metodo_punto_fijo
)

class Metodos_raices:
    def __init__(self, expr_str, intervalo=(-10, 10), subintervalos=None, tol=1e-7):
        self.x = sp.symbols('x')
        self.expr = sp.sympify(expr_str, locals={
            'sin': sp.sin, 'cos': sp.cos, 'tan': sp.tan,
            'asin': sp.asin, 'acos': sp.acos, 'atan': sp.atan,
            'exp': sp.exp, 'ln': sp.ln
        })
        self.func = sp.lambdify(self.x, self.expr, modules=['numpy'])

        self.a, self.b = intervalo
        if subintervalos is None:
            subintervalos = int(abs(self.b - self.a) / 0.025)

        self.puntos = self._detectar_cambios_signo(self.func, self.a, self.b, subintervalos + 1)

        self.metodos = {
            "Newton Raphson": Metodo_newton_raphson.Metodo_Newton_Raphson(expr_str, error=1e-9, iteracciones=30).buscar_raiz,
            "Secante": Metodo_secante.MetodoSecante(expr_str, error=tol * 0.001, iteracciones=40).buscar_raiz,
            "Regula Falsi": Metodo_regula_falsi.Metodo_regula_falsi(expr_str, error=tol * 0.001, iteraciones=50).buscar_raiz,
            "Punto Fijo": Metodo_punto_fijo.Metodo_punto_fijo(expr_str, error=tol * 0.001, iteracion=50).buscar_raiz,
            "Biseccion": Metodo_biseccion.Metodo_biseccion(expr_str, error_maximo=tol * 0.001, iteraciones=50).buscar_raiz
        }

        self.raices = []

    def _detectar_cambios_signo(self, f, a, b, num_subintervalos):
        x_vals = np.linspace(a, b, num_subintervalos)
        candidatos = []
        ant = 10
        ant_x0 = ant_x1 = 0
        band = mantener = False

        for i in range(len(x_vals) - 1):
            x0, x1 = x_vals[i], x_vals[i + 1]
            try:
                f_x0, f_x1 = f(x0), f(x1)
                actual = (abs(f_x0) + abs(f_x1)) / 2

                if np.sign(f_x0) != np.sign(f_x1):
                    candidatos.append((x0, x1))
                elif actual < ant and actual < 1e-3:
                    ant, ant_x0, ant_x1 = actual, x0, x1
                    band = True
                elif actual > ant and band:
                    candidatos.append((ant_x0, ant_x1))
                    band = mantener = False
                    ant = actual
                elif actual > 1 and not mantener:
                    ant, ant_x0, ant_x1 = actual, x0, x1
                    mantener = True

            except Exception:
                continue  # Evita errores como división por cero

        if band:
            candidatos.append((ant_x0, ant_x1))

        return candidatos

    def encontrar_raices(self):
        for xi, xi1 in self.puntos:
            for metodo_nombre, metodo in self.metodos.items():
                raiz, encontrada = metodo(xi, xi1)
                if encontrada and xi <= raiz <= xi1:
                    raiz_redondeada = round(raiz, 7)
                    if all(abs(raiz_redondeada - r[0]) > 1e-7 for r in self.raices):
                        self.raices.append([raiz_redondeada, metodo_nombre])
                        break
        return sorted(self.raices)

if __name__ == "__main__":
    raices = Metodos_raices("x**2", intervalo=(-10, 10), subintervalos=800, tol=1e-8).encontrar_raices()
    for r in raices:
        print(r[0], r[1])


