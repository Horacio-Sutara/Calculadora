document.getElementById("btnCalcularRaices").addEventListener("click", function () {
    const funcion = document.getElementById("funcionInput").value;
    const intervalo = document.getElementById("intervaloInput").value.split(';').map(v => parseFloat(v.trim()));
    const a = intervalo[0];
    const b = intervalo[1];
    const n = parseInt(document.getElementById("nInput").value);
    const metodo = document.getElementById("metodoInput").value;
    /*alert("Calculando la integral de la función: " + funcion + "\nMétodo: " + metodo + "\nIntervalo: [" + a + ", " + b + "]\nNúmero de subintervalos: " + n);
    */
    fetch('/calcular_integral', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            funcion: funcion,
            metodo: metodo,
            a: a,
            b: b,
            n: n
        })
    })
    .then(response => {
        if (!response.ok) throw new Error("Error del servidor");
        return response.json();
    })
    .then(data => {
        console.log("Datos recibidos:", data); // 🔍 Ver en consola

        // Guardarlos en localStorage si los querés usar en la nueva página
        localStorage.setItem("datosIntegral", JSON.stringify(data));

        // Redireccionar
        if (data.redirect) {
            window.location.href = data.redirect;
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Ocurrió un error al procesar la solicitud.');
    });

});
