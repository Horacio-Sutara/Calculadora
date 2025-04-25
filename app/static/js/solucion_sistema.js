const formatearNumero = (num) => {
    const n = parseFloat(num);

    if (isNaN(n)) return "-";

    const factor = Math.pow(10, 6);
    const truncado = Math.trunc(n * factor) / factor;

    return Math.abs(truncado % 1) < 1e-10 ? truncado.toFixed(0) : truncado;
    };

window.onload = function () {
    const datos = JSON.parse(document.getElementById('datos').textContent);
    const { resultado, historial, funciono, metodo } = datos;

    // 1. Mostrar resultados en los <li> de la sección "Soluciones"
    const introPaso = document.getElementById('intro-paso');

    if (funciono) {
        introPaso.textContent = '¡El sistema se resolvió exitosamente! con el método ' + metodo;
    } else {
        introPaso.textContent = 'El sistema no se pudo resolver. Revisá los datos ingresados.';

    }
    const letras =["x","y","z","w","v"];
    // Crear dinámicamente los <li> según resultado
    const listaSoluciones = document.getElementById("lista-soluciones");
    listaSoluciones.innerHTML = ""; // Limpiar por si ya había algo

    resultado.forEach((valor, index) => {
        const li = document.createElement("li");
        const nombreVariable = letras[index]
        li.textContent = `${nombreVariable}= ${valor}`;
        listaSoluciones.appendChild(li);
    });
    const procedimiento = document.getElementById("Procedimiento");
    procedimiento.innerHTML = ""; // Limpiar lo que había   
    // Aca hace la generacion de la matrices si son estos 2 procedimientos
    if (metodo === "Gauss" || metodo === "Gauss-jordan") {
        // 2. Crear bloques pero no animarlos todavía
        const bloques = [];

        historial.forEach((matriz, index) => {
            const bloque = document.createElement("div");
            bloque.classList.add("bloque-matriz", "paso");

            const cuerpo = document.createElement("div");
            cuerpo.classList.add("matriz-cuerpo");

            matriz.forEach(fila => {
                const filaDiv = document.createElement("div");
                filaDiv.classList.add("fila");

                fila.forEach(valor => {
                    const celda = document.createElement("div");
                    celda.classList.add("celda");
                    celda.textContent = parseFloat(parseFloat(valor).toFixed(2));
                    filaDiv.appendChild(celda);
                });

                cuerpo.appendChild(filaDiv);
            });

            bloque.appendChild(cuerpo);

            // Flecha (si no es la última iteración)
            if (index < historial.length - 1) {
                const flecha = document.createElement("div");
                flecha.classList.add("flecha");
                flecha.textContent = "→";
                bloque.appendChild(flecha);
            }

            procedimiento.appendChild(bloque);
            bloques.push(bloque); // guardamos cada bloque
        });

        // 3. Mostrar de a uno con animación
        let i = 0;
        function mostrarPaso() {
            if (i < bloques.length) {
                bloques[i].classList.add("mostrar");
                i++;
                setTimeout(mostrarPaso, 200); // ajustá el tiempo si querés más lento o más rápido
            }
        }

        // inicia animación
        mostrarPaso();
        setTimeout(() => {
            const todasLasCeldas = document.querySelectorAll('.celda');
            let maxWidth = 0;
            todasLasCeldas.forEach(celda => {
                const ancho = celda.offsetWidth;
                if (ancho > maxWidth) maxWidth = ancho;
            });
            todasLasCeldas.forEach(celda => {
                celda.style.width = `${maxWidth}px`;
            });
        }, 0); // Esperamos un toque para que las celdas ya estén visibles
    //Los otros algoritmos
    } else {
        console.log(historial)
        const cantidadVariables = resultado.length; 
        // Historial viene como array plano
        const historialPlano = historial;

        // Agrupar historial en filas según la cantidad de variables
        const historialAgrupado = [];
        for (let i = 0; i < historialPlano.length; i += cantidadVariables) {
            const fila = historialPlano.slice(i, i + cantidadVariables).map(Number);
            historialAgrupado.push(fila);
        }

        // Crear tabla
        const tabla = document.createElement("table");
        tabla.classList.add("tabla-iteraciones");

        // Encabezado
        const thead = document.createElement("thead");
        const filaEncabezado = document.createElement("tr");

        const thIteracion = document.createElement("th");
        thIteracion.textContent = "Iteración";
        filaEncabezado.appendChild(thIteracion);

        for (let i = 0; i < cantidadVariables; i++) {
            const th = document.createElement("th");
            th.textContent = letras[i] || `Var${i + 1}`;
            filaEncabezado.appendChild(th);
        }

        thead.appendChild(filaEncabezado);
        tabla.appendChild(thead);

        // Cuerpo de la tabla
        const tbody = document.createElement("tbody");

        historialAgrupado.forEach((fila, index) => {
            const tr = document.createElement("tr");
        
            const tdIteracion = document.createElement("td");
            tdIteracion.textContent = index + 1;
            tr.appendChild(tdIteracion);
        
            for (let i = 0; i < cantidadVariables; i++) {
                const td = document.createElement("td");
            
                if (fila[i] !== undefined && fila[i] !== "") {
                    td.textContent = formatearNumero(fila[i]);
                } else {
                    td.textContent = "–";
                    td.style.color = "#bbb"; // gris para vacíos
                }
            
                tr.appendChild(td);
            }
        
            tbody.appendChild(tr);
        });

        tabla.appendChild(tbody);
        procedimiento.appendChild(tabla);
    }
}
