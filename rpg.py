#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 18:37:55 2018

@author: tirilkoplandtrondsen
"""

#Et lite tekstbasert eventyr RPG-spill.


navn = input ("Hva er karakter navnet ditt? ")

from time import sleep

sleep(2) #vent i 2 sekunder

print ("Velkommen ", navn, ".")
sleep(2)
print (navn, "går inn i et mørkt, skummelt fjell på leting etter eventyr.")
sleep (2)

for i in range(5):
    
    sleep (2)
    print ("Du kan enten utforske, sove, rømme, angripe eller overgi deg.")
    sleep(2)

    svar = input ("Hva vil du gjøre? ")
    
    if svar == 'utforske':
        sleep(2)
        print (navn, "utforsker og kommer til en passasje og møter et troll. Hva vil du gjøre?")
        
    elif svar == 'sove':
        sleep (2)
        print (navn, "føler seg trøtt og tar en lur. Litt senere våkner", navn, " og vil utforske videre.")
       
    elif svar == 'rømme':
        sleep (2) 
        print (navn, "løper rundt i sirkler. Til slutt føler", navn, "seg sliten.")
       
    elif svar == 'overgi meg':
        sleep (2)
        print ("Oh no, du kan ikke overgi deg!")
        break
        
       
    elif svar == 'angripe':
        sleep (2)
        print (navn, "angriper trollet og overvinner det! Hurra!")
        print ("Gratulerer," , navn , ", du vant spillet!")
    
    else:
        sleep (2)
        print ("Oh, jeg forstod ikke hva du sa, prøv en gang til." )
        
exit()
        
        
        
        
        
        
        
        
        
    
    