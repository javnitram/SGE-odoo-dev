# Introducción
Proyecto final para principantes con el stack de Odoo, Docker y Docker Compose. Haz un fork de este repositorio y desarrolla sobre el tuyo.

# Primeros pasos

En tu repositorio, haz una rama con tu nombre de GitHub seguido de **XX** (el valor correspondiente a tu número de puesto, según el último byte de la dirección de IP de clase, entre el 11 y el 33).

Usa esa rama para desarrollar tus propios módulos de Odoo. Para ello, deberás clonarla en local con Visual Studio Code. En esta ocasión, vamos a prescindir de pgadmin4 y de las opciones de menú para gestionar Docker Compose. En su lugar, hay que usar las extensiones oportunas de VS Code para sustituir a dichas herramientas.

```
ext install jigar patel.OdooSnippets
ext install ms python.python
ext install ms azuretools.vscode Docker
ext install ckolkman.vscode postgres
```

Al instalar estas extensiones, obtendrás nuevas funciones en tu VS Code, a las cuales puedes acceder rápidamente desde la paleta de comandos con ```Control + Shift + P```. Asimismo, también podrás observar dos nuevos iconos en la barra lateral, uno correspondiente al plugin de Docker y otro al de PostgreSQL, nos familiarizaremos con ellos durante las demonstraciones en clase.

Ejecuta el script ```menu.sh```, la primera vez se autoconfigurará:
```bash
./menu.sh
```

Te pedirá que cierres el terminal y vuelvas a abrir otro.
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

Para asegurar un correcto acceso a los datos compartidos
mediante volúmenes entre host y contenedores, antes de arrancar o detener contenedores, ejecuta el script que da permisos completos:
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

# Creación de la primera base de datos en Odoo y backup del entorno

Lanza los contenedores usando la extensión de Docker en Visual Studio. Desde la propia extensión puedes lanzar también tu navegador por defecto para conectar al servicio Odoo en su puerto expuesto.

Como recuerdas de anteriores prácticas, es razonable que en ocasiones tengas problemas para acceder desde la máquina anfitriona a ficheros creados desde un contenedor (o viceversa). Cuando haya importantes cambios en el contenido de los volúmenes compartidos entre host y contenedores, ejecuta ```set-permissions.sh```. 

Dicho script te orientará para que arranques los contenedores y vuelvas a invocarlo si es el único modo de recuperar el acceso completo. Esto es necesario en aquellos equipos en los que no poder ser root ni ejecutar sudo.

Este repositorio está configurado para sincronizar únicamente código y configuración, por lo que ningún commit hará un backup del estado de tu servidor Odoo ni de la base de datos. Para ello, sigues teniendo la opción de usar tar a través del script menu.sh

# Siguientes pasos...

Usando la extensión de Docker, usa la función que te permita abrir una shell en el contenedor de odoo. Ejecuta el comando 

```bash
odoo scaffold prueba /mnt/extra-addons
```

Observa el contenido de ese directorio desde el propio contenedor y desde el volumen mapeado en el anfitrión. ¿Qué ha hecho ese comando?

Si pulsas en el icono de Git en la barra lateral de GitHub, verás que los directorios y ficheros que ha generado el subcomando scaffold aparecen en estado **U** de Untracked, es decir, no estarían teniendo seguimiento todavía por esta herramienta y no se sincronizarían.

**Este README está pendiente de actualización, sincroniza tu fork cuando encuentres cambios**