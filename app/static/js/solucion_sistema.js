window.onload = function() {
    // Revisamos si funciono es verdadero o falso
    const contenedor = document.getElementById('Mensaje_calcular');

    if (funciono) {
        // Si funcionó, mostramos los resultados
        contenedor.innerHTML = '<p style="color:green;">¡El sistema se resolvió exitosamente!</p>';
        // Aquí puedes mostrar el resultado de la solución
        const resultadoHTML = resultado.map((valor, index) => {
            return `<p>x${index + 1} = ${valor}</p>`;
        }).join('');
        contenedor.innerHTML += resultadoHTML;

    } else {
        // Si no funcionó, mostramos un mensaje de error
        contenedor.innerHTML = '<p style="color:red;">El sistema no se pudo resolver. Revisá los datos ingresados.</p>';
        console.error('Error: El sistema no se pudo resolver.');
    }

    // Si quieres mostrar el historial
    const historialContenedor = document.getElementById('historial');
    if (historialContenedor && historial.length > 0) {
        let historialHTML = '<h3>Historial de la solución:</h3>';
        historial.forEach((matriz, index) => {
            historialHTML += `<p><strong>Iteración ${index + 1}:</strong> ${JSON.stringify(matriz)}</p>`;
        });
        historialContenedor.innerHTML = historialHTML;
    }
};
