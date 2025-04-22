// document.addEventListener('DOMContentLoaded', function () {
//     const pantallaFuncion = document.getElementById('displayFuncion');
//     const pantallaIntervalo = document.getElementById('displayIntervalo');
//     const botones = document.querySelectorAll('.btn-math, .btn-header, .btn-especial');

//     botones.forEach(function (boton) {
//         boton.addEventListener('click', function (e) {
//             const valor = e.target.textContent.trim();

//             // Si el valor es "Del", eliminamos el último carácter
//             if (valor === "Del") {
//                 pantallaFuncion.value = pantallaFuncion.value.slice(0, -1);
//             }
//             // Si el valor es "C", limpiamos ambos campos
//             else if (valor === "C") {
//                 pantallaFuncion.value = '';
//                 pantallaIntervalo.value = '';
//             }
//             // Si el valor es "=" (el cálculo), puedes procesar la operación
//             else if (valor === "=") {
//                 // Aquí puedes implementar la lógica de evaluación si se desea
//             }
//             // Si el valor es un número o carácter válido, lo agregamos al campo de la función
//             else {
//                 switch (valor) {
//                     case 'sen': pantallaFuncion.value += 'sin('; break;
//                     case 'cos': pantallaFuncion.value += 'cos('; break;
//                     case 'tan': pantallaFuncion.value += 'tan('; break;
//                     case 'exp': pantallaFuncion.value += 'exp('; break;
//                     case 'In': pantallaFuncion.value += 'ln('; break;
//                     case '√': pantallaFuncion.value += '√('; break;
//                     case '^': pantallaFuncion.value += '^'; break;
//                     case 'asen': pantallaFuncion.value += 'asin('; break;
//                     case 'acos': pantallaFuncion.value += 'acos('; break;
//                     case 'atan': pantallaFuncion.value += 'atan('; break;
//                     case 'X': pantallaFuncion.value += 'x'; break;
//                     default: pantallaFuncion.value += valor;
//                 }
//             }

//             // Volver a enfocar el input de la función para que siga recibiendo texto
//             pantallaFuncion.focus();
//         });
//     });
// });

//Ingresar los datos en los campos tocando en la calcu
document.addEventListener('DOMContentLoaded', function () {
    const pantallaFuncion = document.getElementById('displayFuncion');
    const pantallaIntervalo = document.getElementById('displayIntervalo');
    const botones = document.querySelectorAll('.btn-math, .btn-header, .btn-especial');
    const btnCalcularRaices = document.getElementById('btnCalcularRaices');


    // Detectar el campo activo cuando el usuario hace clic en los campos de entrada
    pantallaFuncion.addEventListener('click', function () {
        this.setAttribute('data-active', 'true');
        pantallaIntervalo.removeAttribute('data-active');
    });

    pantallaIntervalo.addEventListener('click', function () {
        this.setAttribute('data-active', 'true');
        pantallaFuncion.removeAttribute('data-active');
    });

    botones.forEach(function (boton) {
        boton.addEventListener('click', function (e) {
            const valor = e.target.textContent.trim();
            let campoActivo;

            // Identificar cuál campo está activo (función o intervalo)
            if (pantallaFuncion.hasAttribute('data-active')) {
                campoActivo = pantallaFuncion;
            } else if (pantallaIntervalo.hasAttribute('data-active')) {
                campoActivo = pantallaIntervalo;
            }

            // Si el campo activo es pantallaFuncion, agregamos el valor allí
            if (campoActivo === pantallaFuncion) {
                if (valor === "Del") {
                    pantallaFuncion.value = pantallaFuncion.value.slice(0, -1);
                } else if (valor === "C") {
                    pantallaFuncion.value = '';
                    pantallaIntervalo.value = '';
                } else if (valor === "=") {
                    // Aquí puedes implementar la lógica de evaluación si se desea
                } else {
                    switch (valor) {
                        case 'sen': pantallaFuncion.value += 'sin('; break;
                        case 'cos': pantallaFuncion.value += 'cos('; break;
                        case 'tan': pantallaFuncion.value += 'tan('; break;
                        case 'exp': pantallaFuncion.value += 'exp('; break;
                        case 'In': pantallaFuncion.value += 'ln('; break;
                        case '√': pantallaFuncion.value += '√('; break;
                        case '^': pantallaFuncion.value += '^'; break;
                        case 'asen': pantallaFuncion.value += 'asin('; break;
                        case 'acos': pantallaFuncion.value += 'acos('; break;
                        case 'atan': pantallaFuncion.value += 'atan('; break;
                        case 'X': pantallaFuncion.value += 'x'; break;
                        default: pantallaFuncion.value += valor;
                    }
                }
            }

            // Si el campo activo es pantallaIntervalo, agregamos el valor allí
            else if (campoActivo === pantallaIntervalo) {
                if (valor === "Del") {
                    pantallaIntervalo.value = pantallaIntervalo.value.slice(0, -1);
                } else if (valor === "C") {
                    pantallaIntervalo.value = '';
                } else {
                    pantallaIntervalo.value += valor;
                }
            }

            // Después de cada clic, volvemos a asegurarnos que el campo correcto mantenga el foco
            campoActivo.focus();
        });
    });

    //Enviar datos al back
    // Cuando el botón "Calcular Raíces" es presionado
    btnCalcularRaices.addEventListener('click', function() {
        // Capturar la función y el intervalo
        const funcion = pantallaFuncion.value.trim();
        const intervalo = pantallaIntervalo.value.trim();

        // Validación de los campos
        if (!funcion) {
            alert("Por favor ingresa una función.");
            return;
        }
        

        // if (intervalo.length !== 2 || isNaN(intervalo[0]) || isNaN(intervalo[1])) {
        //     alert("El intervalo debe tener el formato: 'inicio, fin'.");
        //     return;
        // }

        // Enviar los datos al backend usando fetch
        fetch('/calcular_raices', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                funcion: funcion,
                intervalo: intervalo  // Enviar el intervalo como array [inicio, fin]
            })
        })
        .then(response => response.text())
        .then(html => {
            document.open();
            document.write(html);
            document.close();
        })
        .catch(error => {
            console.error('Error:', error);
            alert('Ocurrió un error al procesar la solicitud.');
        });
    });
});