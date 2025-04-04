from Metodo_biseccion import Metodo_biseccion
from Metodo_newton_raphson import Metodo_Newton_Raphson
from Metodo_secante import MetodoSecante
from Metodo_punto_fijo import Metodo_punto_fijo
from Metodo_regula_falsi import Metodo_regula_falsi

def Metodos(funcion, a, b, tol=1e-7, iteraciones=100):
    
    
    ecuacion=Metodo_Newton_Raphson(a,tol,funcion,iteraciones)
    res,funciona=ecuacion.calculo()
    a,b,raices,funciona=newton_raphson(funcion,a,b,tol,iteraciones,res,funciona)
    print("Raices ",raices)
    if funciona:
        print("raices: ",raices)

        return raices
    return raices

def newton_raphson(funcion,a,b,tol,iteraciones,res_1,funciona):
    raices=[]
    if funciona:
        if a<=res_1<=b:
            raices.append(res_1) 
        extremo_derecho=b
        extremo_izquierdo=a
        res_2,funciona=Metodo_Newton_Raphson(extremo_derecho,tol,funcion,iteraciones).calculo()

        resta=valor=(abs(a)+abs(b))*0.01
        while funciona:
            if res_2 not in raices and res_2/raices[-1]<(1-tol*100) and a<=res_2<=b:
                raices.append(res_2)
                resta=valor
            else: 
                resta*=2
            if res_2 in raices and res_2!=raices[-1] or res_1==res_2:
                break
            extremo_derecho=(extremo_derecho-resta)if (extremo_derecho-(resta))!=0 else -0.1
            if extremo_derecho<extremo_izquierdo:
                return extremo_izquierdo,extremo_derecho,raices,funciona
            res_2,funciona=Metodo_Newton_Raphson(extremo_derecho,tol,funcion,iteraciones).calculo()
            #print(extremo_izquierdo,extremo_derecho)
        funciona=True if extremo_izquierdo<extremo_derecho else False
        band=False
        while funciona:
            #print("divisiones")
            if res_1 not in raices and band==False and res_1/raices[0]<(1-tol*100) and a<=res_1<=b or res_1 not in raices and band and res_1/raices[-1]<(1-tol*100) and a<=res_1<=b :
                raices.append(res_1)
                band=True
                resta=valor
            else: resta*=2
            if res_1 in raices and res_1!=raices[-1]and res_1!=raices[0] or res_1==res_2 :
                return extremo_izquierdo,extremo_derecho,raices,funciona
            extremo_izquierdo=(extremo_izquierdo+resta)if (extremo_izquierdo+resta)!=0 else 0.1
            if extremo_derecho<extremo_izquierdo:
                return extremo_izquierdo,extremo_derecho,raices,funciona
            res_1,funciona=Metodo_Newton_Raphson(extremo_izquierdo,tol,funcion,iteraciones).calculo()
        #print(extremo_izquierdo, extremo_derecho,funciona,"   Raices encontradas: ",raices)
        return extremo_izquierdo,extremo_derecho,raices,funciona
    else:
        return a,b,raices,funciona
if __name__=='__main__':

    print("Metodos de busqueda de raices\n")
    funcion=input("Ingrese la funcion: ")
    a=float(input("Ingrese el extremo inferior: "))
    b=float(input("Ingrese el extremo superior: "))
    tol=float(input("Ingrese la tolerancia: "))
    iteraciones=int(input("Ingrese el numero de iteraciones: "))
    Metodos(funcion,a,b,tol,iteraciones)
            


