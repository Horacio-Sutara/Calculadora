document.addEventListener('DOMContentLoaded', () => {
    const pantalla = document.getElementById('pantalla');
    const botones = document.querySelectorAll('.btn-header, .btn-math');
    let vector = [""];

    botones.forEach(boton => {
        boton.addEventListener('click', () => {
            const valor = boton.textContent;

            // Traducimos funciones especiales a su formato para cálculo
            switch (valor) {
                case 'sen': pantalla.value += 'sin('; break;
                case 'cos': pantalla.value += 'cos('; break;
                case 'tan': pantalla.value += 'tan('; break;
                case 'exp': pantalla.value += 'exp('; break;
                case 'In': pantalla.value += 'ln('; break;
                case '√': pantalla.value += '√('; break;
                case '^': pantalla.value += '^'; break;
                case 'asen': pantalla.value += 'asin('; break;
                case 'acos': pantalla.value += 'acos('; break;
                case 'atan': pantalla.value += 'atan('; break;
                case 'X': pantalla.value += 'x'; break;
                default: pantalla.value += valor;
            }
            vector.push(pantalla.value);
        });
    });

    // Botón igual "="
    document.querySelector('.btn-especial-igual').addEventListener('click', () => {
        const expresionOriginal = pantalla.value;
    
        fetch('/resolver', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ expresion: expresionOriginal })
        })
        .then(response => response.json())
        .then(data => {
            if (data.resultado === 'Error') {
                pantalla.value = 'Error';
            } else {
                pantalla.value = data.resultado;
                vector=[data.resultado]
            }
        })
        .catch(error => {
            pantalla.value = 'Error';
            console.error("Fallo en la solicitud:", error); // ⬅️ Problema con la conexión, etc.
        });
    });
    

    // Botón Del
    document.querySelectorAll('.btn-especial')[0].addEventListener('click', () => {
        vector.pop();
        if (vector && vector.length > 0) {
            pantalla.value = vector[vector.length - 1];
        } else {
            pantalla.value = "";
        }

    });

    // Botón Clear (C)
    document.querySelectorAll('.btn-especial')[1].addEventListener('click', () => {
        pantalla.value = '';
        vector=[""];
    });
});

//Animaciones
document.querySelectorAll('.volver-btn').forEach(link => {
    link.addEventListener('click', function (e) {
        e.preventDefault(); // Evita la navegación inmediata

        const main = document.querySelector('.main-content');
        main.classList.add('fade-out');

        setTimeout(() => {
            window.location.href = this.href;
        }, 500); // Tiempo para que la animación termine
    });
});
