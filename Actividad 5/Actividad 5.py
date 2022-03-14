from pathlib import Path
from collections import Counter
import os
import time

directory = Path("D:/Users/marcn/Desktop/Proyectos-de-ingenieria-de-software-Actividades-master/Actividad 5/Diccionario")
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


def word_count(fname):
        with open(fname) as f:
                return Counter(f.read().split())
            
file_Sorted2 = open("DiccionarioTokens", "w+", encoding='utf-8', errors='ignore')
Counter2=word_count("DiccionarioCompleto")


your_list = [list(i) for i in Counter2.items()]
print(your_list)

for f in your_list:
    file_Sorted2.write(str(f))
    file_Sorted2.write('\n')

file_Sorted2.close()

End = time.time()
log_diccionario.write("Tiempo total: " + str(End - Start))
