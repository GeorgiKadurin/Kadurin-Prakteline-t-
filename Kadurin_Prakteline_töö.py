#10----------------------------------
from math import *
print("Ajateisendus")
q=float(input("Sisestage aeg minutites => "))
a=int(q//60)
b=int(q%60)
print(f"{a}:{b}")




#9------------------------------------
from math import *
print("Rull Uisutaja keskmine kiirus on 29,9 km/h Kui kaugele jõuab 24 minutiga?")
b=24/60
a=b*29,9
print(f"Vastus:\n{a} km, {b} min, ")
print()




#8-------------------------------------
from math import *
from random import *
print("Kütusekulu arvutamine")
a=randint(1,100)
b=randint (1,100)
print(f"Vastus:\n a={a} \n b={b}")
r=(a/b)*100
print(f"kütusekulu:, {round(r,2)}")
print()





#7---------------------------------------
from math import * 
print("Pitsa")
p=12.90
n=0.10 #10% * 100 = 0.10
s=(p+n)/3
print(f"Vastus:\nSumma {round(s,2)}")
print()


#6-----------------------------------------
from math import * 
from random import * 
print("Kolmnurga ümbermõõt")
a=randint (1,100)
b=randint (1,100)
c=randint (1,100)
print()
print(f"Vastus:\nKülg a={a} \nKülg b={b} \nKülg c={c}")
print(f"Kolmnurga ümbermõõt = {a+b+c}")
print()

#5-------------------------------------------
print("    @..@" )
print("   (----)" )  
print("  ( \__/ )" )     
print("  ^^ '' ^^  ")    
print()
#4--------------------------------------------
from math import *
print("Keskmine")
a=float(input("1 number => "))
b=float(input("2 number => "))
v=float(input("3 number => "))
g=float(input("4 number => "))
d=float(input("5 number => "))
m=(a+b+v+g+d)/5
print()
print(f"Vastus:\nAritmeetiline arv",round(m,2))
print()

#3---------------------------------------------
print("harjutus")
aeg = float(input("Mitu tundi kulus sõiduks? "))
teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
kiirus = aeg / teepikkus
print()
print("Sinu kiirus oli " + str(round(kiirus,2)) + " km/h")



#2---------------------------------------------
from math import * 
print("Ristikülikukujulise matüki diagonaal")
N=float(input("Sisesta ristiküliku 1. külje pikkus =>  "))
M=float(input("Sisesta ristiküliku 2. külje pikkus =>  "))
d=sqrt(N**2+M**2)
print()
print("Диагональ", round(d,2))
print(f"Vastus:\nMaatüki diagonaal on {d} m**2")


#1---------------------------------------------
from math import * 
print("Puu läbimõõdu arvutamine")
C=float(input("Puu ümbermõõt?  "))
r=C/(2*pi)
print()
print("Puu raadius", round(r,2))
d=2*r
print()
print("Puu diagonaal", round(d,2))
print(f"Vastus:\nPuu läbimõõdoga {C} ümbermõõt võrdub {d}")


