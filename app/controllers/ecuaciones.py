from flask import Flask, request, render_template, redirect, url_for, session, jsonify
from LogicaNegocio import Metodos_ecuaciones

app = Flask(__name__)
app.secret_key = 'clave-secreta'
def calcular():
    datos = request.get_json()
    expresion = datos.get('expresion')  # La matriz del sistema
    metodo = datos.get('metodo')        # El método seleccionado ("Gauss", "Jacobi", etc.)
    print("Hola, estoy en el ecuaciones.py\n",expresion, type(expresion))
    print("metodo:",metodo, type(metodo))
    res,iteraciones,historial,funciono=Metodos_ecuaciones.Metodos_ecuaciones(expresion, metodo)
    print("res:",res, type(res), "funciono:",funciono, type(funciono), " Historial: ",type(historial))
    if not funciono:
        return jsonify({
            'funciono': False
        })
    # Guardar los datos en sesión para pasarlos a la próxima página
    session['resultado'] = res
    session['iteraciones'] = iteraciones
    session['historial'] = historial
    session['funciono'] = funciono
    session['metodo'] = metodo

    return {
    'resultado': res,
    'metodo':metodo,
    'iteraciones': iteraciones,
    'historial': historial,
    'funciono': funciono,
    'redirect': url_for('solucion_sistema')
}  # JavaScript usará esta URL para redirigir
