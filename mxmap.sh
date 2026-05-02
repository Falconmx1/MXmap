#!/bin/bash
# MXMap - La navaja suiza de escaneo para Termux

VERSION="1.0"
echo "⚡ MXMap v$VERSION - Modo Termux ⚡"

if [ -z "$1" ]; then
    echo "Uso: mxmap -t <IP> -p <puertos>"
    echo "Ejemplo: mxmap -t 192.168.1.1 -p 1-1000"
    exit 1
fi

python lib/scan.py "$@"
