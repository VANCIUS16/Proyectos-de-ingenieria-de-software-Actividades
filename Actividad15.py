#!D:\Users\marcn\AppData\Local\Programs\Python\Python310\python.exe
print("Content-type:text/html\r\n\r\n")
import cgi

form = cgi.FieldStorage()
palabra = form.getvalue("search")

from pathlib import Path
import os
import time
from collections import Counter

directory = Path(r"D:\xampp\htdocs\pycgi\Fase5\Diccionario")
counterFrec = Counter()
log_tokensTotales = open("log_tokensTotales", 'w+')
cont = 0

palabra

def limpiar(texto):
    texto = ' '.join(e for e in texto.split() if e.isalpha())
    texto = texto.lower()
    return texto

def frecuencia(archivo, palabra):
    data = open(directory/archivo, 'r', encoding='utf-8', errors='ignore')
    data2 = data.read()
    frecuencia = []
    frecuencia = data2.split()
    frecuencia2 = frecuencia.count(palabra)
    return frecuencia2

print('<html>')
print('<head>')
print('<title>Actividad 15</title>')
print('<h1>Actividad 15</h1>')
print('<h2>Resultados de la busqueda: ',palabra,'</h2>')
print('</head>')
print('<body>')
print('<table class="default">')
print('<tr>')
print('<td></h3>Word<h3></td>')
print('<td></h3>ID<h3></td>')
print('<td></h3>Archivo<h3></td>')
print('<td></h3>Frecuencia<h3></td>')
print('</tr>')

Start = time.time()
for name in os.listdir(directory):
    with open(directory/name, 'r', encoding='utf-8', errors='ignore') as filehandle:
        datafile = filehandle.readlines()
        for line in datafile:
            cont = cont + 1
            if palabra in line:
                
                ff = frecuencia(name, palabra)
                
                print('<tr>')
                print('<td></h2>', palabra, '<h2></td>')
                print('<td></h2>', cont, '<h2></td>')
                print('<td></h2>', name, '<h2></td>')
                print('<td></h2>', ff, '<h2></td>')
                print('</tr>')
                break
    cont = 0

End = time.time()
log_tokensTotales.write("Tiempo total: " + str(End - Start))

print('</tr>')
print('</table>')
print('<h2>Tiempo Total: ',str(End - Start),'</h2>')
print('</body>')
print('</html>')
