function x_trunc = truncar(x, error)
    decimales=0;
    while error<1
        decimales=decimales+1;
        error=error*10;
    end
    x_trunc=round(x,decimales);
end