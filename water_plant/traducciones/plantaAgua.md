<p align = "center">
<font size ="4.7px"><a href = "https://github.com/spuerta10/projects/blob/main/recursos/traducciones/plantaAgua.md">Español</a>
                                                                              |
<a href = "https://github.com/spuerta10/projects/blob/main/water%20plant/waterplant.md">English</a></font> 
</p>

# Contextualizacion
Este proyecto es la solucion a un Assessment propuesto para ingresar al cargo de Asistente de Investigacion en la Universidad EAFIT. 
<br></br>

## El problema
El Assessment en concreto trataba sobre **emular el comportamiento de una planta de agua**.   
La planta poseeia una capacidad maxima y minima de agua, cuando la capacidad se reducia 
esta comenzaba a llenarse a una tasa aleatoria hasta alcanzar el nivel maximo nuevamente; 
a medida de que la planta se llenaba los quimicos se agotaban causando que se tuviera que comprar mas.

![](https://github.com/spuerta10/projects/blob/main/recursos/waterTreatmentPlant.jpg)

*Figura 1*. Planta de tratamiento de aguas residuales.
<br></br>

Los siguientes son **objetivos que el programa debia de cumplir:**
1. Notificar cuando se detectara que los quimicos para el tratamiento del agua de la planta se acabarian al dia siguiente.
2. Dar reportes diarios de: nivel del tanque, el total de quimicos usados, el precio de los quimicos usados, la maxima, minima y promedio turbidez del agua encontrada, 
el maximo, minimo y promedio nivel de almacenamiento del tanque, mediante graficas las cuales debian de descargarse en formato PDF.
3. Mostrar variables tales como: Nivel del tanque, pureza del agua del tanque, niveles de quimicos para el tratmiento del agua, entre otros en plataformas IoT; 
  en este proyecto en particular se uso UbiDots.
4.  Guardar los datos hallados en una base de datos, ya sea relacional o no relacional; para el proyecto se uso SQL Server.
<br></br>

## La solucion
El modulo [chemicales.py](https://github.com/spuerta10/projects/blob/main/water%20plant/code/chemicals.py) da ayuda a la solucion del objetivo dos (2); este modulo se encarga de calcular una estimacion del precio real de los quimicos usados en la planta
haciendo uso de tecnicas de web scraping, extrayendo el precio real de los quimicos de la pagina [Mercado Libre](https://www.mercadolibre.com.co/).  

Para dar solucion al objetivo uno (1) se calculaba cual era el gasto de quimicos esperado basado en el gasto de quimicos del dia anterior, se le restaba este esperado a la cantidad real, dado el caso de que no quedaran mas quimicos se lanzaba la alerta. El modulo [system.py](https://github.com/spuerta10/projects/blob/main/water%20plant/code/system.py) le da solucion a los objetivos  uno (1), dos (2), tres (3) y cuatro (4) ya que este es el modulo principal del programa encargado de orquestar las interacciones entre modulos.

Por su parte el modulo [ploting.py](https://github.com/spuerta10/projects/blob/main/water%20plant/code/ploting.py) se encarga de preparar las graficas que seran presentadas en los reportes, ayudando a la solucion del objetivo dos (2).

[db.py](https://github.com/spuerta10/projects/blob/main/water%20plant/code/db.py) es el modulo responsable de establecer una conexion con la base de datos para
el posterior alamacenamiento de los mismos. 
<br></br>

## Los resultados
El proyecto concluye satisfaciendo las necesidades plasmadas en los objetivos uno (1), dos (2), tres (3) y cuatro (4); sin embargo el programa presentaba
una mejora en el como se estaba calculando el tiempo transcurrido.
<br></br>
