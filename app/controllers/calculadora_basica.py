from flask import Flask, request, jsonify
from LogicaNegocio.raices import Ecuacion_procesar

app = Flask(__name__)
def calcular():
    data = request.get_json()
    expresion = data['expresion']
    print("Hola, estoy en el calculadora.py\n",expresion, type(expresion))
    if expresion=="" or expresion==" ":
        return jsonify({'resultado': "", 'detalle': "vacio"})
    if "^" in expresion:
        expresion=expresion.replace("^","**")
    if "√" in expresion:
        expresion=expresion.replace("√","sqrt")
        print("Hola, estoy en el calculadora.py\n",expresion, type(expresion))
    try:
        # Prepará un entorno seguro para evaluar
        datos=expresion.split(";")
        ecuacion=Ecuacion_procesar.Ecuacion_procesar(datos[0])
        if ecuacion.reconocer() and type(ecuacion.resultado(datos[1] if len(datos)>1 else 0))==float:
            resultado=str(ecuacion.resultado(datos[1] if len(datos)>1 else 0 ))
            return jsonify({'resultado': resultado})
        else:
            return jsonify({'resultado': 'Error', 'detalle': "No se reconoce expresion"})

    except Exception as e:
        return jsonify({'resultado': 'Error', 'detalle': str(e)})
