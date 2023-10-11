#!/usr/bin/env python3
import os as rx
from colorama import init, Fore, Style
init()

def google():
    rx.system("pkg install w3m")
    rx.system("apt install w3m")
    title = Fore.GREEN+Style.BRIGHT+""" 
    Created by: Hans Saldias
    
    by: 1LugarParaProgramar
    
    Script : Navegar en la web con Termux\n\n"""
    for i in title:
        print(i, end="")
    print(Fore.CYAN+Style.BRIGHT+"Busqueda con Termux en la web\n\n ")
    print("Uso:\n subir y bajar con las flechas y para ingresar a datos o link presiona entrer encima moviendote con las ((flechas))\n\neje: www.facebook.com\nwww.google.com\n\n")
    find = input("Ingrese sitio a navegar: ")
    rx.system("w3m {}".format(find))
    
google()  
    