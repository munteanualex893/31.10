#Problema 5
"""
Se dau două numere. Să se înmulţească cel mai mare cu doi şi cel mai mic cu trei şi să se afişeze rezultatele. Exemplu
: date de intrare: 3  7  date de ieşire: 9  14
"""
a=int(input("Introduceti 1 numar:"))
b=int(input("Introduceti 2 numar:"))
if a>b:
    print(a*2, b*3)
elif a<b:
    print(a*3,b*2)
else:
    print(a*2,b*3)