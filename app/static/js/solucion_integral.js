document.addEventListener('DOMContentLoaded', () => {
    const data = localStorage.getItem("resultadoIntegral");

    if (!data) {
        alert("No hay datos de la integral. Por favor realizá un cálculo primero.");
        window.location.href = "/integrales";
        return;
    }

    const { resultado, metodo, a, b, n, funcion } = JSON.parse(data);
    const resultadoFormateado = parseFloat(resultado.toFixed(6)).toString();
    document.getElementById("resultado").textContent = `Resultado: ${resultadoFormateado}`;
    document.getElementById("metodo").textContent = metodo;
    document.getElementById("intervalo").textContent = `[${a}; ${b}]`;
    document.getElementById("n").textContent = n;
    document.getElementById("funcion").textContent = funcion || "No disponible";
});