#!/bin/bash

if [ -d /data/data/com.termux ]; then
    PREFIX="/data/data/com.termux/files/usr"
    echo "📱 Desinstalando MXMap de Termux..."
else
    PREFIX="/usr"
    echo "💻 Desinstalando MXMap de Linux..."
fi

# Eliminar symlink
rm -f "$PREFIX/bin/mxmap"

# Eliminar directorio
rm -rf "$PREFIX/../home/MXMap"

echo "✅ MXMap desinstalado correctamente"
