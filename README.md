# Juego de la Vida de Conway — Terminal Edition

Simulación en consola del clásico Juego de la Vida de John Conway, escrita en Python.  
Incluye patrones predefinidos, exportación de ciclos, y un modo educativo interactivo.

[![Run on Replit](https://replit.com/badge/github/CARLOSLHG/conway-juego-de-la-vida)](https://replit.com/github/CARLOSLHG/conway-juego-de-la-vida)  
[![Abrir en Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/CARLOSLHG/conway-juego-de-la-vida)

---

## ¿Qué hace este proyecto?

- Simula la evolución de una cuadrícula de celdas según las reglas del Juego de la Vida.
- Permite elegir patrones iniciales clásicos o generar el tablero aleatoriamente.
- Exporta las generaciones a archivos `.txt` y `.csv`.
- Incluye un modo educativo accesible mediante el parámetro `--readme`.

---

## Reglas del Juego de la Vida

1. Una celda viva con 2 o 3 vecinas vivas sobrevive.
2. Una celda muerta con exactamente 3 vecinas vivas nace.
3. En cualquier otro caso, la celda muere o permanece muerta.

---

## Cómo ejecutar

### Desde consola:
```bash
python vida.py <ancho> <alto> <prob_vida> <max_generaciones> <delay> <patron>
```

### Modo educativo:
```bash
python vida.py --readme
```

### Ejemplos:
```bash
python vida.py 40 20 0.4 50 0.2 glider
python vida.py 30 30 0.3 -1 0.1 random --export_txt salida.txt --export_csv salida.csv
```

---

## Patrones incluidos

- `random` — distribución aleatoria de celdas vivas
- `glider` — nave diagonal
- `lwss` — nave ligera horizontal
- `blinker` — oscilador lineal
- `toad` — oscilador de 4 celdas

---

## Exportación de datos

- `--export_txt archivo.txt` → genera una vista visual con caracteres
- `--export_csv archivo.csv` → exporta los datos binarios (0 = muerta, 1 = viva)

---

## Ejecutar en la nube

Puedes probar este proyecto directamente desde el navegador sin instalar nada:

[Replit](https://replit.com/github/CARLOSLHG/conway-juego-de-la-vida)  
[Gitpod](https://gitpod.io/#https://github.com/CARLOSLHG/conway-juego-de-la-vida)

---

## Licencia

Este proyecto está bajo la Licencia MIT. Puedes usarlo, modificarlo y distribuirlo libremente.

---

## Autor

Desarrollado por Carlos  
GitHub: https://github.com/CARLOSLHG
