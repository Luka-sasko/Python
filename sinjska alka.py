N=int(input())
while(N<1 or N>10):
    N=int(input())
bodovi=input()
lista=bodovi.split()
br=0
print(lista)
for i in range(0,N):
    lista[i]=int(lista[i])
lista.sort()
for i in range(0,N):
    m=lista[-1]
    if (lista[i]+3>=m):
        br+=1
print(br)
