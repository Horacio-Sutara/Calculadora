from flask import Flask,render_template,session
from controllers import racies,calculadora_basica,ecuaciones,integrales as integr
#from controllers.calculadora import calcular
app = Flask(__name__)
app.secret_key = 'clave-secreta'
#Ruta de prueba
@app.route('/')
def index():
    #return 'Hola Mundo'    
    return render_template('main.html') # render_template permite cargar archivos html

@app.route('/sobre-nosotros')
def sobre_nosotros():
    return render_template('sobre-nosotros.html')

@app.route('/calculadora')
def calculadora():
    return render_template('calculadora.html')

@app.route('/resolver', methods=['POST'])
def resolver():
    print("Recibido")
    return calculadora_basica.calcular()
    #return calcular()

@app.route('/raices')
def raices():
    return render_template('raices.html')

# Ruta para la calculadora de raíces
@app.route('/calcular_raices', methods=['POST'])
def calcular_raices():
    # Llamamos a la función en el controlador 'raices.py'
    print("Recibido")
    return racies.calcular_raices()

@app.route('/sistemas_ecuaciones')
def sistemas_ecuaciones():
    return render_template('sistemas.html')

@app.route('/resolver_sistema', methods=['POST'])
def resolver_sistema():
    return ecuaciones.calcular()

@app.route('/solucion')
def solucion_sistema():
    return render_template('solucion_sistema.html')

@app.route('/integrales')
def integrales():
    return render_template('integrales.html')

@app.route('/calcular_integral', methods=['POST'])
def calcular_integral():
    # Llamamos a la función en el controlador 'integrales.py'
    print("Recibido")
    return integr.calcular_integral()

@app.route('/solucion_integral')
def solucion_integral():
    return render_template('solucion_integral.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)  # Ejecuta la app en modo de desarrollo en el puerto 5000