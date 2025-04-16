## **Juego de la Vida \- en Python**

[![Run on Replit](https://replit.com/badge/github/CARLOSLHG/conway-juego-de-la-vida)](https://replit.com/github/CARLOSLHG/conway-juego-de-la-vida)
[![Abrir en Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/CARLOSLHG/conway-juego-de-la-vida)

### **¿Qué es el Juego de la Vida?**

El **Juego de la Vida** es un experimento matemático creado por el científico **John Conway** en 1970\. Se trata de un **autómata celular** que simula la evolución de una población de células en una cuadrícula.  
 Cada celda puede estar **viva(1)** ó **muerta(0)** y cambia su estado en cada generación según reglas simples basadas en las celdas vecinas.

Aunque no hay jugadores ni decisiones activas, el juego crea **comportamientos complejos y fascinantes**, como criaturas que se mueven, oscilan o se reproducen.

### **Reglas del juego**

En cada generación:

1.  **Supervivencia**: Una celda viva con 2 o 3 vecinas vivas sobrevive.

2.  **Soledad**: Una celda viva con menos de 2 vecinas vivas muere.

3.  **Sobrepoblación**: Una celda viva con más de 3 vecinas vivas muere.

4.  **Nacimiento**: Una celda muerta con exactamente 3 vecinas vivas se convierte en una celda viva.

### **Cómo usar este script**

#### **Ejecución básica:**

| python vida.py \<ancho\> \<alto\> \<prob\_vida\> \<max\_generaciones\> \<delay\> \<patron\> \[--export\_txt archivo.txt\] \[--export\_csv archivo.csv\] |
| :---- |

#### **Parámetros:**

| Parámetro | Descripción |
| ----- | ----- |
| `<ancho>` | Número de columnas del grid (ej: `30`) |
| `<alto>` | Número de filas del grid (ej: `15`) |
| `<prob_vida>` | Probabilidad inicial de que una celda esté viva (0.0 a 1.0) |
| `<max_generaciones>` | Número máximo de generaciones (`-1` para infinito) |
| `<delay>` | Tiempo entre generaciones (en segundos, ej: `0.2`) |
| `<patron>` | Patrón inicial (`random`, `glider`, `lwss`, `blinker`, `toad`) |
| `--export_txt` | (Opcional) Exporta la evolución visual en un `.txt` |
| `--export_csv` | (Opcional) Exporta los datos binarios en un `.csv` |

### **Ejemplos de uso:**

#### **🔹 Generación aleatoria infinita:**

| python vida.py 30 20 0.3 \-1 0.2 random |
| :---- |

#### **🔹 Simular una nave espacial (`glider`) durante 50 generaciones:**

| python vida.py 40 20 0.3 50 0.1 glider |
| :---- |

#### **🔹 Simulación y exportación a archivos:**

| python vida.py 50 25 0.5 100 0.1 lwss \--export\_txt resultado.txt \--export\_csv resultado.csv |
| :---- |

###  **Patrones disponibles:**

| Nombre | Tipo | Descripción |
| ----- | ----- | ----- |
| `random` | Aleatorio | Celdas vivas generadas al azar |
| `glider` | Nave | Se desplaza diagonalmente |
| `lwss` | Nave | Lightweight spaceship (horizontal) |
| `blinker` | Oscilador | Cambia entre 2 estados lineales |
| `toad` | Oscilador | Cambia entre 2 fases (2x3 celdas) |

### **Requisitos**

* Python 3.x

* Sistema operativo con soporte de terminal (Windows, Linux, macOS)

[![Run on Replit](https://replit.com/badge/github/CARLOSLHG/conway-juego-de-la-vida)](https://replit.com/github/CARLOSLHG/conway-juego-de-la-vida)
[![Abrir en Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/CARLOSLHG/conway-juego-de-la-vida)
