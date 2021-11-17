def stutter(word):
	return f"{word[0:2]}... {word[0:2]}... {word}"
stutter('siema')
#%%
import numpy as np
x=1200 - 500 + np.cos(np.pi/6)*1000 + np.cos(np.pi/4)*800
print(x)
#%%
y=np.sin(np.pi/6)*1000-np.sin(np.pi/4)*800
print(y)
#%%
x1=np.cos(np.pi/6)*2000
print(x1)
#%%
y1=np.sin(np.pi/6)*2000
print(y1)
#%%
moment=-np.sqrt(5**2+2**2)*2000
print(moment)
#%%
boat1x=3/5*4000
print(boat1x)
boat1y=-4/5*4000
print(boat1y)
#%%
boat2x=np.cos(np.pi/4)*4000
print(boat2x)
boat2y=np.sin(np.pi/4)*4000
print(boat2y)
#%%
boat3x=0
print(boat3x)
boat3y=-4000
print(boat3y)
#%%
boatx=sum([boat1x,boat2x,boat3x])
print(boatx)
boaty=sum([boat1y,boat2y,boat3y])
print(boaty)
#%%
def arm(x,y):
    z=np.sqrt(x*x+y*y)
    return z
arm1=arm(100,50)
print(arm1)
arm2=arm(250,50)
print(arm2)
arm3=arm(400,50)
print(arm3)
force=-arm1*4000+arm2*4000-arm3*4000
print(force)
#%%
Frr=500*9
Frt=0.5*300*9
force=Frr+Frt
print(force)
#%%
moveR=0.5*9*Frr
moveT=(2/3)*9*Frt
move=(moveR+moveT)/(Frr*Frt)
print(move)
#%%
move=(Frr*4.5+Frt*9*2/3)/(Frr+Frt)
print(move)
#%%
#zadanie 3
Ac=np.pi*np.power(5.25,2)/4
print(Ac)
Ar=5.25*6.5
print(Ar)
Asum=Ac+Ar
print(Asum)
#%%
S1=Ac*(4*5.25)/(3*np.pi)
S2=Ar*5.25/2
Xtotal=(S1+S2)/(Ac+Ar)
print(Xtotal)