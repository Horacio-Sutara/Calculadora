function generarSistema() {
    const letras = ['x', 'y', 'z', 'w']; 
    const cantidad = parseInt(document.getElementById('cantidadEcuaciones').value);
    const contenedor = document.getElementById('sistemaContenedor');
    contenedor.innerHTML = '';

    if (isNaN(cantidad) || cantidad < 2 || cantidad > 4) {
        contenedor.innerHTML = '<p style="color:red;">Ingresá un número válido entre 2 y 4.</p>';
        return;
    }

    for (let i = 0; i < cantidad; i++) {
        const fila = document.createElement('div');
        fila.classList.add('fila-sistema');
        fila.style.display = 'flex';
        fila.style.alignItems = 'center';
        fila.style.marginBottom = '10px';
        fila.style.gap = '5px';

        for (let j = 0; j < cantidad; j++) {
            const input = document.createElement('input');
            input.type = 'number';
            input.placeholder = letras[j];
            input.style.width = '50px';

            input.classList.add('input-sistema'); // 
            fila.appendChild(input);
        }

        const igual = document.createTextNode(' = ');
        fila.appendChild(igual);

        const resultado = document.createElement('input');
        resultado.type = 'number';
        resultado.style.width = '60px';

        resultado.classList.add('input-sistema'); //
        fila.appendChild(resultado);  

        contenedor.appendChild(fila);
    }
}