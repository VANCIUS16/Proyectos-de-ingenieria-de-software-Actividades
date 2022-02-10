# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 20:36:04 2022

@author: marcn
"""
from bs4 import BeautifulSoup
from pathlib import Path
import os
import time

# path del archivo
directory = "D:/Users/marcn/Documents/AAAA/Tecmilenio/Octavo Semestre/Proyectos de Ingeniería de Software/Fase 1/Actividad 3/Files"

# funcion para extraer texto
def removetags(html):
    # Se lee el archivo
    html_thing = open(html, 'r', encoding='utf-8', errors='ignore')
    # Convertimos el archivo leido a un objeto beautifulSoup
    soup = BeautifulSoup(html_thing, 'lxml')
    # Extraemos el texto del archivo a un string
    file_text = soup.get_text()
    return file_text

for fileName in os.listdir(directory):
    Start = time.time()
    
    path2 = "D:/Users/marcn/Documents/AAAA/Tecmilenio/Octavo Semestre/Proyectos de Ingeniería de Software/Fase 1/Actividad 3/Files/"+fileName
    # Creamos un archivo txt
    newFilePath = "D:/Users/marcn/Documents/AAAA/Tecmilenio/Octavo Semestre/Proyectos de Ingeniería de Software/Fase 1/Actividad 3/NewFiles2/"+fileName
    f = open(newFilePath, "w+", encoding='utf-8', errors='ignore')
   
    # Escribimos el texto en el nuevo documento
    f.write(removetags(path2))
    f.close()
    #p = Path(newFilePath)
    #p.rename(p.with_suffix('.txt'))
    end = time.time()
    print("File Name: "+fileName+" || Times: ", end-Start)


# Actividad 3. Extraer palabras de archivos HTML
pathClean = "D:/Users/marcn/Documents/AAAA/Tecmilenio/Octavo Semestre/Proyectos de Ingeniería de Software/Fase 1/Actividad 3/NewFiles2/"
    
for name in os.listdir(pathClean):
    Start = time.time()
    oldPath = "D:/Users/marcn/Documents/AAAA/Tecmilenio/Octavo Semestre/Proyectos de Ingeniería de Software/Fase 1/Actividad 3/NewFiles2/" + name
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
    p = Path(newPath)
    p.rename(p.with_suffix('.txt'))
    
    end = time.time()
    print("File Name: "+name+" || Times: ", end-Start)