import numpy as np
def verificar_variables(matriz,longitud):
    for i in range(longitud):
        num=matriz[i][i]
        for j in range(i+1,longitud):
            num_2=matriz[j][i]
            multiplicador=-1*num_2/num
            #print(f"multiplicador: {multiplicador} num: {num} num_2: {num_2}")
            matriz[j]=matriz[j]+ multiplicador*matriz[i]
        #print(f"fila {i}: ",matriz[i])

    resultados=[]
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
    print(f"resultado: {resultados}")
    return resultados

if __name__ == '__main__':
    matriz=[[1.,1.0,1.0,2.0],
            [3.0,-2.0,-1.0,4.0],
            [-2.0,1.0,2.0,2.0]
            ]
    matriz=np.array(matriz)
    tipo=3
    verificar_variables(matriz,tipo)


