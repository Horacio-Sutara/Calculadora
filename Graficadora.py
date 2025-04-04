import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# Función para graficar y agregar una tabla a la derecha
def graficar_con_tabla(expresion_usuario):
    x = sp.symbols('x')  # Definir variable simbólica

    try:
        # Convertir la expresión en función simbólica
        expresion_simbolica = sp.sympify(expresion_usuario, locals={'sin': sp.sin, 'cos': sp.cos, 'tan': sp.tan,
                                                                    'asin': sp.asin, 'acos': sp.acos, 'atan': sp.atan,
                                                                    'exp': sp.exp, 'ln': sp.ln})
        
        # Convertir la función simbólica en una función evaluable en NumPy
        funcion_np = sp.lambdify(x, expresion_simbolica, 'numpy')

        # Definir rango de valores de x
        x_vals = np.linspace(-10, 10, 400)
        y_vals = funcion_np(x_vals)

        condicion=True
        # Crear figura con dos áreas (1 para la gráfica, 1 para la tabla)
        if condicion:
            fig, ax = plt.subplots(1, 2, figsize=(10, 5), gridspec_kw={'width_ratios': [3, 1]})
            ax1,ax2=ax
            # 📋 Agregar una tabla en la parte derecha
            data = [["x", "f(x)"], [-2, round(funcion_np(-2), 4)], [0, round(funcion_np(0), 4)], [2, round(funcion_np(2), 4)]]
            table = ax2.table(cellText=data, loc='center', cellLoc='center', colWidths=[0.4, 0.4])
            ax2.axis("off")  # Ocultar ejes en la tabla
            ax2.set_title("Tabla de Valores")
        else:
            fig, ax1 = plt.subplots(figsize=(10, 5))


        # 📈 Graficar función
        ax1.plot(x_vals, y_vals, label=f'f(x) = {expresion_usuario}', color='b')
        ax1.axhline(0, color='black', linewidth=0.5)
        ax1.axvline(0, color='black', linewidth=0.5)
        ax1.legend()
        ax1.grid(True)
        ax1.set_title("Gráfica de la Función")
        ax1.set_xlabel("x")
        ax1.set_ylabel("f(x)")


        plt.show()

    except Exception as e:
        print(f"Error al procesar la función: {e}")

# 🚀 Prueba con entrada del usuario
expresion = input("Ingresa una función en términos de x: ")
graficar_con_tabla(expresion)
