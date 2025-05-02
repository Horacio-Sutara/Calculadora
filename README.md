<h1>
  <img src="app/static/Image/icono-logo.svg" alt="BETAsolve Logo" width="40" style="vertical-align: middle;"/>
  BetaSolve
</h1>

**BetaSolve** es una aplicación web interactiva diseñada para resolver problemas matemáticos utilizando enfoques visuales y didácticos.

---

## 🎯 Objetivo

**BETAsolve** tiene como objetivo ofrecer una herramienta web simple, visual y educativa para resolver problemas matemáticos.  
La aplicación fue diseñada pensando en el usuario: con una interfaz intuitiva, estética agradable y un enfoque que prioriza la comprensión.  

Cada método numérico implementado no solo entrega resultados, sino que también **muestra el procedimiento paso a paso**, permitiendo al usuario entender cómo se llega a la solución y reforzar su aprendizaje.

---

## 👨‍💻 Equipo de Desarrollo

- **Frontend**
  - Aquiles Cancinos
  - María del Mar Pellicer

- **Backend**
  - Tomás Mollinedo
  - Horacio Sutara

---

## 🧩 Funcionalidades Principales

**BETAsolve** incluye 3 herramientas matemáticas:

<h3>
  <img src="app/static/Image/calculadora-icono.svg" alt="Calcluadora basica Logo" width="20" style="vertical-align: middle;"/>
  Calculadora basica
</h3>

Realiza operaciones aritméticas estándar y permite **evaluar funciones en un punto específico**, ideal para análisis rápidos.

<h3>
  <img src="app/static/Image/funcion-icono.svg" alt="Calculadora raices Logo" width="20" style="vertical-align: middle;"/>
  Calculadora de Busqueda de Raices
</h3>

Permite encontrar ceros de funciones usando 5 métodos numéricos:
  - Bisección
  - Punto Fijo
  - Newton-Raphson
  - Secante
  - Regula_falsi

  El usuario puede ingresar su función, definir un intervalo opcional y visualizar gráficamente las iteraciones y resultados.

<h3>
  <img src="app/static/Image/matriz-icono.svg" alt="Calculadora matrices Logo" width="20" style="vertical-align: middle;"/>
  Calculadora de Sistema de Ecuaciones
</h3>

Resuelve sistemas de hasta 5 incógnitas. El usuario puede **elegir el método deseado**:
  - Eliminación de Gauss
  - Gauss-Jordan
  - Seidel
  - Jacobi

Permite ingresar matrices, ver los pasos del proceso de resolución y las soluciones

---

## 🛠️ Tecnologías Usadas


<p align="center">
  <div style="display: inline-block; text-align: center; margin: 10px;">
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg" width="40"/><br/>
    <sub>HTML5</sub>
  </div>
  <div style="display: inline-block; text-align: center; margin: 10px;">
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg" width="40"/><br/>
    <sub>CSS3</sub>
  </div>
  <div style="display: inline-block; text-align: center; margin: 10px;">
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" width="40"/><br/>
    <sub>JavaScript</sub>
  </div>
  <div style="display: inline-block; text-align: center; margin: 10px;">
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="40"/><br/>
    <sub>Python</sub>
  </div>
  <div style="display: inline-block; text-align: center; margin: 10px;">
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/flask/flask-original.svg" width="40"/><br/>
    <sub>Flask</sub>
  </div>
  <div style="display: inline-block; text-align: center; margin: 10px;">
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/numpy/numpy-original.svg" width="40"/><br/>
    <sub>NumPy</sub>
  </div>
  <div style="display: inline-block; text-align: center; margin: 10px;">
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/matplotlib/matplotlib-original.svg" width="40"/><br/>
    <sub>Matplotlib</sub>
  </div>
</p>

---

## 🔧 Instalación y Ejecución

### ✅ Requisitos Previos

- Python 3.8 o superior
- pip
- Navegador web moderno (Chrome, Firefox, etc.)

---

### ⚙️ Configuración del Backend (Flask)

1. **Clonar el repositorio y navegar al directorio:**

```bash
git clone https://github.com/tu_usuario/betasolve.git
cd betasolve
```

2. **Crear y activar un entorno virtual:**
```bash
python -m venv venv

# En Windows:
venv\Scripts\activate
# En macOS/Linux:
source venv/bin/activate
```
3. **Instalar las dependencias**
```bash
pip install -r requirements.txt
```
4. **Iniciar el servidor Flask:**
```bash
python app.py
```
## Cómo se usa 
