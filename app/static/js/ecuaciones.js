document.addEventListener('DOMContentLoaded', function () {
    const pantallaFuncion = document.getElementById('displayFuncion');
    const pantallaX0 = document.querySelector('.display-puntox');
    const pantallaY0 = document.querySelector('.display-puntoy');
    const inputH = document.getElementById('valorH');
    const inputN = document.getElementById('valorN');
    const botones = document.querySelectorAll('.btn-math, .btn-header, .btn-especial');
    const modo = document.getElementById('modo');
    const metodoRK = document.getElementById('metodoRK');
    const campoH = document.getElementById('campoH');
    const campoN = document.getElementById('campoN');
    const btnCalcular = document.getElementById('btnCalcular');

    let campoActivo = null;

    // Función para bloquear y registrar click
    function bloquearYRegistrar(campo) {
        campo.addEventListener('keydown', e => e.preventDefault());
        campo.addEventListener('paste', e => e.preventDefault());
        campo.addEventListener('click', () => campoActivo = campo);
    }

    // Aplica en todos
    [pantallaFuncion, pantallaX0, pantallaY0, inputH, inputN].forEach(bloquearYRegistrar);

    botones.forEach(boton => {
        boton.addEventListener('click', e => {
            if (!campoActivo) return alert('Por favor, seleccioná un campo.');
            const valor = e.target.textContent.trim();

            if (valor === "Del") {
                campoActivo.value = campoActivo.value.slice(0, -1);
            } else if (valor === "C") {
                campoActivo.value = '';
            } else {
                switch (valor) {
                    case 'sen': campoActivo.value += 'sin('; break;
                    case 'cos': campoActivo.value += 'cos('; break;
                    case 'tan': campoActivo.value += 'tan('; break;
                    case 'In': campoActivo.value += 'ln('; break;
                    case '√': campoActivo.value += '√('; break;
                    case '^': campoActivo.value += '^'; break;
                    case 'asen': campoActivo.value += 'asin('; break;
                    case 'acos': campoActivo.value += 'acos('; break;
                    case 'atan': campoActivo.value += 'atan('; break;
                    case 'X': campoActivo.value += 'x'; break;
                    case 'π': campoActivo.value += 'π'; break;
                    default: campoActivo.value += valor;
                }
            }
        });
    });

    modo.addEventListener('change', function () {
        campoH.style.display = 'none';
        campoN.style.display = 'none';
        if (this.value === 'h') campoH.style.display = 'block';
        if (this.value === 'n') campoN.style.display = 'block';
    });

    btnCalcular.addEventListener('click', function () {
        const funcion = pantallaFuncion.value.trim();
        const x0 = pantallaX0.value.trim();
        const y0 = pantallaY0.value.trim();
        const h = inputH.value.trim();
        const n = inputN.value.trim();
        const modoSeleccionado = modo.value;
        const metodoSeleccionado = metodoRK.value;

        if (!funcion) {
            alert('Por favor ingrese la función y\'');
            return;
        }
        if (x0 === '' || isNaN(x0)) {
            alert('X0 debe ser un número válido.');
            return;
        }
        if (y0 === '' || isNaN(y0)) {
            alert('Y0 debe ser un número válido.');
            return;
        }
        if (!metodoSeleccionado) {
            alert('Por favor seleccione un método.');
            return;
        }
        if (!modoSeleccionado) {
            alert('Por favor seleccione un modo.');
            return;
        }
        if (modoSeleccionado === 'h') {
            if (h === '' || isNaN(h)) {
                alert('h debe ser un número válido.');
                return;
            }
        } else if (modoSeleccionado === 'n') {
            if (n === '' || isNaN(n) || !Number.isInteger(Number(n)) || Number(n) <= 0) {
                alert('n debe ser un número entero positivo.');
                return;
            }
        }

        fetch('/calcular_ecuacion', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                funcion, x0, y0, h, n, modo: modoSeleccionado, metodo: metodoSeleccionado
            })
        })
        .then(res => res.text())
        .then(html => {
            document.open();
            document.write(html);
            document.close();
        })
        .catch(err => {
            console.error('Error:', err);
            alert('Ocurrió un error al procesar la solicitud.');
        });
    });
});


