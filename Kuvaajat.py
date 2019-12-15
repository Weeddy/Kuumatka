#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 14:45:00 2019

@author: eetmakk
"""

import numpy as np
import matplotlib.pyplot as plt

Tulokset = np.loadtxt("Kuumatkatulokset")
askel = Tulokset[:,0]
alkunopeus = Tulokset[:,1]
kesto = Tulokset[:,2]

###################################################################

plt.plot(askel,alkunopeus, 'x')
plt.xlabel("Käytetty aika-askel (s)",  fontsize = 15)
plt.ylabel("Raketin alkuvauhti v (m/s)", fontsize = 15)

sovitus1 = np.polyfit(askel,alkunopeus,3)

x = np.linspace(0,100,100)
plt.plot(x,sovitus1[0]*x**3+sovitus1[1]*x**2+sovitus1[2]*x+sovitus1[3], color='red')

plt.annotate(f"Raja-arvo {'%.2f'%sovitus1[3]} m/s",xy=(0.6,0.2),xycoords = "axes fraction", fontsize = 15)
plt.legend(("Alkuvauhdit","3. Asteen sovitus"),fontsize = 15)
plt.show()

###################################################################

plt.plot(askel, kesto, 'x')
plt.xlabel("Käytetty aika-askel dt (s)", fontsize = 15)
plt.ylabel("Matka-aika kuuhun t (h)", fontsize = 15)

sovitus2 = np.polyfit(askel,kesto,3)

x1 = np.linspace(0,100,100)
plt.plot(x1,sovitus2[0]*x1**3+sovitus2[1]*x1**2+sovitus2[2]*x1+sovitus2[3], color='red')
plt.annotate(f"Raja-arvo {'%.2f'%sovitus2[3]} h",xy=(0.7,0.2),xycoords = "axes fraction", fontsize = 15)
plt.legend(("Matka-ajat","3. Asteen sovitus"),fontsize = 15)
plt.show()

###################################################################