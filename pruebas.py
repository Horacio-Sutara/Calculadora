from sympy import symbols,Eq ,sin,asin,acos,atan, cos, tan, exp, sympify,solve
def remplazar(texto):
    ecuaciones=[]
    cont=0
    for i in texto:
        save=texto
        if i == 'x':
            if save[cont-1]!='e':            
                save=save[:cont]+"y"+save[(cont+1):]
                ecuaciones.append(save)
        cont+=1
    ecuaciones.append(texto+"+x-y")
    return ecuaciones
ecuaciones=remplazar("x**2 + 10*cos(x) +exp(x)")

print(ecuaciones)

# Definir las variables simbólicas
x, y = symbols('x y')

def despejar_y(ecuacion_str):
    # Convertir la ecuación de string a expresión simbólica
    ecuacion = sympify(ecuacion_str)
    
    # Intentar despejar y en función de x
    solucion_y = solve(ecuacion, y)

    if len(solucion_y) == 0:
        print("No se puede despejar y en función de x.")
    elif len(solucion_y) > 1:
        aux = solucion_y[0]
        solucion_y[0] = solucion_y[1]
        solucion_y[1] = aux

    return solucion_y

# Llamar a la función con la ecuación en formato string
if len(ecuaciones)>5:
    print("usa otro metodo")
for i in ecuaciones:
    solucion = despejar_y(i)
    print(f"y en función de x: {solucion}")

