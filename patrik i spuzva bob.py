n=int(input())
brojevi=input()
poredani=brojevi.split()
for i in range(0,n):
    poredani[i]=int(poredani[i])
poredani.sort()
p=poredani[n-1]
s=''
for i in range(n-1,0,-1):
    if poredani[i]<p:
        s=poredani[i]
        break
if s=='':
    print('0')
if s!='':
    print(s)
