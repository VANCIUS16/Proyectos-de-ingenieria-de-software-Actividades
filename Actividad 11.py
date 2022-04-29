# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 00:14:07 2022

@author: marcn
"""

from pathlib import Path
from collections import Counter
import os
import time

directory = Path("D:/Users/marcn/Documents/AAAA/Tecmilenio/Octavo Semestre/Proyectos de Ingeniería de Software/Fase 4/Actividad 11\Diccionario")
log_tokensTotales = open("log_tokensTotales", 'w+')
tokensTotales = open("TokensTotales", "w+", encoding='utf-8', errors='ignore')
Archivo_Doc = open("Archivo_Doc", "w+", encoding='utf-8', errors='ignore')
Archivo_Posting = open("Archivo_Posting", "w+", encoding='utf-8', errors='ignore')
counter = Counter()
counterFrec = Counter()
IdUnico = 0


def limpiar(texto):
    texto = ' '.join(e for e in texto.split() if e.isalpha())
    texto = texto.lower()
    return texto


Start = time.time()
for name in os.listdir(directory):
    with open(directory/name, 'r', encoding='utf-8', errors='ignore') as filehandle:
        IdUnico = IdUnico + 1
        m = str(IdUnico) + " " + name
        Archivo_Doc.write(m + '\n')
        k = str(directory/name)
        # ^ Se crea el ID Diccionario
        
        sizefile = os.stat(k).st_size
        posting = str(IdUnico) + " " + str(sizefile)
        Archivo_Posting.write(posting + '\n')
        # ^ para obtener numero de archivos donde viene la palabra|
        # ^ Se crea el Archivo Posting

for name in os.listdir(directory):
    with open(directory/name, 'r', encoding='utf-8', errors='ignore') as filehandle:
        counterFrec.update(limpiar(filehandle.read()).split())
        # ^ para obtener la frecuencia de la palabra en todos los archivos

for word, count in counter.most_common():
    tokensTotales.write('{} ; {}'.format(word, count) + " ; " + str(counterFrec.get(word)))
    tokensTotales.write('\n')
End = time.time()
log_tokensTotales.write("Tiempo total: " + str(End - Start))