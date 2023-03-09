# Introducción
Proyecto final para principantes con el stack de Odoo, Docker, Docker Compose, Git y GitHub.

- [Introducción](#introducción)
- [Preparación del repo y del entorno](#preparación-del-repo-y-del-entorno)
  - [_Fork_ del repositorio original](#fork-del-repositorio-original)
  - [Creación de rama de desarrollo y clonación del repositorio en local](#creación-de-rama-de-desarrollo-y-clonación-del-repositorio-en-local)
  - [Instalación de extensiones útiles](#instalación-de-extensiones-útiles)
  - [Menú interactivo para el terminal](#menú-interactivo-para-el-terminal)
- [Primeros pasos para nuestro desarrollo](#primeros-pasos-para-nuestro-desarrollo)
  - [Inicialización de Odoo y creación de la primera base de datos](#inicialización-de-odoo-y-creación-de-la-primera-base-de-datos)
  - [Primer _commit_](#primer-commit)
  - [Copia de seguridad completa (código, configuración y datos)](#copia-de-seguridad-completa-código-configuración-y-datos)
  - [Resetear el estado de Odoo y PostgreSQL](#resetear-el-estado-de-odoo-y-postgresql)
  - [Comando _odoo scaffold_](#comando-odoo-scaffold)
  - [Deshacer cambios desde el último _commit_](#deshacer-cambios-desde-el-último-commit)
- [Próximos pasos...](#próximos-pasos)


# Preparación del repo y del entorno

## _Fork_ del repositorio original

Inicia sesión en tu cuenta de GitHub, haz un _fork_ de [javnitram/SGE-odoo-dev](https://github.com/javnitram/SGE-odoo-dev) y llama el tuyo SGE-odoo-dev-**XX** (el valor correspondiente a tu número de puesto, según el último byte de la dirección IP de clase.

![Fork](https://user-images.githubusercontent.com/1954675/214649968-b21af29d-8bfc-4f95-b117-f48c7506c9cf.png)

## Creación de rama de desarrollo y clonación del repositorio en local

En tu repositorio, además de tener una rama _main_ o _master_, crea una rama con tu nombre de GitHub seguido de **XX**, según el número que te corresponda por puesto en el aula. Esta será tu rama de desarrollo.

![Branch](https://user-images.githubusercontent.com/1954675/214651541-e8e95116-671a-472b-be09-970f98de78f7.gif)

Vas a usar esa rama para desarrollar tu propio módulo de Odoo. Para ello, deberás clonar la rama en local con Visual Studio Code.

Primero, si no lo has hecho anteriormente, deberás autorizar el acceso a GitHub desde Visual Studio Code.

![Autorizar GitHub en Visual Studio Code](https://user-images.githubusercontent.com/1954675/214658283-2563168c-9a89-4950-b5d8-3b492c748d0a.gif)

A continuación, clona el repositorio (es posible que GitHub te pida autorizar permisos adicionales)

![Git Clone](https://user-images.githubusercontent.com/1954675/214662378-484a9aaa-1be2-4ded-ac78-b3b997bc2fb7.gif)

Asegúrate de estar apuntando a la rama de desarrollo.

![Checkout](https://user-images.githubusercontent.com/1954675/214665198-03e8f2b6-670c-4384-9ced-557ea86e6632.gif)

Considera guardar tu workspace de Visual Studio Code.

## Instalación de extensiones útiles

En esta última entrega, vamos a prescindir de pgAdmin 4 y de las opciones del script ```./menu.sh``` para gestionar Docker Compose. En su lugar, hay que usar las extensiones oportunas de Visual Studio Code para sustituir dichas herramientas. Busca por estos identificadores, de modo que por cada uno encontrarás exactamente una extensión para instalar:


* ```jigar-patel.OdooSnippets```
* ```ms-python.python```
* ```ms-azuretools.vscode Docker```
* ```ckolkman.vscode-postgres```

Tras instalar estas extensiones, obtendrás nuevas funciones en Visual Studio Code, a las cuales puedes acceder rápidamente desde la paleta de comandos con el atajo ```Control + Shift + P```. Asimismo, también podrás observar dos nuevos iconos en la barra de actividad (a la izquierda), uno correspondiente a la extensión de Docker y otro a la de PostgreSQL, nos familiarizaremos con ellas durante las demostraciones en clase.

![iconos_barra_actividad](https://user-images.githubusercontent.com/1954675/214654250-62f53d6f-4200-4bf4-89fb-b20d320a1f95.gif)

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

Desde prácticas anteriores hemos usado estos scripts por necesidades de aula y para facilitarte las cosas mientras aprendías, pero es el momento de prescindir de estas ayudas tanto como puedas exprimir las funciones que te proporciona un IDE.

# Primeros pasos para nuestro desarrollo

## Inicialización de Odoo y creación de la primera base de datos

![Inicialización de Odoo](https://user-images.githubusercontent.com/1954675/214669540-193c94c0-81d8-451e-9cac-f8a8c3a03afd.gif)

Lanza los contenedores usando la extensión de Docker en Visual Studio. Desde la propia extensión puedes lanzar también tu navegador por defecto para conectar al servicio Odoo en su puerto expuesto.

Crea tu base de datos de Odoo con la configuración que consideres oportuna.

![Primera base de datos Odoo](https://user-images.githubusercontent.com/1954675/214677032-1a1958ef-8f9e-4942-9cdf-8a09673c50b5.png)

Como recuerdas de anteriores prácticas, es razonable que en ocasiones tengas problemas para acceder desde la máquina anfitriona a ficheros creados desde un contenedor (o viceversa). Cuando haya importantes cambios en el contenido de los volúmenes compartidos entre host y contenedores, ejecuta ```./set-permissions.sh```. 

Dicho script te orientará para que arranques los contenedores y vuelvas a invocarlo si es el único modo de recuperar el acceso completo. Esto es necesario en aquellos equipos en los que no podemos ser root ni ejecutar sudo.

## Primer _commit_

Al iniciar Odoo por primera vez y configurar nuestra primera base de datos, hemos asignado una _master password_. Como recuerdas, esta contraseña queda cifrada en el fichero de configuración ```odoo.conf```, que también se ha actualizado para eliminar comentarios. Todo esto hace que Git detecte que el fichero ha sido modificado respecto a su contenido previo. Puedes observar cómo el fichero queda en estado **M** (_Modified_, modificado) y comparar las diferencias producidas en la modificación. 

![Odoo conf modificado y diff](https://user-images.githubusercontent.com/1954675/214678982-2358dff2-57ab-47ed-a57d-6371750c886d.png)

La inicialización del servidor Odoo ha provocado muchos más cambios, pero este repositorio está configurado para sincronizar únicamente código y configuración, por lo que ningún _commit_ hará un _backup_ del estado de tu servidor Odoo ni del servidor de base de datos. Recuerda que un sistema de control de versiones no está para esas cosas y, por eso, se han configurado reglas específicas en ficheros _.gitignore_ en algunos directorios.

```bash
# Postgresql data
postgres/

# Backup
*.tgz
*.tar.gz

# Python byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

```

Haz tu primer _commit_ (esto es confirmar los cambios en el repositorio local de Git) y _push_ (sincronizar cambios locales hacia el repositorio remoto, en este caso GitHub).

## Copia de seguridad completa (código, configuración y datos)

Si necesitas hacer una copia de seguridad de tu directorio de trabajo, sin perder los datos que no se sincronizan con GitHub, tienes la opción de usar tar a través del script ```./menu.sh``` (como en prácticas anteriores).

## Resetear el estado de Odoo y PostgreSQL

Durante la práctica, si llegases a un punto muerto en el que tu instalación de Odoo o la base de datos PostgreSQL han quedado en un estado corrupto o irreparable, tienes la opción ```git clean -xfd``` en el script ```./menu.sh```. Esto fuerza el borrado de ficheros sin seguimiento (*untracked*, es decir, que todavía no han sido añadidos al control de versiones) y de ficheros ignorados según el fichero _.gitignore_ (en este caso el estado de Odoo y de su base de datos).

![git clean -xfd](https://user-images.githubusercontent.com/1954675/214683179-42151af4-9bc7-4e6a-90c4-ef113d344790.gif)

Usa esto en casos excepcionales, evita lanzarlo por error o sin entender sus implicaciones. Después de esto, tendrás que volver a ejecutar ```./set-permissions.sh```, reiniciar contenedores, inicializar tu servidor Odoo y crear de nuevo la base de datos.

## Comando _odoo scaffold_

Usando la extensión de Docker de Visual Studio Code, localiza la función que te permita abrir una shell en el contenedor de Odoo.

Dentro del contenedor, ejecuta:

```bash
odoo scaffold prueba /mnt/extra-addons
```

![odoo scaffold](https://user-images.githubusercontent.com/1954675/214684898-0bcdea9c-887e-4224-aba1-7e842a223883.gif)

Observa el contenido de ese directorio desde el propio contenedor y desde el volumen mapeado en el anfitrión. Este comando ha generado una estructura mínima de directorios y ficheros para agilizar el desarrollo de un módulo en Odoo. Explora el contenido del directorio _prueba_ desde Visual Studio Code, si tienes algún problema para modificar los ficheros, recuerda ejecutar ```./set-permissions.sh```.

## Deshacer cambios desde el último _commit_

Si pulsas en el icono de Git en la barra lateral de Visual Studio Code, verás que los directorios y ficheros que ha generado el comando ```odoo scaffold``` aparecen en estado **U** de *Untracked*, es decir, todavía no estarían teniendo seguimiento por esta herramienta y no se sincronizarían. Añádelos al control de versiones, observa que ya no se marcan con estado **U** sino **A** (_Added_, añadido).

![git add --all](https://user-images.githubusercontent.com/1954675/214686075-f0ce5798-161e-464c-acc2-8b713c8499e2.gif)

En lugar de hacer _commit_, prueba la opción ```git reset --hard HEAD``` del script ```./menu.sh```. Observa lo que sucede y piensa en qué caso te plantearías hacer algo tan radical. Haz las pruebas que necesites para averiguar en qué se diferencia de la opción ```git clean -xfd```.

![git reset --hard HEAD](https://user-images.githubusercontent.com/1954675/214687303-f6cb18c3-a810-45a5-bcca-ef19aad42376.gif)

# Próximos pasos...

Crea tu propio módulo de Odoo de acuerdo a los apuntes de clase y al enunciado de la práctica que se te ha proporcionado en el aula virtual.

Debes utilizar Git y GitHub. Para ello, se espera que hagas varios _commits_ y _pushes_ en tu rama de desarrollo y finalmente hagas un _merge_ a tu rama _main_ cuando hayas desarrollado y probado tu módulo.

Si finalizas tu desarrollo con éxito y aprovechas la potencia de Git y GitHub, podrás realizar un _pull request_, es decir, una petición al propietario del repositorio original para que valore tu propuesta e integre tus cambios (_merge_). Es especialmente conveniente que tu proyecto proporcione datos de demo o hagas un _export_ de la base de datos con ```pg_dump``` o alguna utilidad gráfica. 

Quien clone el repositorio original y despliegue el entorno podrá probar tu módulo y todos los otros que hayan quedado integrados.
