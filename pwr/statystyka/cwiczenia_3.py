import numpy as np
import seaborn as sns
import math
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
import seaborn as sns
import seaborn_qqplot as sqp
#Prawdopodobieństwo
#Dystrybuanta
#Rozkład Poissona
#Rozkład normalny
#Odchylenie standardowe

#zad1
x=np.array([-2,-1,0,1,2])
y=np.array([0.125,0.25,0.25,0.25,0.125])
#%%
def wariancja(lista,ddof=1):
    nnum=lista.__len__()
    x_sum=np.sum([np.power(i,2)for i in lista])
    x_mean=np.power(np.sum(lista),2)/nnum
    s_squared=(x_sum-x_mean)/(nnum-ddof)
    s=np.sqrt(s_squared)
    #print(nnum)
    #print(x_sum)
    #print(x_mean)
    #print( "%.16f" % float(str(s_squared)))
    #print(s)
    return ("%.16f" % float(str(s_squared)))
wariancja(y)
#%%
def odchylenie_std(lista,ddof=1):#0.0000208392857143
    nnum=lista.__len__()
    licznik=[np.power(i-np.mean(lista),2) for i in lista]
    licznik=np.sum(licznik)
    standard=licznik/(nnum-ddof)
    standard=np.sqrt(standard)
    #print("%.16f" % float(str(standard)))
    return ("%.16f" % float(str(standard)))
odchylenie_std(y)
#%%
def zakres(lista):
    max=lista.max()
    min=lista.min()
    return min, max
#%%
#a)
def probability(array, array2):
    omega=len(array)
    a=len(array2)
    return float(a/omega)
a_arr=np.array([i for i in x if i<=1])
a=probability(x, a_arr)
print(a)
#%%
#b)
b_arr=np.array([i for i in x if i>=-2])
b=probability(x, b_arr)
print(b)
#%%
#c)
c_arr=np.array([i for i in x if -1<=i<=1])
c=probability(x, c_arr)
print(c)
#%%
#d)
d_arr=np.array([i for i in x if i<=-1 or i==2])
d=probability(x, d_arr)
print(d)
#%%
#e)
def dystrybuanta(lista):
    x=[]
    suma=0
    for i in range(lista.__len__()):
        #print(y[i])
        suma+=lista[i]
        x.append(suma)
    #x.insert(0,0)
    return x
y_copy=dystrybuanta(y)
x_copy=list(x)
#x_copy.insert(0,0)
#plt.plot(x_copy, y_copy)
for i in range(len(x_copy)):
    plt.plot()
plt.xlabel("x")
plt.ylabel("F(X)")
plt.show()
#https://stackoverflow.com/questions/15408371/cumulative-distribution-plots-python
#https://matplotlib.org/stable/gallery/statistics/histogram_cumulative.html
#%%
#f)
def oczekiwana(x,y):
    lista=[]
    for i in range(len(x)):
        lista.append(x[i]*y[i])
    return sum(lista)
    return lista
EX=oczekiwana(x,y)
print(EX)
odchylenie_std([0.1,0.2,0.3,0.15,0.15,0.1])
np.std([0.1,0.2,0.3,0.15,0.15,0.1],ddof=1)
#%%
#g)
#sigma=odchylenie_std(y)
VX=wariancja(y)
print(VX)
#%%
#zad2
x2=np.array([0,1,2,3,4])
y2=[]
for i in x2:
    y2.append((2*i+1)/25)
sum(y2)
#%%
def prawdo(array, string=""):
    omega=len(array)
    array2=np.array( [x for x in array if eval(string)])
    a=len(array2)
    return float(a/omega)
#a)
print(prawdo(x2,"x==3"))
#b)
print(prawdo(x2,"x<=1"))
#c)
print(prawdo(x2,"2<=x<4"))
#d)
print(prawdo(x2,"x>-10"))

#%%
#e)
dystrybuanta(lista=y2)
#%%
#f)
oczekiwana(x2,y2)
#%%
#g)
wariancja(y2,ddof=1)
#%%
#zad3
#https://www.statystyka-zadania.pl/rozklad-dwumianowy/
def enka(en,ka):
    nsilnia=math.factorial(en)
    ksilnia=math.factorial(ka)
    mianownik=math.factorial(en-ka)*ksilnia
    return nsilnia/mianownik
enka(10,6)
#%%
def roz_dwumian(en,ka,pe):
    return enka(en,ka)*pe**ka*np.power(1-pe,en-ka)
roz_dwumian(10,6,0.9)
#%%
#zad5
print((1-0.02)**40)
#%%
#zad6
#https://statystyka.online/rozklad-dwumianowy-i-poissona-zadania/#1525427569640-49ddc3ca-79bd
#http://wyznacznik.pl/rozklad-poissona-zadania
