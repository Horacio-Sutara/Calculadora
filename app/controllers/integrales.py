from flask import Flask, jsonify, request, url_for
from LogicaNegocio import Metodos_integracion
from LogicaNegocio.utils.utils import validar_intervalo, validar_expresion_real
app = Flask(__name__)

def calcular_integral():
    data = request.get_json()
    funcion = data['funcion']
    metodo = data['metodo']
    a = data['a']
    b = data['b']
    n = data['n']

    # Validar la expresión de la función
    if not validar_expresion_real(funcion):
        return jsonify({'error': 'Expresión no válida'}), 400

    # Validar el intervalo
    if not validar_intervalo(a, b):
        return jsonify({'error': 'Intervalo no válido'}), 400

    resultado, metodo, a, b, n, funciono = Metodos_integracion.calcular_integral(funcion, metodo, a, b, n)

    if not funciono:
        return jsonify({'error': 'Error al calcular la integral'}), 500

    return jsonify({
        'resultado': resultado,
        'metodo': metodo,
        'a': a,
        'b': b,
        'n': n,
        'funciono': funciono,
        'redirect': url_for('solucion_integral')
    })