document.addEventListener('DOMContentLoaded', () => {
    const data = localStorage.getItem("resultadoIntegral");

    if (!data) {
        alert("No hay datos de la integral. Por favor realizá un cálculo primero.");
        window.location.href = "/integrales";
        return;
    }

    const { resultado, metodo, a, b, n, funcion, historial,puntos} = JSON.parse(data);
    const resultadoFormateado = parseFloat(resultado.toFixed(6)).toString();

    document.getElementById("resultado").textContent = `Resultado: ${resultadoFormateado}`;
    document.getElementById("metodo").textContent = metodo;
    document.getElementById("intervalo").textContent = `[${a}; ${b}]`;
    document.getElementById("n").textContent = n;
    document.getElementById("funcion").textContent = funcion || "No disponible";

    const historialContainer = document.getElementById("tablaHistorialBody");

    // 1. Puntos de la función f(x)
    const x = [];
    const y = [];

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

            //cargar puntos en el grafico
            //x.push(formatNumber(intervalo[0],6));
            //y.push(formatNumber(intervalo[1],6)); // cambiá por tu f(x)
            
        });
        puntos.forEach((item, index) => {
            if (!Array.isArray(item) || item.length < 2) return;

            const [xValue, yValue] = item;
            x.push(xValue);
            y.push(yValue);
        });
        // 2. Trazado de la función completa
        const grafico_funcion = {
        x: x,
        y: y,
        type: 'scatter',
        mode: 'lines',
        name: 'f(x)',
        line: { color: 'blue' }
        };

        // 3. Área inicial vacía
        let xArea = [];
        let yArea = [];

        const grafico_area = {
        x: xArea,
        y: yArea,
        type: 'scatter',
        fill: 'tozeroy',
        fillcolor: 'rgba(255, 0, 0, 0.3)',
        line: { color: 'transparent' },
        name: 'Área bajo curva'
        };

        // 4. Dibujo inicial
        Plotly.newPlot('grafico', [grafico_funcion, grafico_area]);
        console.log("x:",x,"y:",y);
        // 5. Animación progresiva
        let i = 0;
        const paso = 5;
        const intervaloAnimacion  = setInterval(() => {
        if (i >= x.length) {
            // Asegurar que se agregue el último punto
            const nuevaAreaFinal = {
                ...grafico_area,
                x: x,
                y: y
            };
            Plotly.react('grafico', [grafico_funcion, nuevaAreaFinal]);
            clearInterval(intervaloAnimacion );
            return;
        }


        // Crear nuevas copias de los arrays hasta el índice actual
        const newX = x.slice(0, i);
        const newY = y.slice(0, i);

        const nuevaArea = {
            ...grafico_area,
            x: newX,
            y: newY
        };

        Plotly.react('grafico', [grafico_funcion, nuevaArea]);

        i += paso;
        }, 20); // velocidad
    } else {
        const row = document.createElement("tr");
        const td = document.createElement("td");
        td.colSpan = 3;
        td.textContent = "No hay historial disponible";
        row.appendChild(td);
        historialContainer.appendChild(row);
    }




});