#Problema 2
#Se introduc vârstele a doi copii. Afişaţi care copil este mai mare şi diferenţa de vârstă dintre cei doi. Exemplu : Date de intrare : 6  13  date de ieşire : al doilea copil este mai mare  cu  7 ani. 
v1=int(input("Introduceti varsta 1 copil:"))
v2=int(input("Introduceti varsta 2 copil:"))
if v1>v2:
    print("Copilul 1 are o varsat mai mare, diferenta fiind ",v1-v2," de ani.")
elif v2>v1:
    print("Copilul 2 are o varsta mai mare, diferenta fiind ",v2-v1," de ani.")
else:
    print("Ei au aceeasi varsta.")