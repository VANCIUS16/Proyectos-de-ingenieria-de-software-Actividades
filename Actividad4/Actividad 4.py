from pathlib import Path
import os
import time


directory = Path("D:\PycharmProjects\Proyectos-de-ingenieria-de-software-Actividades\Actividad 3\Diccionario")
log_diccionario = open("log_diccionarioCompleto", 'w+')
# Declaramos una lista
words = []
for name in os.listdir(directory):
    Start = time.time()
    FilePath = directory / name
    f = open(FilePath, "r", encoding='utf-8', errors='ignore')

    # Iteramos por cada linea del documento de texto
    for line in f:
        # iteramos por cada palabra obtenida al dividir la linea
        for word in line.split():
            # Confirmamos que la palabra sea unica y agreamos a la lista
            if word.isalpha():
                words.append(word)
    f.close()

file_Sorted = open("DiccionarioCompleto", "w+", encoding='utf-8', errors='ignore')
# Ordenamos la lista
words_Sorted = sorted(words, key=str.lower)
for w in words_Sorted:
    file_Sorted.write(w)
    file_Sorted.write('\n')
file_Sorted.close()
End = time.time()
log_diccionario.write("Tiempo total: " + str(End - Start))


