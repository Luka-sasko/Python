from tkinter import*
import math
global ulaz
global output
global elementi

t=Tk()
t.title('Kalkulator, Iva Mergeduš')
t.geometry('320x350')
t.config(bg='lightblue')
output=''
ulaz=''

Label(t,text='= ',font=('Arial',15)).place(relx=1/8,rely=4/5)
ispis=Label(t,text=output)
ispis.place(relx=2/9,rely=4/5)
ispis.config(bg='lightblue',font=('Arial',15,'bold'),fg='orange')

Label(t,text='Input: ',font=('Arial',15)).place(relx=1/8,rely=1/10)
ulaz2=Label(t,text=ulaz)
ulaz2.place(relx=1/3,rely=1/10)
ulaz2.config(bg='lightblue',font=('Arial',15,'bold'),fg='black')


def reset():
    global ulaz
    global output
    ulaz='                                     '
    output='                                     '
    refresh()
    refresh2()
    ulaz=''
    output=''
    refresh()
    refresh2()
    output=0
def refresh():
    ulaz2=Label(t,text=ulaz)
    ulaz2.place(relx=1/3,rely=1/10)
    ulaz2.config(bg='lightblue',font=('Arial',15,'bold'),fg='black')
def refresh2():
    ispis=Label(t,text=output)
    ispis.place(relx=2/9,rely=4/5)
    ispis.config(bg='lightblue',font=('Arial',15,'bold'),fg='red')
def znamenka1():
    global ulaz
    ulaz+='1'
    refresh()
    return
def znamenka2():
    global ulaz
    ulaz+='2'
    refresh()
    return
def znamenka3():
    global ulaz
    ulaz+='3'
    refresh()
    return
def znamenka4():
    global ulaz
    ulaz+='4'
    refresh()
    return
def znamenka5():
    global ulaz
    ulaz+='5'
    refresh()
    return
def znamenka6():
    global ulaz
    ulaz+='6'
    refresh()
    return
def znamenka7():
    global ulaz
    ulaz+='7'
    refresh()
    return
def znamenka8():
    global ulaz
    ulaz+='8'
    refresh()
    return
def znamenka9():
    global ulaz
    ulaz+='9'
    refresh()
    return
def znamenka0():
    global ulaz
    ulaz+='0'
    refresh()
    return
def tocka():
    global ulaz
    a=ulaz
    Reset()
    ulaz=''
    for i in range(0,len(a)):
        ulaz+=a[i]
    refresh()
    ulaz+='.'
    refresh()
    return
def zbroji():
    global ulaz
    ulaz+=' + '
    refresh()
    return
def oduzmi():
    global ulaz
    ulaz+=' - '
    refresh()
    return
def pomnozi():
    global ulaz
    ulaz+=' * '
    refresh()
    return
def podijeli():
    global ulaz
    ulaz+=' / '
    refresh()
    return
def SQRT():
    global ulaz
    ulaz+=' SQRT '
    refresh()
    return
def POT():
    global ulaz
    ulaz+=' ^ '
    refresh()
    return
def LN():
    global ulaz
    ulaz+=' LN '
    refresh()
    return
def LOG():
    global ulaz
    ulaz+=' LOG '
    refresh()
    return
def inv():
    global ulaz
    ulaz+=' ^-1 '
    refresh()
def ABS():
    global ulaz
    ulaz+=' ABS '
    refresh()
def Calculate():
    global output
    global ulaz
    elementi=ulaz.split()
    
    if ('*' in elementi):
        output=float(elementi[0])*float(elementi[2])
    elif ('/' in elementi):
        output=float(elementi[0])/float(elementi[2])
    elif ('+' in elementi):
        output=float(elementi[0])+float(elementi[2])
    elif('ABS' in elementi):
        if (elementi[1]=='-'):
            output=float(elementi[2])
        else:
            output=float(elementi[1])
    elif ('-' in elementi):
        output=float(elementi[0])-float(elementi[2])
    elif ('^' in elementi):
        output=pow(float(elementi[0]),float(elementi[2]))
    elif ('SQRT' in elementi):
        output=math.sqrt(float(elementi[1]))
    elif ('LN' in elementi):
        output=math.log(float(elementi[1]),2.718281)
    elif ('LOG' in elementi):
        output=math.log(float(elementi[1]),10)

    elif('^-1' in elementi):
        output=float(elementi[1])**-1

    refresh2()
    return
    

Button(t,text='1',command=znamenka1,bg='pink',font=('Arial',15)).place(x=30,y=90)
Button(t,text='2',command=znamenka2,bg='pink',font=('Arial',15)).place(x=65,y=90)
Button(t,text='3',command=znamenka3,bg='pink',font=('Arial',15)).place(x=100,y=90)
Button(t,text='4',command=znamenka4,bg='pink',font=('Arial',15)).place(x=135,y=90)
Button(t,text='5',command=znamenka5,bg='pink',font=('Arial',15)).place(x=30,y=140)
Button(t,text='6',command=znamenka6,bg='pink',font=('Arial',15)).place(x=65,y=140)
Button(t,text='7',command=znamenka7,bg='pink',font=('Arial',15)).place(x=100,y=140)
Button(t,text='8',command=znamenka8,bg='pink',font=('Arial',15)).place(x=135,y=140)
Button(t,text='9',command=znamenka9,bg='pink',font=('Arial',15)).place(x=30,y=190)
Button(t,text='0',command=znamenka0,bg='pink',font=('Arial',15)).place(x=65,y=190)

Button(t,text='.',command=tocka,bg='pink',font=('Arial',15)).place(x=100,y=190)
Button(t,text='=',command=Calculate,bg='purple',font=('Arial',15)).place(x=135,y=190)
Button(t,text='+',command=zbroji,bg='purple',font=('Arial',15)).place(x=170,y=90)
Button(t,text='-',command=oduzmi,bg='purple',font=('Arial',15)).place(x=205,y=90)
Button(t,text='*',command=pomnozi,bg='purple',font=('Arial',15)).place(x=240,y=90)
Button(t,text='/',command=podijeli,bg='purple',font=('Arial',15)).place(x=275,y=90)

Button(t,text='^-1',command=inv,bg='yellow',font=('Arial',16)).place(x=170,y=240)
Button(t,text='ABS',command=ABS,bg='yellow',font=('Arial',16)).place(x=225,y=240)

Button(t,text='sqrt',command=SQRT,bg='yellow',font=('Arial',16)).place(x=170,y=140)
Button(t,text='^n',command=POT,bg='yellow',font=('Arial',16)).place(x=240,y=140)
Button(t,text='ln',command=LN,bg='yellow',font=('Arial',16)).place(x=170,y=190)
Button(t,text='log ',command=LOG,bg='yellow',font=('Arial',16)).place(x=220,y=190)
Button(t,text='Reset',command=reset,bg='red',font=('Arial',16)).place(x=30,y=235)

