from tkinter import *
from tkinter import ttk
import tkinter as tk
from xml.dom import minidom    # minidom je deo biblioteke XML za parsiranje
e = minidom.parse("Asoc.xml")  # Povezvanje parsera sa Asoc.xml
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

#Nisam uspela da stavim background na Frame bez ttk.Style
ttk.Style().configure("blue.TFrame", background="#002240")

ram=ttk.Frame(root, style="blue.TFrame")
ram.grid(row=0,column=0)

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

dugmeA1 = tk.Button(ram, textvariable = A1, command = lambda: state(dugmeA1),
                  bg='#02A2F2', fg='white', width = 16, font = BUTT_FONT, state = NORMAL) #ovo je postavljanje buttona i entryija
dugmeA1.grid(column=0, row=0, padx=(0,0), pady=(0,0), sticky='w')                                                  #klasicni fizicki posao :) 
dugmeA2 = tk.Button(ram, textvariable = A2, command = lambda: state(dugmeA2),
                  bg='#02A2F2', fg='white', width = 16, font = BUTT_FONT, state = NORMAL)
dugmeA2.grid(column=0, row=1,  padx=(40,0),pady=(0,0),sticky='w')
dugmeA3 = tk.Button(ram, textvariable = A3, command = lambda: state(dugmeA3),
                  bg='#02A2F2', fg='white', width = 16, font = BUTT_FONT, state = NORMAL)
dugmeA3.grid(column=0, row=2, padx=(80,0),pady=(0,0),sticky='w')
dugmeA4 = tk.Button(ram, textvariable = A4, command = lambda: state(dugmeA4),
                  bg='#02A2F2', fg='white', width = 16, font = BUTT_FONT, state = NORMAL)
dugmeA4.grid(column=0, row=3, padx= (120,0), pady=(0,0),sticky='w')
kolonaAent = tk.Entry(ram, textvariable = kolonaA, fg='#02A2F2', justify='center', font = ENT_FONT, width=18)
kolonaAent.grid(column=0,row=4, padx=(120,0),pady=(0,0), sticky='w')

kolonaAent.bind("<Button-1>", brisiEntry)

#kolone B
dugmeB1 = tk.Button(ram, textvariable = B1, command = lambda: state(dugmeB1),
                  bg='#02A2F2', fg='white', width = 16, font = BUTT_FONT, state = NORMAL)
dugmeB1.grid(column=2, row=0,  padx=(190,0), pady=(0,0),sticky='w')
dugmeB2 = tk.Button(ram, textvariable = B2, command = lambda: state(dugmeB2),
                  bg='#02A2F2', fg='white', width = 16, font = BUTT_FONT, state = NORMAL)
dugmeB2.grid(column=2, row=1, padx=(150,0), pady=(0,0),sticky='w')
dugmeB3 = tk.Button(ram, textvariable = B3, command = lambda: state(dugmeB3),
                  bg='#02A2F2', fg='white', width = 16, font = BUTT_FONT, state = NORMAL)
dugmeB3.grid(column=2, row=2, padx=(110,0), pady=(0,0), sticky='w')
dugmeB4 = tk.Button(ram, textvariable = B4, command = lambda: state(dugmeB4),
                  bg='#02A2F2', fg='white', width = 16, font = BUTT_FONT, state = NORMAL)
dugmeB4.grid(column=2, row=3, padx=(70,0), pady=(0,0), sticky='w')
kolonaBent = tk.Entry(ram, textvariable = kolonaB, fg='#02A2F2', justify='center', font = ENT_FONT, width=18)
kolonaBent.grid(column=2,row=4, padx=(0,0), pady=(0,0),sticky='w')

kolonaBent.bind("<Button-1>", brisiEntry)

#RJSENJE
rjesenjeEnt = tk.Entry(ram, textvariable=rjesenje, fg='#02A2F2', justify='center', width = 35, font = RJ_FONT)
rjesenjeEnt.grid(column=0, row=5, padx=(2,0), pady=(20,0), ipady=(2),columnspan=3)

rjesenjeEnt.bind("<Button-1>", brisiEntry)

#kolone C

dugmeC1 = tk.Button(ram, textvariable = C1, command = lambda: state(dugmeC1),
                  bg='#02A2F2', fg='white', width = 16, font = BUTT_FONT, state = NORMAL)
dugmeC1.grid(column=0, row=7, padx=(120,0), pady=(0,0), sticky='w')
dugmeC2 = tk.Button(ram, textvariable = C2, command = lambda: state(dugmeC2),
                  bg='#02A2F2', fg='white', width = 16, font = BUTT_FONT, state = NORMAL)
dugmeC2.grid(column=0, row=8, padx=(80,0), pady=(0,0),sticky='w')
dugmeC3 = tk.Button(ram, textvariable = C3, command = lambda: state(dugmeC3),
                  bg='#02A2F2', fg='white', width = 16, font = BUTT_FONT, state = NORMAL)
dugmeC3.grid(column=0, row=9, padx=(40,0), pady=(0,0),sticky='w')
dugmeC4 = tk.Button(ram, textvariable = C4, command = lambda: state(dugmeC4),
                  bg='#02A2F2', fg='white', width = 16, font = BUTT_FONT, state = NORMAL)
dugmeC4.grid(column=0, row=10, padx=(0,0), pady=(0,0),sticky='w')
kolonaCent = tk.Entry(ram, textvariable = kolonaC, fg='#02A2F2', justify='center', font = ENT_FONT, width=18)
kolonaCent.grid(column=0,row=6,padx=(120,0), pady=(0,0),sticky='w')

kolonaCent.bind("<Button-1>", brisiEntry)


#kolone D

dugmeD1 = tk.Button(ram, textvariable = D1, command = lambda: state(dugmeD1),
                  bg='#02A2F2', fg='white', width = 16, font = BUTT_FONT, state = NORMAL)
dugmeD1.grid(column=2, row=7,  padx=(70,0),sticky='w')
dugmeD2 = tk.Button(ram, textvariable = D2, command = lambda: state(dugmeD2),
                  bg='#02A2F2', fg='white', width = 16, font = BUTT_FONT, state = NORMAL)
dugmeD2.grid(column=2, row=8, padx=(130,0),sticky='w')
dugmeD3 = tk.Button(ram, textvariable = D3, command = lambda: state(dugmeD3),
                  bg='#02A2F2', fg='white', width = 16, font = BUTT_FONT, state = NORMAL)
dugmeD3.grid(column=2, row=9, padx=(150,0),sticky='w')
dugmeD4 = tk.Button(ram, textvariable = D4, command = lambda: state(dugmeD4),
                  bg='#02A2F2', fg='white', width = 16, font = BUTT_FONT, state = NORMAL)
dugmeD4.grid(column=2, row=10,  padx=(190,0),sticky='w')
kolonaDent = tk.Entry(ram, textvariable = kolonaD, fg='#02A2F2', justify='center', font = ENT_FONT, width=18)
kolonaDent.grid(column=2,row=6,padx=(0,0),sticky='w')

kolonaDent.bind("<Button-1>", brisiEntry)

#slika
slika=PhotoImage(file='sko.png')
slika=slika.subsample(5,5)
slikalabel=tk.Label(ram,image=slika)
slikalabel.grid(column=1, row=7,rowspan=2, sticky=(N, S, E, W))

root.columnconfigure(0,weight=1)
root.rowconfigure(0,weight=1)
ram.columnconfigure(0,weight=1)
ram.columnconfigure(1,weight=1)
ram.columnconfigure(2,weight=1)
ram.rowconfigure(0,weight=1)
ram.rowconfigure(1,weight=1)
ram.rowconfigure(2,weight=1)
ram.rowconfigure(3,weight=1)
ram.rowconfigure(4,weight=1)
ram.rowconfigure(5,weight=1)
ram.rowconfigure(6,weight=1)
ram.rowconfigure(7,weight=1)
ram.rowconfigure(8,weight=1)
ram.rowconfigure(9,weight=1)
ram.rowconfigure(10,weight=1)

for a in ram.winfo_children(): a.grid_configure(pady=5)
rjesenjeEnt.grid_configure(pady=15)

root.bind("<Button-1>", setEntry)
root.mainloop()
