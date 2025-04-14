classdef Metodo_Biseccion
    %clase biseccion

    properties
        funcion %atributos que se usaran
        error_max
        iteraciones_max
    end

    methods
        function obj = Metodo_Biseccion(expresion,error,iteraciones)
            %instanciar los atributos inicales
            obj.funcion = expresion;
            obj.error_max=error;
            obj.iteraciones_max=iteraciones;
        end

        function [res,encontrado] = encontrar_raiz(obj,a,b)% se carga el objeto y las variable
            cont=0;
            xr=(a+b)/2;
            while cont<obj.iteraciones_max
                cont=cont+1;
                f_xr=resultado(obj.funcion,xr);
                %disp(xr);
                if abs(f_xr)< obj.error_max ||(abs(a-xr)/2)<obj.error_max
                    res=truncar(xr,obj.error_max);
                    encontrado=true;
                    return;
                end
                f_a=resultado(obj.funcion,a);
                if (f_a*f_xr)>0
                    a=xr;
                    xr=b;
                else
                    b=xr;
                end
                xr=(a+xr)/2;
            end
            res=0;
            encontrado=false;
        end
    end
end