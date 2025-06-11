const datos = JSON.parse(localStorage.getItem("datosIntegral"));

if (datos) {
    console.log("Datos en la página de solución:", datos);
    // Podés mostrar los datos en el DOM, por ejemplo:
    document.getElementById("resultado").textContent = "Resultado: " + datos.resultado;
    document.getElementById("metodo").textContent = "Método: " + datos.metodo;
    document.getElementById("intervalo").textContent = "Intervalo: [" + datos.a + ", " + datos.b + "]";
    document.getElementById("n").textContent = "Número de subintervalos: " + datos.n;
    // etc.
} else {
    console.log("No se encontraron datos");
}