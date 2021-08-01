from random import random

sayı = round(random()*6)


a = 0
liste=[]

while a < 6:
    a += 1
    sayı = round(random() * 6)
    while sayı == 0:
        sayı = round(random() * 6)

    liste.append(sayı)


liste.sort()
print(liste)

bir = 0
iki = 0
üç = 0
dört = 0
beş = 0
altı = 0
a = 0
liste2=[0,0,0,0,0,0]

while a < 6:

    if liste[a] == 1:
        bir += 1
        liste2[0] = bir
    elif liste[a] == 2:
        iki += 1
        liste2[1] = iki
    elif liste[a] == 3:
        üç += 1
        liste2[2] = üç
    elif liste[a] == 4:
        dört += 1
        liste2[3] = dört
    elif liste[a] == 5:
        beş += 1
        liste2[4] = beş
    else:
        altı += 1
        liste2[5] = altı

    a += 1

print(liste2)

def check(l):
    return len(set(l)) == 1

if (liste.__contains__(1) and liste.__contains__(2) and liste.__contains__(3)):
    print(" 1-2-3 var, '10' puan kazandınız!")

elif (liste.__contains__(1) and liste.__contains__(2) and liste.__contains__(3) and liste.__contains__(4) and liste.__contains__(5) and liste.__contains__(6)):
    print(" 1-2-3-4-5-6 var \n Extra '50' puan kazandınız!")

elif (liste2.__contains__(2) or liste2.__contains__(4)):
    print(" Çift var \n Extra '10' puan kazandınız!")

elif (check(liste) == True):
    print(" Tebrikler!! '100' puan kazandınz!")

else:
    print(" Maalesef puan kazanamadınız :( ")
