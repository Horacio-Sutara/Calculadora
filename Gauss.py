import numpy as np
def verificar_variables(matriz):
    longitud=len(matriz)
    resultados=[]
    exito=False
    for i in range(longitud):
        num=matriz[i][i]
        band=True
        if num==0:
            band=False
            for j in range(i+1,longitud):
                if matriz[j][i]!=0:
                    fila=matriz[j]
                    matriz[j]=matriz[i]
                    matriz[i]=fila
                    num=matriz[i][i]
                    band=True
                    break
        if band==False:
            print("no se puede resolver")
            return
        for j in range(i+1,longitud):
            num_2=matriz[j][i]
            multiplicador=-1*num_2/num
            #print(f"multiplicador: {multiplicador} num: {num} num_2: {num_2}")
            matriz[j]=matriz[j]+ multiplicador*matriz[i]
            if np.all(matriz[:-1] == 0):
                print("no se puede resolver")
                return  resultados, exito
        #print(f"fila {i}: ",matriz[i])

    for i in range(longitud-1,-1,-1):
        resultado=matriz[i][longitud]
        var=0
        for j in range(i+1,longitud):
            var+=matriz[i][j]
        x=matriz[i][i]
        resultados.append(float(np.round((resultado-var)/x,7)))
        for j in range(i,-1,-1):
            num=matriz[j][i]
            matriz[j][i]=num*resultados[-1]
    resultados.reverse()
    print(f"resultado: {resultados}")
    exito=True
    return resultados, exito

if __name__ == '__main__':
    matriz=[[2,-1,4,1,-1,7], # el ultimo valor es ek resultado
            [-1,3,-2,-1,2,1],
            [5,1,3,-4,1,33],
            [3,-2,-2,-2,3,24],
            [-4,-1,-5,3,-4,-49]
            ]
    """matriz=[[2,1,1],
            [-1,2,7]]"""
    """matriz=[
        [1,1,1,1],
        [2,2,2,44],
        [1,1,1,3]
    ]"""
    matriz=np.array(matriz).astype(float)
    verificar_variables(matriz)


