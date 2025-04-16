from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')

def index():
    #return 'Hola Mundo'
    nombres=['Juan','Pedro','Luis']

    data={'titulo':'Prueba de Flask',
          'contenido':'Este es un mensaje de prueba',
          'nombres':nombres,
          "numero_persona":len(nombres)} # se crea un diccionario con el contenido que se va a mostrar en la plantilla
    
    return render_template('index.html',data=data) # render_template permite cargar archivos html

if __name__ == '__main__':
    app.run(debug=True,port=5000)# modo de desarrollo activado para ver errores y en que puerto esta visible