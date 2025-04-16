import matlab.engine
import os

# Obtener la ruta del archivo Python que se está ejecutando
script_path = os.path.dirname(os.path.abspath(__file__))
matlab_path = os.path.join(script_path, 'MATLAB')

# Iniciar MATLAB
eng = matlab.engine.start_matlab()

# Agregar la ruta donde está la clase y otros archivos .m
eng.addpath(matlab_path,nargout=0)

# 1. Instanciar la clase
expresion = "cos(4*x-2)+exp(1-x)"
error_max = 1e-8
iteraciones_max = 100
objeto_biseccion = eng.Metodo_Biseccion(expresion, error_max, iteraciones_max)

# 2. Llamar al método `encontrar_raiz` usando la notación correcta
res, encontrado = eng.encontrar_raiz(objeto_biseccion, 0.8, 1.2, nargout=2)

# Imprimir el resultado
print(f'Raíz aproximada: {res}')
print(f'¿Se encontró la raíz? {encontrado}')
eng.quit()
