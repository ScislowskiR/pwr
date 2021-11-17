import numpy as np
lista=np.array([74.002, 74.003, 74.015, 74.000, 74.005, 74.002, 74.005, 74.005])
#zad2.1
#%%
def wariancja(lista):
    nnum=lista.__len__()
    x_sum=np.sum([np.power(i,2)for i in lista])
    x_mean=np.power(np.sum(lista),2)/nnum
    s_squared=(x_sum-x_mean)/(nnum-1)
    s=np.sqrt(s_squared)
    #print(nnum)
    #print(x_sum)
    #print(x_mean)
    #print( "%.16f" % float(str(s_squared)))
    #print(s)
    return ("%.16f" % float(str(s_squared)))
wariancja(lista)
#%%
#zad2.2
wariancja(lista)
print("Z bibliotekami numpy:")
print( "%.16f" % float(str(np.var(lista,ddof=1))))#próba
print( "%.16f" % float(str(np.var(lista,ddof=0))))#populacja
print(np.mean(lista))
#%%
#zad2.2
def odchylenie_std(lista):#0.0000208392857143
    nnum=lista.__len__()
    licznik=[np.power(i-np.mean(lista),2) for i in lista]
    licznik=np.sum(licznik)
    standard=licznik/(nnum-1)
    standard=np.sqrt(standard)
    #print("%.16f" % float(str(standard)))
    return ("%.16f" % float(str(standard)))

odchylenie_std(lista)
print("Z bibliotekami numpy:")
print(np.std(lista,ddof=1))#próbka
print(np.std(lista,ddof=0))#populacja
#%%
#zad2.2
#Zakres
def zakres(lista):
    max=lista.max()
    min=lista.min()
    return min, max
zakres(lista)
#%%
#zad2.2
import time
import matplotlib.pyplot as plt
plt.plot(lista,'ro')
plt.show()
#%%
#zad2.3
lista2=np.array([0.19, 0.78, 0.96, 1.31, 2.78, 3.16, 4.15, 4.67, 4.85, 6.50,
          7.35, 8.01, 8.27, 12.06, 31.75, 32.52, 33.91, 36.71, 72.89])
print("Wartość średnia próbki")
print(lista2.mean())
print("Wariancja")
print(wariancja(lista2))
print("Odchylenie standardowe")
print(odchylenie_std(lista2))
#%%
#zad2.4
lista3=np.array([562, 869, 708, 775, 775, 704, 809, 856, 655, 805, 878, 909, 918, 558,
768, 870, 918, 940, 946, 660, 820, 898, 935, 952, 957, 693, 835, 905, 939, 955, 960, 499, 653, 730,
753])
print("Wartość średnia próbki")
print(lista3.mean())
print("Wariancja")
print(wariancja(lista3))
print("Odchylenie standardowe")
print(odchylenie_std(lista3))
#%%
#zad2.4
plt.plot(lista3)
plt.axhline(lista3.mean(),color='r',linestyle='-')
plt.show()
"""
Wartość średnia próbki jest średnią arytmetyczną wszystkich elementów próbki.
Charakteryzuje wielkości najbardziej reprezentatywne dla danych, centralną 
"tendencję" danych, określają "centrum" lub "środek" próbki.
"""
#%%
#zad2.5
"""
Wartość średnia całookresowa prądu sinusoidalnego
"""
#%%
#zad2.6
"""
lista=[1,2,3,4,100]
średnia=55
n=5
len(n<55)==4
"""
#%%
#zad2.7
#%%
#zad2.8
#%%
#zad2.9
#%%
#zad2.10
#Sześć cyfr to populacja

#Sześć wyników pomiarów stężenia pH to póbka
#%%
#zad2.11
lista4=np.array([63.2, 67.1, 65.8, 64.0, 66.1, 65.9])

print("Wartość średnia próbki")
print(lista4.mean())


print("Wariancja")
print(wariancja(lista4))
print("Odchylenie standardowe")
print(odchylenie_std(lista4))
plt.plot(lista4)
plt.axhline(lista4.mean(),color='r',linestyle='-')
plt.show()
#To zależy od tolerancji, jaką chcielibyśmy przyjąć