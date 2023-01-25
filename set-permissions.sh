#!/bin/bash
###############################################################################
# Este script resuelve problemas encontrados en algunos contenedores Docker
# cuando se ejecutan sin ser root en el anfitrión y el usuario pierde el control
# sobre los directorios de los volúmenes involucrados
# @author https://github.com/javnitram/
# GNU GENERAL PUBLIC LICENSE Version 3
# Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)
###############################################################################

# VARIABLES GLOBALES
# Estos nombres deben coincidir con los nombres de directorios en la ruta actual
# y de los contenedores definidos en el fichero docker-compose.yml
declare -a SERVICES=( odoo postgres pgadmin4 )
RED_TEXT='\033[0;31m'
RESET_TEXT='\033[0m' # No Color

function my_env() {
    # Usaremos la variable de entorno DOCKER_USER para que los datos del contenedor
    # postgresql puedan ser gestionados por el usuario que ejecuta docker, que no
    # es root ni puede hacer sudo.

    # Consultamos si existe la variable de entorno
    if [ -z "${DOCKER_USER}" ]; then
        # La variable de entorno no se ha inicializado
        local env_definition
        env_definition='export DOCKER_USER="$(id -u):$(id -g)"'
        if ! grep "$env_definition" ~/.bashrc > /dev/null; then
            # Definitivamente no está donde la esperamos, la agregamos
            echo "$env_definition" >> ~/.bashrc
        fi
        echo -ne "${RED_TEXT}"
        cat << EOF
        Este script ha definido una variable de entorno, antes de seguir cierra este terminal y abre uno nuevo
    
EOF
        # EOF debe ser una línea exacta sin caracteres delante o detrás @see sintaxis HEREDOC (<<)
        echo -ne "${RESET_TEXT}"
        exit 255
    fi
}

function set_permissions_for_containers() {
    # Aplicamos permisos de acceso completo a los directorios de los contenedores
    # que se usan como punto de montaje de los volúmenes compartidos. Así nos
    # aseguramos que los contenedores puedan escribir y que el usuario del host
    # anfitrión pueda acceder.
    for i in "${SERVICES[@]}"; do
        docker ps --quiet --filter "name=^$i" | while read -r container_id; do
            grep '${PWD}'/$i docker-compose.yml | cut -d: -f2 | while read -r volume; do
                    # depurar con --tty
                    echo "Estableciendo permisos en el contenedor con id $container_id basado en la imagen $i, volumen $volume"
                    docker exec --privileged --user root "$container_id" sh -c "/usr/bin/find $volume -type d -exec /bin/chmod 777 {} \;" 
                    docker exec --privileged --user root "$container_id" sh -c "/usr/bin/find $volume -type f -exec /bin/chmod 666 {} \;" 
                    docker exec --privileged --user root "$container_id" sh -c "/bin/chown -R ${DOCKER_USER} $volume" 
            done
        done
    done
}

function set_permissions_for_host() {
    # Aplicamos permisos de acceso completo a los directorios del host que nuestros 
    # contenedores montan como volúmenes para tener persistencia. Así nos
    # aseguramos que los contenedores puedan escribir y que el usuario del host
    # anfitrión pueda acceder.
    error="false"
    for i in "${SERVICES[@]}"; do
        mkdir -p "$i" || error="true"
        find "$i" -type d -exec chmod 777 {} \; || error="true"
        find "$i" -type f -exec chmod 666 {} \; || error="true"
        chown -R "${DOCKER_USER}" "$i" || error="true"
    done

    if $error; then
        echo -ne "${RED_TEXT}"
        cat << EOF >&2
        
    Ha habido problemas al asignar algunos permisos de directorios locales. Entre otras cosas, puede afectar a:
        - La correcta ejecución y persistencia de los contenedores.
        - La correcta migración de los directorios de los volúmenes a otros entornos.

    Si los contenedores están en ejecución, vuelve a lanzar "$0" tras hacer "docker-compose down".
    Si no, vuelve a lanzar "$0" tras hacer "docker-compose up -d".

EOF
        # EOF debe ser una línea exacta sin caracteres delante o detrás @see sintaxis HEREDOC (<<)
        echo -ne "${RESET_TEXT}"
        exit 1
    else
        echo -e "Permisos locales asignados correctamente.\n"
    fi
}

function main() {
    my_env
    if [ -n "${DOCKER_USER}" ]; then
        set_permissions_for_containers
        set_permissions_for_host
    fi
}

if [ "${BASH_SOURCE[0]}" -ef "$0" ]
then
    # Están ejecutando directamente este script, no importándolo con source
    main "$@"
fi