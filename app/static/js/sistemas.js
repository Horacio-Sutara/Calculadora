//variable para almacenar el número de ecuaciones
let numEcuaciones = 0;

function generarSistema() {
    const letras = ['X', 'X2', 'X3', 'X4','X5']; 
    const cantidad = parseInt(document.getElementById('cantidadEcuaciones').value);
    const contenedor = document.getElementById('sistemaContenedor');
    contenedor.innerHTML = '';

    const mensaje_calcular= document.getElementById('Mensaje_calcular');
    mensaje_calcular.innerHTML = ''; // Limpiar el mensaje de error anterior
    numEcuaciones = cantidad; // Guardar el número de ecuaciones
    if (isNaN(cantidad) || cantidad < 2 || cantidad > 5) {
        contenedor.innerHTML = '<p style="color:red;">Ingresá un número válido entre 2 y 5.</p>';
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

        const igual = document.createTextNode(' = ');
        fila.appendChild(igual);

        const resultado = document.createElement('input');
        resultado.type = 'number';
        resultado.style.width = '70px';

        resultado.classList.add('input-sistema'); //
        fila.appendChild(resultado);  

        contenedor.appendChild(fila);
    }
    // Asegurarse de que el botón de calcular raíces tenga un event listener
  document.querySelector(".btn-raices").addEventListener("click", calcularRaices)
}

function calcularRaices() {
    // Obtener la cantidad de ecuaciones seleccionada
    const contenedor = document.getElementById('Mensaje_calcular');
    contenedor.innerHTML = '';
    // Verificar si se ha generado un sistema
    if (isNaN(numEcuaciones) || numEcuaciones < 2 || numEcuaciones > 5) {
      //alert("Primero debes generar un sistema de ecuaciones válido.")
      contenedor.innerHTML = '<p style="color:red;">Primero debes generar un sistema de ecuaciones válido.</p>';
      return
    }
  
    // Obtener todas las filas del sistema
    const filas = document.querySelectorAll(".fila-sistema")

    // Verificar que todas las filas tengan todos los campos completos
    let todosCompletos = true
    const camposFaltantes = []
  
    filas.forEach((fila, indiceFila) => {
      const inputs = fila.querySelectorAll("input")
  
      // Cada fila debe tener cantidad + 1 inputs (los coeficientes + el resultado)
      if (inputs.length !== numEcuaciones + 1) {
        todosCompletos = false
        return
      }
  
      // Verificar que cada input tenga un valor
      inputs.forEach((input, indiceInput) => {
        if (input.value === "") {
          todosCompletos = false
  
          // Determinar qué campo falta
          let nombreCampo
          if (indiceInput < numEcuaciones) {
            nombreCampo = `X${indiceInput + 1 === 1 ? "" : indiceInput + 1} en ecuación ${indiceFila + 1}`
          } else {
            nombreCampo = `Resultado en ecuación ${indiceFila + 1}`
          }
  
          camposFaltantes.push(nombreCampo)
        }
      })
    })
  
    if (!todosCompletos) {
      // Mostrar mensaje de error con los campos faltantes
      //contenedor.innerHTML = '<p style="color:red;">Ingresá un número válido entre 2 y 5.</p>';
      contenedor.innerHTML = '<p style="color:red;">Por favor, completa todos los campos.</p>';
      return
    }
  
    // Si todos los campos están completos, proceder con el cálculo
    const metodo = document.getElementById("metodo").value
  
    // Aquí iría la lógica para calcular las raíces según el método seleccionado
    // Por ahora, solo mostramos un mensaje de éxito
    //alert(`Calculando raíces usando el método: ${metodo}`)
    

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
        window.location.href = res.redirect;
      } else {
        contenedor.innerHTML = '<p style="color:red;">El sistema no se pudo resolver. Revisá los datos.</p>';
      }
      
    })
    .catch(error => {
      console.error('Error al resolver el sistema:', error);
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