#!/bin/bash

# Detectar Termux
if [ -d /data/data/com.termux ]; then
    PREFIX="/data/data/com.termux/files/usr"
    echo "📱 Instalando para Termux..."
    pkg update -y
    pkg install nmap python git -y
else
    PREFIX="/usr"
    echo "💻 Instalando para Linux..."
    sudo apt update
    sudo apt install nmap python3 git -y
fi

# Instalar dependencias Python
pip install colorama

# Crear directorio de instalación
MXMAP_DIR="$PREFIX/../home/MXMap"
if [ -d "$MXMAP_DIR" ]; then
    echo "[-] MXMap ya existe, actualizando..."
    cd "$MXMAP_DIR"
    git pull
else
    echo "[+] Clonando MXMap..."
    git clone https://github.com/TU_USER/MXMap.git "$MXMAP_DIR"
fi

# Dar permisos
chmod +x "$MXMAP_DIR/mxmap.sh"
chmod +x "$MXMAP_DIR/lib/"*.py

# Crear symlink
ln -sf "$MXMAP_DIR/mxmap.sh" "$PREFIX/bin/mxmap"

echo ""
echo "✅ MXMap instalado correctamente!"
echo "   Usa: mxmap -h para ayuda"
echo "   Ejemplo: mxmap -t scanme.nmap.org -p 80,443"
