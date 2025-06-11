from sympy import symbols, sympify, Function, sin, cos, tan, exp, log, asin, acos, atan
from sympy.parsing.sympy_parser import parse_expr
from sympy.utilities.lambdify import lambdify
from sympy.core.sympify import SympifyError

class FuncionXYProcesar:
    def __init__(self, funcion_str):
        self.funcion_str = funcion_str.replace("X", "x").replace("Y", "y")
        self.x, self.y = symbols('x y')
        self.expr = None
        self.f_lambdificada = None
        self.valida = False  # Bandera de reconocimiento

        self.funciones_permitidas = {
            'sin': sin, 'cos': cos, 'tan': tan, 'exp': exp,
            'log': log, 'ln': log, 'asin': asin, 'acos': acos, 'atan': atan
        }

        try:
            self.expr = parse_expr(self.funcion_str, local_dict=self.funciones_permitidas)
            self.f_lambdificada = lambdify((self.x, self.y), self.expr, modules=["math"])
            self.valida = self.reconocer()
        except (SympifyError, SyntaxError, TypeError, Exception):
            self.expr = None
            self.f_lambdificada = None
            self.valida = False

    def resultado(self, x_val, y_val):
        """
        Evalúa f(x, y) de forma robusta:
        - Primero verifica si la función es válida.
        - Intenta evaluarla con los valores dados.
        - Si hay error matemático (división por cero, log negativo, etc.), devuelve False.
        """
        if not self.valida:
            return False
        try:
            resultado = self.f_lambdificada(x_val, y_val)
            if resultado is None or resultado == float('inf') or resultado == float('-inf'):
                return False
            return round(resultado, 10)
        except Exception:
            return False


    def reconocer(self):
        if self.expr is None:
            return False
        variables = {str(s) for s in self.expr.free_symbols}
        funciones = {f.func for f in self.expr.atoms(Function)}
        if not variables.issubset({"x", "y"}):
            return False
        if not funciones.issubset(set(self.funciones_permitidas.values())):
            return False
        return True

if __name__ == "__main__":
    # Ejemplo de uso
    f = FuncionXYProcesar("ln(x) + 1/y")
    print(f.resultado(0, 0))  # Evalúa f(1, 0.5)
    print(f.reconocer())      # True si es válida
