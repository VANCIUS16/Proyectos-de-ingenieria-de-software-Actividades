from pathlib import Path
from collections import Counter
import os
import time

directory = Path("D:\PycharmProjects\Proyectos-de-ingenieria-de-software-Actividades\Actividad 5\Diccionario")
log_Act7 = open("a7_matricula", 'w+')
tokensTotalesDic = open("TokensTotalesDic", "w+", encoding='utf-8', errors='ignore')
postingFile = open("PostingFile", "w+", encoding='utf-8', errors='ignore')
counter = Counter()


def limpiar(texto):
    texto = ' '.join(e for e in texto.split() if e.isalpha())
    texto = texto.lower()
    return texto


Start = time.time()
for name in os.listdir(directory):
    with open(directory/name, 'r', encoding='utf-8', errors='ignore') as filehandle:
        counter.update(set(limpiar(filehandle.read()).split()))
        # ^ para obtener numero de archivos donde viene la palabra


for word, count in counter.most_common():
    for name in os.listdir(directory):
        with open(directory / name, 'r', encoding='utf-8', errors='ignore') as filehandle:
            word_counter = limpiar(filehandle.read()).split().count(str(word))
            if word_counter > 0:
                postingFile.write('{} ; {}'.format(name, word_counter))
                postingFile.write('\n')

toll = 0
for word, count in counter.most_common():
    tokensTotalesDic.write('{} ; {}'.format(word, count) + " ; " + str(toll))
    tokensTotalesDic.write('\n')
    toll = toll + count
End = time.time()
log_Act7.write("Tiempo total: " + str(End - Start))
