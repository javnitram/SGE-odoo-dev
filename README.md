# Introducción
Proyecto final para principantes con el stack de Odoo, Docker, Docker Compose, Git y GitHub.

**Este README está pendiente de actualización, sincroniza tu fork cuando encuentres cambios**

# Preparación del repo y del entorno

## _Fork_ del repositorio original

Inicia sesión en tu cuenta de GitHub y haz un _fork_ de [javnitram/SGE-odoo-dev](https://github.com/javnitram/SGE-odoo-dev) y llama el tuyo SGE-odoo-dev-**XX** (el valor correspondiente a tu número de puesto, según el último byte de la dirección IP de clase.

## Creación de rama de desarrollo y clonación del repositorio en local

En tu repositorio, además de tener una rama _main_ o _master_, crea una rama con tu nombre de GitHub seguido de **XX**, según el número que te corresponda por puesto en el aula.



Vas a usar esa rama para desarrollar tu propio módulo de Odoo. Para ello, deberás clonar la rama en local con Visual Studio Code.


## Instalación de extensiones útiles

En esta última entrega, vamos a prescindir de pgAdmin 4 y de las opciones del script ```./menu.sh``` para gestionar Docker Compose. En su lugar, hay que usar las extensiones oportunas de Visual Studio Code para sustituir dichas herramientas. Busca por estos identificadores, de modo que por cada uno encontrarás exactamente una extensión para instalar:


* ```jigar-patel.OdooSnippets```
* ```ms-python.python```
* ```ms-azuretools.vscode Docker```
* ```ckolkman.vscode-postgres```




Tras instalar estas extensiones, obtendrás nuevas funciones en Visual Studio Code, a las cuales puedes acceder rápidamente desde la paleta de comandos con el atajo ```Control + Shift + P```. Asimismo, también podrás observar dos nuevos iconos en la barra lateral, uno correspondiente al plugin de Docker y otro al de PostgreSQL, nos familiarizaremos con ellos durante las demostraciones en clase.

## Menú interactivo para el terminal

Ejecuta el script ```./menu.sh```:
```bash
./menu.sh
```

Si anteriormente no has usado el script, la primera vez se autoconfigurará. En ese caso te pedirá que cierres el terminal y vuelvas a abrir otro.
Regresa a la ruta de tu copia local del repositorio y vuelve a lanzar el menú.
Si no se encuentra el paquete ```smenu```, puedes instalarlo (o pedir al profe que lo haga como root):
```bash
sudo apt install smenu -y
```

Ahora el menú debería ser interactivo:
```bash
./menu.sh
```

Puedes moverte por este menú utilizando los cursores o directamente el número de la opción que quieras ejecutar. Pulsa _Enter_ para ejecutar la selección.

Para asegurar un correcto acceso a los datos compartidos mediante volúmenes entre host y contenedores, antes de arrancar o detener contenedores, ejecuta el script que da permisos completos:
```bash
./set-permissions.sh
```

Si deseas añadir opciones al script ```./menu.sh``` o documentar las que hay, edita este fichero en cualquier momento:
```bash
nano menu.txt
```

Asegúrate de que cada línea que escribas siga el patrón:
_```comando tabulador # comentario```_

Los cambios que introduzcas en ```menu.txt``` aparecerán como nuevas opciones en el menú interactivo.

Desde prácticas anteriores hemos usado estos scripts por necesidades de aula y para facilitarte las cosas mientras aprendías, pero es el momento de prescindir de estas ayudas tanto como puedas.

# Primeros pasos para nuestro desarrollo

## Inicialización de Odoo y creación de la primera base de datos

Lanza los contenedores usando la extensión de Docker en Visual Studio. Desde la propia extensión puedes lanzar también tu navegador por defecto para conectar al servicio Odoo en su puerto expuesto.

Como recuerdas de anteriores prácticas, es razonable que en ocasiones tengas problemas para acceder desde la máquina anfitriona a ficheros creados desde un contenedor (o viceversa). Cuando haya importantes cambios en el contenido de los volúmenes compartidos entre host y contenedores, ejecuta ```./set-permissions.sh```. 

Dicho script te orientará para que arranques los contenedores y vuelvas a invocarlo si es el único modo de recuperar el acceso completo. Esto es necesario en aquellos equipos en los que no podemos ser root ni ejecutar sudo.

## Primer commit

Al iniciar Odoo por primera vez y configurar nuestra primera base de datos, hemos asignado una master password, como recuerdas, esta queda cifrada en el fichero de configuración ```odoo.conf```. Esto hace que Git detecte que el fichero ha sido modificado respecto a su contenido en el último _commit_. 

La inicialización del servidor Odoo ha provocado muchos más cambios, pero este repositorio está configurado para sincronizar únicamente código y configuración, por lo que ningún commit hará un backup del estado de tu servidor Odoo ni del servidor de base de datos. Recuerda que un sistema de control de versiones no está para esas cosas y, por eso, se han configurado reglas específicas en ficheros _.gitignore_.

Haz tu primer commit (confirmar cambio de datos en el repositorio local) y push (confirmar cambios locales en el repositorio remoto).

## Copia de seguridad completa (código, configuración y datos)

Si necesitas hacer una copia de seguridad de tu directorio de trabajo, sin perder datos que no se sincronizan con GitHub, tienes la opción de usar tar a través del script ```./menu.sh``` (como en prácticas anteriores).

## Resetear el estado de Odoo y PostgreSQL

Durante la práctica, si llegases a un punto muerto en el que tu instalación de Odoo o la base de datos PostgreSQL estáN en un estado corrupto o irreparable, tienes la opción ```git clean -xfd``` en el script ```./menu.sh```. Esto fuerza el borrado de ficheros sin seguimiento (*untracked*, es decir, que todavía no añadidos al control de versiones) de ficheros ignorados por determinadas reglas de un fichero _.gitignore_ (en este caso el estado de Odoo y de su base de datos).

Usa esto en casos excepcionales, evita lanzarlo por error o sin entender sus implicaciones. Después de esto, tendrás que volver a inicializar tu servidor Odoo.

## Comando _odoo scaffold_

Usando la extensión de Docker de Visual Studio Code, localiza la función que te permita abrir una shell en el contenedor de Odoo.

Dentro del contenedor, ejecuta:

```bash
odoo scaffold prueba /mnt/extra-addons
```

Observa el contenido de ese directorio desde el propio contenedor y desde el volumen mapeado en el anfitrión. Este comando ha generado una estructura mínima de directorios y ficheros para agilizar el desarrollo de un módulo en Odoo. Explora esta el contenido del directorio _prueba_ desde Visual Studio Code.

## Deshacer cambios desde el último _commit_

Si pulsas en el icono de Git en la barra lateral de Visual Studio Code, verás que los directorios y ficheros que ha generado el comando ```odoo scaffold``` aparecen en estado **U** de *Untracked*, es decir, todavía no estarían teniendo seguimiento por esta herramienta y no se sincronizarían. Añádelos al control de versiones, observa que ya no se marcan con estado **U** sino **A** (_added_, añadido).

En lugar de hacer _commit_, prueba la opción ```git reset --hard HEAD``` del script ```./menu.sh```. Observa lo que sucede y piensa en qué caso te plantearías hacer algo tan radical. Haz las pruebas que necesites para averiguar en qué se diferencia de la opción ```git clean -xfd```.

# Próximos pasos...

Crea tu propio módulo de Odoo de acuerdo a los apuntes de clase y al enunciado de la práctica que se te ha proporcionado en el aula virtual.

Si finalizas tu desarrollo con éxito y aprovechas la potencia de Git y GitHub, podrás realizar un _pull request_, es decir, una petición al propietario del repositorio original para que valore tu propuesta e integre tus cambios (_merge_). Es especialmente conveniente que tu proyecto proporcione datos de demo. 

Quien clone el repositorio original y despliegue el entorno podrá probar tu módulo y los de tus compañeros/as.