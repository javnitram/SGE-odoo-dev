#!/bin/bash
green='\033[0;32m'
nc='\033[0m' # No Color
if [ -z "${DOCKER_USER}" ]; then
    source ./set-permissions.sh
    my_env
fi
while true; do
    if which smenu > /dev/null; then
        echo "CASOS DE USO COMUNES:"
        choice=$(smenu -n20 -W $'\t\n' -N -c -b -e "#.*" -g -s /./set-permissions.sh < menu.txt)
        echo -e "\n$ $choice"
        [[ "$choice" -eq "exit" ]] && exit 0
        bash -c "$choice" || exit $?
        echo -e "\t${green}OK${nc}\n"
    else
        echo "Instala el paquete smenu para que este menú sea interactivo:"
        echo -e '\t "sudo apt install smenu -y"'
        echo "CASOS DE USO COMUNES:"
        cat menu.txt
        exit 1
    fi
done