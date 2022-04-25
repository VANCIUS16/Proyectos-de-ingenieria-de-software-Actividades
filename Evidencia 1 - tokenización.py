from pathlib import Path
from collections import Counter
import matplotlib.pyplot as plt
import os
import time

dir5  = "D:/Users/marcn/Documents/AAAA/Tecmilenio/Octavo Semestre/Proyectos de Ingeniería de Software/Fase 3/Proyectos-de-ingenieria-de-software-Actividades-master/Actividad 7/Diccionario5"
dir10 = "D:/Users/marcn/Documents/AAAA/Tecmilenio/Octavo Semestre/Proyectos de Ingeniería de Software/Fase 3/Proyectos-de-ingenieria-de-software-Actividades-master/Actividad 7/Diccionario10"
dir20 = "D:/Users/marcn/Documents/AAAA/Tecmilenio/Octavo Semestre/Proyectos de Ingeniería de Software/Fase 3/Proyectos-de-ingenieria-de-software-Actividades-master/Actividad 7/Diccionario20"
dir30 = "D:/Users/marcn/Documents/AAAA/Tecmilenio/Octavo Semestre/Proyectos de Ingeniería de Software/Fase 3/Proyectos-de-ingenieria-de-software-Actividades-master/Actividad 7/Diccionario30"
dir40 = "D:/Users/marcn/Documents/AAAA/Tecmilenio/Octavo Semestre/Proyectos de Ingeniería de Software/Fase 3/Proyectos-de-ingenieria-de-software-Actividades-master/Actividad 7/Diccionario40"
dir50 = "D:/Users/marcn/Documents/AAAA/Tecmilenio/Octavo Semestre/Proyectos de Ingeniería de Software/Fase 3/Proyectos-de-ingenieria-de-software-Actividades-master/Actividad 7/Diccionario50"
dir51 = "D:/Users/marcn/Documents/AAAA/Tecmilenio/Octavo Semestre/Proyectos de Ingeniería de Software/Fase 3/Proyectos-de-ingenieria-de-software-Actividades-master/Actividad 7/Diccionario51"

directorio = [dir20,dir30,dir40,dir50,dir51]

tiempoTot = list([])

for k in directorio:
    directory = Path(k)
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
    tiempoTot.append(End)
    log_tokensTotales.write("Tiempo total: " + str(End - Start))
    print("Dato: " + str(End - Start))

plt.plot([1,2,3,4,5], tiempoTot)
plt.ylabel('Tiempo')
plt.xlabel('Archivos')
plt.show()