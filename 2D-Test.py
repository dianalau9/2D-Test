"""
Autor: Diana Laura Pérez Pérez
Fecha: 14 de diciembre de 2020
Asignación: 2D Test
"""
import numpy as np
import matplotlib.pyplot as plt
from math import cos, sin, radians 

plt.axis([-70,90,-60,90])
plt.axis('on')
plt.axis(True)

#Rectángulo 1
x1=-40
x2=40
y1=-25
y2=25

#DRAWE FIGURE
plt.plot([x1,x1],[y1,y2],linewidth=1,color='k')
plt.plot([x2,x2],[y1,y2],linewidth=1,color='k')
plt.plot([x1,x2],[y1,y1],linewidth=1,color='k')
plt.plot([x1,x2],[y2,y2],linewidth=1,color='k')

#Rectángulo 2
x1=0
x2=80
y1=-0
y2=-50

#DRAWE FIGURE
plt.plot([x1,x1],[y1,y2],linewidth=1,color='k')
plt.plot([x2,x2],[y1,y2],linewidth=1,color='k')
plt.plot([x1,x2],[y1,y1],linewidth=1,color='k')
plt.plot([x1,x2],[y2,y2],linewidth=1,color='k')

#circulo 
xc=0
yc=0
r=15
p1=0*np.pi/180
p2=360*np.pi/180
dp=(p2-p1)/100

xlast=xc+r*np.cos(p1)
ylast=yc+r*np.sin(p1)
plt.axes().set_aspect('equal')

for p in np.arange(p1,p2+dp,dp):
    xp=xc+r*np.cos(p)
    yp=yc+r*np.sin(p)
    plt.plot([xlast,xp],[ylast,yp],color='k',linewidth=2)
    xlast=xp
    ylast=yp

plt.show()