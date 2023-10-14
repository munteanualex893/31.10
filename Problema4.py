#Problema 4
"""
Dintr-o cutie cu trei numere se extrag două numere. Cunoscând suma celor două numere extrase, să se afişeze numărul rămas în cutie. Exemplu
: date de intrare: numere  existente in cutie 5 12 8 suma numerelor extrase  13  date de ieşire: 12. 
"""
a=int(input("Introceti 1 numar: "))
b=int(input("Introceti 1 numar: "))
c=int(input("Introceti 1 numar: "))
suma1=int(input("Introduceti suma celor doua numere:"))
sumat=a+b+c
if sumat-suma1==a:
    print("Numarul ce a ramsa in cutie este ", a, ".")
elif sumat-suma1==b:
    print("Numarul ce a ramsa in cutie este ", b, ".")
elif sumat-suma1==c:
    print("Numarul ce a ramsa in cutie este ", c, ".")
else:
    print("Invatate sa socoti!")
