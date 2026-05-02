#!/usr/bin/env python3

import sys
import os
import subprocess
import argparse
import json
from datetime import datetime
from colors import Colors

def check_termux():
    """Detectar si estamos en Termux"""
    if os.path.exists('/data/data/com.termux'):
        return True
    return False

def save_results(output, filename, format_type):
    """Guardar resultados en diferentes formatos"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    if format_type == 'normal':
        with open(f"{filename}_normal.txt", 'w') as f:
            f.write(output)
        print(f"{Colors.GREEN}[+] Resultados guardados en {filename}_normal.txt")
    
    elif format_type == 'xml':
        with open(f"{filename}_scan.xml", 'w') as f:
            f.write(output)
        print(f"{Colors.GREEN}[+] Resultados XML guardados en {filename}_scan.xml")
    
    elif format_type == 'grepable':
        with open(f"{filename}_grepable.txt", 'w') as f:
            f.write(output)
        print(f"{Colors.GREEN}[+] Resultados grepable guardados en {filename}_grepable.txt")

def run_nmap_scan(target, ports, scan_type, os_detect, udp_scan, script, output_file):
    """Ejecutar escaneo con nmap"""
    
    # Construir comando nmap
    cmd = ["nmap"]
    
    # Agregar puertos
    if ports:
        cmd.extend(["-p", ports])
    else:
        cmd.extend(["-p", "1-1000"])
    
    # Tipo de escaneo
    if scan_type == 'syn':
        cmd.append("-sS")
        print(f"{Colors.YELLOW}[*] Usando escaneo SYN (rápido y furtivo)")
    else:
        cmd.append("-sT")  # TCP connect por defecto
    
    # Detectar OS
    if os_detect:
        cmd.append("-O")
        print(f"{Colors.YELLOW}[*] Detectando sistema operativo...")
    
    # Escaneo UDP
    if udp_scan:
        cmd.append("-sU")
        print(f"{Colors.YELLOW}[*] Escaneando puertos UDP...")
    
    # Scripts
    if script:
        cmd.extend(["--script", script])
        print(f"{Colors.YELLOW}[*] Ejecutando script: {script}")
    
    # Agregar target
    cmd.append(target)
    
    # Verbosidad y output
    cmd.append("-v")
    
    print(f"{Colors.CYAN}[*] Comando: {' '.join(cmd)}")
    print(f"{Colors.GREEN}[*] Iniciando escaneo a {target}...\n")
    
    # Ejecutar nmap
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
        output = result.stdout + result.stderr
        
        # Mostrar resultados
        print(output)
        
        # Guardar si se solicitó
        if output_file:
            save_results(output, output_file, 'normal')
            save_results(output, output_file, 'xml')
            save_results(output, output_file, 'grepable')
        
        return True
        
    except subprocess.TimeoutExpired:
        print(f"{Colors.RED}[!] Escaneo tardó demasiado, timeout después de 5 minutos")
        return False
    except Exception as e:
        print(f"{Colors.RED}[!] Error: {str(e)}")
        return False

def main():
    # Mostrar banner
    print(Colors.banner())
    
    # Detectar Termux
    if check_termux():
        print(f"{Colors.GREEN}✅ Termux detectado - Usando rutas optimizadas{Colors.RESET}")
    else:
        print(f"{Colors.BLUE}💻 Sistema Linux detectado{Colors.RESET}")
    
    # Parsear argumentos manualmente (para compatibilidad total)
    args = sys.argv[1:]
    
    target = None
    ports = None
    scan_type = None
    os_detect = False
    udp_scan = False
    script = None
    output_file = None
    
    i = 0
    while i < len(args):
        if args[i] == '-t' and i+1 < len(args):
            target = args[i+1]
            i += 2
        elif args[i] == '-p' and i+1 < len(args):
            ports = args[i+1]
            i += 2
        elif args[i] == '--scan-type' and i+1 < len(args):
            scan_type = args[i+1]
            i += 2
        elif args[i] == '--os':
            os_detect = True
            i += 1
        elif args[i] == '-sU':
            udp_scan = True
            i += 1
        elif args[i] == '--script' and i+1 < len(args):
            script = args[i+1]
            i += 2
        elif args[i] == '-oA' and i+1 < len(args):
            output_file = args[i+1]
            i += 2
        elif args[i] == '-h':
            print("Uso: mxmap -t <IP> [opciones]")
            print("\nOpciones:")
            print("  -t <IP/DOMINIO>        Target")
            print("  -p <PUERTOS>           Puertos (ej: 22,80 o 1-1000)")
            print("  --scan-type syn        Escaneo SYN")
            print("  --os                   Detectar OS")
            print("  -sU                    Escaneo UDP")
            print("  --script <nombre>      Script NSE")
            print("  -oA <archivo>          Guardar resultados")
            sys.exit(0)
        else:
            i += 1
    
    # Validar target
    if not target:
        print(f"{Colors.RED}[!] Error: Necesitas especificar un target con -t{Colors.RESET}")
        sys.exit(1)
    
    # Ejecutar escaneo
    success = run_nmap_scan(target, ports, scan_type, os_detect, udp_scan, script, output_file)
    
    if success:
        print(f"\n{Colors.GREEN}✅ Escaneo completado exitosamente{Colors.RESET}")
    else:
        print(f"\n{Colors.RED}❌ Escaneo falló{Colors.RESET}")

if __name__ == "__main__":
    main()
