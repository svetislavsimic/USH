from tkinter import *
from tkinter import ttk
import tkinter as tk

BUTT_FONT = ('Consolas', 14, 'bold')
ENT_FONT = ('Consolas', 17, 'bold')
RJ_FONT = ('Consolas', 25, 'bold')
root = Tk()
root.configure(background='#002240')


root.geometry('800x600')
root.title('Igra Asocijacije')
rjesenje = StringVar()
rjesenje.set('*rjesenje*')
#VARIJABLE A             #kada se program pokrene varijable se setuju na imena polja
kolonaA = StringVar()
kolonaA.set('***A***')
A1 = StringVar()
A1.set('A1')
A2 = StringVar()
A2.set('A2')
A3 = StringVar()
A3.set('A3')
A4 = StringVar()
A4.set('A4')
#VARIJABLE B
kolonaB = StringVar()
kolonaB.set('***B***')
B1 = StringVar()
B1.set('B1')
B2 = StringVar()
B2.set('B2')
B3 = StringVar()
B3.set('B3')
B4 = StringVar()
B4.set('B4')
#VARIJABLE C
kolonaC = StringVar()
kolonaC.set('***C***')
C1 = StringVar()
C1.set('C1')
C2 = StringVar()
C2.set('C2')
C3 = StringVar()
C3.set('C3')
C4 = StringVar()
C4.set('C4')

#VARIJABLE D
kolonaD = StringVar()
kolonaD.set('***D***')
D1 = StringVar()
D1.set('D1')
D2 = StringVar()
D2.set('D2')
D3 = StringVar()
D3.set('D3')
D4 = StringVar()
D4.set('D4')


def state(dugme):
       if dugme == dugmeA1:
              dugme.config(state = DISABLED)  #funkcija koja setuje varijable na vrijednost (ovo je samo testna verzija)
              A1.set('vazduh')                   #inace ce da ih setuje na vrijednosti koje povuce iz fajla koji proslijedimo
       elif dugme == dugmeA2:                    #u programu
              dugme.config(state = DISABLED)
              A2.set('voda')
       elif dugme == dugmeA3:
              dugme.config(state = DISABLED)
              A3.set('vatra')
       elif dugme == dugmeA4:
              dugme.config(state = DISABLED)
              A4.set('zemlja')
       elif dugme == dugmeB1:
              dugme.config(state = DISABLED)
              B1.set('vazduh')
       elif dugme == dugmeB2:
              dugme.config(state = DISABLED)
              B2.set('voda')
       elif dugme == dugmeB3:
              dugme.config(state = DISABLED)
              B3.set('vatra')
       elif dugme == dugmeB4:
              dugme.config(state = DISABLED)
              B4.set('zemlja')
       elif dugme == dugmeC1:
              dugme.config(state = DISABLED)
              C1.set('vazduh')
       elif dugme == dugmeC2:
              dugme.config(state = DISABLED)
              C2.set('voda')
       elif dugme == dugmeC3:
              dugme.config(state = DISABLED)
              C3.set('vatra')
       elif dugme == dugmeC4:
              dugme.config(state = DISABLED)
              C4.set('zemlja')
       elif dugme == dugmeD1:
              dugme.config(state = DISABLED)
              D1.set('vazduh')
       elif dugme == dugmeD2:
              dugme.config(state = DISABLED)
              D2.set('voda')
       elif dugme == dugmeD3:
              dugme.config(state = DISABLED)
              D3.set('vatra')
       elif dugme == dugmeD4:
              dugme.config(state = DISABLED)
              D4.set('zemlja')

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

root.bind("<Button-1>", setEntry)
root.mainloop()
