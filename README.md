# tpl_automation_web_selenium_python
Proyecto base de automatización web con python y selenium.

Vamos a usar [Selenium con Python](https://selenium-python.readthedocs.io/getting-started.html) porque

* Puede controlar chrome, firefox, safari, en computadoras y móviles.
* Se programa fácil, sin funciones asíncronas ni verborrea.

## Lo básico

Podés ver ejemplos de cómo hacer distintas cosas en la carpeta ... "ejemplos" (¿sorprendidos?), algunos requieren pa_lib y los podés probar así desde la carpeta donde está este mismo archivo.

~~~
python -mejemplos.upload
python -mejemplos.react
~~~

## Como tests

Podés partir del ejemplo en tests/test_00_ejemplo.py

Fijate que extiende una clase BaseTest que está en pa_lib, y en esa se define si usas Chrome o Firefox para testear, tal vez tengas que cambiarlo según que webdrivers tengas instalados. Aquí están las [instrucciones](https://chromedriver.chromium.org/getting-started)

ToDo: armar un entorno docker o simplificar este despliegue.

Los tests se ejecutan con

~~~
python -m pytest
~~~

que busca todos los archivos cuyo nombre empiece con "test" 

## Grabar los tests desde el navegador

Hay [plugins para Chrome y Firefox](https://chromedriver.chromium.org/getting-started) que te permiten grabar los tests mientras usas una página o app. 

Después los podés guardar en un formato muy simple Y exportarlos como tests para python.

Suele ser conveniente mejorar el código generado

* cambiando la forma de encontrar los elementos ej. al texto que lee el usuario o alguna forma que siga funcionando aunque cambies el diseño
* eliminando las acciones que se grabaron pero no hacen falta
* agregando validaciones
