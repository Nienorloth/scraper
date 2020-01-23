# Web scraper

## Preámbulo
Se estima que en la actualidad (enero 2020) existen entre [1.7](https://www.internetlivestats.com/total-number-of-websites/) y [6](https://www.worldwidewebsize.com/) billones de páginas web en el mundo. Dentro de este universo digital tan grande y tan variado, ¿cómo aprovechar la gran cantidad de información que se genera y expone a través de internet de una manera eficiente?

Desde una perspectiva técnica, existen formas de optimizar el acceso y hasta la recolección de la información específica.
Por ejemplo, muchos sitios web cuentan con APIs por medio de las cuales podemos obtener y utilizar su información. Pero para aquellos que no, requerimos de otros métodos para poder obtener grandes cantidades de información que después podamos utilizar en nuestras aplicaciones o análisis de datos. Uno de esos métodos es el **web scraping**, que consiste en extraer, copiar y almacenar información de sitios web. La técnica busca transformar, a través de scripts, ciertos elementos sin estructura de los sitios web (por ejemplo los de HTML), lo que permitiría su almacenamiento (por ejemplo en bases de datos) y análisis. Aunque el **web scraping** es una técnica muy popular, no todos los sitios web permiten su uso.

## Introducción

Se desarrolló una herramienta de línea de comando (*CLI*) de **web scraping** que nos ayude con la **búsqueda de empleo**, obteniendo la información relevante sobre las vacantes en el área de nuestro interés que se encuentran en los motores de búsqueda de [Indeed](https://www.indeed.com.mx/) y [Computrabajo](https://www.computrabajo.com.mx/).

El objetivo de esta herramienta es tener acceso diariamente a la información de nuevas vacantes de nuestro interés en los dos sitios (o más) de manera automática.

## Consideraciones Generales

La herramienta se desarrolló en Python y se ejecuta mediante *CLI*.

Además, se hizo uso de [Requests](https://pypi.org/project/requests/) y de [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/), librerías de Python que, respectivamente, sirven para cargar páginas web y extraer datos del contenido no estructurado(HTML y XML).

También se utilizó la librería [argparse](https://docs.python.org/3/library/argparse.html) para la creación de la herramienta en línea de comandos utilizando argumentos en la *CLI* y banderas.

## Avances esperados

Se espera, al terminar el proyecto, contar con una herramienta de **web scraping** que se pueda correr en la línea de comandos y permita precisar argumentos para hacer búsquedas con los siguientes parámetros:

* el puesto, en una sola palabra clave,
* el lugar (estado, ciudad, región), también debe ser una sola palabra.

Se obtendrá un listado de vacantes que coincida con nuestros parámetros de búsqueda, y que incluya la siguiente información:

* título de la vacante,
* nombre de la compañía que la oferta,
* localidad de la vacante,
* Enlace para postular a la vacante.

Esta lista se mostrará en la línea de comandos.

## Hacker Edition

Una vez alcanzados los objetivos del proyecto, se pretende agregar más funciones:

* que la herramienta funcione con la paginación de los sitios web,
* agregar más sitios web,
* agregar la opción de filtrar las búsquedas por medio de una palabra clave,
* almacenar los resultados en un archivo .csv descargable.

## Uso






**Job scraper** también puede descargarse directamente de este repositorio: 

*Asegurarse de contar con una versión de [Python 3.6] (https://www.python.org/) o mayor, y con las librerías [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) y [requests](https://pypi.org/project/requests/)*


1. Dar click al botón *Clone or download*, y elegir la opción *DOWNLOAD ZIP*. Con esto se descargará una copia del archivo del proyecto en formato .zip.

2. Descomprimir el archivo .zip.

3. Abrir una terminal de comandos, y acceder al lugar donde se guardó el archivo descomprimido, que puede hacerse con la instrucción *cd*

      home$ cd ruta_a_carpeta_de_scrapers

4. Una vez en la ubicación del archivo, es necesario definir el lenguaje que usaremos (Python 3.6 o versiones posteriores) más el nombre del archivo que ejecutaremos (scraper.py) y las siguientes claves: -job seguida del tipo de trabajo que buscamos y -location con el lugar.

Un ejemplo del script completo es:

      home/ruta_a_carpeta_de_scrapers$ python3 scraper.py -job developer -location Guadalajara

5. Los resultados aparecerán en la consola.
