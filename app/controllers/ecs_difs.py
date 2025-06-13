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