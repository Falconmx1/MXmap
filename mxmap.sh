#!/bin/bash

# Detectar si estamos en Termux
if [ -d /data/data/com.termux ]; then
    PREFIX="/data/data/com.termux/files/usr"
    echo "📱 Modo Termux detectado"
else
    PREFIX="/usr"
    echo "💻 Modo Linux detectado"
fi

VERSION="2.0"
BANNER="
╔═══╗╔══╗╔═══╗╔═══╗
║╔═╗║╚╣╠╝║╔══╝║╔══╝
║╚═╝║ ║║ ║╚══╗║╚══╗
║╔╗╔╝ ║║ ║╔══╝║╔══╝
║║║╚╗╔╣╠╗║╚══╗║╚══╗
╚╝╚═╝╚══╝╚═══╝╚═══╝
     MXMap v$VERSION
   Termux Network Mapper
"

echo "$BANNER"

# Verificar argumentos
if [ $# -eq 0 ]; then
    echo "Uso: mxmap [opciones]"
    echo ""
    echo "Opciones:"
    echo "  -t <IP/DOMINIO>        Target a escanear"
    echo "  -p <PUERTOS>           Puertos (ej: 22,80 o 1-1000)"
    echo "  --scan-type syn        Escaneo SYN (rápido y furtivo)"
    echo "  --os                   Detectar sistema operativo"
    echo "  -sU                    Escaneo UDP"
    echo "  --script <nombre>      Ejecutar script NSE"
    echo "  -oA <archivo>          Guardar resultados (normal, xml, grepable)"
    echo "  -h                     Esta ayuda"
    echo ""
    echo "Ejemplos:"
    echo "  mxmap -t 192.168.1.1 -p 1-1000"
    echo "  mxmap -t google.com --scan-type syn --os"
    echo "  mxmap -t 192.168.1.1 -sU --script vuln"
    exit 1
fi

# Ejecutar core.py con todos los argumentos
python3 "$PREFIX/../home/MXMap/lib/core.py" "$@"
