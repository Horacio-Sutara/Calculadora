from flask import Flask, jsonify, request, render_template
import matplotlib
matplotlib.use('Agg')
import numpy as np

from LogicaNegocio.ecsdif import rungekutta1, rungekutta4, ecdif

app = Flask(__name__)

def calcular_solucion():
    print("Datos recibidos para calcular la solución:")
    data = request.get_json()
    funcion = data['funcion']
    x0 = data['x0']
    y0 = data['y0']  
    xn = data['xn']  
    n = data['n']
    h = data['h']
    modo = data['modo']
    metodo = data['metodo']

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
    ecuacion = ecdif.FuncionXYProcesar(funcion)
    if not ecuacion.reconocer():
        return render_template('error_ecuaciones.html', titulo='No se pudo reconocer la función.')