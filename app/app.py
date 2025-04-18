from flask import Flask,render_template
from controllers import racies

app = Flask(__name__)

#Ruta de prueba
@app.route('/')
def index():
    #return 'Hola Mundo'
    nombres=['Juan','Pedro','Luis']

    data={'titulo':'Prueba de Flask',
          'contenido':'Este es un mensaje de prueba',
          'nombres':nombres,
          "numero_persona":len(nombres)} # se crea un diccionario con el contenido que se va a mostrar en la plantilla
    
    return render_template('prueba.html',data=data) # render_template permite cargar archivos html


# Ruta para la calculadora de raíces
@app.route('/calcular_raices', methods=['GET', 'POST'])
def calcular_raices():
    # Llamamos a la función en el controlador 'raices.py'
    return racies.calcular_raices()

if __name__ == '__main__':
    app.run(debug=True, port=5000)  # Ejecuta la app en modo de desarrollo en el puerto 5000