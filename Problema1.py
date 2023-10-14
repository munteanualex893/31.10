#Problema 1
#Sunt date două numere, afişaţi-l pe cel mai mic. Exemplu : Date de intrare : 44   32  Date de ieşire : 32.
a=int(input("Introduceti primul numar:"))
b=int(input("Introduceti al doilea numar:"))
if a>b:
    print(b, " este cel mai mic numar.")
else:
    print(a, " este cel mai mic numar.")