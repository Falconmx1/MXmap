# 🚀 MXMap - Escaneo como los grandes, pero desde Termux

Herramienta de escaneo de puertos y redes, estilo nmap, optimizada para Termux.

## 📦 Instalación
```bash
git clone https://github.com/Falconmx1/MXMap
cd MXMap
bash install.sh

🎯 Comandos
mxmap -t 192.168.1.1
mxmap -p 22,80,443 -t google.com
mxmap --scan-type syn -t 192.168.0.1/24


### **install.sh** (para todo automatico)
```bash
#!/bin/bash
echo "[+] Instalando MXMap para Termux..."
pkg update -y
pkg install nmap python git -y
pip install colorama scapy-python3
chmod +x mxmap.sh
ln -s $PWD/mxmap.sh $PREFIX/bin/mxmap
echo "✅ Instalado! Usa: mxmap"
