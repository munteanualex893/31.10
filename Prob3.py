"""Se citesc numere de la tastatură până la introducerea unui număr impar divizibil cu 3. Să se afişeze suma tuturor numerelor pare introduse.  
Exemplu: Date de intrare  7  4   6   2   1   9   Date de ieşire 12.  
"""
i=eval(input("Introduce-ti un numar:"))
suma=0
while not((i%2!=0) and (i%3==0)):
    if i%2==0:
        suma+=i
    i=eval(input("Introduce-ti un numar:")) 
print(suma)