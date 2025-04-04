import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# Función para graficar expresiones ingresadas por el usuario
def graficar_funcion(expresion_usuario):
    x = sp.symbols('x')  # Definir variable simbólica

    try:
        # Convertir la expresión en una función simbólica
        expresion_simbolica = sp.sympify(expresion_usuario, locals={'sin': sp.sin, 'cos': sp.cos, 'tan': sp.tan,
                                                                    'asin': sp.asin, 'acos': sp.acos, 'atan': sp.atan,
                                                                    'exp': sp.exp, 'ln': sp.log})
        
        # Convertir la función simbólica en una función evaluable en NumPy
        funcion_np = sp.lambdify(x, expresion_simbolica, 'numpy')

        # Definir rango de valores de x
        x_vals = np.linspace(-10, 10, 400)
        y_vals = funcion_np(x_vals)

        # Graficar
        plt.figure(figsize=(8, 5))
        plt.plot(x_vals, y_vals, label=f'f(x) = {expresion_usuario}', color='b')

        # Configuración de la gráfica
        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)
        plt.legend()
        plt.grid(True)
        plt.title("Gráfica de la Función")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.show()

    except Exception as e:
        print(f"Error al procesar la función: {e}")
if __name__ == "__main__":
    # 🚀 Prueba con entrada del usuario
    expresion = input("Ingresa una función en términos de x: ")
    graficar_funcion(expresion)
