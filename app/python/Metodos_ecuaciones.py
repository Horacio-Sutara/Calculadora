from Ecuaciones import Gauss,jacobi,Seidel
from utils import utils
import numpy as np
def Metodos_ecuaciones(matriz,metodo,iteraciones=100,error=1e-7):
    array=matriz.copy()
    metodos={
        "Gauss": Gauss.Gauss,
        "Jacobi":jacobi.jacobi,
        "Seidel":Seidel.gauss_seidel
    }
    array=utils.ordenar(array)
    array,res=utils.separar_resultado(array)
    
    if metodo not in metodos:
        print("No existe ese metodo")
        return None,None,None,False
    res,iteraciones,historial,funciono=metodos[metodo](array,res,tol=error,max_iter=iteraciones)
    utils.redondear(res,error)
    if funciono:
        return res,iteraciones,historial,funciono
    else:
        print("No converge")
        return res,iteraciones,historial,funciono
if __name__ == '__main__':
    
    """matriz=[[2,-1,4,1,-1,7], # el ultimo valor es ek resultado
            [-1,3,-2,-1,2,1],
            [5,1,3,-4,1,33],
            [3,-2,-2,-2,3,24],
            [-4,-1,-5,3,-4,-49]
            ]"""
    
    matriz=[[2,1,1],
            [-1,2,7]]
    """matriz=[
        [1,1,1,1],
        [2,2,2,44],
        [1,1,1,3]
    ]"""

    #print(matriz)
    
    elegir_metodo="sasas"# Gauss,Seidel,Jacobi
    res,iteraciones,historial,funciono=Metodos_ecuaciones(matriz,elegir_metodo)


    if funciono:
        print(f"{elegir_metodo}:",res)
    else:
        print("No converge")




    #Codigo de prueba
    """matriz=utils.ordenar(matriz)
    matriz,res=utils.separar_resultado(matriz)

    res1,iteraciones,historial,funciono=Gauss.Gauss(matriz,res)
    print("Gauss:",res1)

    res2,iteraciones,historial,funciono=jacobi.jacobi(matriz,res)
    if funciono:
        print("Jacobi:",res2)
    else:
        print("No converge")
    res3,iteraciones,historial,funciono=Seidel.gauss_seidel(matriz,res)
    if funciono:
        print("Seidel:",np.round(res3, 5).tolist())
    else:
        print("No converge")
    
    diccionario={
        "Gauss":res1,
        "Jacobi":res2,
        "Seidel":res3
    }
    res="Seisdel"
    if res in diccionario:
        print("Se encuentra en el diccionario")
        print(diccionario[res])"""
