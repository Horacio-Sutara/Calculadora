function validar = verificar_funcion(funcion)
    try
        x=1;
        res=eval(funcion);
        validar=true;
    catch
        validar=false;
    end
end
    