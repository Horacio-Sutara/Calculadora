// === JS para calculadora de integrales ===
document.addEventListener('DOMContentLoaded', function () {
    const funcionInput = document.getElementById("funcionInput");
    const intervaloInput = document.getElementById("intervaloInput");
    const nInput = document.getElementById("nInput");
    const metodoSelect = document.getElementById("metodo");
    const btnCalcular = document.querySelector(".btn-raices");

    // ==== Enviar al backend ====
    btnCalcular.addEventListener("click", () => {
        const funcion = funcionInput.value.trim();
        const intervalo = intervaloInput.value.trim().replace(/[()]/g, '');
        const partes = intervalo.split(";").map(p => parseFloat(p.trim()));
        const n = parseInt(nInput.value);
        const metodo = metodoSelect.value;

        if (!funcion || partes.length !== 2 || isNaN(partes[0]) || isNaN(partes[1]) || isNaN(n)) {
            alert("Por favor completá correctamente todos los campos.");
            return;
        }

        const a = partes[0];
        const b = partes[1];

        if (a >= b) {
            alert("El límite inferior debe ser menor que el superior.");
            return;
        }

        fetch("/calcular_integral", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ funcion, metodo, a, b, n }),
        })
        .then(res => {
            if (!res.ok) throw new Error("Error al calcular");
            return res.json();
        })
        .then(data => {
            if (data.redirect) {
                localStorage.setItem("resultadoIntegral", JSON.stringify({
                    ...data,
                    funcion: funcion 
                }));
                window.location.href = data.redirect;
            } else {
                alert("No se recibió una redirección.");
            }
        })
        .catch(err => {
            console.error(err);
            alert("Hubo un error al calcular la integral.");
        });
    });

    // ==== Calculadora visual ====
    const botones = document.querySelectorAll('.btn-math, .btn-header, .btn-especial');
    let campoActivo = funcionInput;

    funcionInput.addEventListener('click', () => { campoActivo = funcionInput; });
    intervaloInput.addEventListener('click', () => { campoActivo = intervaloInput; });
    nInput.addEventListener('click', () => { campoActivo = nInput; });

    botones.forEach(boton => {
        boton.addEventListener('click', e => {
            const valor = e.target.textContent.trim();
            if (!campoActivo) return;

            if (valor === "Del") {
                campoActivo.value = campoActivo.value.slice(0, -1);
            } else if (valor === "C") {
                funcionInput.value = "";
                intervaloInput.value = "";
                nInput.value = "";
            } else {
                if (campoActivo === funcionInput) {
                    switch (valor) {
                        case 'sen': campoActivo.value += 'sin('; break;
                        case 'cos': campoActivo.value += 'cos('; break;
                        case 'tan': campoActivo.value += 'tan('; break;
                        case 'e': campoActivo.value += 'e'; break;
                        case 'In': campoActivo.value += 'ln('; break;
                        case '√': campoActivo.value += '√('; break;
                        case '^': campoActivo.value += '^'; break;
                        case 'asen': campoActivo.value += 'asin('; break;
                        case 'acos': campoActivo.value += 'acos('; break;
                        case 'atan': campoActivo.value += 'atan('; break;
                        case 'X': campoActivo.value += 'x'; break;
                        case 'π': campoActivo.value += '3.14159'; break;
                        default: campoActivo.value += valor;
                    }
                } else {
                    campoActivo.value += valor;
                }
            }

            campoActivo.focus();
        });
    });

    // ==== Bloquear inputs manualmente ====
    ["funcionInput", "intervaloInput", "nInput"].forEach(id => {
        const input = document.getElementById(id);
        input.addEventListener("keydown", e => e.preventDefault());
        input.addEventListener("paste", e => e.preventDefault());
    });

    // ==== Volver con animación ====
    document.querySelectorAll('.volver-btn').forEach(link => {
        link.addEventListener('click', function (e) {
            e.preventDefault();
            const main = document.querySelector('.main-contenido');
            main.classList.add('fade-out');
            setTimeout(() => {
                window.location.href = this.href;
            }, 500);
        });
    });
});