lista=[""]*7
for i in range(7):
    ime=input()
    pomak=int(input())
    lista[i+pomak]=ime
for i in lista:
    print(i)
print(lista)
