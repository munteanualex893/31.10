#Problema 3
#Se introduc punctajele a doi sportivi. Afişaţi-le în ordine descrescătoare. Exemplu:  Date de intrare 100  134   Date de ieşire: 134 puncte   100 puncte
a=int(input("Introduceti numarul de puncte ale 1 sportiv:"))
b=int(input("Introduceti numarul de puncte ale 2 sportiv:"))
if a>b:
    print(a," puncte, ", b," puncte.")
else:
    print(b," puncte, ", a," puncte.")