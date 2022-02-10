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
directory = "D:/Users/marcn/Documents/AAAA/Tecmilenio/Octavo Semestre/Proyectos de Ingeniería de Software/Fase 1/Actividad 2/Files"

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
    
    path2 = "D:/Users/marcn/Documents/AAAA/Tecmilenio/Octavo Semestre/Proyectos de Ingeniería de Software/Fase 1/Actividad 2/Files/"+fileName
    # Creamos un archivo txt
    newFilePath = "D:/Users/marcn/Documents/AAAA/Tecmilenio/Octavo Semestre/Proyectos de Ingeniería de Software/Fase 1/Actividad 2/NewFiles/"+fileName
    f = open(newFilePath, "w+", encoding='utf-8', errors='ignore')
   
    # Escribimos el texto en el nuevo documento
    f.write(removetags(path2))
    f.close()
    p = Path(newFilePath)
    p.rename(p.with_suffix('.txt'))
    end = time.time()
    print("File Name: "+fileName+" || Times: ", end-Start)
