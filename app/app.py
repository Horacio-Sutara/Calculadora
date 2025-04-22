from flask import Flask,render_template
from controllers import racies,calculadora_basica
#from controllers.calculadora import calcular
app = Flask(__name__)

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

@app.route('/solucion_sistema')
def solucion_sistema():
    matrices = [
        [[1, 2, 3.22], [3.2, 4, 4], [3, 4, 5]],
        [[5, 6, 7], [8, 9, 10], [3.2, 5, 1]],
        [[5, 3, 2], [1, 2, 10], [1, 5, 2]],
        [[5, 3, 2], [1, 2, 10], [1, 5, 2]],
        [[5, 3, 2], [1, 2, 10.2], [1.2, 5, 2]],
        [[5, 3, 2], [1, 2, 10], [1, 5, 2]],
        [[5, 3, 2], [1, 2, 10], [1, 5, 2]],
    ]
    letras = [f"Matriz {chr(65 + i)}" for i in range(len(matrices))]  # ['Matriz A', 'Matriz B', 'Matriz C']
    soluciones = ['x = ...', 'y = ...', 'z = ...']
    return render_template('solucion_sistema.html', matrices=matrices, letras=letras, soluciones=soluciones)

if __name__ == '__main__':
    app.run(debug=True, port=5000)  # Ejecuta la app en modo de desarrollo en el puerto 5000