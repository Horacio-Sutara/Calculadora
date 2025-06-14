document.addEventListener("DOMContentLoaded", function () {
    const x_vals = JSON.parse(document.getElementById("x-data").textContent);
    const y_vals = JSON.parse(document.getElementById("y-data").textContent);

    const trace = {
        x: x_vals,
        y: y_vals,
        mode: 'lines+markers',
        type: 'scatter',
        name: 'Aproximación'
    };

    const layout = {
        title: 'Solución Aproximada de la EDO',
        xaxis: { title: 'x' },
        yaxis: { title: 'y' }
    };

    Plotly.newPlot('grafico', [trace], layout);
});
