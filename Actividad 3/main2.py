# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Actividad 1. Arranque del proyecto y verificación de archivos HTML


import os
import time
from bs4 import BeautifulSoup
from pathlib import Path



# Actividad 3. Extraer palabras de archivos HTML


pathClean = "D:/Users/marcn/Documents/AAAA/Tecmilenio/Octavo Semestre/Proyectos de Ingeniería de Software/Fase 1/Actividad 3/NewFiles"

for name in os.listdir(pathClean):
    Start = time.time()
    oldPath = "D:/Users/marcn/Documents/AAAA/Tecmilenio/Octavo Semestre/Proyectos de Ingeniería de Software/Fase 1/Actividad 3/NewFiles/" + name
    newPath = "D:/Users/marcn/Documents/AAAA/Tecmilenio/Octavo Semestre/Proyectos de Ingeniería de Software/Fase 1/Actividad 3/Diccionario/" + name
    file_Sorted = open(newPath, "w+", encoding='utf-8', errors='ignore')
    # Abrimos el .txt en read
    f = open(oldPath, "r", encoding='utf-8', errors='ignore')

# Declaramos una lista
words = []

# Iteramos por cada linea del documento de texto
for line in f:
    # iteramos por cada palabra obtenida al dividir la linea
    for word in line.split():
        # Confirmamos que la palabra sea unica y agreamos a la lista
        if word not in words:
            words.append(word)
f.close()

# Ordenamos la lista
words_Sorted = sorted(words, key=str.lower)
# Ingresamos la lista al nuevo documento
for w in words_Sorted:
    file_Sorted.write(w)
    file_Sorted.write('\n')
file_Sorted.close()



end = time.time()