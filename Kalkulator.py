from tkinter import*
from tkinter.messagebox import *
import math
global Unos
global poruka
global Izlaz
Unos=''
poruka=''
t=Tk()
t.title('Kalkulator')
t.geometry('400x500')
t.config(bg='white')
Label(t,text='Rezultat: ',font=('Arial',20)).place(relx=1/20,rely=18/20)
ispis=Label(t,text=poruka)
ispis.place(relx=7/20,rely=18/20)
ispis.config(bg='white',font=('Arial',20,'bold'),fg='red')

def ispis():
    print('Funkcije:\n1. ... \n2. ... \n   ... \nn. ...')
def primjeri():
    print('Primjer funkcije:\n1. ...\n2. ... \n   ... \nn. ...')
izbornik=Menu(t)
datoteka_izbornik=Menu(izbornik)
datoteka_izbornik.add_command(label='Popis funkcija',command=ispis)
datoteka_izbornik.add_command(label='Primjeri fukncija',command=primjeri)
izbornik.add_cascade(label='Help',menu=datoteka_izbornik)
t.config(menu=izbornik)

Label(t,text='Unos: ',font=('Arial',20)).place(relx=1/20,rely=1/50)
ulaz=Label(t,text=Unos)
ulaz.place(relx=3/11,rely=1/50)
ulaz.config(bg='white',font=('Arial',20,'bold'),fg='black')
def refreshIzlaz():
    ispis=Label(t,text=poruka)
    ispis.place(relx=7/20,rely=18/20)
    ispis.config(bg='white',font=('Arial',20,'bold'),fg='red')
    return
def refresh():
    ulaz=Label(t,text=Unos)
    ulaz.place(relx=3/11,rely=1/50)
    ulaz.config(bg='white',font=('Arial',20,'bold'),fg='black')
    return

def Ans():
    global Unos
    global Izlaz
    Unos+=str(Izlaz)
    refresh()
    return
def Unos1():
    global Unos
    Unos+='1'
    refresh()
    return
def Unos2():
    global Unos
    Unos+='2'
    refresh()
    return
def Unos3():
    global Unos
    Unos+='3'
    refresh()
    return
def Unos4():
    global Unos
    Unos+='4'
    refresh()
    return
def Unos5():
    global Unos
    Unos+='5'
    refresh()
    return
def Unos6():
    global Unos
    Unos+='6'
    refresh()
    return
def Unos7():
    global Unos
    Unos+='7'
    refresh()
    return
def Unos8():
    global Unos
    Unos+='8'
    refresh()
    return
def Unos9():
    global Unos
    Unos+='9'
    refresh()
    return
def Unos0():
    global Unos
    Unos+='0'
    refresh()
    return
def Unos_DT():
    global Unos
    a=Unos
    Reset()
    Unos=''
    for i in range(0,len(a)):
        Unos+=a[i]
    refresh()
    Unos+='.'
    refresh()
    return
def zbroji():
    global Unos
    Unos+=' + '
    refresh()
    return
def oduzmi():
    global Unos
    Unos+=' - '
    refresh()
    return
def pomnozi():
    global Unos
    Unos+=' * '
    refresh()
    return
def podijeli():
    global Unos
    Unos+=' / '
    refresh()
    return
def zagrada1():
    global Unos
    Unos+=' ( '
    refresh()
    return
def zagrada2():
    global Unos
    Unos+=' ) '
    refresh()
    return
def cos():
    global Unos
    Unos+=' cos '
    refresh()
    return
def sin():
    global Unos
    Unos+=' sin '
    refresh()
    return
def tg():
    global Unos
    Unos+=' tg '
    refresh()
    return
def ln():
    global Unos
    Unos+=' ln '
    refresh()
    return
def log():
    global Unos
    Unos+=' log '
    refresh()
    return
def space():
    global Unos
    Unos+=' '
    refresh()
    return
def fact():
    global Unos
    Unos+=' ! '
    refresh()
    return
def potencija():
    global Unos
    Unos+=' ^ '
    refresh()
    return
def povrh():
    global Unos
    Unos+=' povrh '
    refresh()
    return
def korijen():
    global Unos
    Unos+=' sqrt '
    refresh()
    return
def inverz():
    global Unos
    Unos+=' ^-1 '
    refresh()
def ABS():
    global Unos
    Unos+=' ABS '
    refresh()
def Exit():
    t.destroy()
    return
def Reset():
    global Unos
    global poruka
    global Izlaz
    Izlaz=0
    Unos='                                     '
    poruka='                                     '
    refresh()
    Unos=''
    refresh()
    refreshIzlaz()
    return
def Reset_bez_izlaza():
    global Unos
    global poruka
    global Izlaz
    Unos='                                     '
    poruka='                                     '
    refresh()
    Unos=''
    refresh()
    refreshIzlaz()
    return
def Delete():
    global Unos
    global poruka
    a=Unos
    Reset_bez_izlaza()
    Unos=''
    for i in range(0,len(a)-2):
        Unos+=a[i]
    refresh()
    return
def Calculate(x,y,radnja):
    if (radnja=='+'):
        return(x+y)
    elif(radnja=='-'):
        return(x-y)
    elif(radnja=='*'):
        return(x*y)
    elif(radnja=='/'):
        return(x/y)
def CalcZagrada():
    global Unos
    global Izlaz
    global parametri
    i=0
    Izlaz=0
    while(parametri[i]!='('):
        i+=1
    while(parametri[i]=='('):
        i+=1
    if(parametri[i-1]=='(' and parametri[i+1]==')'):
        del parametri[i+1]
        del parametri[i-1]
        Izlaz=float(parametri[i-1])
    else:
        Izlaz+=Calculate(float(parametri[i]),float(parametri[i+2]),parametri[i+1])
        parametri.insert(i,Izlaz)
        del parametri[i+1]
        del parametri[i+1]
        del parametri[i+1]
        del parametri[i+1]
        del parametri[i+-1]
    return
def CalcCos():
    global Unos
    global Izlaz
    global parametri
    i=0
    Izlaz=0
    while (parametri[i]!='cos'):
        i+=1
    del parametri[i]
    Izlaz=math.cos(float(parametri[i]))
    parametri.insert((i),Izlaz)
    del parametri[i+1]
    return
def CalcSin():
    global Unos
    global Izlaz
    global parametri
    i=0
    Izlaz=0
    while (parametri[i]!='sin'):
        i+=1
    del parametri[i]
    Izlaz=math.sin(float(parametri[i]))
    parametri.insert((i),Izlaz)
    del parametri[i+1]
    return
def CalcTg():
    global Unos
    global Izlaz
    global parametri
    i=0
    Izlaz=0
    while (parametri[i]!='tg'):
        i+=1
    del parametri[i]
    Izlaz=math.tan(float(parametri[i]))
    parametri.insert((i),Izlaz)
    del parametri[i+1]
    return
def Calcpotencija():
    global Unos
    global Izlaz
    global parametri
    i=0
    Izlaz=0
    while (parametri[i]!='^'):
        i+=1
    del parametri[i]
    Izlaz=(float(parametri[i-1]))**(float(parametri[i]))
    parametri.insert((i-1),Izlaz)
    del parametri[i]
    del parametri[i]
    return
def CalcLN():
    global Unos
    global Izlaz
    global parametri
    i=0
    Izlaz=0
    while (parametri[i]!='ln'):
        i+=1
    del parametri[i]
    Izlaz=math.log((float(parametri[i])),2.718281)
    parametri.insert((i-1),Izlaz)
    del parametri[i]
    return
def CalcLOG():
    global Unos
    global Izlaz
    global parametri
    i=0
    Izlaz=0
    while (parametri[i]!='log'):
        i+=1
    del parametri[i]
    Izlaz=math.log(float(parametri[i+1]),(float(parametri[i])))
    parametri.insert((i-1),Izlaz)
    del parametri[i]
    del parametri[i]
    return
def Calcfaktorijel():
    global Unos
    global Izlaz
    global parametri
    suma=1
    i=0
    Izlaz=0
    while (parametri[i]!='!'):
        i+=1
    br=i
    del parametri[i]
    for i in range(1,int(parametri[i])+1):
        suma*=i
    Izlaz=suma
    del parametri[br]
    parametri.insert(i,Izlaz)
def F(parametar):
    suma=1
    i=0
    for i in range(1,parametar+1):
        suma*=i
    return(suma)
def CalcPovrh():
    global Unos
    global Izlaz
    global parametri
    suma=1
    i=0
    Izlaz=0
    while (parametri[i]!='povrh'):
        i+=1
    br=i
    del parametri[i]
    Izlaz=((F(int(parametri[i-1])))/((F(int(parametri[i])))*(F((int(parametri[i-1]))-(int(parametri[i]))))))
    del parametri[i-1]
    del parametri[i-1]
    parametri.insert(i,Izlaz)
def CalcSqrt():
    global Unos
    global Izlaz
    global parametri
    i=0
    Izlaz=0
    while (parametri[i]!='sqrt'):
        i+=1
    del parametri[i]
    Izlaz=math.sqrt(float(parametri[i]))
    del parametri[i]
    parametri.insert(i,Izlaz)
    return
def CalcInverz():
    global Unos
    global Izlaz
    global parametri
    i=0
    Izlaz=0
    while (parametri[i]!='^-1'):
        i+=1
    del parametri[i]
    Izlaz=(float(parametri[i-2]))**(-1)
    parametri.insert((i-1),Izlaz)
    del parametri[i]
    return
    
    

def Calc():
    global Unos
    global Izlaz
    global parametri
    global poruka
    parametri=Unos.split()
    for i in range(len(parametri)):
        if (parametri[i]==' '):
            parametri[i]=''
    while ('(' in parametri):
        CalcZagrada()
    while('cos' in parametri):
        CalcCos()
    while('sin' in parametri):
        CalcSin()
    while('tg' in parametri):
        CalcTg()
    while('^' in parametri):
        Calcpotencija()
    while('ln' in parametri):
        CalcLN()
    while('log' in parametri):
        CalcLOG()
    while ('(' in parametri):
        CalcZagrada()
    while('!' in parametri):
        Calcfaktorijel()
    while('povrh' in parametri):
        CalcPovrh()
    while ('sqrt' in parametri):
        CalcSqrt()
    while('^-1' in parametri):
        CalcInverz()
    while('ABS' in parametri):
        i=0
        b=''
        a=''
        Izlaz=0
        while (parametri[i] != 'ABS'):
            i+=1
        del parametri[i]
        a=parametri[i]
        if(a!='-'):
            Izlaz=parametri[i]
        else:
            Izlaz=parametri[i+1]
        parametri.insert(i,Izlaz)
        del parametri[i+1]
        del parametri[i+1]
        print(parametri)
    while ('*' in parametri):
        i=0
        Izlaz=0
        while (parametri[i] != '*'):
            i+=1
        Izlaz+=(float(parametri[i-1])*float(parametri[i+1]))
        del parametri[i+1]
        del parametri[i]
        del parametri[i-1]
        parametri.insert((i-1),Izlaz)
    while ('/' in parametri):
        i=0
        Izlaz=0
        while (parametri[i] != '/'):
            i+=1
        Izlaz+=(float(parametri[i-1]) / float(parametri[i+1]))
        del parametri[i+1]
        del parametri[i]
        del parametri[i-1]
        parametri.insert((i-1),Izlaz)
    while ('+' in parametri):
        i=0
        Izlaz=0
        while (parametri[i] != '+'):
            i+=1
        Izlaz+=(float(parametri[i-1]) + float(parametri[i+1]))
        del parametri[i+1]
        del parametri[i]
        del parametri[i-1]
        parametri.insert((i-1),Izlaz)
    while ('-' in parametri):
        i=0
        Izlaz=0
        while (parametri[i] != '-'):
            i+=1
        Izlaz+=(float(parametri[i-1]) - float(parametri[i+1]))
        del parametri[i+1]
        del parametri[i]
        del parametri[i-1]
        parametri.insert((i-1),Izlaz)
    poruka=Izlaz
    refreshIzlaz()
    return


Button(t,text='1',command=Unos1,bg='lightblue',font=('Arial',15)).place(x=30,y=120)
Button(t,text='2',command=Unos2,bg='lightblue',font=('Arial',15)).place(x=65,y=120)
Button(t,text='3',command=Unos3,bg='lightblue',font=('Arial',15)).place(x=100,y=120)
Button(t,text='4',command=Unos4,bg='lightblue',font=('Arial',15)).place(x=135,y=120)
Button(t,text='5',command=Unos5,bg='lightblue',font=('Arial',15)).place(x=30,y=170)
Button(t,text='6',command=Unos6,bg='lightblue',font=('Arial',15)).place(x=65,y=170)
Button(t,text='7',command=Unos7,bg='lightblue',font=('Arial',15)).place(x=100,y=170)
Button(t,text='8',command=Unos8,bg='lightblue',font=('Arial',15)).place(x=135,y=170)
Button(t,text='9',command=Unos9,bg='lightblue',font=('Arial',15)).place(x=30,y=220)
Button(t,text='0',command=Unos0,bg='lightblue',font=('Arial',15)).place(x=65,y=220)
Button(t,text='.',command=Unos_DT,bg='lightblue',font=('Arial',15)).place(x=100,y=220)

Button(t,text='=',command=Calc,bg='blue',font=('Arial',16)).place(x=135,y=220)
Button(t,text='(',command=zagrada1,bg='blue',font=('Arial',16)).place(x=190,y=220)
Button(t,text=')',command=zagrada2,bg='blue',font=('Arial',16)).place(x=225,y=220)
Button(t,text='Space',command=space,bg='blue',font=('Arial',16)).place(x=95,y=270)

Button(t,text='!',command=fact,bg='purple',font=('Arial',16)).place(x=190,y=270)
Button(t,text='povrh',command=povrh,bg='purple',font=('Arial',16)).place(x=225,y=270)
Button(t,text='sqrt',command=korijen,bg='purple',font=('Arial',16)).place(x=300,y=270)
Button(t,text='Ans',command=Ans,bg='pink',font=('Arial',15)).place(x=30,y=270)

Button(t,text='cos',command=cos,bg='yellow',font=('Arial',16)).place(x=315,y=170)
Button(t,text='sin',command=sin,bg='yellow',font=('Arial',16)).place(x=265,y=170)
Button(t,text='tg',command=tg,bg='yellow',font=('Arial',16)).place(x=275,y=120)
Button(t,text='^n',command=potencija,bg='yellow',font=('Arial',16)).place(x=320,y=120)

Button(t,text='ln',command=ln,bg='lightgreen',font=('Arial',16)).place(x=260,y=220)
Button(t,text='log B (x)',command=log,bg='lightgreen',font=('Arial',16)).place(x=300,y=220)

Button(t,text='^-1',command=inverz,bg='lightgreen',font=('Arial',16)).place(x=300,y=320)
Button(t,text='ABS',command=ABS,bg='lightgreen',font=('Arial',16)).place(x=230,y=320)


Button(t,text='Exit',command=Exit,bg='red',font=('Arial',16)).place(x=325,y=400)
Button(t,text='Reset',command=Reset,bg='red',font=('Arial',16)).place(x=30,y=70)

Button(t,text='Delete',command=Delete,bg='orange',font=('Arial',16)).place(x=110,y=70)


Button(t,text='+',command=zbroji,bg='blue',font=('Arial',15)).place(x=190,y=120)
Button(t,text='-',command=oduzmi,bg='blue',font=('Arial',15)).place(x=225,y=120)
Button(t,text='*',command=pomnozi,bg='blue',font=('Arial',15)).place(x=190,y=170)
Button(t,text='/',command=podijeli,bg='blue',font=('Arial',15)).place(x=225,y=170)
t.mainloop()
