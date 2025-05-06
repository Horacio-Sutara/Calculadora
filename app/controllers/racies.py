from flask import Flask, jsonify, request, render_template
import matplotlib
matplotlib.use('Agg')
from multiprocessing import Process, cpu_count,Queue
import multiprocessing
multiprocessing.set_start_method('spawn', force=True)
import numpy as np

from LogicaNegocio.Metodos_raices import Metodos_raices
from LogicaNegocio.raices import Ecuacion_procesar
from LogicaNegocio.utils.utils import validar_intervalo, validar_expresion_real

app = Flask(__name__)

@app.route('/calcular_raices', methods=['POST'])  # Asegúrate de tener esto en tu Flask app
def iniciar_procesamiento(funcion, intervalo):
    cant_procesos = cpu_count()
    puntos = np.linspace(intervalo[0], intervalo[1], num=cant_procesos + 1)
    procesos = []
    queue = Queue()
    resultados = []

    for i in range(cant_procesos):
        p = Process(target=worker, args=(funcion, (puntos[i], puntos[i + 1]), queue))
        procesos.append(p)
        p.start()

    for p in procesos:
        p.join()

    # Recolectar resultados
    while not queue.empty():
        resultados.append(queue.get())

    return resultados
def worker(funcion, intervalo, queue):
    metodos = Metodos_raices(funcion, intervalo=intervalo)
    resultado = metodos.encontrar_raices()
    queue.put(resultado)  # manda el resultado al proceso principal

def calcular_raices():
    try:
        data = request.get_json()

        funcion = data['funcion']
        if "^" in funcion:
            funcion = funcion.replace("^", "**")
        if "√" in funcion:
            funcion = funcion.replace("√", "sqrt")
        if "π" in funcion:
            funcion = funcion.replace("π", "pi")

        ecuacion = Ecuacion_procesar.Ecuacion_procesar(funcion)
        if not ecuacion.reconocer():
            return render_template('error_raices.html', titulo='No se pudo reconocer la función.')

        intervalo_str = data.get('intervalo', (-10, 10))
        a, b = tuple(map(float, intervalo_str.split(';'))) if intervalo_str else (-10, 10)
        intervalo, validar = ecuacion.verificar_dominio_y_subintervalo(a, b)
        if not validar:
            return render_template('error_raices.html', titulo="No tiene dominio válido.")
        if not validar_expresion_real(funcion):
            return render_template('error_raices.html', titulo="La función contiene valores no reales.")

        metodos_raices = Metodos_raices(funcion, intervalo=intervalo)
        result=iniciar_procesamiento(funcion,intervalo)
        resultado = [item for sublist in result if sublist for item in sublist]
        raices = []
        for item in resultado:
            if item not in raices:
                raices.append(item)
        print("Raices:", raices, type(raices), list(raices))

        # Crear datos para Plotly
        x_vals = np.linspace(intervalo[0], intervalo[1], int((abs(intervalo[0])+(intervalo[1]))/0.025))
        y_vals = [float(metodos_raices.func(x)) for x in x_vals]

        plot_data = {
    'x': x_vals.tolist(),
    'y': y_vals,
    'funcion': funcion,
    'raices_x': [raiz for raiz, _ in raices],
    'raices_y': [0 for _ in raices],

}

        # Tabla para HTML
        tabla_raices = [{"x": raiz, "f(x)": 0, "Metodo": metodo} for raiz, metodo in raices]

        return render_template('solucion_raices.html', plot_data=plot_data, tabla=tabla_raices)

    except Exception as e:
        #print(f"Error: {str(e)}")
        return jsonify({'error': str(e)}), 400

