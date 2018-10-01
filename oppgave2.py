#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 14:36:23 2018

@author: tirilkoplandtrondsen
"""

#Oppgave 2
#Program for kinetisk energi for et legeme i bevegelse, som finner en ukjent variabel.
#E=1/2mv^2, m = massen i kg, v = farten i m/s, E = den kinetiske energien i joule (J).

print ("Dette programmet kalkulerer den kinetiske enerigen for et legeme i bevegelse.")

svar = input("Vil du regne ut E, m eller v? ")


if svar == 'E':
    m_string = input("Tast inn objektets masse i kg: ")
    m = float (m_string)
    v_string = input ("Tast inn objektets fart i m/s: ")
    v = float (v_string)
    
    E = (1/2)*(m)*(v**2)
    print ("Objektet har en kinetisk energi på " + str(E) + " joules.")
    
    
elif svar == 'm':
    E_string = (input("Hvor stor er den kinetiske energien oppgit i joule? "))
    E = float (E_string)
    v_string = input("Tast inn objektets fart i m/s: ")
    v = float(v_string)
    
    m = (E) / ((1/2)*v**2)
    print ("Massen til objektet er" +str(m) + "kg.")
    
    
elif svar == 'v':
    E_string = (input("Hvor stor er den kinetiske energien oppgit i joule? "))
    E = float (E_string)
    m_string = input("Tast inn objektets masse i kg: ")
    m = float (m_string)
    
    v = (E) / ( (1/2)*m)
    v = math.sqrt(v)
    print ("Farten til objektet er " + str(v) + " m/s")

    
else:
    print("Feil inndata, prøv på nytt.")