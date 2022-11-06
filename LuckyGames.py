from tkinter import*
from tkinter.messagebox import *
import math
import random
global STANJE
global UPLATA
STANJE=0
UPLATA=0

def main():
    #globalne varijable
    global STANJE
    global UPLATA
    global bg_srecka
    global brojac
    global dobitak
    global running_dobitna_skrinja
    global running_srecka
    global running_high_low
    global ulog
    ulog=5
    #sve funkcije unutar maina
    #funkcija za prikaz stanja
    def start():
        Label(t,text=' '*18,font=('Script',80),bg='black').place(relx=(1/100),rely=(0.85))
        Label(t,text='STANJE: '+str(STANJE)+"kn",bg='orange',font=('MS Sans Serif',30)).place(relx=1/50,rely=0.86)
        Label(t,text='Posljednja uplata: '+str(UPLATA)+"kn",bg='yellow',font=('MS Sans Serif',30)).place(relx=1/50,rely=0.93)
        return

    #funkcija za uplatu
    def uplati():
        global STANJE
        global UPLATA
        STANJE+=int(uplata.get())
        UPLATA=int(uplata.get())
        showinfo("Uplata","Uspješno uplačeno:"+str(UPLATA)+"kn"+"\nUkupno stanje:"+str(STANJE)+"kn")
        start()
        return
    
    #funkcija za refresh stanja i dobitka
    def stanje():
        global brojac
        if (brojac%2==0):
            Label(t2,text=' '*25,font=('Script',30),bg='red').place(relx=(0.05),rely=(0.8))
            Label(t2,text=' '*25,font=('Script',30),bg='red').place(relx=(0.05),rely=(0.85))
            Label(t2,text='STANJE: '+str(STANJE)+"kn",bg='red',font=('MS Sans Serif',30),fg='orange').place(relx=0.05,rely=0.8)
            Label(t2,text='DOBITAK: '+str(dobitak)+"kn",bg='red',font=('MS Sans Serif',30),fg='orange').place(relx=0.05,rely=0.85)
        else:
            Label(t2,text=' '*26,font=('Script',30),bg='red').place(relx=(0.05),rely=(0.8))
            Label(t2,text=' '*26,font=('Script',30),bg='red').place(relx=(0.05),rely=(0.85))
        brojac+=1
        
    #funkcija iz isplatu
    def isplati():
        global STANJE
        showinfo('ISPLATA','Isplačeno:'+str(STANJE)+'kn')
        STANJE=0
        start()
        
    #funkcija za izlaz iz programa "Srečka"
    def quit1():
        t2.destroy()
        global running_srecka
        running_srecka=not(running_srecka)
        main()

    def quit1error():
        showerror('Error','Nedovoljno sredstava na računu\nPotrebno je izvršiti uplatu na račun \nCijena jedne srećke iznosi 5kn.')
        t2.destroy()
        global running_srecka
        running_srecka=not(running_srecka)
        main()

    #funkcija za izlaz iz programa "Higer-Lower"
    def quit2():
        t3.destroy()
        global running_high_low
        running_high_low=not(running_high_low)
        main()

    def quit2error():
        showerror('Error','Nedovoljno sredstava na računu\nPotrebno je izvršiti uplatu na račun.\nMinimalni ulog za igru iznosi 5kn')
        t3.destroy()
        global running_high_low
        running_high_low=not(running_high_low)
        main()

    #funkcija za izlaz iz programa "Dobitna Škrinja"
    def quit3():
        t4.destroy()
        global running_dobitna_skrinja
        running_dobitna_skrinja=not(running_dobitna_skrinja)
        main()

    def quit3error():
        showerror('Error','Nedovoljno sredstava na računu\nPotrebno je izvršiti uplatu na račun \nCijena jedne igre iznosi 10kn.')
        t4.destroy()
        global running_dobitna_skrinja
        running_dobitna_skrinja=not(running_dobitna_skrinja)
        main()

    #funkcije za pokretanje drugih igrica, izlaz iz pocetnog prozora
    def srecka():
        t.destroy()
        global running_srecka
        running_srecka=not(running_srecka)
        
    def high_low():
        t.destroy()
        global running_high_low
        running_high_low=not(running_high_low)

    def skrinja():
        t.destroy()
        global running_dobitna_skrinja
        running_dobitna_skrinja=not(running_dobitna_skrinja)
    
    #funkcije za otvaranje polja u programu "Srečka"
    def nova_srecka():
        global mistery
        global STANJE
        global ulog
        global br
        br=0
        if(STANJE>ulog):
            global odigrano
            STANJE-=ulog
            odigrano=0
            Button(t2,image=mistery,command=igraj_bubamara1).place(relx=0.05,rely=0.10)
            Button(t2,image=mistery,command=igraj_bubamara2).place(relx=0.05,rely=0.30)
            Button(t2,image=mistery,command=igraj_bubamara3).place(relx=0.05,rely=0.50)
            Button(t2,image=mistery,command=igraj_bubamara4).place(relx=0.25,rely=0.10)
            Button(t2,image=mistery,command=igraj_bubamara5).place(relx=0.25,rely=0.30)
            Button(t2,image=mistery,command=igraj_bubamara6).place(relx=0.25,rely=0.50)
            Button(t2,image=mistery,command=igraj_bubamara7).place(relx=0.45,rely=0.10)
            Button(t2,image=mistery,command=igraj_bubamara8).place(relx=0.45,rely=0.30)
            Button(t2,image=mistery,command=igraj_bubamara9).place(relx=0.45,rely=0.50)
            showinfo("NOVA IGRA","Uspješno ste kupili novu srečku.\nVaše trenutno stanje iznosi:"+str(STANJE)+" kn")
        else:
            showerror("ERROR","Nedovoljno sredstava na računu")
    def igraj_bubamara1():
        global STANJE
        global dobitak
        global br
        global odigrano
        global skakavac
        global mrav
        global bubamara
        global lista
        index=random.randint(0,2)
        if(index==1):
            br+=1
        r=lista[index]
        Label(t2,image=r).place(relx=0.05,rely=0.10)
        odigrano+=1
        odigrana()
        return
    
    def igraj_bubamara2():
        global STANJE
        global br
        global dobitak
        global odigrano
        global skakavac
        global mrav
        global bubamara
        global lista
        index=random.randint(0,2)
        if(index==1):
            br+=1
        r=lista[index]
        Label(t2,image=r).place(relx=0.05,rely=0.30)
        odigrano+=1
        odigrana()
        return
    
    def igraj_bubamara3():
        global STANJE
        global dobitak
        global br
        global odigrano
        global skakavac
        global mrav
        global bubamara
        global lista
        index=random.randint(0,2)
        if(index==1):
            br+=1
        r=lista[index]
        Label(t2,image=r).place(relx=0.05,rely=0.50)
        odigrano+=1
        odigrana()
        return
    
    def igraj_bubamara4():
        global STANJE
        global dobitak
        global br
        global odigrano
        global skakavac
        global mrav
        global bubamara
        global lista
        index=random.randint(0,2)
        if(index==1):
            br+=1
        r=lista[index]
        Label(t2,image=r).place(relx=0.25,rely=0.10)
        odigrano+=1
        odigrana()
        return
    
    def igraj_bubamara5():
        global STANJE
        global dobitak
        global br
        global odigrano
        global skakavac
        global mrav
        global bubamara
        global lista
        index=random.randint(0,2)
        if(index==1):
            br+=1
        r=lista[index]
        Label(t2,image=r).place(relx=0.25,rely=0.30)
        odigrano+=1
        odigrana()
        return
    
    def igraj_bubamara6():
        global STANJE
        global dobitak
        global br
        global odigrano
        global skakavac
        global mrav
        global bubamara
        global lista
        index=random.randint(0,2)
        if(index==1):
            br+=1
        r=lista[index]
        Label(t2,image=r).place(relx=0.25,rely=0.50)
        odigrano+=1
        odigrana()
        return
    
    def igraj_bubamara7():
        global STANJE
        global dobitak
        global br
        global odigrano
        global skakavac
        global mrav
        global bubamara
        global lista
        index=random.randint(0,2)
        if(index==1):
            br+=1
        r=lista[index]
        Label(t2,image=r).place(relx=0.45,rely=0.10)
        odigrano+=1
        odigrana()
        return
    
    def igraj_bubamara8():
        global STANJE
        global br
        global odigrano
        global skakavac
        global mrav
        global bubamara
        global lista
        index=random.randint(0,2)
        if(index==1):
            br+=1
        r=lista[index]
        Label(t2,image=r).place(relx=0.45,rely=0.30)
        odigrano+=1
        odigrana()
        return
    
    def igraj_bubamara9():
        global STANJE
        global dobitak
        global br
        global odigrano
        global skakavac
        global mrav
        global bubamara
        global lista
        index=random.randint(0,2)
        if(index==1):
            br+=1
        r=lista[index]
        Label(t2,image=r).place(relx=0.45,rely=0.50)
        odigrano+=1
        odigrana()
        return
    
    def odigrana():
        global STANJE
        global dobitak
        global odigrano
        global br
        if((odigrano==9)and(br>2)):
            STANJE+=5 * (br-2) * pow(2,br-2)
            dobitak=5 * (br-2) * pow(2,br-2)
            showinfo("Dobitna srečka","Osvojili ste: "+str(dobitak)+" kn "+"sa "+str(br)+" bubamare")
    
    #fukcija za ispis pravila
    def pravila_bubamara():
        text="Cijena jedne srećke iznosi 5kn \n\nNakon što igrač otvori sva polja,računalo izračunava dobitak i izbacuje podatke.\n\nTime se srečka smatra iskroštenom te je potrebno izaći pritiskom na tipku EXIT, ukoliko igrač pritisne X u gornjem desnom kutu automatski se kupuje nova srečka ukoliko ima dovoljno sredstava.\n\nIgraču se omogučuje prikaz stanja i dobitka pritiskom na tipku stanje, također igrač može sakriti te vrijednosti ponovnim klikom na tipku stanja.\n\nDobitak ovisi o broju bubamara koje igrač otkrije, potrebno je minimalno 3 bubamare za dobitak.\n Za 3 bubamare igrač osvaja 10kn\n Za 4 bubamare igrač osvaja 40kn\n Za 5 bubamara osvaja 120kn\n Za 6 bubamara igrač osvaja 320kn \n Za 7 bubamara igrač osvaja 800kn\n\nUkoliko igrač izađe iz prozora prije nego otvori sva polja srećka se smatra nedobitnom"
        showinfo("PRAVILA IGRE",text)
        return
    def pravila_high_lo():
        text="Dobitak iznosi x2 ulog, ukoliko kocka bude jednaka prvoj kocki korisniku se vraća ulog\n\nIgrač može mijenjati ulog u donjem kutu pritiskom na +/-, vrijednost uloga mijenja se za 5 kn\n\nIgrač može promjeniti vrijednost uloga najviše na vrijednost stanja.\n\nU slučaju da je ulog ostane veći od vrijednosti stanja, izbacuje se error sa porukom.\n\nNakon što igrač pritisne IGRAJ željeni ulog se uplaćuje i otvara se prva kocka s lijeve strane,u to vrijeme nije moguće mjenjati ulog skroz dok igrač ne završi do kraja trenutnu igru, tj. odabere (veće/manje) za drugu kocku  ."
        showinfo("PRAVILA IGRE",text)
        return
    def pravila_skrinja():
        text='Cijene jedne igre iznosi 10kn. \n\nKorisnik igru započinje pritiskom na tipku IGRAJ, nakon čega se korisniku s računa skida cijene jedne igre te korisnik otvara željenu kutiju.\n\nIgrač može otvori zaključanu,praznu ili dobitnu kutiji, nakon svakog otvaranja izbacuje se obavijest. \n\nMaksimalni dobitak iznosi: 500 kn.\nMinimalni dobitak iznosi: 10kn.\nRačunalo samo određuje dobitak koji igrač osvaja.  '
        showinfo("PRAVILA IGRE",text)
    def pravila():
        text="Uplata se obavlja u gornjem lijevom rubu unosom željenog iznosa u žuto polje i potvrdom na gumb UPLATI,nakon čega korisnik dobiva potvrdu o uplati.\n\nIsplata se izvšava prilikom pritiska na gumb ISPLATA, isplačuje se ukupno stanje na računu,nakon čega korisnik dobiva potvrdu o obavljenoj isplati.\n\nUplate i isplate se obavljaju isključivo u početnom prozoru na koji se je moguće vraćati nakon ulaska u igre.\n\nKorisnik u igre ulazi pritiskom za željeni gumb(sliku) ispod imena svake igre.\n\nPrikaz stanja i posljednje uplate ispisano je u donjem kutu prozora.\n\nKorisniku nije omogućen ulaz o igre ukoliko na stanju nema dovoljno sredstava za minimalni iznos za naknadu igre."
        showinfo("PRAVILA IGRE",text)
        return

    #funckije za higher-lower gumbove
    def igraj_high():
        global lista_kocki
        global prva_kocka
        global STANJE
        global ulog
        global played
        played=not(played)
        druga_kocka=random.randint(0,5)
        slika=lista_kocki[druga_kocka]
        Label(t3,image=slika).place(relx=0.22,rely=0.45)
        if (druga_kocka>prva_kocka):
            dobitak=ulog*2
            STANJE+=dobitak
            showinfo("Dobitak","Osvajate: "+str(dobitak)+'kn')
            Label(t3,text='Stanje '+str(STANJE)+' kn',bg='red',fg='black',font=('Arial',20)).place(relx=0.025,rely=0.01)
        if (druga_kocka==prva_kocka):
            STANJE+=ulog
            showinfo("Dobitak","Osvajate: "+str(ulog)+" kn")
            Label(t3,text='Stanje '+str(STANJE)+' kn',bg='red',fg='black',font=('Arial',20)).place(relx=0.025,rely=0.01)
        return
    
    def igraj_low():
        global lista_kocki
        global prva_kocka
        global STANJE
        global ulog
        global played
        played=not(played)
        druga_kocka=random.randint(0,5)
        slika=lista_kocki[druga_kocka]
        Label(t3,image=slika).place(relx=0.22,rely=0.45)
        if (druga_kocka<prva_kocka):
            dobitak=ulog*2
            STANJE+=dobitak
            showinfo("Dobitak","Osvajate: "+str(dobitak)+'kn')
            Label(t3,text='Stanje '+str(STANJE)+' kn',bg='red',fg='black',font=('Arial',20)).place(relx=0.025,rely=0.01)
        if (druga_kocka==prva_kocka):
            STANJE+=ulog
            showinfo("Dobitak","Osvajate: "+str(ulog)+" kn")
            Label(t3,text='Stanje '+str(STANJE)+' kn',bg='red',fg='black',font=('Arial',20)).place(relx=0.025,rely=0.01)
        return
    
    def igraj_hl():
        global STANJE
        global kocka
        global lista_kocki
        global prva_kocka
        global ulog
        global played
        played=True
        if (STANJE>=ulog):
            Label(t3,image=kocka).place(relx=0.22,rely=0.45)
            Label(t3,image=kocka).place(relx=0.62,rely=0.45)
            STANJE-=ulog
            Label(t3,text='                           ',bg='red',fg='black',font=('Arial',20)).place(relx=0.025,rely=0.01)
            Label(t3,text='Stanje '+str(STANJE)+' kn',bg='red',fg='black',font=('Arial',20)).place(relx=0.025,rely=0.01)
            prva_kocka=random.randint(0,5)
            slika=lista_kocki[prva_kocka]
            Label(t3,image=slika).place(relx=0.62,rely=0.45)
        else:
            showerror("ERROR","Ulog veći od stanja, smanjite ulog")
        return
    
    #funkcije za mjenjanje ulog +/-
    def ulog_p():
        global STANJE
        global ulog
        global played
        if(not(played)):
            if((ulog+5)<=STANJE):
                ulog+=5
                Label(t3,text='                     ',fg='red',bg='grey',font=('Monospace',20)).place(relx=0.4,rely=0.87)
                Label(t3,text='ULOG: '+str(ulog)+'kn',fg='red',bg='grey',font=('Monospace',20)).place(relx=0.4,rely=0.87)
            else:
                ulog=5
                Label(t3,text='                     ',fg='red',bg='grey',font=('Monospace',20)).place(relx=0.4,rely=0.87)
                Label(t3,text='ULOG: '+str(ulog)+'kn',fg='red',bg='grey',font=('Monospace',20)).place(relx=0.4,rely=0.87)
        return
    
    def ulog_m():
        global STANJE
        global ulog
        global played
        if(not(played)):
            if((ulog-5)>=5):
                ulog-=5
                Label(t3,text='                     ',fg='red',bg='grey',font=('Monospace',20)).place(relx=0.4,rely=0.87)
                Label(t3,text='ULOG: '+str(ulog)+'kn',fg='red',bg='grey',font=('Monospace',20)).place(relx=0.4,rely=0.87)
            else:
                ulog=STANJE
                Label(t3,text='                     ',fg='red',bg='grey',font=('Monospace',20)).place(relx=0.4,rely=0.87)
                Label(t3,text='ULOG: '+str(ulog)+'kn',fg='red',bg='grey',font=('Monospace',20)).place(relx=0.4,rely=0.87)
        return

    #funkcije za igru dobitna skrinja
    def igraj_skrinja():
        global odigrana_skrinja
        global STANJE
        global ulog
        global pocetna
        
        ulog=10
        if (STANJE>=ulog):
            odigrana_skrinja=True
            STANJE-=ulog
            Button(t4,image=pocetna,command=igraj_skrinju1).place(relx=0.1,rely=0.55)
            Button(t4,image=pocetna,command=igraj_skrinju2).place(relx=0.3,rely=0.55)
            Button(t4,image=pocetna,command=igraj_skrinju3).place(relx=0.5,rely=0.55)
            Button(t4,image=pocetna,command=igraj_skrinju4).place(relx=0.7,rely=0.55)
            showinfo("IGRAJ","Odaberite škrinju\n"+"Trenutno stanje iznosi:" +str(STANJE)+" kn")
        else:
            showerror("ERROR","Nedovoljno sredstava")
        Label(t4,text="                                   ",bg='black').place(relx=0.1,rely=0.9)
        Label(t4,text="STANJE: "+str(STANJE)+" kn",fg='red',bg='black').place(relx=0.1,rely=0.9)
        return
    
    def  igraj_skrinju1():
        global odigrana_skrinja
        global STANJE
        global ulog 
        global dobitak
        global lista_skrinja
        if(odigrana_skrinja):
            r=random.randint(0,2)
            izabrana=lista_skrinja[r]
            Label(t4,image=izabrana).place(relx=0.1,rely=0.55)
            if(r==0):
                dobitak=ulog*random.randint(1,50)
                STANJE+=dobitak
                showinfo("Dobitna škrinja","Čestitamo otvorili ste dobitnu škrinju\n"+"Vaš dobitak iznosi:"+str(dobitak)+" kn\n"+"Trenutno stanje iznosi:"+str(STANJE)+" kn")
            elif(r==1):
                showinfo("Prazna škrinja","Nažalost otvorili ste praznu škrinju\n"+"Trenutno stanje iznosi:"+str(STANJE)+" kn")
            elif(r==2):
                showinfo("Zaključana škrinja","Nažalost otvorili ste zaključanu škrinju\n"+"Trenutno stanje iznosi:"+str(STANJE)+" kn")
            odigrana_skrinja=False
        return
    def  igraj_skrinju2():
        global odigrana_skrinja
        global STANJE
        global ulog 
        global dobitak
        global lista_skrinja
        if(odigrana_skrinja):
            r=random.randint(0,2)
            izabrana=lista_skrinja[r]
            Label(t4,image=izabrana).place(relx=0.3,rely=0.55)
            if(r==0):
                dobitak=ulog*random.randint(1,50)
                STANJE+=dobitak
                showinfo("Dobitna škrinja","Čestitamo otvorili ste dobitnu škrinju\n"+"Vaš dobitak iznosi:"+str(dobitak)+" kn\n"+"Trenutno stanje iznosi:"+str(STANJE)+" kn")
            elif(r==1):
                showinfo("Prazna škrinja","Nažalost otvorili ste praznu škrinju\n"+"Trenutno stanje iznosi:"+str(STANJE)+" kn")
            elif(r==2):
                showinfo("Zaključana škrinja","Nažalost otvorili ste zaključanu škrinju\n"+"Trenutno stanje iznosi:"+str(STANJE)+" kn")
            odigrana_skrinja=False
        return
    def  igraj_skrinju3():
        global odigrana_skrinja
        global STANJE
        global ulog 
        global dobitak
        global lista_skrinja
        if(odigrana_skrinja):
            r=random.randint(0,2)
            izabrana=lista_skrinja[r]
            Label(t4,image=izabrana).place(relx=0.5,rely=0.55)
            if(r==0):
                dobitak=ulog*random.randint(1,50)
                STANJE+=dobitak
                showinfo("Dobitna škrinja","Čestitamo otvorili ste dobitnu škrinju\n"+"Vaš dobitak iznosi:"+str(dobitak)+" kn\n"+"Trenutno stanje iznosi:"+str(STANJE)+" kn")
            elif(r==1):
                showinfo("Prazna škrinja","Nažalost otvorili ste praznu škrinju\n"+"Trenutno stanje iznosi:"+str(STANJE)+" kn")
            elif(r==2):
                showinfo("Zaključana škrinja","Nažalost otvorili ste zaključanu škrinju\n"+"Trenutno stanje iznosi:"+str(STANJE)+" kn")
            odigrana_skrinja=False
        return
    def  igraj_skrinju4():
        global odigrana_skrinja
        global STANJE
        global ulog 
        global dobitak
        global lista_skrinja
        if(odigrana_skrinja):
            r=random.randint(0,2)
            izabrana=lista_skrinja[r]
            Label(t4,image=izabrana).place(relx=0.7,rely=0.55)
            if(r==0):
                dobitak=ulog*random.randint(1,50)
                STANJE+=dobitak
                showinfo("Dobitna škrinja","Čestitamo otvorili ste dobitnu škrinju\n"+"Vaš dobitak iznosi:"+str(dobitak)+" kn\n"+"Trenutno stanje iznosi:"+str(STANJE)+" kn")
            elif(r==1):
                showinfo("Prazna škrinja","Nažalost otvorili ste praznu škrinju\n"+"Trenutno stanje iznosi:"+str(STANJE)+" kn")
            elif(r==2):
                showinfo("Zaključana škrinja","Nažalost otvorili ste zaključanu škrinju\n"+"Trenutno stanje iznosi:"+str(STANJE)+" kn")
                
            odigrana_skrinja=False
        return
            
        
    #početak maina 
    running_srecka=False
    running_high_low=False
    running_dobitna_skrinja=False
    
    t=Tk()
    t.title(' Lucky   Games ')
    t.geometry('800x800')
    
    #pozadina
    bg_ulazni = PhotoImage(file="icon.png")
    Label(t,image=bg_ulazni).place(x=0,y=0,relwidth=1,relheight=1)
    start()
    
    #unos
    uplata=Entry(t,bg='yellow',font=('DISPLAY',15),width=10)
    Label(t,text='Unesi unos uplate: ',font=('Arial',15)).place(relx=(1/80),rely=(1/80))
    uplata.place(x=200,y=10)

    Button(t,text="UPLATI",fg='yellow',font=('Arial',15,'bold'),bg='black',command=uplati).place(x=320,y=5)
    Button(t,text="ISPLATA",fg='orange',font=('Arial',15,'bold'),bg='black',command=isplati).place(x=420,y=5)
    Button(t,text="PRAVILA",fg='red',font=('Arial',15,'bold'),bg='black',command=pravila).place(x=650,y=5)
    
    #dugme za ulaz u igru "Srečka"
    bg_srecka_button=PhotoImage(file="srecka_button.png")
    Button(t,image=bg_srecka_button,command=srecka).place(relx=0.2,rely=0.25)

    #dugme za ulaz u igru "High-Low"
    bg_high_low_button=PhotoImage(file="high_low_button.png")
    Button(t,image=bg_high_low_button,command=high_low).place(relx=0.2,rely=0.50)

    #dugme za ulaz u igru "Dobitna Škrinja"
    bg_dobitna_skrinja=PhotoImage(file="dobitna_skrinja_button.png")
    Button(t,image=bg_dobitna_skrinja,command=skrinja).place(relx=0.55,rely=0.25)


    #naslovi igara
    Label(t,text='Pronađi dobitnu škrinju',bg='black',fg='pink',font=('Arial',15)).place(relx=0.51,rely=0.21)
    Label(t,text='Dobitna bubamara',bg='black',fg='red',font=('Arial',15)).place(relx=0.18,rely=0.21)
    Label(t,text='Higer-Lower',bg='black',fg='white',font=('Arial',15)).place(relx=0.21,rely=0.46)

    t.mainloop()

    #Igra Dobitna škrinja
    while(running_dobitna_skrinja):
        global dobitak
        global odigrana_skrinja
        odigrana_skrinja=False
        
        global dobitna
        global prazna
        global pocetna
        global lista_skrinja

        t4=Tk()
        t4.title(' Lucky   Games Dobitna Škrinja')
        t4.geometry('600x600')
        pozadina=PhotoImage(file="bg_skrinja.png")
        Label(t4,image=pozadina).place(x=0,y=0,relwidth=1,relheight=1)
        Label(t4,text="                                   ",bg='black').place(relx=0.1,rely=0.9)
        Label(t4,text="STANJE: "+str(STANJE)+" kn",fg='red',bg='black').place(relx=0.1,rely=0.9)
        
        #slike skrinja
        dobitna=PhotoImage(file="dobitnaskrinja.png")
        prazna=PhotoImage(file="praznaskrinja.png")
        pocetna=PhotoImage(file="zatvorenaskrinja.png")
        lista_skrinja=[dobitna,prazna,pocetna]

        #dugme za skrinje
        Button(t4,text='IGRAJ',font=('Arial',20),command=igraj_skrinja).place(relx=0.05,rely=0.05)
        Button(t4,text='PRAVILA',font=('Arial',10),command=pravila_skrinja).place(relx=0.85,rely=0.92)
        Label(t4,image=pocetna).place(relx=0.1,rely=0.55)
        Label(t4,image=dobitna).place(relx=0.3,rely=0.55)
        Label(t4,image=prazna).place(relx=0.5,rely=0.55)
        Label(t4,image=pocetna).place(relx=0.7,rely=0.55)

        #izlaz ukoliko nema dovoljno sredstava za igru
        if(STANJE<ulog):
            quit3error()
        #dugme za izlaz
        Button(t4,text="EXIT",command=quit3,fg='red',bg='black',font=('Monospace',15)).place(relx=0.85,rely=0.05)
        t4.mainloop()
    
    #Igra Higher-Lower
    while(running_high_low):
        global lista_kocki
        global dobitak
        global played
        played=False
        
        global kocka
        global kocka1
        global kocka2
        global kocka3
        global kocka4
        global kocka5
        global kocka6
        
        t3=Tk()
        t3.title(' Lucky   Games Higher-Lower')
        t3.geometry('500x500')

        #pozadina
        bg_high_low = PhotoImage(file="high_low.png")
        Label(t3,image=bg_high_low).place(x=0,y=0,relwidth=1,relheight=1)

        #izlaz ukoliko nema dovoljno sredstava za igru
        if(STANJE<ulog):
            quit2error()

        #slike
        kocka=PhotoImage(file="kocka.png")
        kocka1=PhotoImage(file="kocka1.png")
        kocka2=PhotoImage(file="kocka2.png")
        kocka3=PhotoImage(file="kocka3.png")
        kocka4=PhotoImage(file="kocka4.png")
        kocka5=PhotoImage(file="kocka5.png")
        kocka6=PhotoImage(file="kocka6.png")
        higher=PhotoImage(file="high.png")
        lower=PhotoImage(file="low.png")
        lista_kocki=[kocka1,kocka2,kocka3,kocka4,kocka5,kocka6]

        #gumbovi
        Button(t3,image=higher,command=igraj_high).place(relx=0.20,rely=0.70)
        Button(t3,image=lower,command=igraj_low).place(relx=0.60,rely=0.70)
        Button(t3,text='Igraj',fg='lightblue',font=('Arial',30),bg='Black',command=igraj_hl).place(relx=0.05,rely=0.10)
        Label(t3,text='Stanje '+str(STANJE)+' kn',bg='red',fg='black',font=('Arial',20)).place(relx=0.025,rely=0.01)
        Button(t3,text="+",command=ulog_p,fg='orange',bg='grey',font=('Monospace',20)).place(relx=0.8,rely=0.85)
        Button(t3,text="-",command=ulog_m,fg='yellow',bg='grey',font=('Monospace',20)).place(relx=0.9,rely=0.85)
        Label(t3,text='ULOG: '+str(ulog)+'kn',fg='red',bg='grey',font=('Monospace',20)).place(relx=0.4,rely=0.87)
        Button(t3,text="EXIT",command=quit2,fg='red',bg='black',font=('Monospace',15)).place(relx=0.8,rely=0.01)
        
        Button(t3,text="PRAVILA",command=pravila_high_lo,fg='red',bg='black',font=('Monospace',15)).place(relx=0.05,rely=0.9)
        t3.mainloop()
        
    #Igra srećka(Bubamara)
    while(running_srecka):
        global br
        global dobitak
        global odigrano
        global index
        global skakavac
        global mrav
        global brojac
        global bubamara
        global lista
        global mistery
        odigrano=0
        br=0
        brojac=0
        index=0
        dobitak=0
        x=0
        y=0
        t2=Tk()
        t2.title(' Lucky   Games Srečka')
        t2.geometry('800x800')

        #pozadina
        bg_srecka = PhotoImage(file="srecka.png")
        Label(t2,image=bg_srecka).place(x=0,y=0,relwidth=1,relheight=1)

        #izlaz ukoliko nema dovoljno sredstava za igru
        if(STANJE<ulog):
            quit1error()
        STANJE-=5

        #slike
        skakavac=PhotoImage(file="skakavac.png")
        bubamara=PhotoImage(file="bubamara.png")
        mrav=PhotoImage(file="mrav.png")
        mistery=PhotoImage(file='mistery.png')


        #gumbovi
        Button(t2,text="PRAVILA",fg='red',bg='black',command=pravila_bubamara).place(relx=0.75,rely=0.15)
        Button(t2,text="NOVA SREČKA",fg='lightblue',bg='black',command=nova_srecka).place(relx=0.73,rely=0.2)
        Button(t2,image=mistery,command=igraj_bubamara1).place(relx=0.05,rely=0.10)
        Button(t2,image=mistery,command=igraj_bubamara2).place(relx=0.05,rely=0.30)
        Button(t2,image=mistery,command=igraj_bubamara3).place(relx=0.05,rely=0.50)
        Button(t2,image=mistery,command=igraj_bubamara4).place(relx=0.25,rely=0.10)
        Button(t2,image=mistery,command=igraj_bubamara5).place(relx=0.25,rely=0.30)
        Button(t2,image=mistery,command=igraj_bubamara6).place(relx=0.25,rely=0.50)
        Button(t2,image=mistery,command=igraj_bubamara7).place(relx=0.45,rely=0.10)
        Button(t2,image=mistery,command=igraj_bubamara8).place(relx=0.45,rely=0.30)
        Button(t2,image=mistery,command=igraj_bubamara9).place(relx=0.45,rely=0.50)
        Button(t2,text='stanje',command=stanje).place(relx=0.05,rely=0.75)
        Button(t2,text='EXIT',font=('Arial',25),bg='RED',command=quit1).place(relx=0.85,rely=0.9)
        lista=[skakavac,bubamara,mrav]

        t2.mainloop()

main()

