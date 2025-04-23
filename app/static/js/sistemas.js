//variable para almacenar el número de ecuaciones
let numEcuaciones = 0;
function mostrarError(texto) {
  const mensaje = document.getElementById('Mensaje_calcular');
  const flecha = document.getElementById('flechita');
  mensaje.innerHTML = texto;
  mensaje.style.display = 'block';
  mensaje.style.color= 'red'; 
  flecha.style.display = 'block';

}
function ocultarError() {
  const mensaje = document.getElementById('Mensaje_calcular');
  const flecha = document.getElementById('flechita');

  mensaje.innerHTML = '';
  mensaje.style.display = 'none';
  flecha.style.display = 'none';
}

function generarSistema() {
    const letras = ['x', 'y', 'z', 'w','v']; 
    const cantidad = parseInt(document.getElementById('cantidadEcuaciones').value);
    const contenedor = document.getElementById('sistemaContenedor');
    // Limpiar el mensaje de error anterior
    contenedor.innerHTML = '';
    ocultarError();

    numEcuaciones = cantidad; // Guardar el número de ecuaciones
    if (isNaN(cantidad) || cantidad < 2 || cantidad > 5) {
        mostrarError('Ingresa un numero valido entre 2 y 5');
        return;
    }
    for (let i = 0; i < cantidad; i++) {
        const fila = document.createElement('div');
        fila.classList.add('fila-sistema');
        fila.style.display = 'flex';
        fila.style.alignItems = 'center';
        fila.style.marginBottom = '10px';
        fila.style.gap = '5px';

        for (let j = 0; j < cantidad; j++) {
            const input = document.createElement('input');
            input.type = 'number';
            input.placeholder = letras[j];
            input.style.width = '60px';

            input.classList.add('input-sistema'); // 
            fila.appendChild(input);
        }

        fila.appendChild(document.createTextNode(' = '));

        const resultado = document.createElement('input');
        resultado.type = 'number';
        resultado.classList.add('input-sistema'); //
        fila.appendChild(resultado);  

        contenedor.appendChild(fila);
    }

    // Asegurarse de que el botón de calcular raíces tenga un event listener
  document.querySelector(".btn-raices").addEventListener("click", calcularRaices)
}

function calcularRaices() {
    ocultarError();
    
    // Obtener todas las filas del sistema
    const filas = document.querySelectorAll(".fila-sistema")
    // Obtener la cantidad de ecuaciones seleccionada;
    if (isNaN(numEcuaciones) || numEcuaciones < 2 || numEcuaciones > 5) {
      //alert("Primero debes generar un sistema de ecuaciones válido.")
      mostrarError('Primero debes generar un sistema valido');
      return
    }
  
    // Verificar que todas las filas tengan todos los campos completos
    let todosCompletos = true
  
    filas.forEach(fila => {
      const inputs = fila.querySelectorAll("input");
      inputs.forEach(input => {
          if (input.value === "") todosCompletos = false;
      });
    });
  
  
    if (!todosCompletos) {
      mostrarError('Porfavor, completa todos los campos');
      return
    }
  
    // Si todos los campos están completos, proceder con el cálculo
    const metodo = document.getElementById("metodo").value

    // Construir la matriz del sistema (coeficientes + resultados)
    const sistema = [];
    filas.forEach(fila => {
      const inputs = fila.querySelectorAll("input");
      const ecuacion = [];
      inputs.forEach(input => {
        ecuacion.push(parseFloat(input.value));
      });
      sistema.push(ecuacion);
    });

    // Crear el objeto a enviar
    const data = {
      expresion: sistema,
      metodo: metodo.charAt(0).toUpperCase()+ metodo.slice(1) //"Gauss"
    };

    // Enviar los datos al servidor con fetch
    fetch('/resolver_sistema', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(res => {
      if (res.funciono) {
        const mensaje = document.getElementById('Mensaje_calcular');
        const flecha = document.getElementById('flechita');
        mensaje.innerHTML = `
          <span>Procesando resultados...</span>
          <div class="barra-carga">
            <div class="barra-carga-interna"></div>
          </div>
        `;
        mensaje.style.color='white';
        mensaje.style.display = 'block';
        flecha.style.display = 'block';
        setTimeout(() => {
          mensaje.innerHTML = '¡Sistema resuelto con éxito!';
          mensaje.style.color = '#00ff88';
          flecha.style.display = 'none';
          setTimeout(() => {
              window.location.href = res.redirect;
          }, 800);
      }, 1300);
      } else {
        mostrarError('El sistema no se pudo resolver. Revisá los datos.');
      }
      
    })
    .catch(error => {
      console.error('Error al resolver el sistema:', error);
      mostrarError('Error inesperado en el servidor')
    });
  }
  // Asegurarse de que el botón de calcular raíces tenga un event listener cuando se carga la página
  document.addEventListener("DOMContentLoaded", () => {
    // Agregar event listener al botón de calcular raíces
    const btnRaices = document.querySelector(".btn-raices")
    if (btnRaices) {
      btnRaices.addEventListener("click", calcularRaices)
    }
  })

