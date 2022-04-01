from pathlib import Path
from collections import Counter
import os
import time

directory = Path("D:\PycharmProjects\Proyectos-de-ingenieria-de-software-Actividades\Actividad 3\Diccionario")
log_tokensTotales = open("log_tokensTotales", 'w+')
tokensTotales = open("TokensTotales", "w+", encoding='utf-8', errors='ignore')
counter = Counter()
counterFrec = Counter()


def limpiar(texto):
    texto = ' '.join(e for e in texto.split() if e.isalpha())
    texto = texto.lower()
    return texto


Start = time.time()
for name in os.listdir(directory):
    with open(directory/name, 'r', encoding='utf-8', errors='ignore') as filehandle:
        counter.update(set(limpiar(filehandle.read()).split()))
        # ^ para obtener numero de archivos donde viene la palabra

for name in os.listdir(directory):
    with open(directory/name, 'r', encoding='utf-8', errors='ignore') as filehandle:
        counterFrec.update(limpiar(filehandle.read()).split())
        # ^ para obtener la frecuencia de la palabra en todos los archivos

for word, count in counter.most_common():
    tokensTotales.write('{} ; {}'.format(word, count) + " ; " + str(counterFrec.get(word)))
    tokensTotales.write('\n')
End = time.time()
log_tokensTotales.write("Tiempo total: " + str(End - Start))
