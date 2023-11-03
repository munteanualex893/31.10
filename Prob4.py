"""
Elaborați un program care va calcula suma, produsul și media aritmetică a numerelor de la 1 la n, pentru n introdus de la tastatură.
"""
sum=0
pro=1
n=int(input("Introduce-ti un numar:"))
i=1
while n>=i:
    sum+=i
    pro*=i
    i+=1
print("Suma e:", sum)
print("Produsul e:",pro)
print("media aritmetica e:", pro/sum)