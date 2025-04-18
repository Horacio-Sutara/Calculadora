import numpy as np
def Gauss(matriz,constante,tol=None,max_iter=None):
    constante=constante.copy()
    longitud=len(matriz)
    resultados=[]
    exito=False
    matriz=np.array(matriz).astype(float)
    historial=[]
    iteraciones=0
    for i in range(longitud):
        num=matriz[i][i]
        for j in range(i+1,longitud):
            num_2=matriz[j][i]
            multiplicador=-1*num_2/num
            iteraciones+=1
            #print(f"multiplicador: {multiplicador} num: {num} num_2: {num_2}")
            constante[j]=constante[j]+float(multiplicador)*constante[i]
            matriz[j]=matriz[j]+ multiplicador*matriz[i]
            if np.all(matriz[:-1] == 0):
                print("no se puede resolver")
                return  resultados,iteraciones,historial, exito
            historial.append(matriz.tolist())
    


    for i in range(longitud-1,-1,-1):
        resultado=constante[i]
        var=0
        for j in range(i+1,longitud):
            var+=matriz[i][j]
        x=matriz[i][i]
        resultados.append(float((resultado-var)/x))
        for j in range(i,-1,-1):
            num=matriz[j][i]
            matriz[j][i]=num*resultados[-1]
            historial.append(matriz.tolist())
            iteraciones+=1
    resultados.reverse()
    #print(f"resultado: {resultados}")
    exito=True
    return resultados,iteraciones ,historial,exito

if __name__ == '__main__':
    matriz=[[2,-1,4,1,-1], # el ultimo valor es ek resultado
            [-1,3,-2,-1,2],
            [5,1,3,-4,1],
            [3,-2,-2,-2,3],
            [-4,-1,-5,3,-4]
            ]
    constante=[7,1,33,24,-49]
    """matriz=[[2,1,1],
            [-1,2,7]]"""
    """matriz=[
        [1,1,1,1],
        [2,2,2,44],
        [1,1,1,3]
    ]"""
    num=1e-7
    print(num)
    print(round(num,5))
    matriz=np.array(matriz).astype(float)
    resultados,iteraciones,historial,funciono=Gauss(matriz,constante)
    print(constante)
    print("Gauss:",resultados)

