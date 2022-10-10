<p align = "center">
<font size ="4.7px"><a href = "https://github.com/spuerta10/projects/blob/main/stores_sales_bi/recursos/traducciones/nombre_curso_espaniol.md">Español</a>
                                                                              |
<a href = "https://github.com/spuerta10/projects/blob/main/stores_sales_bi/README.md">English</a></font> 
</p>

# Contextualizacion
El presente proyecto es un entregable para la materia Introduccion a la Ingenieria en Ciencias de Datos de la carrera Ingenieria en Ciencias de Datos. El proposito del mismo es el de emular el flujo de trabajo que sigue un analista de datos, concretamente, un analista de datos de inteligencia empresarial (bussiness intelligence data analyst) a la hora de elaborar un tablero de BI.  

Los datos adquiridos para este proyecto son open source, los siguientes son enlaces para acceder a estos [Super Store Sales Dataset](https://www.kaggle.com/datasets/rohitsahoo/sales-forecasting), [Sample Sales Data](https://www.kaggle.com/datasets/kyanyoga/sample-sales-data) y [sales_data_samples(1).csv](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjnkdeF9cn6AhVsmIQIHYtvCSMQFnoECAgQAQ&url=https%3A%2F%2Fintersectjobsims.files.wordpress.com%2F2018%2F06%2Fsales_data_sample-1.xlsx&usg=AOvVaw14wOsod1qZzRAUjfwWpkeL)

El proyecto supone que los datos recopilados pertenecen a una compañia de retail, la cual vende productos de todo tipo al por menor, ademas de cierto tipo de vehiculos. 
<br></br>

## El Problema
El problema se hace evidente cuando en la compañia se plantean diferentes preguntas acerca de sus datos y se tiene que invertir gran cantidad de tiempo en hallarles una respuesta, o, en el peor de los casos, no se saben responder. 

Ademas, la compañia posee distintas fuentes de datos las cuales poseen formatos y estructuras diferentes complicando su integracion y visualizacion.

![](https://github.com/spuerta10/projects/blob/main/stores_sales_bi/recursos/imagenes_y_videos/etl_databases/extract_databases.png)

*Figura 1*. Fuentes de datos que posee la compañia
<br></br>

La compañia requiere de un tablero BI, el cual debera de permitir principalmente el analisis de las ventas a traves de los años. Dicho tablero debera de tener como minimo dos (2) secciones, una que permita el analisis de las ventas de su seccion de retail, la segunda debera de permitir el analisis de las ventas de su seccion de vehiculos.

Ambas secciones deberan de responder las siguientes preguntas:
1. ¿Cuanto dinero se ha generado?
2. ¿Cuantas unidades se han vendido?
3. ¿Se ha generado mas dinero con respecto al año pasado?
4. ¿Se han vendido mas unidades con respecto al año pasado?
5. ¿El tiempo de entrega de los productos (eficiencia) ha mejorado con respecto al del año pasado?
6. ¿Cuanto dinero se ha generado a traves de los años, meses y dias?
7. ¿Cuantas unidades han sido vendidas en los diferentes años, meses y dias?
8. ¿En cual pais se han vendido mas unidades?
9. ¿En que ciudad se han vendido mas unidades?
10. ¿Que categoria es la mas comprada?
11. ¿Cuanto tiempo estamos tardando en entregar las diferentes categorias?
12. ¿Cual es el producto mas vendido?
13. ¿Cuanto tiempo tardamos en entregar los productos?

<br></br>
Los lineamientos propuestos para la elaboracion de este proyecto se pueden encontrar en el siguiente enlace: [Lineamientos](https://github.com/spuerta10/projects/blob/main/stores_sales_bi/recursos/otros/guidelines.pdf)

<br></br>

## La solucion
Antes de pensar en una solucion particular para el problema debemos de entender los datos, las tablas uno (1) a tres (3) decriben con mayor profundidad los datos hallados en las diferentes fuentes de datos.

*Tabla 1*. Diccionario de datos de la fuente ukStore
| Nombre | Nombre de columna | Definicion | Tipo de dato |
|--------|-------------------|------------|--------------|
|Numero de factura |Invoice No |Identificador unico de factura generada al momento de la venta |BigInt 
|Numero de inventario |StockCode |Identificador unico del producto ligado al inventario |String  
|Descripcion |Description |Descripcion del producto vendido |String 
|Cantidad |Quantity |Cantidad de unidades vendidas |Int 
|Fecha de la factura |Invoice Date |Fecha de la venta |DateTime 
|Precio por unidad |Unit Price | Precio de la unidad vendida |Float 
|Identificacion del cliente |Customer ID |Identificador unico de cliente |BigInt
|Pais |Country |Pais en el que se vendio el producto |String

<br> </br>
*Tabla 2*. Diccionario de datos de la fuente carsWorldWide
| Nombre | Nombre de columna | Definicion | Tipo de dato |
|--------|-------------------|------------|--------------|
|Numero de orden |OrderNumber |Identificador unico de la orden |BigInt 
|Cantidad ordenada |QuantityOrdered |Cantidad de unidades ordenadas |Int  
|Precio por unidad |PriceEach |Precio de la unidad ordenada |Float 
|Linea de orden |OrderLineNumber |Identificador unico de la linea de orden |Int 
|Venta |Sales |Valor total de la venta |Float 
|Fecha de orden |OrderDate |Fecha en la que se hizo la orden |DateTime
|Estado |Status |Estado de la orden |String
|Quatrimestre |Qtr_ID |Identificador unico del quatrimestre en el que se solicito la orden |Int
|Mes |Month_ID |Identificador unico del mes en el que se solicito la orden |Int
|Año |Year_ID |Identificador unico del año en el que se solicito la orden |Int
|Unidad Vendida |ProductLine |Tipo de unidad vendida |String
|Codigo del producto |ProductCode |Identificador unico del producto |String
|Nombre del cliente |CustomerName |Nombre comercial de quien solicita la orden |String
|Telefono |Phone |Telefono celular de la persona que hizo la orden |String
|Direccion 1 |AddressLine1 |Direccion donde se enviara la orden |String
|Direccion 2 |AddressLine2 |Segunda direccion posible para el envio de la orden |String
|Ciudad |City |Ciudad donde se hizo la orden |String
|Estado |State |Estado de donde se hizo la orden |String
|Codigo Postal |PostalCode |Codigo postal de la zona donde se hizo la orden |Int
|Pais |Country |Pais donde se hizo la orden |String
|Territorio |Territory |Estado de la orden |String
|Apellido |ContactLastName |Apellido de la persona que hizo la orden |String
|Nombre |ContactFirstName |Nombre de la persona que hizo la orden |String
|Tamaño|DealSize |Tamaño de la orden |String

<br> </br>
*Tabla 3*. Diccionario de datos de la fuente retailWorldWide
| Nombre | Nombre de columna | Definicion | Tipo de dato |
|--------|-------------------|------------|--------------|
|Identificador de fila |RowID |Identificador unico de la fila |Int
|Identificador de la orden |OrderID |Identificador unico de la orden |String
|Fecha de orden |OrderDate |Fecha en la que se hizo la orden |DateTime
|Fecha de envio |ShipDate |Fecha en la que se envio la orden al cliente |DateTime
|Modo de envio |ShipMode |Modo en el que se envia la orden solicitada |String
|Identificacion del cliente |CustomerID |Identificador unico del cliente |String
|Nombre del cliente |CustomerName |Nombre del cliente que hizo la orden |String
|Segmento |Segment |Tipo de cliente que hace la orden |String
|Pais |Country |Pais donde se hizo la orden |String
|Ciudad |City |Ciudad donde se hizo la orden |String
|Estado |State |Estado de donde se hizo la orden |String
|Codigo Postal |PostalCode |Codigo postal de la zona donde se hizo la orden |Int
|Region |Region |Identificador unico de la orden |String  
|Identificacion del producto |ProductID |Identificador unico del producto |String
|Categoria |Category |Categoria del producto ordenado |String
|Sub Categoria |Sub-Category |Sub-categoria del producto ordenado |String
|Producto |ProductName |Nombre del producto ordenado |String
|Ventas |Sales |Valor total de la venta |Float    

<br> </br>
Una vez comprendidos los datos deberemos de implementar un proceso de ETL (extraccion, transformacion y carga) el cual, en primer lugar, extraiga los datos de las diferentes fuentes de datos existentes, transforme los datos a una estructura deseada y posteriormente los cargue a Power BI.

La siguiente figura expone la estructura que debera de ser seguida por los datos de salida del proceso de ETL.

![](https://github.com/spuerta10/projects/blob/main/stores_sales_bi/recursos/imagenes_y_videos/etl_databases/load_databases.png)
*Figura 2*. Estructura de los datos de salida del proceso de ETL.

<br></br>
Se puede acceder al proceso de ETL implementado a traves del siguiente link: [etl.ipynb](https://github.com/spuerta10/projects/tree/main/stores_sales_bi/codigo)
<br></br>

## Los resultados
Especificar los resultados del proyecto. ¿El enfoque tomado le dio solucion al problema? ¿Esta el proyecto terminado? ¿La solucion alcanzada tiene alguna mejora?
<br></br>

