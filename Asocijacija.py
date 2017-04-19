from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
import tkinter as tk
from xml.dom import minidom      # minidom je deo biblioteke XML za parsiranje

#Lista Asocijacija
lista=["Prva.xml","Druga.xml","Treca.xml","Cetvrta.xml","Peta.xml",
       "Sesta.xml","Sedma.xml","Osma.xml","Deveta.xml","Deseta.xml",
       "Jedanesta.xml","Dvanesta.xml","Trinesta.xml","Cetrnesta.xml","Petnesta.xml",
       "Sesnesta.xml","Sedamnesta.xml","Osamnesta.xml","Devetnesta.xml","Dvadeseta.xml",
       "Dvadesetprva.xml","Dvadesetdruga.xml","Dvadesettreca.xml" ]

izbor=random.choice(lista) #Odabir jedne od Asocijacija iz liste

e = minidom.parse("reci/"+izbor)  # Povezvanje parsera sa XML fajlom
podaciA=e.getElementsByTagName("poljeA")   #Dohvatanje elemenata iz XML-a
podaciB=e.getElementsByTagName("poljeB")
podaciC=e.getElementsByTagName("poljeC")
podaciD=e.getElementsByTagName("poljeD")

BUTT_FONT = ('Consolas', 14, 'bold')
ENT_FONT = ('Consolas', 17, 'bold')
RJ_FONT = ('Consolas', 25, 'bold')
root = Tk()
root.configure(background='#002240')


root.geometry('800x600')
root.title('Igra Asocijacije')
rjesenje = StringVar(value='*rjesenje*')
#VARIJABLE A             #kada se program pokrene varijable se setuju na imena polja
kolonaA = StringVar()
kolonaA.set('***A***')
A1 = StringVar(value='A1')
A2 = StringVar(value='A2')
A3 = StringVar(value='A3')
A4 = StringVar(value='A4')
#VARIJABLE B
kolonaB = StringVar(value='***B***')
B1 = StringVar(value='B1')
B2 = StringVar(value='B2')
B3 = StringVar(value='B3')
B4 = StringVar(value='B4')
#VARIJABLE C
kolonaC = StringVar(value='***C***')
C1 = StringVar(value='C1')
C2 = StringVar(value='C2')
C3 = StringVar(value='C3')
C4 = StringVar(value='C4')

#VARIJABLE D
kolonaD = StringVar(value='***D***')
D1 = StringVar(value='D1')
D2 = StringVar(value='D2')
D3 = StringVar(value='D3')
D4 = StringVar(value='D4')




def state(dugme):   #Funkcija se pokreće kada se klikne na dugme onda se dugme setuje na određenu vrednost iz fajla Asoc.xml
       if dugme == dugmeA1:
              dugme.config(state = DISABLED)
              A1.set(podaciA[0].attributes["vrednostA"].value)
       elif dugme == dugmeA2:
              dugme.config(state = DISABLED)
              A2.set(podaciA[1].attributes["vrednostA"].value)
       elif dugme == dugmeA3:
              dugme.config(state = DISABLED)
              A3.set(podaciA[2].attributes["vrednostA"].value)
       elif dugme == dugmeA4:
              dugme.config(state = DISABLED)
              A4.set(podaciA[3].attributes["vrednostA"].value)
       elif dugme == dugmeB1:
              dugme.config(state = DISABLED)
              B1.set(podaciB[0].attributes["vrednostB"].value)
       elif dugme == dugmeB2:
              dugme.config(state = DISABLED)
              B2.set(podaciB[1].attributes["vrednostB"].value)
       elif dugme == dugmeB3:
              dugme.config(state = DISABLED)
              B3.set(podaciB[2].attributes["vrednostB"].value)
       elif dugme == dugmeB4:
              dugme.config(state = DISABLED)
              B4.set(podaciB[3].attributes["vrednostB"].value)
       elif dugme == dugmeC1:
              dugme.config(state = DISABLED)
              C1.set(podaciC[0].attributes["vrednostC"].value)
       elif dugme == dugmeC2:
              dugme.config(state = DISABLED)
              C2.set(podaciC[1].attributes["vrednostC"].value)
       elif dugme == dugmeC3:
              dugme.config(state = DISABLED)
              C3.set(podaciC[2].attributes["vrednostC"].value)
       elif dugme == dugmeC4:
              dugme.config(state = DISABLED)
              C4.set(podaciC[3].attributes["vrednostC"].value)
       elif dugme == dugmeD1:
              dugme.config(state = DISABLED)
              D1.set(podaciD[0].attributes["vrednostD"].value)
       elif dugme == dugmeD2:
              dugme.config(state = DISABLED)
              D2.set(podaciD[1].attributes["vrednostD"].value)
       elif dugme == dugmeD3:
              dugme.config(state = DISABLED)
              D3.set(podaciD[2].attributes["vrednostD"].value)
       elif dugme == dugmeD4:
              dugme.config(state = DISABLED)
              D4.set(podaciD[3].attributes["vrednostD"].value)

def brisiEntry(event):
       event.widget.delete(0, 'end') #funkcija brise bilo koji entry koji joj proslijedimo
       return None
def setEntry(event):
       if root.focus_get()!= event.widget: #funkcija koja setuje entryije na pocetne vrijednosti kada kliknete
              kolonaA.set('***A***')             #bilo gdje van entryja
              kolonaB.set('***B***')
              kolonaC.set('***C***')
              kolonaD.set('***D***')
              rjesenje.set('*rjesenje*')
              root.focus_set()

#kolone A

dugmeA1 = tk.Button(root, textvariable = A1, command = lambda: state(dugmeA1),
                  bg='#02A2F2', fg='white', width = 16, font = BUTT_FONT, state = NORMAL) #ovo je postavljanje buttona i entryija
dugmeA1.grid(column=0, row=0, sticky='w')                                                  #klasicni fizicki posao :) 

dugmeA2 = tk.Button(root, textvariable = A2, command = lambda: state(dugmeA2),
                  bg='#02A2F2', fg='white', width = 16, font = BUTT_FONT, state = NORMAL)
dugmeA2.grid(column=0, row=2, sticky='w')
dugmeA2.place(x=40, y=50)
dugmeA3 = tk.Button(root, textvariable = A3, command = lambda: state(dugmeA3),
                  bg='#02A2F2', fg='white', width = 16, font = BUTT_FONT, state = NORMAL)
dugmeA3.grid(column=0, row=3, sticky='w')
dugmeA3.place(x=80, y=100)
dugmeA4 = tk.Button(root, textvariable = A4, command = lambda: state(dugmeA4),
                  bg='#02A2F2', fg='white', width = 16, font = BUTT_FONT, state = NORMAL)
dugmeA4.grid(column=0, row=4, sticky='w')
dugmeA4.place(x=120, y=150)
kolonaAent = tk.Entry(root, textvariable = kolonaA, fg='#02A2F2', justify='center', font = ENT_FONT, width=18)
kolonaAent.grid(column=0,row=5)
kolonaAent.place(x=120, y=195)
kolonaAent.bind("<Button-1>", brisiEntry)

#kolone B
dugmeB1 = tk.Button(root, textvariable = B1, command = lambda: state(dugmeB1),
                  bg='#02A2F2', fg='white', width = 16, font = BUTT_FONT, state = NORMAL)
dugmeB1.grid(column=1, row=0, sticky='w')
dugmeB1.place(x=630, y=0)
dugmeB2 = tk.Button(root, textvariable = B2, command = lambda: state(dugmeB2),
                  bg='#02A2F2', fg='white', width = 16, font = BUTT_FONT, state = NORMAL)
dugmeB2.grid(column=1, row=2, sticky='w')
dugmeB2.place(x=590, y=50)
dugmeB3 = tk.Button(root, textvariable = B3, command = lambda: state(dugmeB3),
                  bg='#02A2F2', fg='white', width = 16, font = BUTT_FONT, state = NORMAL)
dugmeB3.grid(column=1, row=3, sticky='w')
dugmeB3.place(x=550, y=100)
dugmeB4 = tk.Button(root, textvariable = B4, command = lambda: state(dugmeB4),
                  bg='#02A2F2', fg='white', width = 16, font = BUTT_FONT, state = NORMAL)
dugmeB4.grid(column=1, row=4, sticky='w')
dugmeB4.place(x=510, y=150)
kolonaBent = tk.Entry(root, textvariable = kolonaB, fg='#02A2F2', justify='center', font = ENT_FONT, width=18)
kolonaBent.grid(column=1,row=5)
kolonaBent.place(x=440, y=195)
kolonaBent.bind("<Button-1>", brisiEntry)

#RJSENJE
rjesenjeEnt = tk.Entry(root, textvariable=rjesenje, fg='#02A2F2', justify='center', width = 31, font = RJ_FONT)
rjesenjeEnt.grid(column=0, row=6, columnspan=1)
rjesenjeEnt.place(x=120, y=280)
rjesenjeEnt.bind("<Button-1>", brisiEntry)

#kolone C

dugmeC1 = tk.Button(root, textvariable = C1, command = lambda: state(dugmeC1),
                  bg='#02A2F2', fg='white', width = 16, font = BUTT_FONT, state = NORMAL)
dugmeC1.grid(column=0, row=7, sticky='w')
dugmeC1.place(x=120, y=412)
dugmeC2 = tk.Button(root, textvariable = C2, command = lambda: state(dugmeC2),
                  bg='#02A2F2', fg='white', width = 16, font = BUTT_FONT, state = NORMAL)
dugmeC2.grid(column=0, row=8, sticky='w')
dugmeC2.place(x=80, y=462)
dugmeC3 = tk.Button(root, textvariable = C3, command = lambda: state(dugmeC3),
                  bg='#02A2F2', fg='white', width = 16, font = BUTT_FONT, state = NORMAL)
dugmeC3.grid(column=0, row=9, sticky='w')
dugmeC3.place(x=40, y=512)
dugmeC4 = tk.Button(root, textvariable = C4, command = lambda: state(dugmeC4),
                  bg='#02A2F2', fg='white', width = 16, font = BUTT_FONT, state = NORMAL)
dugmeC4.grid(column=0, row=10, sticky='w')
dugmeC4.place(x=0, y=562)
kolonaCent = tk.Entry(root, textvariable = kolonaC, fg='#02A2F2', justify='center', font = ENT_FONT, width=18)
kolonaCent.grid(column=0,row=5)
kolonaCent.place(x=120, y=367)
kolonaCent.bind("<Button-1>", brisiEntry)


#kolone D

dugmeD1 = tk.Button(root, textvariable = D1, command = lambda: state(dugmeD1),
                  bg='#02A2F2', fg='white', width = 16, font = BUTT_FONT, state = NORMAL)
dugmeD1.grid(column=1, row=7, sticky='w')
dugmeD1.place(x=510, y=412)
dugmeD2 = tk.Button(root, textvariable = D2, command = lambda: state(dugmeD2),
                  bg='#02A2F2', fg='white', width = 16, font = BUTT_FONT, state = NORMAL)
dugmeD2.grid(column=1, row=8, sticky='w')
dugmeD2.place(x=550, y=462)
dugmeD3 = tk.Button(root, textvariable = D3, command = lambda: state(dugmeD3),
                  bg='#02A2F2', fg='white', width = 16, font = BUTT_FONT, state = NORMAL)
dugmeD3.grid(column=1, row=9, sticky='w')
dugmeD3.place(x=590, y=512)
dugmeD4 = tk.Button(root, textvariable = D4, command = lambda: state(dugmeD4),
                  bg='#02A2F2', fg='white', width = 16, font = BUTT_FONT, state = NORMAL)
dugmeD4.grid(column=1, row=10, sticky='w')
dugmeD4.place(x=630, y=562)
kolonaDent = tk.Entry(root, textvariable = kolonaD, fg='#02A2F2', justify='center', font = ENT_FONT, width=18)
kolonaDent.grid(column=1,row=5)
kolonaDent.place(x=440, y=367)
kolonaDent.bind("<Button-1>", brisiEntry)
def pop(*args):
    tk.messagebox.showinfo("PROČITAJ", "Prilikom upsivanja rešenja:\nPišite malim latiničnim slovima.\nKoristite slova sa kvačicama(š,đ,č,ć,ž).\nNeka rešenja se sastoje iz dve reči.")

up = tk.Button(root, text = "Uputsvto", command= pop,bg='#02A2F2', fg='yellow', justify="center", width = 10, font = BUTT_FONT, state = NORMAL)
up.grid(column=1, row=11, sticky='w')
up.place(x=345, y=450)



root.bind("<Button-1>", setEntry)
root.mainloop()
