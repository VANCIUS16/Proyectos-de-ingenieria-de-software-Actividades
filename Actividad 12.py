# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 00:54:07 2022

@author: marcn
"""
from pathlib import Path
import os
import time

directory = Path("D:/Users/marcn/Documents/AAAA/Tecmilenio/Octavo Semestre/Proyectos de Ingeniería de Software/Fase 4/Actividad 12\Diccionario")

log_tokensTotales = open("log_tokensTotales", 'w+')
cont = 0
lista = ["Gauch",
    "elephants",
    "CSCE",
    "Arkansas",
    "gift",
    "abcdef",
    "20",
    "20.07",
    "123-456-7890",
    "lawyer consumers",
    "garden computer",
    "United States laws"]

Start = time.time()
for f in lista:
    for name in os.listdir(directory):
        with open(directory/name, 'r', encoding='utf-8', errors='ignore') as filehandle:
            datafile = filehandle.readlines()
            cont = cont + 1
            for line in datafile:
                if f in line:
                    print(cont, name)
                    break
    cont = 0
End = time.time()
log_tokensTotales.write("Tiempo total: " + str(End - Start))