document.addEventListener('DOMContentLoaded', function () {
    const rawData = document.getElementById('datos').textContent;
    const plotData = JSON.parse(rawData);
    //f(x)=x^2 evaluando en x=2
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

    // Obtener los límites del eje X
    const xMin = Math.min(...plotData.x);
    const xMax = Math.max(...plotData.x);
    min=xMax*-1;
    // Configurar el layout
    const layout = {
        title: `Gráfica de ${plotData.funcion}`,
        xaxis: { title: 'x' , 
        },
        yaxis: {
            title: 'f(x)',
            range: [min, xMax],  // Forzar a que Y tenga el mismo rango que X
        },
        showlegend: true
    };

    Plotly.newPlot('plotly-graph', [trace1, trace2], layout);
});
