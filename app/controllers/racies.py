from flask import Flask, jsonify, request, render_template
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
from io import BytesIO
import base64
from LogicaNegocio.Metodos_raices import Metodos_raices
from LogicaNegocio.raices import Ecuacion_procesar
from LogicaNegocio.utils.utils import validar_intervalo, validar_expresion_real

app = Flask(__name__)

def calcular_raices():
    """Recibe una función en formato JSON y devuelve la gráfica y las raíces."""

    try:
        data = request.get_json()

        #Procesamiento de la función
        funcion = data['funcion']
        if "^" in funcion:
            funcion=funcion.replace("^","**")
        if "√" in funcion:
            funcion=funcion.replace("√","sqrt")
            
        print(funcion)
        ecuacion=Ecuacion_procesar.Ecuacion_procesar(funcion)
        
        if not ecuacion.reconocer():
            print("Error en la función")
            return render_template('error_raices.html',titulo='No se pudo reconocer la Función')
        intervalo_str = data.get('intervalo', (-10, 10))  # Si no se pasa intervalo, usar (-10, 10)
        print(intervalo_str, "intervalo pasado", type(intervalo_str))
        a,b = tuple(map(float, intervalo_str.split(';'))) if intervalo_str else (-10, 10)
        intervalo,validar=ecuacion.verificar_dominio_y_subintervalo(a,b)
        print(intervalo, "intervalo", type(intervalo))
        print(validar, "validar")
        if not validar:
            return render_template('error_raices.html', titulo="No tiene domiinio valido")
        if not validar_expresion_real(funcion):
            return render_template('error_raices.html', titulo="La función contiene valores imaginarios, infinitos o no definidos. Solo se permiten funciones reales.")

        print(funcion)


        # Crear la instancia de la clase Metodos_raices
        metodos_raices = Metodos_raices(funcion,intervalo=intervalo)
        raices = metodos_raices.encontrar_raices()  # Encuentra las raíces usando los métodos
        print(raices)

        #Crear la gráfica
        x_vals = np.linspace(intervalo[0], intervalo[1], 800)
        y_vals = [metodos_raices.func(x) for x in x_vals]
        
        fig, ax = plt.subplots()
        ax.plot(x_vals, y_vals, label=f'f(x) = {funcion}')
        ax.axhline(0, color='black', linewidth=1)
        
        # Marcar las raíces en la gráfica
        for raiz, metodo in raices:
            ax.plot(raiz, 0, 'ro')  # Marca las raíces en rojo

        ax.set_xlabel('x')
        ax.set_ylabel('f(x)')
        ax.set_title(f"Gráfica de {funcion}")
        
        # Guardar la gráfica en un buffer y convertirla a base64 para enviar al frontend
        buf = BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        img_str = base64.b64encode(buf.getvalue()).decode('utf-8')
        
        # Crear la tabla con las raíces
        tabla_raices = [{"x": raiz, "f(x)": 0, "Metodo": metodo} for raiz, metodo in raices]

        # Redirigir al template de resultados, pasando la gráfica y las raíces
        return render_template('solucion_raices.html', img_data=img_str, tabla=tabla_raices)

    except Exception as e:
        print(f"Error: {str(e)}")  # Para que podamos ver en la consola el error
        return jsonify({'error': str(e)}), 400  # Retornar un error si algo falla