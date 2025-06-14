from flask import Flask, jsonify, request, render_template
import matplotlib
matplotlib.use('Agg')
import numpy as np
from LogicaNegocio.Metodos_edos import Metodos_edos
from LogicaNegocio.ecsdif.ecdif import FuncionXYProcesar

app = Flask(__name__)

def calcular_solucion():
    print("Datos recibidos para calcular la solución:")
    data = request.get_json()
    # Conversión de datos básicos
    funcion = data['funcion']
    x0 = float(data['x0'])
    y0 = float(data['y0'])
    xn = float(data['xn'])
    modo = data['modo']
    metodo = data['metodo']
    
    # Manejo de h y n
    h = None
    n = None
    
    if modo == 'h':
        h = float(data['h']) if data['h'] and data['h'].strip() else None
    else:  # modo == 'n'
        try:
            n = int(data['n']) if data['n'] and data['n'].strip() else None
        except ValueError:
            return render_template('error_ecuaciones.html', 
                                titulo='El número de pasos debe ser un número entero.')

    print(f"Función: {funcion}, x0: {x0}, y0: {y0}, xn: {xn}, n: {n}, h: {h}, modo: {modo}, metodo: {metodo}")

    if "^" in funcion:
        funcion = funcion.replace("^", "**")
    if "√" in funcion:
        funcion = funcion.replace("√", "sqrt")
    if "π" in funcion:
        funcion = funcion.replace("π", "pi")
    if "e" in funcion:
        funcion = funcion.replace("e", "(exp(1))")
    print(funcion)
    ecuacion = FuncionXYProcesar(funcion)
    if not ecuacion.reconocer():
        return render_template('error_ecuaciones.html', titulo='No se pudo reconocer la función.')
    
    result = Metodos_edos(funcion, x0, y0, xn, n, h, modo, metodo)

    print("Resultado de la solución:", result)
    if result is None: #corregir esto porque en la logica de metodos edos ni de rk1 ni rk4 se deuvelve none
        return render_template('error_ecuaciones.html', titulo='Error al calcular la solución.')
    
        # Separar los puntos en listas para pasarlas al template
    puntos = result[0]
    h = result[1]

    x_vals = [p[0] for p in puntos]
    y_vals = [p[1] for p in puntos]

    tabla = [
        {'i': i, 'x': p[0], 'y': p[1]}
        for i, p in enumerate(puntos)
    ]

    return render_template(
        'solucion_ecuacion.html',
        x_vals=x_vals,
        y_vals=y_vals,
        metodo=metodo,
        funcion_original=data['funcion'],
        h=h,
        tabla=tabla
    )


