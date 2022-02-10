# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 20:36:04 2022

@author: marcn
"""

import os
import time
path = "D:/Users/marcn/Documents/AAAA/Tecmilenio/Octavo Semestre/Proyectos de Ingeniería de Software/Fase 1/Actividad 1/Files"

for filename in os.listdir(path):
    Start = time.time()
    f = open(os.path.join(path, filename), 'r')
    #print("File Name: "+filename)
    f.close()
    end = time.time()
    print("File Name: "+filename+" || Times: ", end-Start)
    