from sympy import symbols, Eq, sympify, solve,diff, sin, cos, tan,exp, asin, acos, atan,log,Function,nsolve
from sympy import floor, S
from sympy.core.sympify import SympifyError
from sympy.parsing.sympy_parser import parse_expr
from sympy import Interval
from sympy.calculus.util import continuous_domain

class Ecuacion_procesar:
    def __init__(self,nombre_archivo):
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

    def despejar_y(self,ecuacion_str,y="y"):
        # Convertir la ecuación de string a expresión simbólica
        x, y = symbols(f'x {y}')
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

    def procesar_ecuacion(self, ecuacion_txt=None, valor_x=None):
        x = symbols('x')
        funciones = {
            'sin': sin, 'cos': cos, 'tan': tan, 'exp': exp,
            'asin': asin, 'acos': acos, 'atan': atan, 'ln': log
        }

        texto = ecuacion_txt if ecuacion_txt is not None else self.ecuacion

        try:
            if '=' in texto:
                izquierda, derecha = texto.split('=')
                izquierda = parse_expr(izquierda.strip(), local_dict=funciones)
                derecha = parse_expr(derecha.strip(), local_dict=funciones)
                ecuacion = Eq(izquierda, derecha)

                if valor_x is not None:
                    return Eq(izquierda.subs(x, valor_x).evalf(), derecha.subs(x, valor_x).evalf())
                else:
                    try:
                        soluciones = solve(ecuacion, x)
                        return soluciones
                    except Exception:
                        # Resolución numérica con nsolve
                        from sympy import S
                        aproximada = nsolve(izquierda - derecha, x, 1)  # 1 es el punto inicial
                        return f"Solución numérica aproximada: {aproximada}"

            else:
                expr = parse_expr(texto.strip(), local_dict=funciones)
                if valor_x is not None:
                    return expr.subs(x, valor_x).evalf()
                else:
                    return expr

        except (SympifyError, Exception) as e:
            return f"Error al interpretar la ecuación: {e}"
        
    def truncar_sympy(self,numero, decimales):
        factor = 10 ** decimales
        return (int(floor(numero * factor)) / factor)
    
    def resultado(self,valor,ecuacion=None):
        if ecuacion is None:
            if self.reconocer():
                res=self.procesar_ecuacion(valor_x=valor)
                try:
                    res=self.truncar_sympy(float(res),10)
                    #print("hola ")
                    return self.truncar_sympy(float(res),10)
                except:
                    return False
        else:
            if self.reconocer():
                res=self.procesar_ecuacion(valor_x=valor)
                try:
                    #print("chao")
                    return self.truncar_sympy(float(res),10)
                except:
                    return False
        return False

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

    def reconocer(self):
        funciones_permitidas = {sin, cos, tan, exp, asin, acos, atan, log}
        variables_permitidas = {'x'}
        funciones = {
            'sin': sin, 'cos': cos, 'tan': tan, 'exp': exp,
            'asin': asin, 'acos': acos, 'atan': atan, 'ln': log
        }

        try:
            texto = self.ecuacion.strip()

            if '=' in texto:
                izquierda, derecha = texto.split('=')
                izquierda = parse_expr(izquierda.strip(), local_dict=funciones)
                derecha = parse_expr(derecha.strip(), local_dict=funciones)
                exprs = [izquierda, derecha]
            else:
                exprs = [parse_expr(texto, local_dict=funciones)]

            for expr in exprs:
                # Validar variables
                if not {str(s) for s in expr.free_symbols}.issubset(variables_permitidas):
                    return False

                # Validar funciones
                funciones_encontradas = {f.func for f in expr.atoms(Function)}
                if not funciones_encontradas.issubset(funciones_permitidas):
                    return False

            return True

        except Exception as e:
            return False

    def reescribir(self,ecuacion):
        self.ecuacion=ecuacion

    def verificar_dominio_y_subintervalo(self, a, b,expr_str=None):
        if expr_str is None:
            expr_str = self.ecuacion
        x = symbols('x')
        expr = parse_expr(expr_str)
        dominio = continuous_domain(expr, x, S.Reals)
        sub_intervalo_abierto = Interval.open(a, b)
        sub_intervalo_cerrado= Interval(a, b)
        if sub_intervalo_abierto.is_subset(dominio) and (not sub_intervalo_cerrado.is_subset(dominio)):
            return (a+(a+b)*1e-7,b),True
        if sub_intervalo_cerrado.is_subset(dominio):
            return (a,b),True
        return dominio, False



if __name__ == "__main__":
    print("primera ecuacion:")
    ecuacion = Ecuacion_procesar("x**2-24=76")
    print(ecuacion.reconocer())
    print(ecuacion.procesar_ecuacion())
    print(ecuacion.resultado(10))
    print(ecuacion.resultado(5))
    
    print("segunda ecuacion:")

    ecuacion = Ecuacion_procesar("x**x")
    print(ecuacion.reconocer())
    print(ecuacion.resultado(5))

    print("tercera ecuacion:")
    ecuacion = Ecuacion_procesar("x**xx")
    print(ecuacion.reconocer())
    print(ecuacion.resultado(5))

    print("cuarta ecuacion:")
    ecuacion = Ecuacion_procesar("exp(exp(x))")
    print(ecuacion.reconocer())
    print(ecuacion.resultado(5))

    print("quinta ecuacion:")
    ecuacion = Ecuacion_procesar("x+sqrt(-5)")
    print(ecuacion.reconocer())
    print(ecuacion.resultado(10))

    print("sexta ecuacion:")
    ecuacion = Ecuacion_procesar("1/x")
    print(ecuacion.reconocer())
    print(ecuacion.resultado(0))
    print(type(ecuacion.resultado(0)))

    print("septima ecuacion:")
    ecuacion = Ecuacion_procesar("ln(x)")
    print(ecuacion.reconocer())
    print(ecuacion.resultado(0))
    print(ecuacion.verificar_dominio_y_subintervalo(-10,10))
    dominio,sub_intervalo=ecuacion.verificar_dominio_y_subintervalo(0,10)
    print(dominio,sub_intervalo)
    dominio,sub_intervalo=ecuacion.verificar_dominio_y_subintervalo(1,10)
    print(dominio,sub_intervalo)

    print("octava ecuacion:")
    ecuacion = Ecuacion_procesar("sqrt(x)-sqrt(-1)")
    print(ecuacion.reconocer())
    dominio,sub_intervalo=ecuacion.verificar_dominio_y_subintervalo(-10,10)
    print(dominio,sub_intervalo)