# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 17:45:44 2022

@author: marcn

"""
import PyPDF2
import time
inicio = time.time()

pdfFileObj=open("Actividad9_stoplist.pdf", 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

'''
for x in range(0, pdfReader.numPages):
    pagObj = pdfReader.getPage(x)
    print(pagObj.extractText())

'''
finalValue = ""
for x in range(0, pdfReader.numPages):
    pagObj = pdfReader.getPage(x)
    word = pagObj.extractText()
    print(word)
    for i in word.split():
        #print("Pagina: ", x)
        cont = word.count(i)
        #print("Count: ",cont.count(i))
        #print(i, cont)
        characters = i
        #print("characteres: ", characters)
        if cont < 2:
            for x in range(len(characters)):
                string = word.replace(characters[x],"")
                finallValue = string
                #print(string)
        if len(string) < 2:
            for x in range(len(characters)):
                finallValue = string.replace(characters[x],"")
        
            print(finallValue)

fin = time.time()
print("\nTimer: ", fin-inicio) 