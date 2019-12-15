#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 14:12:08 2019

@author: eetmakk
"""
import matplotlib.pyplot as plt

M = 5.974*10**24                # Maan massa
m = 7.348*10**22                # Kuun massa
m_r = 1000                      # Raketin massa (turha)

G = 6.67428*10**(-11)           # Gravitaatiovakio
  
x = 6370*10**3                  # Etäisyys alussa (Maan säde)
r_kuu = 1737*10**3              # Kuun säde
R = 384400*10**3                # Kuun keskimääräinen etäisyys maasta
r_l = R                         # Etäisyys lopussa (Kuun etäisyys)

dt = 0.1                        # Iteroinnin aika-askel 
v =  11075.274                  # Lähtövauhti (muuta tätä)

F_maa = lambda x: G*M/x**2      # Maan vetovoima
F_kuu = lambda x: G*m/(R-x)**2  # Kuun vetovoima

#########################################################################

print(f"Lähtövauhti {v} m/s")

t = 0
sijainti = []
aika = []

while x < R-r_kuu:
    
    if v < 0 :
        print("Raketti ei päässyt kuuhun. Nosta lähtövauhtia.")
        break
    
    else:
        
        dp = (F_kuu(x)-F_maa(x))*dt
        dv = dp
        v_avg = v + dv/2
        t += dt
        dx = v_avg*dt
        x = x + dx
        v += dv
        
        sijainti.append(x/1000)
        aika.append(t/3600)

if v > 0:
    print("Kuulento onnistunut.")
    print(f"Raketin vauhti kuussa: {'%.3f'%v} m/s")
    print(f"Matka-aika {'%.3f'%(t/3600)} h")
    
plt.plot(aika,sijainti,'.', markersize = 1)
plt.ylabel("Etäisyys maasta (km)", fontsize = 15)
plt.xlabel("Lentoaika (h)", fontsize = 15)
plt.legend("Sijainti", fontsize = 15)
plt.show()

##########################################################################
















