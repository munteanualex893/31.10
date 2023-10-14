#Problema 6
"""
Se introduc două numere întregi. Să se testeze dacă primul număr este predecesorul (succesorul) celui de-al doilea şi să se afişeze un mesaj corespunzător. Exemple
: date de intrare: 2  4  date de ieşire: Nu; date de intrare: 5    6   date de ieşire: Da.
"""
a=int(input("Introduceti 1 numar:"))
b=int(input("Introduceti 2 numar:"))
if (a==b-1):
    print(b, "este succesorul lui ", a)
elif(a==b+1):
    print(b," este predecesorul lui ", a)
else:
    print(b," nu este nici predecesorul si nici succesorul lui ",a)