#!/usr/bin/env python3
import sys
import subprocess
from colorama import Fore, init

init(autoreset=True)

def show_banner():
    print(Fore.RED + """
    ╔═══╗╔══╗╔═══╗╔═══╗
    ║╔═╗║╚╣╠╝║╔══╝║╔══╝
    ║╚═╝║ ║║ ║╚══╗║╚══╗
    ║╔╗╔╝ ║║ ║╔══╝║╔══╝
    ║║║╚╗╔╣╠╗║╚══╗║╚══╗
    ╚╝╚═╝╚══╝╚═══╝╚═══╝
          MXMap v1.0
    """ + Fore.CYAN + "  Termux Network Mapper\n")

def parse_args():
    args = sys.argv[1:]
    target = None
    ports = "1-1000"
    
    for i in range(len(args)):
        if args[i] == "-t" and i+1 < len(args):
            target = args[i+1]
        if args[i] == "-p" and i+1 < len(args):
            ports = args[i+1]
    
    return target, ports

def scan(target, ports):
    print(Fore.YELLOW + f"\n[*] Escaneando {target} en puertos {ports}")
    cmd = f"nmap -p {ports} {target}"
    subprocess.call(cmd, shell=True)

if __name__ == "__main__":
    show_banner()
    target, ports = parse_args()
    if target:
        scan(target, ports)
    else:
        print(Fore.RED + "[!] Usa -t <IP o dominio>")
