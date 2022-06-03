# Contextualizacion
Este proyecto es la solucion a un Assessment propuesto para ingresar al cargo de Asistente de Investigacion en la Universidad EAFIT. 
<br></br>

## El problema
El Assessment en concreto trataba sobre **emular el comportamiento de una planta de agua**.   
La planta poseeia una capacidad maxima y minima de agua, cuando la capacidad se reducia 
esta comenzaba a llenarse a una tasa aleatoria hasta alcanzar el nivel maximo nuevamente; 
a medida de que la planta se llenaba los quimicos se agotaban causando que se tuviera que comprar mas.

Los siguientes son objetivos que el programa debia de cumplir:
1. Notificar cuando se detectara que los quimicos para el tratamiento del agua de la planta se acabarian al dia siguiente.
2. Dar reportes diarios de: nivel del tanque, el total de quimicos usados, el precio de los quimicos usados, la maxima, minima y promedio turbidez del agua encontrada, 
el maximo, minimo y promedio nivel de almacenamiento del tanque, mediante graficas las cuales debian de descargarse en formato PDF.
3. Mostrar variables tales como: Nivel del tanque, pureza del agua del tanque, niveles de quimicos para el tratmiento del agua, entre otros en plataformas IoT; 
  en este proyecto en particular se uso UbiDots.
4.  Guardar los datos hallados en una base de datos, ya sea relacional o no relacional; para el proyecto se uso SQL Server.
<br></br>

## La solucion
Para dar solucion al objetivo 1 se calculaba cual era el gasto de quimicos esperado basado en el gasto de quimicos del dia anterior, se le restaba este esperado a la cantidad real, 
dado el caso de que no quedaran mas quimicos se lanzaba la alerta. El modulo [sistem.py](https://github.com/spuerta10/proyects/blob/main/water%20plant/sistem.py)
desarrolla el objetivo 1.

Los modulos [chemicals.py](), [ploting.py]() y [sistem.py]() desarrollan y dan solucion al objetivo 2.




## Los resultados