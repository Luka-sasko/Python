lista=[""]*39
for i in range(0,39):
    lista[i]='*'
for i in range(0,7):
    n=int(input())
    lista[n-1]='X'
for i in range(0,13):
    print(lista[3*i]+lista[3*i+1]+lista[3*i+2])
    
