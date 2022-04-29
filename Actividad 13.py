# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 00:54:07 2022

@author: marcn
"""
from pathlib import Path
import os
import time
from collections import Counter

directory = Path("D:/Users/marcn/Documents/AAAA/Tecmilenio/Octavo Semestre/Proyectos de Ingeniería de Software/Fase 4/Actividad 13\Diccionario")
counterFrec = Counter()
log_tokensTotales = open("log_tokensTotales", 'w+')
cont = 0
lista = [
    "Gauch",
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
    "United States laws"
]


def limpiar(texto):
    texto = ' '.join(e for e in texto.split() if e.isalpha())
    texto = texto.lower()
    return texto

def frecuencia(archivo, palabra):
    data = open(directory/archivo, 'r', encoding='utf-8', errors='ignore')
    data2 = data.read()
    frecuencia = []
    frecuencia = data2.split()
    frecuencia2 = frecuencia.count(palabra)
    return frecuencia2


Start = time.time()
for f in lista:
    for name in os.listdir(directory):
        with open(directory/name, 'r', encoding='utf-8', errors='ignore') as filehandle:
            datafile = filehandle.readlines()
            cont = cont + 1
            for line in datafile:
                if f in line:
                    ff = frecuencia(name, f)
                    print("| Word: ", f, " | ID: ", cont, " | Archivo: ", name, " | Frecuencia", ff)
                    break
    cont = 0

End = time.time()
log_tokensTotales.write("Tiempo total: " + str(End - Start))