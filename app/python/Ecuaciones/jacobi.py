#es un método iterativo para resolver sistemas de ecuaciones lineales de la forma:𝐴𝑥=𝑏
#Se usa cuando la matriz tiene muchos ceros, se usa en simulaciones físicas, redes eléctricas, mallas de calor, etc.
##Le pongo yo el error para parar y la cantidad maxima de iteraciones
# Por lo general se comienza con 0,0,0,0 pero se puede dar que el usuario elija (no recomendado)
def jacobi(matriz, constante, tol=1e-6, max_iter=100):
    #Preparacion de las variables
    matriz=matriz.copy()
    n = len(matriz)
    x = [0]*n
    x_new = [0]*n
    historial=[]
    ##Armado del encabezado
    Variables = ['z','y', 'x', 'w'] 

    #print(encabezado)
    #print("-" * len(encabezado))
    ######
    
    ##Calculo matematico

    for iteraciones in range(max_iter):
        for i in range(n):
            #Aca va sumando cada variable 
            suma = sum(matriz[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (constante[i] - suma) / matriz[i][i]
            historial.append(x_new[i])
        # Cálculo del error relativo
        
        error = max(abs(x_new[i] - x[i]) for i in range(n))
        
        # Imprime la iteracciones (genera la tabla)
        
        #fila = f"{iteraciones+1:<10}"  # Imprime el número de iteración
        #for i in range(n):
            #fila += f"{x_new[i]:>10.6f} "  # Imprime las variables con 6 decimales
        #fila += f"{error:>12.6f}"  # Imprime el error
        #print(fila)
        
        ######
        # Se analiza el error 
        if error < tol:
            #print(f"Convergió en {k+1} iteraciones.")
            # Ponder decimales a 5 y paso de 6.0 a 6
            return x_new,iteraciones,historial,True
        
        x = x_new.copy()
    #print("No convergió dentro del máximo de iteraciones.")
    return x_new,max_iter,historial,False

if __name__ == "__main__":
    
    """A = [
        [25, -0.9, -0.3],
        [3.7, -7.3, -0.1],
        [0.7, 0.1, -8.2],
    ]

    b = [20.2,-18.9,-56.4]"""
    A=[[2,1],
        [-1,2]]
    b=[1,7]



    solucion,iteraciones,historial,funciono=jacobi(A,b)
    print("Solución:",solucion) ##Redondea para arriba
