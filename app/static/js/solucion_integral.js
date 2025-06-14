document.addEventListener('DOMContentLoaded', () => {
    const data = localStorage.getItem("resultadoIntegral");

    if (!data) {
        alert("No hay datos de la integral. Por favor realizá un cálculo primero.");
        window.location.href = "/integrales";
        return;
    }

    const { resultado, metodo, a, b, n, funcion, historial } = JSON.parse(data);
    const resultadoFormateado = parseFloat(resultado.toFixed(6)).toString();

    document.getElementById("resultado").textContent = `Resultado: ${resultadoFormateado}`;
    document.getElementById("metodo").textContent = metodo;
    document.getElementById("intervalo").textContent = `[${a}; ${b}]`;
    document.getElementById("n").textContent = n;
    document.getElementById("funcion").textContent = funcion || "No disponible";

    const historialContainer = document.getElementById("tablaHistorialBody");

    if (Array.isArray(historial)) {
        historial.forEach((item, index) => {
            if (!Array.isArray(item) || item.length < 2) return;

            const [intervalo, area] = item;
            const row = document.createElement("tr");

            const tdDesde = document.createElement("td");
            const tdHasta = document.createElement("td");
            const tdArea = document.createElement("td");

            function formatNumber(num, maxDecimals = 6) {
                // Convierte a número, corta decimales innecesarios, y remueve ceros finales
                const parsed = parseFloat(num);
                return parsed.toLocaleString('en-US', {
                    minimumFractionDigits: 0,
                    maximumFractionDigits: maxDecimals
                });
            }
            
            tdDesde.textContent = formatNumber(intervalo[0], 4);
            tdHasta.textContent = formatNumber(intervalo[1], 4);
            tdArea.textContent = formatNumber(area, 6);

            row.appendChild(tdDesde);
            row.appendChild(tdHasta);
            row.appendChild(tdArea);

            historialContainer.appendChild(row);
        });
    } else {
        const row = document.createElement("tr");
        const td = document.createElement("td");
        td.colSpan = 3;
        td.textContent = "No hay historial disponible";
        row.appendChild(td);
        historialContainer.appendChild(row);
    }
});