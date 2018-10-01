#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 18:37:55 2018

@author: tirilkoplandtrondsen
"""

#Et lite tekstbasert eventyr RPG-spill.


navn = input ("Hva er karakter navnet ditt? ")

from time import sleep

sleep(1) #vent i 1 sekund

print ("Velkommen ", navn, ".")
sleep(1)
print (navn, "går inn i et mørkt, skummelt fjell på leting etter eventyr.")
sleep (1)

for i in range(5):
    
    sleep (1)
    print ("Du kan enten utforske, sove, rømme, angripe eller overgi deg.")
    sleep(1)

    svar = input ("Hva vil du gjøre? ")
    
    if svar == 'utforske':
        sleep(1)
        print (navn, "utforsker og kommer til en passasje og møter et troll.")
        
    elif svar == 'sove':
        sleep (1)
        print (navn, "føler seg trøtt og tar en lur. Litt senere våkner", navn, " og vil utforske videre.")
       
    elif svar == 'rømme':
        sleep (1) 
        print (navn, "løper rundt i sirkler. Til slutt føler", navn, "seg sliten.")
       
    elif svar == 'overgi meg':
        sleep (1)
        print ("Oh no, du kan ikke overgi deg!")
        break
        
       
    elif svar == 'angripe':
        sleep (1)
        print (navn, "angriper trollet og overvinner det! Hurra!")
        print ("Gratulerer," , navn , ", du vant spillet!")
    
    else:
        sleep (1)
        print ("Oh, jeg forstod ikke hva du sa, prøv en gang til." )
        
exit()
 