from Ecuacion_procesar import Ecuacion_procesar

def verificar_variables(vect):
    for j in range(len(vect)):
        x_cant=vect[j].count("x")
        cont=0
        for i in range(1,len(vect)+1):
            if f"x{i}" in vect[j]:
                #print(f"Se encontro la ecuacion x{i} en la ecuacion {vect[j]}")
                cont+=1
        if cont<x_cant:
            #print("error ecuacion: ", vect[j])
            return False
    return True

if __name__ == '__main__':
    vector = []
    vector.append("x1+x2")
    vector.append("x1+x2-x3")
    vector.append("x1-x2+x2")
    salir=verificar_variables(vector)
    print(salir)


