
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 01 11:56:10 2015

@author: Zombie.Soc // similarities
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib

from PIL import Image
from pylab import *

print ("Reconstruction of ion parabolas (Thomson spectrometer) by expansion of sum v^i*Z/A")




#Parameters

# !!! 0 point coordinates in px
x0 = 853
y0 = 305


B = 0.27 #magnetic field strength in Tesla

D = 0.633 # Drift of spectrometer

q = 1.6027E-19 # elemental charge q

l = 0.05 # lenght of magnet in m

Abbildung = 0.0001081 # Abbildungsmasstab m/pix

mp = 1.673E-27 # mass proton

E1 = 4.5E3 # potential of E-field in applied Voltage

Le = 0.0106 # distance of field plates in m

EF = E1/Le

v0 = 1E7 #v0 in m/s

print("mass number of ion?")
A= input("A:") # mass number of ion (197 for gold e.g.)


print ("maximal charge?")

Zmax = input("Z max: ")

if Zmax < 0:
	print "....Honestly"
elif Zmax == 1:
	print "ok but rather to small"

print("coefficient for expansion Ki*v^i, !!! < 0.5 !!!")


K0 = input("K0: ")

K1 = input("K1: ")

K2 = input("K2: ")

K3 = input("K3: ")

K4 = input("K4: ")

CC = B * l * D * q / ( A * mp * Abbildung )

CCC = EF * l * D * q / ( A * mp * Abbildung )



# calculates spectrometer function(x) in dependence of Z and v
def ganz(x):
    
    xganz = [x0]
    
    vi = [0]
    
    for i in range (1,x+1):
        
        #print i
        
        vi=(K0 * v0 ) 
        + (K1 * v0 * i / A) 
        + (K2 * v0 * i ** 2 / A) 
        + (K3 * v0 * i ** 3 / A) 
        + (K4 * v0 * i ** 4 / A)
        
        xganz.append(x0-i*CC/vi)
        
    return xganz
    



# calculates spectrometer function(y) in dependence of Z and v
def ganzy(x):
    
    yganz = [y0]
    
   # print(yganz)
    
    vi = [0]
    
    for i in range ( 1, x+1):
        
        vi=(K0 * v0)
        + (K1 * v0 * i / A)
        + (K2 * v0 * i ** 2 / A)
        + (K3 * v0 * i ** 3 / A)
        + (K4 * v0 * i ** 4 / A)
        
        yganz.append(y0 + i * CCC / vi ** 2)
        
    return yganz




def xp(x1):
    
    xp = [x1]
    
    for i in range (1, x1):
        
       xp.append(x1 - i)
       
    return xp
    
        
def parabely(x1, c):
    
    hh = [y0]
    
    const = (mp * A * EF / (c * q * l * D * B ** 2))
    
    for i in range (1, x1):
        
        hh.append(y0 + const * ((i) ** 2) * Abbildung)   
        
    return hh

        




    
#now read image and plot:
    
img = mpimg.imread('20140306_002ions.jpg')

imshow(img)

lum_img = img[:,:]

imgplot = plt.imshow(lum_img)

# spectral, hot, cool, ... tip was falsches ein.. dann kommen vorschläge :)

imgplot.set_cmap('binary_r')

plt.plot(ganz(Zmax), ganzy(Zmax),"ro",c = "w", alpha = 0.8, 
            label="reconstruction")
            
            
## plot parabola of Zmax
            
for i in range(1,Zmax):
    
    plt.plot(xp(x0), parabely(x0, Zmax))
    
plt.axis([0, 1032, 0, 756])

plt.show()



### 
raw_input('press Return>')


