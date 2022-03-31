# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 00:20:34 2022

@author: marcn
"""
import PyPDF2
import time
inicio = time.time()

pdfFileObj=open("Actividad9_stoplist.pdf", 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
NumTokens = 0
Rep = 0
finalValue = ""
for x in range(0, pdfReader.numPages):
    pagObj = pdfReader.getPage(x)
    word = pagObj.extractText()
    print(word)
    Rep = Rep +1
    for i in word.split():
        cont = word.count(i)
        characters = i
        if cont < 2:
            for x in range(len(characters)):
                string = word.replace(characters[x],"")
                finallValue = string
        if len(string) < 2:
            for x in range(len(characters)):
                finallValue = string.replace(characters[x],"")
        NumTokens = NumTokens + len(finallValue.split(' '))

'''
TF * 100 / NumTokens
'''     
print("\nTokens Totales: ", NumTokens)
print("Repeticiones: ", Rep)
WeightTokens = (Rep*100)/NumTokens
print("WeightTokens Value: ", WeightTokens)
fin = time.time()
print("Timer: ", fin-inicio) 
