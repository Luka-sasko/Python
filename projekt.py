from tkinter import*
from tkinter.messagebox import *
import math
global ulaz,izlaz
ulaz='0'
izlaz=0
def exit():
    t.destroy()
def conv():
    global ulaz,izlaz
    x=entry.get()
    ulaz=x+(32-len(x))*'0'
    if(len(x)>32):
        return
    unos=[]
    for i in range(32):
        unos.append(0)
    for i in range(len(x)):
        unos[i]=int(x[i])
    predznak=unos[0]
    if (predznak ==0):
        predznak=1
    else:
        predznak=-1
    karakteristika=unos[1:9]
    k=0
    for i in range(8):
        k+=pow(2,8-i-1)*karakteristika[i]
    mantisa=unos[9:32]

    m=1
    x=k-127
    broj=[m]
    dec=[]
    for i in range(len(mantisa)):
        if (i<x):
            broj.append(mantisa[i])
        else:
            dec.append(mantisa[i])

    for i in range(len(broj)):
        izlaz+=pow(2,len(broj)-i-1)*broj[i]
    
    for i in range(len(dec)):
        izlaz+=pow(2,-i-1)*dec[i]    
    izlaz*=predznak

    u=[]
    heksa=[]
    for i in range(0,32,4):
        u.append(unos[i:i+4])
        zbroj=0
    
    for i in range(0,8):
        ui=u[i]
        zbroj=0
        for i in range(0,4):
            zbroj+=pow(2,4-i-1)*int(ui[i])
        if (zbroj>10):
            if(zbroj==10):
                heksa.append('A')
            elif(zbroj==11):
                heksa.append('B')
            elif(zbroj==12):
                heksa.append('C')
            elif(zbroj==13):
                heksa.append('D')
            elif(zbroj==14):
                heksa.append('E')
            elif(zbroj==15):
                heksa.append('F')
        else:
            heksa.append(str(zbroj))
    heksa_ispis=heksa[0]+5*'  '+heksa[1]+5*'  '+heksa[2]+5*'  '+heksa[3]+5*'  '+heksa[4]+5*'  '+heksa[5]+5*'  '+heksa[6]+5*'  '+heksa[7]
    Label(t,text='Heksadecimalni zapis unosa: ').place(relx=0.02,rely=0.5)
    Label(t,text=heksa_ispis,fg='red',bg='white').place(relx=0.375,rely=0.5)
    Label(t,text=ulaz,bg='white',fg='blue',font=('Monospace',12)).place(relx=0.35,rely=0.6)
    Label(t,text=izlaz,bg='white',fg='blue',font=('Monospace',12)).place(relx=0.35,rely=0.7)
    return



t=Tk()
t.title('IEEE 754 STANDARD CONVERTER BIN TO DEC')
t.geometry('500x300')

photo=PhotoImage(file="photo.png")
Label(t,image=photo).place(x=0,y=0,relwidth=1,relheight=1)

Label(t,text='Unos : ',bg='white',fg='Blue').place(relx=0.05,rely=0.05)
Button(t,text='Convert',command=conv,bg='white',fg='Blue',font=('Monospace',12)).place(relx=0.7,rely=0.04)
entry=Entry(t,width=32)
entry.place(relx=0.2,rely=0.05)
Button(t,text='EXIT',bg='red',font=('Monospace',12),command=exit).place(relx=0.85,rely=0.85)
Label(t,text='Uneseni binarni broj: ',fg='Blue').place(relx=0.02,rely=0.6)
Label(t,text='Pretvoreni dekadski broj: ',fg='Blue').place(relx=0.02,rely=0.7)

t.mainloop()

