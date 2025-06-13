from flask import Flask, jsonify, request, render_template
import matplotlib
matplotlib.use('Agg')
import numpy as np

from LogicaNegocio.ecsdif import rungekutta1, rungekutta4, ecdif

app = Flask(__name__)

def calcular_solucion():
    data = request.get_json()
    funcion = data['funcion']
    if "^" in funcion:
        funcion = funcion.replace("^", "**")
    if "√" in funcion:
        funcion = funcion.replace("√", "sqrt")
    if "π" in funcion:
        funcion = funcion.replace("π", "pi")
    if "e" in funcion:
        funcion = funcion.replace("e", "(exp(1))")
    print(funcion)
    ecuacion = ecdif.FuncionXYProcesar(funcion)
    if not ecuacion.reconocer():
        return render_template('error_ecuaciones.html', titulo='No se pudo reconocer la función.')
    x0 = data['x0']
    y0 = data['y0'] # Valor inicial de y
    xn = data['xn'] # Valor final de x
    n = data['n'] # Número de pasos
    metodo = data['metodo']