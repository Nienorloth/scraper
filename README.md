# Web scraper

## Preámbulo
Se estima que, en la actualidad (enero 2020), existen entre [1.7](https://www.internetlivestats.com/total-number-of-websites/) y [6](https://www.worldwidewebsize.com/) billones de páginas web en el mundo. Dentro de este universo digital tan grande y tan variado, ¿cómo aprovechar la gran cantidad de información que se genera y expone a través de internet de una manera eficiente?

Desde una perspectiva técnica, existen formas de optimizar el acceso y hasta recolección la información específica.
Por ejemplo, muchos sitios web cuentan con APIs por medio de las cuales podemos obtener y utilizar su información. Pero para aquellos que no, requerimos de otros métodos para poder obtener grandes cantidades de información para después utilizarla en nuestras aplicaciones o análisis de datos.

Otra manera eficiente para obtener información de internet es el **web scraping**, que consiste en extraer, copiar y almacenar información de sitios web. La técnica busca transformar, a través de scripts, ciertos elementos sin estructura de los sitios web (por ejemplo los de HTML), lo que permitiría su almacenamiento (por ejemplo en bases de datos) y análisis. Aunque el **web scraping** es una técnica muy popular, no todos los sitios web permiten su uso.

## Introducción

Se desarrollará una herramienta de línea de comando (*CLI*) de **web scraping** que nos ayude con la búsqueda de empleo, obteniendo la información relevante sobre las vacantes en el área de nuestro interés en [OCC Mundial](https://www.occ.com.mx/), sitio que permite esta práctica.

El objetivo es tener acceso diariamente a la información de nuevas vacantes de manera automática.

## Consideraciones Generales

El proyecto se desarrollará en Python y se pretende poder ejecutarlo mediante la línea de comandos.

Además, se hará uso de [Requests](https://pypi.org/project/requests/) y de [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/), librerías de Python que, respectivamente, sirven para cargar páginas web y para hacer extraer datos del contenido no estructurado (HTML y XML).

Otras librerías que se están considerando son:

* [argparse](https://docs.python.org/3/library/argparse.html) para la creación de la herramienta en línea de comandos.

Por el momento, se considera acceder solamente al sitio OCC Mundial porque es el que lo permite.

## Avances esperados

Se espera, al terminar el proyecto, contar con una herramienta de **web scraping** que se pueda correr en la línea de comandos, y permita precisar argumentos para hacer búsquedas con los siguientes parámetros:

* el puesto,
* el lugar (estado, ciudad, región),
* y quizá el sitio web a consultar.


El objetivo es obtener un listado de vacantes que coincida con nuestros parámetros de búsqueda, y que incluya la siguiente información:

* título de la vacante,
* nombre de la compañía que la oferta,
* fecha de publicación,
* localidad de la vacante.

Esta lista se mostrará en la línea de comandos.

## Hacker Edition



Una vez que la herramienta de web scraping esté lista, se pretende enviar la información obtenida a una base de datos en Mongo DB, donde se almacenará para posteriormente poder visualizarla en una interfaz web.

## Uso
