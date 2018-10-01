#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 10:52:40 2018

@author: tirilkoplandtrondsen
"""

#Oppgave 4
#Et program som regner ut n!

n = int(input("Tast inn tallet ditt: "))
factorial = 1

if n < 0:
    print ("Tast inn et positivt tall: ")    
elif n == 0:
    print ("Fakulteten til 0 er 1.")
else:
    for i in range (1, n+1):
        factorial *= i
    print ("Fakulteten til ", n, "er ", factorial)