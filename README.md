# PlotTool_Grupo5 

## Mejoras implementadas
### Puntos y rectas

Se incorporó una nueva opción que permite al usuario graficar puntos y líneas rectas en los distintos plots para realizar anotaciones sobre un gráfico. Esta herramienta resulta muy util para casos en los que se desea marcar un valor de tensión pico, por ejemplo.
El programa permite ingresar puntos y lineas ya sea ingresando las coordenadas en una pestaña al seleccionar el boton "Add line or point" o bien clickeando sobre la pantalla donde se desea colocar un punto o una linea al seleccionar el botón "Draw line" o "Draw point". Estas lineas y puntos presentan distintas opciones de diseño como tamaño y color.

### Texto

Se añadió la posibilidad de agregar texto a los plots. Esta herramienta es compatible con código Latex (si se escribe una exprsión entre $$ se interpretará como una ecuación de Latex), a su vez presenta diversas configuraciones como tamaño de letra y color.

Otras features que tiene la herramienta de agregar texto son:
- Si hay más de un texto creado, cuando se selecciona uno de los mismos, la pestaña de add text se acutaliza según las propiedades de cada texto. Es decir, si un texto tiene tamaño de fuente 15, cuando se seleccione dicho texto, en la pesataña de add text aparecerá el tamaño de fuente en 15.
- Cuando se guarda y se carga un archivo, los textos son almacenados. Por diseño, los textos no se plotean automáticamente cuando se carga el archivo, sino que se encuentran almacenados en la pestaña de add text y se pueden volver a plotear presionando el botón de update.

### Funciones

Junto a la opción de crear funciones de transferencia, se encuentra una nueva herramienta la cual permite al usuario graficar funciones a través de expresiones matemáticas. Estas funciones mantienen las diversas opciones de diseño que el resto de datalines, tales como, tamaño, estilo de línea y color, a su vez incorporan nuevas transformaciones:
- Derivada de primer orden
- Derivada de segundo orden

Esto permite al usuario graficar curvas teóricas que pueden resultar útiles para comparar con gráficos medidos o simulados.
