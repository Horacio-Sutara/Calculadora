from sympy import sympify, Interval, symbols, I, S
from sympy.calculus.util import continuous_domain

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

def validar_expresion_real(funcion_str):
    """
    Valida si una expresión matemática sin x (como sqrt(-3)) 
    pertenece al conjunto de los reales.
    """
    try:
        expr = sympify(funcion_str)

        # Si depende de x, no es una constante => es función válida
        if expr.free_symbols:
            return True

        # Si NO depende de x y tiene parte imaginaria => no válida
        if expr.has(I):
            return False
        
        return True

    except Exception:
        return False


def validar_intervalo(funcion,intervalo):
    x = symbols('x')
    func = sympify(funcion)
    a,b = intervalo
    intervalo_usuario = Interval(a, b)

    #Calcular el dominio de la funcion
    dom_funcion = continuous_domain(func,x,S.Reals)

    #Interseccion del dominio de la funcion con el intervalo del usuario
    subintervalo = intervalo_usuario.intersect(dom_funcion)

    if subintervalo.is_empty:
        return [False,f"La función no está definida en ningún punto del intervalo [{a}, {b}].\n"
                         f"Dominio válido: {dom_funcion}"]
    
    if subintervalo.is_Union:
        subintervalos = list(subintervalo.args)
        
        # Medida máxima
        max_medida = max(i.measure for i in subintervalos)

        # Filtrar solo los de esa medida
        candidatos = [i for i in subintervalos if i.measure == max_medida]

        if len(candidatos) == 1:
            subintervalo = candidatos[0]
        else:
            # Elegir el que tenga el extremo más positivo
            subintervalo = max(candidatos, key=lambda i: i.start)
    
    return [True, subintervalo]

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
    