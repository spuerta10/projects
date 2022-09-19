<p align = "center">
<font size ="4.7px"><a href = "https://github.com/spuerta10/projects/blob/main/recursos/traducciones/plantaAgua.md">Español</a>
                                                                              |
<a href = "https://github.com/spuerta10/projects/edit/main/water%20plant/waterplant.md">English</a></font> 
</p>

# The context
This project is the solution to an Assessment proposed for entering Reaseach Assitant charge at EAFIT University.
<br></br>

## The problem
The Assessment in concrete was about **emulating the procesess happening at a water treatment facility**.
The water plant had a maximum and minimum capacity, when the capacity got reduced the plant began to full with water at a random pase until the maximum level was reached again;
in the process of the plant fulling itself chemicals were used to purify the water causing new chemicales had to be bought.

![](https://github.com/spuerta10/projects/blob/main/recursos/waterTreatmentPlant.jpg)

*Figure 1*. Water treatment facility.
<br></br>

The following are requisites that the program had to fullfil:
1. Notify when the chemicals used for the water treatment would run out the next day.
2. Give daily reports about: thank level, total amount of chemicals used, price of the chemicals used, maximum, minimum and mean water turbidity found,maximum, minimum and mean
tank level, torugh graphs that had to be downloaded in PDF format. 
3.  Show the following variables through a IoT plataform: tank level, waters tank purity, chemicals levels left for water treatment. 
For this project [UbiDots](https://ubidots.com/) was used for displaying the data.
4. Save the acquired data in a relational or non - relational data base. For this project SQL Server was chosen. 
<br></br>

## The solution
The module [chemicals.py](https://github.com/spuerta10/projects/blob/main/water%20plant/code/chemicals.py) helps solving requisite number two (2); this module calculates an estimate of the chemicals real price applying web scraping techniques
getting the actual price from [Mercado Libre's](https://www.mercadolibre.com.co/) page.

To solve objective one (1) an spected chemicals expense was calculated based on yesterday's chemical expense then from the real chemical capacity was substracted the expected 
expenses, in case there were no more chemicals left a notification was thrown. The module [system.py](https://github.com/spuerta10/projects/blob/main/water%20plant/code/system.py)
solves objectives one (1), two (2), three (3) and four (4) due to this model is responsible for managing interactions between modules. 

[ploting.py](https://github.com/spuerta10/projects/blob/main/water%20plant/code/ploting.py) is responsible of ploting the graphs that will be present in the following reports,
solving objective number two (2).

[db.py](https://github.com/spuerta10/projects/blob/main/water%20plant/code/db.py) is the module responsible for establishing a connection with the selected data base for srtoring the colected data.
<br></br>

## The results
The project concludes satisfing requirements one (1), two (2), three (3) and four (4); it's important to mention that the program present an upgrade
concerning how the time elapsed was being calculated.
<br></br>
