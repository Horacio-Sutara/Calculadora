document.addEventListener('DOMContentLoaded', function () {
    // Leer el JSON del script con id "datos"
    const rawData = document.getElementById('datos').textContent;
    const plotData = JSON.parse(rawData);

    const trace1 = {
        x: plotData.x,
        y: plotData.y,
        type: 'scatter',
        name: `f(x) = ${plotData.funcion}`,
        line: { color: 'blue' }
    };

    const trace2 = {
        x: plotData.raices_x,
        y: plotData.raices_y,
        mode: 'markers',
        type: 'scatter',
        name: 'Raíces',
        marker: { color: 'red', size: 8 }
    };

    const layout = {
        title: `Gráfica de la función ${plotData.funcion}`,
        xaxis: { title: 'x' },
        yaxis: { title: 'f(x)' },
        showlegend: true
    };

    Plotly.newPlot('plotly-graph', [trace1, trace2], layout);
});
