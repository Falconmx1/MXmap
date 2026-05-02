# 🚀 MXMap - Herramienta de Escaneo para Termux

[![Version](https://img.shields.io/badge/version-2.0-red)]()

Herramienta profesional de escaneo de redes, compatible con Termux y Linux.

## ✨ Características
- ✅ Escaneo SYN (rápido y furtivo)
- ✅ Detección de Sistema Operativo
- ✅ Escaneo UDP
- ✅ Scripts NSE personalizados
- ✅ Guardado en múltiples formatos (normal, XML, grepable)
- ✅ Optimizado para Termux

## 📦 Instalación Rápida
```bash
git clone https://github.com/Falconmx1/MXMap
cd MXMap
bash install.sh

🎯 Ejemplos de uso
# Escaneo básico
mxmap -t 192.168.1.1 -p 1-1000

# Escaneo SYN con detección de OS
mxmap -t google.com --scan-type syn --os

# Escaneo UDP con script de vulnerabilidades
mxmap -t 192.168.1.1 -sU --script vuln

🛠️ Compatibilidad

    Termux (Android)

    Kali Linux

    Ubuntu/Debian

    Cualquier Linux con nmap

⚡ Rendimiento en Termux

    Usa rutas optimizadas con $PREFIX

    Detecta automaticamente el entorno

    No requiere root (modo TCP connect)

🎮 Comandos de prueba:
# Escaneo normal
mxmap -t scanme.nmap.org -p 22,80

# Escaneo SYN con OS
mxmap -t 192.168.1.1 --scan-type syn --os

# Escaneo UDP
mxmap -t 192.168.1.1 -sU -p 53,123

# Con script
mxmap -t 192.168.1.1 --script http-headers

# Guardar todo
mxmap -t google.com -p 80,443 -oA google_scan

# Guardar resultados
mxmap -t 192.168.1.1 -oA resultados
