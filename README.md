# Introducción
Proyecto final para principantes con el stack de Odoo, Docker y Docker Compose.

**Este README está pendiente de actualización, sincroniza tu fork cuando encuentres cambios**

# Preparación del repo y del entorno

## Fork del repositorio original

Haz un fork de [este repositorio](https://github.com/javnitram/SGE-odoo-dev) y llama el tuyo SGE-odoo-dev-**XX** (el valor correspondiente a tu número de puesto, según el último byte de la dirección de IP de clase, entre el 11 y el 33).

## Crear nueva rama y clonar el repositorio en local

En tu repositorio, además de tener una rama main/master, crea una rama con tu nombre de GitHub seguido de **XX**, según el número que te corresponda por puesto en el aula.



Vas a usar esa rama para desarrollar tus propios módulos de Odoo. Para ello, deberás clonarla en local con Visual Studio Code.


## Instalación de extensiones útiles

En esta ocasión, vamos a prescindir de pgadmin4 y de las opciones de menú para gestionar Docker Compose. En su lugar, hay que usar las extensiones oportunas de VS Code para sustituir a dichas herramientas. Busca por estos identificadores, de modo que en cada caso la búsqueda deberá encontrar exactamente una extensión:

```
jigar-patel.OdooSnippets
ms-python.python
ms-azuretools.vscode Docker
ckolkman.vscode-postgres
```



Al instalar estas extensiones, obtendrás nuevas funciones en tu VS Code, a las cuales puedes acceder rápidamente desde la paleta de comandos con ```Control + Shift + P```. Asimismo, también podrás observar dos nuevos iconos en la barra lateral, uno correspondiente al plugin de Docker y otro al de PostgreSQL, nos familiarizaremos con ellos durante las demostraciones en clase.

## Menú interactivo para el terminal

Ejecuta el script ```menu.sh```:
```bash
./menu.sh
```

Si anteriormente no lo has usado, la primera vez se autoconfigurará. En ese caso te pedirá que cierres el terminal y vuelvas a abrir otro.
Regresa a la ruta de tu copia local del repositorio y vuelve a lanzar el menú.
Si no encuentra el paquete ```smenu```, puedes instalarlo (o pedir que lo hagan):
```bash
sudo apt install smenu -y
```

Ahora el menú debería ser interactivo:
```bash
./menu.sh
```

Puedes moverte por el menú utilizando los cursores o directamente el número de la opción que quieras ejecutar. Pulsa _Enter_ para ejecutar la selección.

Para asegurar un correcto acceso a los datos compartidos mediante volúmenes entre host y contenedores, antes de arrancar o detener contenedores, ejecuta el script que da permisos completos:
```bash
./set-permissions.sh
```

Si deseas añadir opciones al script ```menu.sh``` o documentar las que hay, edita este fichero en cualquier momento:
```bash
nano menu.txt
```

En cada línea que escribas asegúrate de que siga el patrón:
_```comando tabulador # comentario```_

Los cambios que introduzcas en ```menu.txt``` aparecerán como nuevas opciones en el menú interactivo. En prácticas anteriores hemos usado este menú para facilitarte las cosas mientras aprendías, pero es el momento de prescindir de él casi por completo. 

# Primeros pasos para nuestro desarrollo

## Creación de la primera base de datos en Odoo

Lanza los contenedores usando la extensión de Docker en Visual Studio. Desde la propia extensión puedes lanzar también tu navegador por defecto para conectar al servicio Odoo en su puerto expuesto.

Como recuerdas de anteriores prácticas, es razonable que en ocasiones tengas problemas para acceder desde la máquina anfitriona a ficheros creados desde un contenedor (o viceversa). Cuando haya importantes cambios en el contenido de los volúmenes compartidos entre host y contenedores, ejecuta ```set-permissions.sh```. 

Dicho script te orientará para que arranques los contenedores y vuelvas a invocarlo si es el único modo de recuperar el acceso completo. Esto es necesario en aquellos equipos en los que no podemos ser root ni ejecutar sudo.


## Primer commit

Al iniciar Odoo por primera vez y configurar nuestra primera base de datos, hemos asignado una Master Password, como recuerdas, esta queda cifrada en el fichero de configuración ```odoo.conf```.

Este repositorio está configurado para sincronizar únicamente código y configuración, por lo que ningún commit hará un backup del estado de tu servidor Odoo ni del servidor de base de datos. Recuerda que un sistema de control de versiones no está para esas cosas.

Haz tu primer commit (confirmar cambio de datos en el repositorio local) y push (confirmar cambios locales en el repositorio remoto).

## Copia de seguridad completa (código, configuración y datos)
Si necesitas hacer una copia de seguridad de tu directorio de trabajo, sin perder datos que no se sincronizan con GitHub, teniendo la opción de usar tar a través del script menu.sh (como en prácticas anteriores).

Durante la práctica, si llegases a un punto muerto en el que tu instalación de Odoo o la base de datos PostgreSQL está en un estado irreparable, en el script menu.sh tienes la opción ```git clean -xfd``` que fuerza el borrado de ficheros sin seguimiento (*untracked*, todavía no añadidos al control de versiones) e ignorados (*ignored*, en este caso el estado de Odoo y de su base de datos). Usa esto en casos excepcionales y teniendo en cuenta lo que supone.

# Siguientes pasos...

Usando la extensión de Docker de VS Code, localiza la función que te permita abrir una shell en el contenedor de Odoo.

```bash
odoo scaffold prueba /mnt/extra-addons
```

Observa el contenido de ese directorio desde el propio contenedor y desde el volumen mapeado en el anfitrión. ¿Qué ha hecho ese comando?

Si pulsas en el icono de Git en la barra lateral de GitHub, verás que los directorios y ficheros que ha generado el subcomando scaffold aparecen en estado **U** de *Untracked*, es decir, no estarían teniendo seguimiento todavía por esta herramienta y no se sincronizarían. Añádelos al control de versiones y observa con qué estado se marcan.

Haz commit (opcionalmente commit+push de estos cambios).

A continuación, vuelve a editar cualquiera de los ficheros, observa en qué estado quedan. Prueba la opción del script menu.sh ```git reset --hard HEAD``` y piensa en qué caso te plantearías hacer algo tan radical y en qué se diferencia de la opción ```git clean -xfd```.