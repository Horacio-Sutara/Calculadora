from Metodo_biseccion import Metodo_biseccion
from Metodo_newton_raphson import Metodo_Newton_Raphson
from Metodo_secante import MetodoSecante
from Metodo_punto_fijo import Metodo_punto_fijo
from Metodo_regula_falsi import Metodo_regula_falsi
def Metodos(funcion, a, b, tol=1e-7, iteraciones=100):
    
    print("Metodo Raices multiples")
    ecuacion=Metodo_Newton_Raphson(a,tol,funcion,iteraciones)
    res,funciona=ecuacion.calculo_raices_multiples()
    a,b,raices,funciona=newton_raphson(funcion,a,b,tol,iteraciones,res,funciona,Metodo_Newton_Raphson,True)
    if funciona:
        print("raices: ",raices)

        return raices
    print(a,b)
    raices_encontradas=raices
    print("Metodo Newton Raphson")
    res,funciona=Metodo_Newton_Raphson(a,tol,funcion,iteraciones).calculo()
    a,b,raices,funciona=newton_raphson(funcion,a,b,tol,iteraciones,res,funciona,Metodo_Newton_Raphson)
    print("raices: ",raices, "raices_encontradas: ",raices_encontradas)

    raices=list(set(raices+raices_encontradas))
    if funciona:
        print("raices: ",raices)

        return raices
    #print("Raices ",raices)
    print(a,b)
    print("Metodo Secante")
    raices_encontradas=raices
    res,funciona=MetodoSecante(a,a+(abs(a)+abs(b))*0.1,tol,funcion,iteraciones).calcular()
    a,b,raices,funciona=newton_raphson(funcion,a,b,tol,iteraciones,res,funciona,MetodoSecante,tipo=2)
    print("raices: ",raices, "raices_encontradas: ",raices_encontradas)

    raices=list(set(raices+raices_encontradas))
    if funciona:
        print("raices: ",raices)

        return raices
    print(a,b)
    print("Metodo punto fijo")
    res,funciona=Metodo_punto_fijo(a,tol,funcion,iteraciones).calculo()
    a,b,raices,funciona=newton_raphson(funcion,a,b,tol,iteraciones,res,funciona,Metodo_punto_fijo)
    print("raices: ",raices, "raices_encontradas: ",raices_encontradas)

    raices=list(set(raices+raices_encontradas))
    if funciona:
        print("raices: ",raices)

        return raices

    return raices

def newton_raphson(funcion,a,b,tol,iteraciones,res_1,funciona,metodo, tipo=0):
    raices=[]
    if funciona:
        #print(res_1)
        if a<=res_1<=b:
            raices.append(res_1) 
        extremo_derecho=b
        extremo_izquierdo=a
        resta=valor=(abs(a)+abs(b))*0.005
        #print("resta: ",resta)

        if tipo ==0:
            res_2,funciona=metodo(extremo_derecho,tol,funcion,iteraciones).calculo() 
        elif tipo==1:
            res_2,funciona=metodo(extremo_derecho,tol,funcion,iteraciones).calculo_raices_multiples()
        elif tipo==2:
            extremo_izquierdo=b-resta
            res_2,funciona=metodo(extremo_izquierdo,extremo_derecho,tol,funcion,iteraciones).calcular() 
        
        while funciona:
            if res_2 not in raices and res_2/(raices[-1]if len(raices)>1 else (res_2*2) )<(1-tol*100) and a<=res_2<=b:
                raices.append(res_2)
                resta=valor
            else: 
                resta*=2
            if res_2 in raices and res_2!=(raices[-1]if len(raices)!=0 else "") or res_1==res_2:
                break
            if tipo<2:
                extremo_derecho=(extremo_derecho-resta)if (extremo_derecho-(resta))!=0 else -0.1
            else:
                
                if (extremo_derecho-(resta))!=0:
                    extremo_derecho=(extremo_derecho-resta)
                    extremo_izquierdo=(extremo_izquierdo-resta) 
                else:
                    extremo_derecho=-0.1
                    extremo_izquierdo=-0.2
                
            if extremo_derecho<=a:
                return a,extremo_derecho,raices,funciona
            
            if tipo==0:
                res_2,funciona=metodo(extremo_derecho,tol,funcion,iteraciones).calculo() 
            elif tipo==1: 
                res_2,funciona=metodo(extremo_derecho,tol,funcion,iteraciones).calculo_raices_multiples()
            else:
                res_2,funciona=metodo(extremo_izquierdo,extremo_derecho,tol,funcion,iteraciones).calcular() 
        funciona=True if a<extremo_derecho else False
        b=extremo_derecho
        resta=valor if funciona else resta
        if funciona and tipo==2:
            extremo_izquierdo=a
            extremo_derecho=a+resta
        #print("resta: ",resta)

        band=False
        band_derecha=False
        while funciona:
            band_derecha=True
            #print("divisiones")
            if res_1 not in raices and band==False and res_1/(raices[0]if len(raices)>1 else res_1*2)<(1-tol*100) and a<=res_1<=b or res_1 not in raices and band and res_1/raices[-1]<(1-tol*100) and a<=res_1<=b :
                raices.append(res_1)
                band=True
                resta=valor
            else: 
                resta*=2
            if res_1 in raices and res_1!=(raices[-1]if len(raices)!=0 else "")and res_1!=(raices[0]if len(raices)!=0 else "") or res_1==res_2 and extremo_izquierdo>b :
                #print("la caque")
                return extremo_izquierdo,extremo_derecho,raices,funciona
            if tipo<2:
                extremo_izquierdo=(extremo_izquierdo+resta)if (extremo_izquierdo+resta)!=0 else 0.1
                res_1,funciona=metodo(extremo_izquierdo,tol,funcion,iteraciones).calculo() if tipo==0 else metodo(extremo_izquierdo,tol,funcion,iteraciones).calculo_raices_multiples()
            else:
                if (extremo_izquierdo+resta)!=0:
                    extremo_izquierdo+=resta
                    extremo_derecho+=resta
                else:
                    extremo_izquierdo=0.1
                    extremo_derecho=0.2
                res_1,funciona=metodo(extremo_izquierdo,extremo_derecho,tol,funcion,iteraciones).calcular() 
            if b<extremo_izquierdo:
                if tipo<2:
                    return extremo_izquierdo,extremo_derecho,raices,funciona
                else:
                    return extremo_izquierdo,b,raices,funciona
            #print(extremo_izquierdo,b)
        #print(extremo_izquierdo, extremo_derecho,funciona,"   Raices encontradas: ",raices)
        return extremo_izquierdo if funciona else extremo_izquierdo- resta,extremo_derecho if funciona else extremo_derecho if band_derecha else extremo_derecho+ resta,raices,funciona
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
            


