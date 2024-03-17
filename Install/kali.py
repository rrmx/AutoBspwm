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

def menu():
    red()
    print("\n[+] Selecciona lo que quieres instalar [+]")
    blue()
    print("\n1 -> Instalar Dependencias ")
    print("\n2 -> Instalar Bspwm ")
    print("\n3 -> Instalar Sxhkd ")
    print("\n4 -> Instalar Picom ")
    print("\n5 -> Instalar Polybar ")
    print("\n6 -> Instalar Todo ")
    print("\n7 -> Salir ")

    option = input("\n-->> ")

    if option == "1":
        dependecias()
    if option == "2":
        bspwm()
    if option == "3":
        sxhkd()
    if option == "4":
        picom()
    if option == "5":
        polybar()
    if option == "6":
        dependecias()
        bspwm()
        sxhkd()
        picom()
        polybar()
    if option == "7":
        exit()

def dependecias():
    red()
    print("\n[+] Instalando Dependencias [+]")
    green()
    print("\n")
    # Actualizar sistema
    os.system("sudo apt update -y")
    os.system("sudo apt upgrade -y")

    # Dependencias bspwm y sxhkd
    os.system("sudo apt install build-essential git vim libxcb-util0-dev libxcb-ewmh-dev libxcb-randr0-dev libxcb-icccm4-dev libxcb-keysyms1-dev -y")
    os.system("sudo apt install libxcb-xinerama0-dev libasound2-dev libxcb-xtest0-dev libxcb-shape0-dev libxinerama1 libxinerama-dev bspwm -y")

    # Dependencias polybar
    os.system("sudo apt install cmake cmake-data pkg-config python3-sphinx libcairo2-dev libxcb1-dev libxcb-util0-dev libxcb-randr0-dev libxcb-composite0-dev -y")
    os.system("sudo apt install python3-xcbgen xcb-proto libxcb-image0-dev libxcb-ewmh-dev libxcb-icccm4-dev libxcb-xkb-dev libxcb-xrm-dev libxcb-cursor-dev -y")
    os.system("sudo apt install libasound2-dev libpulse-dev libjsoncpp-dev libmpdclient-dev libuv1-dev libnl-genl-3-dev libepoxy-dev libxcb-dpms0 libxcb-dpms0-dev -y")
    os.system("sudo apt install libcurl4-doc libidn-dev libkrb5-dev libldap2-dev librtmp-dev libssh2-1-dev libssl-dev libcurl4-openssl-dev -y")

    # Dependencias picom
    os.system("sudo apt install meson libxext-dev libxcb1-dev libxcb-damage0-dev libxcb-xfixes0-dev libxcb-shape0-dev libxcb-render-util0-dev libxcb-render0-dev -y")
    os.system("sudo apt install libxcb-randr0-dev libxcb-composite0-dev libxcb-image0-dev libxcb-present-dev libxcb-xinerama0-dev libpixman-1-dev libdbus-1-dev -y")
    os.system("sudo apt install libconfig-dev libgl1-mesa-dev libpcre2-dev libpcre3 libpcre3-dev libevdev-dev uthash-dev libev-dev libx11-xcb-dev libxcb-glx0-dev -y")

    red()
    print("\n[+] Dependencias Instaladas [+]")

def bspwm():
    red()
    print("\n[+] Instalando bspwm [+]\n")
    green()
    print("\n")
    # Clona el repo de bspwm
    os.system("git clone https://github.com/baskerville/bspwm.git")
    os.system("mv bspwm/* .")
    os.system("sudo rm -r bspwm/")
    os.system("make")

    # Acava del build
    os.system("sudo make install")

    # Elimina los archivos de bspwm
    os.system("sudo rm -r *.o bspc bspwm artworks contrib doc examples LICENSE Makefile README.md Sourcedeps src tests VERSION")

    red()
    print("\n[+] Bspwm Instalado [+]")

def sxhkd():
    red()
    print("\n[+] Instalando sxhkd [+]")
    green()
    print("\n")
    # Clona el repo de sxhkd
    os.system("git clone https://github.com/baskerville/sxhkd.git")
    os.system("mv sxhkd/* .")
    os.system("sudo rm -r sxhkd/")
    os.system("make")

    # Acaba el build
    os.system("sudo make install")

    # Elimina los archivos de sxhkd
    os.system("sudo rm -r *.o *.md contrib doc examples LICENSE Makefile Sourcedeps src sxhkd  VERSION")

    red()
    print("\n[+] Sxhkd Instalado [+]")

def picom():
    red()
    print("\n[+] Instalando picom [+]")
    green()
    print("\n")
    # Clona el repo de picom
    os.system("git clone https://github.com/yshui/picom.git")
    os.system("mv picom/* .")
    os.system("sudo rm -r picom/")
    os.system("meson setup build")
    os.system("ninja -C build")

    # Hace el build de picom
    os.system("sudo ninja -C build install")

    # Elimina los archivos de picom
    os.system("sudo rm -r *.md *.txt *.spdx *.lock *.glsl *.nix *.build bin CONTRIBUTORS meson build COPYING src dbus-examples LICENSES subprojects tests Doxyfile man media picom.sample.conf compton.desktop picom-dbus.desktop picom.desktop")

    red()
    print("\n[+] Picom Instalado [+]\n")

def polybar():
    red()
    print("\n[+] Instalando polybar [+]\n")
    green()
    print("\n")
    # Clona el r
    # Clona el repo de polybar
    os.system("git clone --recursive https://github.com/polybar/polybar")
    os.system("mv polybar/* .")
    os.system("sudo rm -r polybar/")
    os.system("cmake .")
    os.system("make -j$(nproc)")

    # Acaba el build
    os.system("sudo make install")

    # Elimina los archivos de polybar
    os.system("sudo rm -r bin cmake doc include libs Makefile tests CMakeFiles common contrib generated-sources lib LICENSE src")
    os.system("sudo rm -r *.sh *.md *.txt *.json .cmake ")

    red()
    print("\n[+] Polybar Instalado [+]\n")

if __name__ == '__main__':
    id = os.getuid()

    if id == 0:
        red()
        print()
        print("[!] No hay que ser root para ejecutar la herramienta")
        print()
    else:
        menu()