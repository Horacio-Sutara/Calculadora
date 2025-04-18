
def ordenar(matriz):
    # ordenamos la matriz por columna
    for i in range(len(matriz)):
        inicial=abs(matriz[i][i])
        for j in range(i+1,len(matriz)):
            if abs(matriz[j][i])>inicial:
                ant=matriz[i]
                matriz[i]=matriz[j]
                matriz[j]=ant
                inicial=abs(matriz[i][i])
    con=0
    while con<len(matriz):
        if vericar_diagonal(matriz):
            matriz=re_ordenar(matriz)
            con=0
        else:
            return matriz
        con+=1
    return matriz

def vericar_diagonal(matriz):
    # verificamos que la diagonal no tenga ceros
    for i in range(len(matriz)):
        if matriz[i][i]==0:
            return True
    return False

def re_ordenar(matriz):
    # reordenamos la matriz para que la diagonal no tenga ceros
    for i in range(len(matriz)):
        if matriz[i][i]==0:
            for j in range(0,len(matriz)):
                if matriz[j][i]!=0:
                    ant=matriz[i]
                    matriz[i]=matriz[j]
                    matriz[j]=ant
                    return matriz
    return matriz

def separar_resultado(matriz):
    # creamos una lista con los resultados sacando el ultimo valor de cada fila
    result=[]
    for i in range(len(matriz)):
        result.append(matriz[i][len(matriz[i])-1])
    # eliminamos el ultimo valor de cada fila
    for i in range(len(matriz)):
        matriz[i].pop()
    return matriz,result

def redondear(vector,error):
    cont=0
    while error<1:
        error*=10
        cont+=1
    for i in range(len(vector)):
        vector[i]=round(vector[i],cont)
if __name__ == "__main__":
    a=[
        [2,-1,4,1,-1], # el ultimo valor es ek resultado
        [-1,3,-2,-1,2],
        [5,1,3,-1,1],
        [3,-2,-2,-2,3]
    ]
    a=ordenar(a)
    print("matriz ordenada: ",a)
    a,res=separar_resultado(a)
    print("matriz sin resultados: ",a)
    print("resultados: ",res)
    