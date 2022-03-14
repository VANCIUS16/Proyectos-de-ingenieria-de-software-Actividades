from bs4 import BeautifulSoup
from pathlib import Path
import os
import time

# path del archivo
directory = "D:/joelh/Documents/TecMilenio/ProyectosIngenieriaSoft/Files"
# logs
log_abrir = open("log_abrir.txt", 'w+')
log_remove = open("log_remove", 'w+')
log_diccionario = open("log_diccionario", 'w+')


# funcion para extraer texto
def removetags(html):
    # Se lee el archivo
    html_thing = open(html, 'r', encoding='utf-8', errors='ignore')
    # Convertimos el archivo leido a un objeto beautifulSoup
    soup = BeautifulSoup(html_thing, 'lxml')
    # Extraemos el texto del archivo a un string
    file_text = soup.get_text()
    return file_text


# Actividad 1: leer archivos html
Start1 = time.time()
for filename in os.listdir(directory):
    Start = time.time()
    f = open(os.path.join(directory, filename), 'r')
    f.close()
    end = time.time()
    log_abrir.write("File Name: " + filename + " || Times: " + str(end - Start) + '\n')
End1 = time.time()
log_abrir.write("Tiempo total: " + str(End1 - Start1))

# Actividad 2: remover html tags
Start2 = time.time()
for fileName in os.listdir(directory):
    Start = time.time()

    path2 = "D:/joelh/Documents/TecMilenio/ProyectosIngenieriaSoft/Files/" + fileName
    # Creamos un archivo txt
    newFilePath = "D:/joelh/Documents/TecMilenio/ProyectosIngenieriaSoft/NewFiles2/" + fileName
    f = open(newFilePath, "w+", encoding='utf-8', errors='ignore')

    # Escribimos el texto en el nuevo documento
    f.write(removetags(path2))
    f.close()
    p = Path(newFilePath)
    p.rename(p.with_suffix('.txt'))
    end = time.time()
    log_remove.write("File Name: " + fileName + " || Times: " + str(end - Start) + '\n')
End2 = time.time()
log_remove.write("Tiempo total: " + str(End2 - Start2))

# Actividad 3. Extraer palabras de archivos HTML
pathClean = "D:/joelh/Documents/TecMilenio/ProyectosIngenieriaSoft/NewFiles2/"

Start3 = time.time()
for name in os.listdir(pathClean):
    Start = time.time()
    oldPath = "D:/joelh/Documents/TecMilenio/ProyectosIngenieriaSoft/NewFiles2/" + name
    newPath = "D:/joelh/Documents/TecMilenio/ProyectosIngenieriaSoft/Diccionario/" + name
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
    log_diccionario.write("File Name: " + name + " || Times: " + str(end - Start) + '\n')
End3 = time.time()
log_diccionario.write("Tiempo total: " + str(End3 - Start3))
