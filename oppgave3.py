#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 16:39:11 2018

@author: tirilkoplandtrondsen
"""

#Oppgave 3
#Et program som beregner dyrebefolkningen t år fra i dag.


def regnPopulasjonsendring(): #Lager en funksjon
    bgammel = int(input("Hvor  stor er den nåværende dyrebefolkningen? "))
    t = int(input("Over hvor mange år skjer populasjonsendringen? "))
    ps = input("Stiger populasjonen? ja / nei ")
    
    if ps == 'ja':
        p = float(input("Hvor mange prosent stiger populasjonen?"))
        bny = (bgammel * (1+ (p/100)) **t )
        print ("Det er " + str(bny) + " etter " + str(t) + " år." )
        
    elif ps == 'nei':
        p = float(input("Hvor mange prosent synker populasjonen? "))
        bny = (bgammel * (1 - (p/100))**t)
        print ( "Det er " + str(bny) + " etter " + str(t) + " år.")
    
    else:
        print ("Feil inndata, prøv på nytt.")

while 1: #Lager en løkke
    regnPopulasjonsendring()
    spm = input("Vil du regne det ut en gang til? ja / nei ")
    if spm == 'nei':
        break