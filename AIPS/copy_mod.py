#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 18:24:26 2023

@author: aamg
"""

import shutil

fileA = ""
fileB = ""

text = (Fore.GREEN + "<<PyCopier>>\nUse el siguiente formato:\n/ruta/al/archivo.txt\n\n" + Fore.RESET)
txt_hs(text)

fileA = input("Introduzca la ruta del archivo que desea copiar: ")
fileB = input("Introduzca la ruta de destino: ")

shutil.copy2(fileA, fileB)

text = (Fore.RED + "La copia se ha realizado satisfactoriamente\n" + Fore.RESET)
txt_hs(text)