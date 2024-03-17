import os
from sys import stdout

def red():
    RED = "\033[1;31m"
    stdout.write(RED)

def green():
    GREEN = "\033[0;32m"
    stdout.write(GREEN)

def blue():
    BLUE = "\033[1;34m"
    stdout.write(BLUE)

def yellow():
    YELLOW = "\033[1;33m"
    stdout.write(YELLOW)

def purple():
    PURPLE = "\033[1;35m"
    stdout.write(PURPLE)

def white():
    WHITE = "\033[1;37m"
    stdout.write(WHITE)

banner = """

By: ZLCube, xsJacksx, S4vitar, MrPr1ngles, Elisaelias02

 █████╗ ██╗   ██╗████████╗ ██████╗ ██████╗ ███████╗██████╗ ██╗    ██╗███╗   ███╗
██╔══██╗██║   ██║╚══██╔══╝██╔═══██╗██╔══██╗██╔════╝██╔══██╗██║    ██║████╗ ████║  
███████║██║   ██║   ██║   ██║   ██║██████╔╝███████╗██████╔╝██║ █╗ ██║██╔████╔██║  
██╔══██║██║   ██║   ██║   ██║   ██║██╔══██╗╚════██║██╔═══╝ ██║███╗██║██║╚██╔╝██║
██║  ██║╚██████╔╝   ██║   ╚██████╔╝██████╔╝███████║██║     ╚███╔███╔╝██║ ╚═╝ ██║
╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝ ╚═════╝ ╚══════╝╚═╝      ╚══╝╚══╝ ╚═╝     ╚═╝
  ___        _       ______                             
 / _ \      | |      | ___ \                              
/ /_\ \_   _| |_ ___ | |_/ / ___ _ ____      ___ __ ___  
|  _  | | | | __/ _ \| ___ \/ __| '_ \ \ /\ / / '_ ' _ \ 
| | | | |_| | || (_) | |_/ /\__ \ |_) \ V  V /| | | | | |
\_| |_/\__,_|\__\___/\____/ |___/ .__/ \_/\_/ |_| |_| |_|
                                | |                      
                                |_|                       
"""

def menu():
    red()
    print(banner)
    blue()
    print("\n[+] SELECCIONE SU SISTEMA OPERATIVO [+]")
    yellow()
    print("\n1 -> Kali Linux ")
    print("\n2 -> Parrot OS ")
    print("\n3 -> Arch Linux ")
    print("\n4 -> Salir ")

    option = input("\n-->> ")

    if option == "1":
        kali_linux()
    if option == "2":
        parrot_os()
    if option == "3":
        arch_linux()
    if option == "4":
        exit()

def kali_linux():
    green()

    # Instalcion y temas de kali linx
    expback = input("\n Kali Linux ( 1 --> Instalacion )  ( 2 --> Temas ) ( 3 --> Todo ). 1/2/3 -> ")

    if expback == "1":
        os.system("python3 Install/kali.py")

    if expback == "2":
        os.system("")
    
    if expback == "3":
        os.system("python3 Install/kali.py")
        os.system("")

def parrot_os():
    green()


def arch_linux():
    green()


if __name__ == '__main__':
    id = os.getuid()
    
    if id == 0:
        red()
        print()
        print("[!] No hay que ser root para ejecutar la herramienta")
        print()
    else:
        menu()