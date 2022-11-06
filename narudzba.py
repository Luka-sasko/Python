from tkinter import*
from tkinter.messagebox import *
import tkinter as tk
global entry1
global entry2
global entry3
global entry4
global entry5
def main():
    t=tk.Tk()
    t.geometry('300x300')
    t.config(bg='lightblue')
    izbornik=Menu(t)

    #PIZZA
    def naruci_pizzu():
        showinfo("Narudžba","Vaša pizza će biti dostavaljena u roku od 20 minuta")
        t.destroy()
        main()
        return

    def potvrda():
        izaberi_sastojke()
        showinfo("Nastavite","Nastavite na odabir sastojaka")
        return

    def izaberi_pizzu():
        a=Label(t,text='Koju pizzu želite:')
        a.place(relx=0.3,rely=0.1)
        b=Button(t,text='   OK    ',command=potvrda)
        b.place(relx=0.4,rely=0.8)
        listbox = tk.Listbox(t)
        listbox.insert(1,"1. Mala")
        listbox.insert(2,"2. Velika")
        listbox.insert(3,"3. Jumbo")
        listbox.insert(4,"4. Gigant")
        listbox.place(relx=0.25,rely=0.2) 
        return

    def izaberi_sastojke():
        a=Label(t,text='Izaberite sastojke:')
        a.place(relx=0.3,rely=0.1)
        b=Button(t,text='Naruči',command=naruci_pizzu)
        b.place(relx=0.4,rely=0.8)
        listbox = tk.Listbox(t,selectmode=MULTIPLE)
        listbox.insert(1," 1. Sir")
        listbox.insert(2," 2. Šunka")
        listbox.insert(3," 3. Gljive")
        listbox.insert(4," 4. Kulen")
        listbox.insert(5," 5. Masline")
        listbox.insert(6," 6. Jaje")
        listbox.insert(7," 7. Slanina")
        listbox.insert(8," 8. Feferoni")
        listbox.insert(9," 9. Kukuruz")
        listbox.insert(10,"10. Mozzarella")
        listbox.place(relx=0.25,rely=0.2)
        return
    pizza_izbornik=Menu(izbornik)
    pizza_izbornik.add_command(label="Vrsta",command=izaberi_pizzu)
    pizza_izbornik.add_command(label="Sastojci",command=izaberi_sastojke)
    izbornik.add_cascade(label="Pizza",menu=pizza_izbornik)
    
    #ŠKOLA
    def izracunaj_prosjek():
        global entry1
        global entry2
        global entry3
        global entry4
        global entry5
        prosjek=float(entry1.get())+float(entry2.get())+float(entry3.get())+float(entry4.get())+float(entry5.get())
        prosjek=round(prosjek/5,2)
        prosjek=str(prosjek)
        ispis=Label(t,text="Prosjek ocjena je : "+prosjek,bg="lightgreen")
        ispis.place(relx=0.1,rely=0.75)
        return
    def prosjek():
        global entry1
        global entry2
        global entry3
        global entry4
        global entry5
        label=Label(t,text='Unesite prosjeke: ')
        label.place(relx=0.1,rely=0.1)
        entry1=Entry(t,width=5)
        entry1.place(relx=0.1,rely=0.2)
        entry2=Entry(t,width=5)
        entry2.place(relx=0.1,rely=0.27)
        entry3=Entry(t,width=5)
        entry3.place(relx=0.1,rely=0.34)
        entry4=Entry(t,width=5)
        entry4.place(relx=0.1,rely=0.41)
        entry5=Entry(t,width=5)
        entry5.place(relx=0.1,rely=0.48)
        button=Button(t,text='Izračunaj prosjek',command=izracunaj_prosjek)
        button.place(relx=0.1,rely=0.6)
        button=Button(t,text="Početna",command=vrati_pocetnu,fg='red')
        button.place(relx=0.1,rely=0.85)
        return

    def vrati_pocetnu():
        t.destroy()
        main()
    skola_izbornik=Menu(izbornik)
    skola_izbornik.add_command(label="Ocjene",command=prosjek)
    izbornik.add_cascade(label="Škola",menu=skola_izbornik)


    t.config(menu=izbornik)
    t.mainloop()
main()
