from flask import Flask, jsonify, request, render_template
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO
import base64
from LogicaNegocio.Metodos_raices import Metodos_raices

app = Flask(__name__)

@app.route('/calcular_raices', methods=['GET', 'POST'])
def calcular_raices():
    """Recibe una función en formato string y devuelve la gráfica y las raíces."""
    
    if request.method == 'POST':
        # Obtener la función desde el formulario
        funcion = request.form.get('funcion')
        intervalo_str = request.form.get('intervalo', '-10,10')  # Si no se ingresa un intervalo, usamos el predeterminado
        
        print(f"Función recibida: {funcion}")
        print(f"Intervalo recibido: {intervalo_str}")
        
        if not funcion:
            return jsonify({"error": "No se ha recibido ninguna función."})
        
        # Procesar el intervalo, si no se ingresa, se toma el valor predeterminado
        try:
            intervalo = tuple(map(float, intervalo_str.split(','))) if intervalo_str else (-10, 10)
        except ValueError:
            return jsonify({"error": "El intervalo debe ser en el formato 'a,b'."})

        try:
            # Crear la instancia de la clase Metodos_raices
            print("Creando instancia de Metodos_raices...")
            metodos_raices = Metodos_raices(funcion, intervalo=intervalo)
            print("Achu")
            raices = metodos_raices.encontrar_raices()  # Encuentra las raíces usando los métodos
            print("Raíces encontradas:", raices)
            
            # Crear la gráfica
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
            ax.set_title('Gráfica de la Función')
            ax.legend()
            
            # Guardar la gráfica en un buffer y convertirla a base64 para enviar al frontend
            buf = BytesIO()
            plt.savefig(buf, format='png')
            buf.seek(0)
            img_str = base64.b64encode(buf.getvalue()).decode('utf-8')
            
            # Crear la tabla con las raíces
            tabla_raices = [{"x": raiz, "f(x)": metodos_raices.func(raiz), "Metodo": metodo} for raiz, metodo in raices]

            # Renderizar la página con la gráfica y la tabla
            return render_template('calcular_raices.html', img_data=img_str, tabla=tabla_raices)
        
        except Exception as e:
            print(f"Error al crear la instancia de Metodos_raices: {str(e)}")
            return jsonify({"error": f"Error: {str(e)}"})

    return render_template('index.html')  # Si es un GET, mostrar el formulario