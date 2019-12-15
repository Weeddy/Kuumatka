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
plt.xlabel("Käytetty aika-askel (s)")
plt.ylabel("Alkunopeus (m/s)")


sovitus1 = np.polyfit(askel,alkunopeus,2)


x = np.linspace(0,100,100)
plt.plot(x,sovitus1[0]*x**2+sovitus1[1]*x+sovitus1[2], color='red')

plt.annotate(f"Raja-arvo {'%.2f'%sovitus1[2]} m/s",xy=(0.6,0.2),xycoords = "axes fraction" )

plt.show()

###################################################################

plt.plot(askel, kesto, 'x')
plt.xlabel("Käytetty aika-askel (s)")
plt.ylabel("Matka-aika kuuhun (h)")

sovitus2 = np.polyfit(askel,kesto,2)

x1 = np.linspace(0,100,100)
plt.plot(x1,sovitus2[0]*x1**2+sovitus2[1]*x1+sovitus2[2], color='red')
plt.annotate(f"Raja-arvo {'%.2f'%sovitus2[2]} h",xy=(0.7,0.2),xycoords = "axes fraction" )

plt.show()

###################################################################