from flask import Flask,render_template
from controllers import racies

app = Flask(__name__)

#Ruta de prueba
@app.route('/')
def index():
    #return 'Hola Mundo'    
    return render_template('main.html') # render_template permite cargar archivos html

@app.route('/sobre-nosotros')
def sobre_nosotros():
    return render_template('sobre-nosotros.html')

# Ruta para la calculadora de raíces
@app.route('/calcular_raices', methods=['GET', 'POST'])
def calcular_raices():
    # Llamamos a la función en el controlador 'raices.py'
    return racies.calcular_raices()

@app.route('/calculadora')
def calculadora():
    return render_template('calculadora.html')

@app.route('/raices')
def raices():
    return render_template('raices.html')

@app.route('/sistemas_ecuaciones')
def sistemas_ecuaciones():
    return render_template('sistemas.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)  # Ejecuta la app en modo de desarrollo en el puerto 5000