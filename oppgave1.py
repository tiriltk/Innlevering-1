#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 16:10:34 2018

@author: tirilkoplandtrondsen
"""

#Oppgave 1
#Et program som beregner pH-verdien.

import math

ioner = float(input("Hvor mange ioner per mol er det i løsningen din? ")) #Antall H^+-ioner i mol per liter som input

pH = -math.log(ioner) #En variabel som skal regne ut pH verdien. 

if 0 <= pH < 7: #Sjekker om løsningen er sur, nøytal eller basisk. 
    print ("Løsningen din er sur.")  
elif pH == 7:
    print ("Løsningen din er nøytral.")
elif pH <= 14:
    print ("Løsningen din er basisk.")        
else:
    print ("Løsning din må du se nærmere på, for den er utenfor pH skalaen.") #Dersom en taster inn en ugyldig verdi