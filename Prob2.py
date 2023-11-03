"""
Se citesc pe rând temperaturile medii ale fiecărei luni a unui an, ca numere întregi. Să se afişeze cu două zecimale media anuală a temperaturilor pozitive şi a celor negative.
Exemplu: Date de intrare  -5  -3  1  8  12  17  20  21  18  10  6  -2  Date de ieşire  medie_poz=13.66  medie_neg=-3.33.
"""
sp=0
sn=0
np=0
nn=0
i=1
while i<=12:
    t=eval(input("Introduceti temperatura:"))
    if t>=0:
        sp+=t
        np+=1
    else:
        sn+=t
        nn+=1
    i+=1
print("Media temperaturii pozitive e de ", sp/np)
print("Media temperaturii negative e de ", sn/nn)