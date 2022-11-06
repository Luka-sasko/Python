
unos=''
p=input('pozicija kuglica:x,x ->')
p1=p[0]
p2=p[2]
for i in range(5):
    unos=input()
    u1=''
    u2=''
    u1=unos[0]
    u2=unos[2]
    if u1==p1 and u2==p2:
        p1=p1
    elif u1==p1:
        p1=u2
    elif u1==p2:
        p2=u2
    elif u2==p1:
        p1=u1
    elif u2==p2:
        p2=u1
        
        
if p1<p2:
    print(p1,p2)
else:
    print(p2,p1)
