from tkinter import *
from tkinter import ttk
import tkinter as tk
from xml.dom import minidom    # minidom je deo biblioteke XML za parsiranje
e = minidom.parse("Asoc.xml")  # Povezvanje parsera sa Asoc.xml
podaciA=e.getElementsByTagName("poljeA")   #Dohvatanje elemenata iz XML-a
podaciB=e.getElementsByTagName("poljeB")
podaciC=e.getElementsByTagName("poljeC")
podaciD=e.getElementsByTagName("poljeD")


#rjesenja kolona
rKolonaA = podaciA[4].attributes["vrednostA"].value
rKolonaB = podaciB[4].attributes["vrednostB"].value
rKolonaC = podaciC[4].attributes["vrednostC"].value
rKolonaD = podaciD[4].attributes["vrednostD"].value
konacno=e.getElementsByTagName("Konacno")[0].attributes["vrednostK"].value
TOP_FONT = ('Consolas', 13)
BUTT_FONT = ('Consolas', 14, 'bold')
ENT_FONT = ('Consolas', 17, 'bold')
RJ_FONT = ('Consolas', 25, 'bold')
klik = 0   # klik sluzi za sprjecavanje otvaranja vise polja odjednom i unosenja odgovora prije nego se otvori polje
c = None
def vrijeme(count): # tajmer koji prebacuje zutu boju sa igraca na igraca
       global c
       brojac['text'] = count
       if count >= 0:
              if count == 0:
                     if plavi['bg']=='yellow':
                            plavi['bg']='blue'
                            crveni['bg']='yellow'
                     else:
                            crveni['bg']='red'
                            plavi['bg']='yellow'
                     count = 16
              c=root.after(1000, vrijeme, count-1)
def start(): # start se poziva iz prozorcica koji sluzi da startuje tajmer i pokrene igru
       vrijeme(16)
       plavi['bg']= 'yellow'
       popUp.destroy()
       root.attributes("-topmost", True)
root = Tk()
#toplevel se pokrece pri pokretanu programa.
popUp = Toplevel()
popUp.geometry('300x200+375+180')
popUp.attributes("-topmost", True)
popUp.title('Igra Asocijacije')
popUp.configure(background='#002240')
obavjestenje = tk.Label(popUp, text='--Igra acocijacija--',
                        font=TOP_FONT, bg='#002240', fg='yellow')
obavjestenje.place(x=60)
pocni = tk.Button(popUp, text='Pocni igru', width=15, font=ENT_FONT, bg="#02A2F2", fg="yellow", command=start)
pocni.place(x=50, y=80)

root.configure(background='#002240')
root.geometry('800x600+200+50')
root.title('Igra Asocijacije')

info = StringVar()
rjesenje = StringVar()
rjesenje.set('*rjesenje*')
#VARIJABLE A             #kada se program pokrene varijable se setuju na imena polja
kolonaA = StringVar()
#kolonaA.set('***A***')
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
#kolonaB.set('***B***')
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
#kolonaC.set('***C***')
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
#kolonaD.set('***D***')
D1 = StringVar()
D1.set('D1')
D2 = StringVar()
D2.set('D2')
D3 = StringVar()
D3.set('D3')
D4 = StringVar()
D4.set('D4')

#funkcija koja setuje labelu koja daje informacije i uputstva tokom igre.. pojavljuje se 2 sekunde i onda nestane
def infoPanel(str):
       info.set(str)
       root.after(2000, clear)
def clear():
       info.set("")



def state(dugme):
       global klik
       if dugme == dugmeA1:
              if klik == 0:
                     dugme.config(state = DISABLED)
                     A1.set(podaciA[0].attributes["vrednostA"].value)
                     klik += 1
              else:
                     infoPanel('Ponudite odgovor!!')
                     return
       elif dugme == dugmeA2:
              if klik == 0:
                     dugme.config(state = DISABLED)
                     A2.set(podaciA[1].attributes["vrednostA"].value)
                     klik += 1
              else:
                     infoPanel('Ponudite odgovor!!')
                     return
       elif dugme == dugmeA3:
              if klik == 0:
                     dugme.config(state = DISABLED)
                     A3.set(podaciA[2].attributes["vrednostA"].value)
                     klik += 1
              else:
                     infoPanel('Ponudite odgovor!!')
                     return
       elif dugme == dugmeA4:
              if klik == 0:
                     dugme.config(state = DISABLED)
                     A4.set(podaciA[3].attributes["vrednostA"].value)
                     klik += 1
              else:
                     infoPanel('Ponudite odgovor!!')
                     return
       elif dugme == dugmeB1:
              if klik == 0:
                     dugme.config(state = DISABLED)
                     B1.set(podaciB[0].attributes["vrednostB"].value)
                     klik += 1
              else:
                     infoPanel('Ponudite odgovor!!')
                     return
       elif dugme == dugmeB2:
              if klik == 0:
                     dugme.config(state = DISABLED)
                     B2.set(podaciB[1].attributes["vrednostB"].value)
                     klik += 1
              else:
                     infoPanel('Ponudite odgovor!!')
                     return
       elif dugme == dugmeB3:
              if klik == 0:
                     dugme.config(state = DISABLED)
                     B3.set(podaciB[2].attributes["vrednostB"].value)
                     klik += 1
              else:
                     infoPanel('Ponudite odgovor!!')
                     return
       elif dugme == dugmeB4:
              if klik == 0:
                     dugme.config(state = DISABLED)
                     B4.set(podaciB[3].attributes["vrednostB"].value)
                     klik += 1
              else:
                     infoPanel('Ponudite odgovor!!')
                     return
       elif dugme == dugmeC1:
              if klik == 0:
                     dugme.config(state = DISABLED)
                     C1.set(podaciC[0].attributes["vrednostC"].value)
                     klik += 1
              else:
                     infoPanel('Ponudite odgovor!!')
                     return
       elif dugme == dugmeC2:
              if klik == 0:
                     dugme.config(state = DISABLED)
                     C2.set(podaciC[1].attributes["vrednostC"].value)
                     klik += 1
              else:
                     infoPanel('Ponudite odgovor!!')
                     return
       elif dugme == dugmeC3:
              if klik == 0:
                     dugme.config(state = DISABLED)
                     C3.set(podaciC[2].attributes["vrednostC"].value)
                     klik += 1
              else:
                     infoPanel('Ponudite odgovor!!')
                     return
       elif dugme == dugmeC4:
              if klik == 0:
                     dugme.config(state = DISABLED)
                     C4.set(podaciC[3].attributes["vrednostC"].value)
                     klik += 1
              else:
                     infoPanel('Ponudite odgovor!!')
                     return
       elif dugme == dugmeD1:
              if klik == 0:
                     dugme.config(state = DISABLED)
                     D1.set(podaciD[0].attributes["vrednostD"].value)
                     klik += 1
              else:
                     infoPanel('Ponudite odgovor!!')
                     return
       elif dugme == dugmeD2:
              if klik == 0:
                     dugme.config(state = DISABLED)
                     D2.set(podaciD[1].attributes["vrednostD"].value)
                     klik += 1
              else:
                     infoPanel('Ponudite odgovor!!')
                     return
       elif dugme == dugmeD3:
              if klik == 0:
                     dugme.config(state = DISABLED)
                     D3.set(podaciD[2].attributes["vrednostD"].value)
                     klik += 1
              else:
                     infoPanel('Ponudite odgovor!!')
                     return
       elif dugme == dugmeD4:
              if klik == 0:
                     dugme.config(state = DISABLED)
                     D4.set(podaciD[3].attributes["vrednostD"].value)
                     klik += 1
              else:
                     infoPanel('Ponudite odgovor!!')
                     return


def brisiEntry(event):
       event.widget.delete(0, 'end') #funkcija brise bilo koji entry koji joj proslijedimo
       return None
##def setEntry(event):
##       if root.focus_get()!= event.widget: #funkcija koja setuje entryije na pocetne vrijednosti kada kliknete
##              kolonaA.set('***A***')             #bilo gdje van entryja
##              kolonaB.set('***B***')
##              kolonaC.set('***C***')
##              kolonaD.set('***D***')
##              rjesenje.set('*rjesenje*')
##              root.focus_set()


# funkcije tacan odgovor su razdvojene po kolonama (A, B, C, D), provjeravaju da li je odgovor tacan i otkrivaju polja kolona..
def tacanOdgovorA(): 
       brojac['text'] =''
       global c
       global klik   
       root.after_cancel(c)
       vrijeme(16)
       if kolonaA.get() == rKolonaA:
              if plavi['bg'] == 'yellow':
                     dugmeA1.config(state = DISABLED)
                     A1.set(podaciA[0].attributes["vrednostA"].value)
                     dugmeA1["bg"] = "blue"
                     dugmeA2.config(state = DISABLED)
                     A2.set(podaciA[1].attributes["vrednostA"].value)
                     dugmeA2["bg"] = "blue"
                     dugmeA3.config(state = DISABLED)
                     A3.set(podaciA[2].attributes["vrednostA"].value)
                     dugmeA3["bg"] = "blue"
                     dugmeA4.config(state = DISABLED)
                     A4.set(podaciA[3].attributes["vrednostA"].value)
                     dugmeA4["bg"] = "blue"
                     kolonaAent.config(state=DISABLED)
                     kolonaA.set("*{}*".format(rKolonaA))
              elif crveni['bg'] == 'yellow':
                     dugmeA1.config(state = DISABLED)
                     A1.set(podaciA[0].attributes["vrednostA"].value)
                     dugmeA1["bg"] = "red"
                     dugmeA2.config(state = DISABLED)
                     A2.set(podaciA[1].attributes["vrednostA"].value)
                     dugmeA2["bg"] = "red"
                     dugmeA3.config(state = DISABLED)
                     A3.set(podaciA[2].attributes["vrednostA"].value)
                     dugmeA3["bg"] = "red"
                     dugmeA4.config(state = DISABLED)
                     A4.set(podaciA[3].attributes["vrednostA"].value)
                     dugmeA4["bg"] = "red"
                     kolonaAent.config(state=DISABLED)
                     kolonaA.set("{}".format(rKolonaA))
       elif kolonaA.get() == '':
              infoPanel('Unesite odgovor!!')
              klik = 1
              return
       elif kolonaA.get() != rKolonaA:
              infoPanel('Odgovor netacan!')
              if plavi['bg'] == 'yellow':
                     crveni['bg'] = 'yellow'
                     plavi['bg'] = 'blue'
                     root.after_cancel(c)
                     vrijeme(16)
                     kolonaA.set("")
                     root.focus_set()
              elif crveni['bg'] == 'yellow':
                     plavi['bg'] = 'yellow'
                     crveni['bg'] = 'red'
                     root.after_cancel(c)
                     vrijeme(16)
                     kolonaA.set("")
                     root.focus_set()
def tacanOdgovorB():
       brojac['text'] =''
       global c
       global klik
       root.after_cancel(c)
       vrijeme(16)                     
       if kolonaB.get() == rKolonaB:
              if plavi['bg'] == 'yellow':
                     dugmeB1.config(state = DISABLED)
                     B1.set(podaciB[0].attributes["vrednostB"].value)
                     dugmeB1["bg"] = "blue"
                     dugmeB2.config(state = DISABLED)
                     B2.set(podaciB[1].attributes["vrednostB"].value)
                     dugmeB2["bg"] = "blue"
                     dugmeB3.config(state = DISABLED)
                     B3.set(podaciB[2].attributes["vrednostB"].value)
                     dugmeB3["bg"] = "blue"
                     dugmeB4.config(state = DISABLED)
                     B4.set(podaciB[3].attributes["vrednostB"].value)
                     dugmeB4["bg"] = "blue"
                     kolonaBent.config(state=DISABLED)
                     kolonaB.set("*{}*".format(rKolonaB))
              elif crveni['bg']== 'yellow':
                     dugmeB1.config(state = DISABLED)
                     B1.set(podaciB[0].attributes["vrednostB"].value)
                     dugmeB1["bg"] = "red"
                     dugmeB2.config(state = DISABLED)
                     B2.set(podaciB[1].attributes["vrednostB"].value)
                     dugmeB2["bg"] = "red"
                     dugmeB3.config(state = DISABLED)
                     B3.set(podaciB[2].attributes["vrednostB"].value)
                     dugmeB3["bg"] = "red"
                     dugmeB4.config(state = DISABLED)
                     B4.set(podaciB[3].attributes["vrednostB"].value)
                     dugmeB4["bg"] = "red"
                     kolonaBent.config(state=DISABLED)
                     kolonaB.set("*{}*".format(rKolonaB))
       elif kolonaB.get() == '':
              infoPanel('Unesite odgovor!!')
              klik = 1
              return
       elif kolonaB.get() != rKolonaB:
              infoPanel('Odgovor netacan!')
              if plavi['bg'] == 'yellow':
                     crveni['bg'] = 'yellow'
                     plavi['bg'] = 'blue'
                     root.after_cancel(c)
                     vrijeme(16)
                     kolonaB.set("")
                     root.focus_set()
              else:
                     plavi['bg'] = 'yellow'
                     crveni['bg'] = 'red'
                     root.after_cancel(c)
                     vrijeme(16)
                     kolonaB.set("")
                     root.focus_set()
def tacanOdgovorC():
       brojac['text'] =''
       global c
       global klik
       root.after_cancel(c)
       vrijeme(16)                     
       if kolonaC.get() == rKolonaC:
              if plavi['bg'] == 'yellow':
                     dugmeC1.config(state = DISABLED)
                     C1.set(podaciC[0].attributes["vrednostC"].value)
                     dugmeC1["bg"] = "blue"
                     dugmeC2.config(state = DISABLED)
                     C2.set(podaciC[1].attributes["vrednostC"].value)
                     dugmeC2["bg"] = "blue"
                     dugmeC3.config(state = DISABLED)
                     C3.set(podaciC[2].attributes["vrednostC"].value)
                     dugmeC3["bg"] = "blue"
                     dugmeC4.config(state = DISABLED)
                     C4.set(podaciC[3].attributes["vrednostC"].value)
                     dugmeC4["bg"] = "blue"
                     kolonaCent.config(state=DISABLED)
                     kolonaC.set("*{}*".format(rKolonaC))
              elif crveni['bg']== 'yellow':
                     dugmeC1.config(state = DISABLED)
                     C1.set(podaciC[0].attributes["vrednostC"].value)
                     dugmeC1["bg"] = "red"
                     dugmeC2.config(state = DISABLED)
                     C2.set(podaciC[1].attributes["vrednostC"].value)
                     dugmeC2["bg"] = "red"
                     dugmeC3.config(state = DISABLED)
                     C3.set(podaciC[2].attributes["vrednostC"].value)
                     dugmeC3["bg"] = "red"
                     dugmeC4.config(state = DISABLED)
                     C4.set(podaciC[3].attributes["vrednostC"].value)
                     dugmeC4["bg"] = "red"
                     kolonaCent.config(state=DISABLED)
                     kolonaC.set("*{}*".format(rKolonaC))
       elif kolonaC.get() == '':
              infoPanel('Unesite odgovor!!')
              klik = 1
              return
       elif kolonaC.get() != rKolonaC:
              infoPanel('Odgovor netacan!')
              if plavi['bg'] == 'yellow':
                     crveni['bg'] = 'yellow'
                     plavi['bg'] = 'blue'
                     root.after_cancel(c)
                     vrijeme(16)
                     kolonaC.set("")
                     root.focus_set()
              else:
                     plavi['bg'] = 'yellow'
                     crveni['bg'] = 'red'
                     root.after_cancel(c)
                     vrijeme(16)
                     kolonaC.set("")
                     root.focus_set()                     
def tacanOdgovorD():
       brojac['text'] =''
       global c
       global klik
       root.after_cancel(c)
       vrijeme(16)                     
       if kolonaD.get() == rKolonaD:
              if plavi['bg'] == 'yellow':
                     dugmeD1.config(state = DISABLED)
                     D1.set(podaciD[0].attributes["vrednostD"].value)
                     dugmeD1["bg"] = "blue"
                     dugmeD2.config(state = DISABLED)
                     D2.set(podaciD[1].attributes["vrednostD"].value)
                     dugmeD2["bg"] = "blue"
                     dugmeD3.config(state = DISABLED)
                     D3.set(podaciD[2].attributes["vrednostD"].value)
                     dugmeD3["bg"] = "blue"
                     dugmeD4.config(state = DISABLED)
                     D4.set(podaciD[3].attributes["vrednostD"].value)
                     dugmeD4["bg"] = "blue"
                     kolonaDent.config(state=DISABLED)
                     kolonaD.set("*{}*".format(rKolonaD))
              elif crveni['bg']== 'yellow':
                     dugmeD1.config(state = DISABLED)
                     D1.set(podaciD[0].attributes["vrednostD"].value)
                     dugmeD1["bg"] = "red"
                     dugmeD2.config(state = DISABLED)
                     D2.set(podaciD[1].attributes["vrednostD"].value)
                     dugmeD2["bg"] = "red"
                     dugmeD3.config(state = DISABLED)
                     D3.set(podaciD[2].attributes["vrednostD"].value)
                     dugmeD3["bg"] = "red"
                     dugmeD4.config(state = DISABLED)
                     D4.set(podaciD[3].attributes["vrednostD"].value)
                     dugmeD4["bg"] = "red"
                     kolonaDent.config(state=DISABLED)
                     kolonaD.set("*{}*".format(rKolonaB))
       elif kolonaD.get() == '':
              infoPanel('Unesite odgovor!!')
              klik = 1
              return
       
       elif kolonaD.get() != rKolonaD:
              infoPanel('Odgovor netacan!')
              if plavi['bg'] == 'yellow':
                     crveni['bg'] = 'yellow'
                     plavi['bg'] = 'blue'
                     root.after_cancel(c)
                     vrijeme(16)
                     kolonaD.set("")
                     root.focus_set()
              else:
                     plavi['bg'] = 'yellow'
                     crveni['bg'] = 'red'
                     root.after_cancel(c)
                     vrijeme(16)
                     kolonaD.set("")
                     root.focus_set()
       
def tacanOdgovorR():
       brojac['text'] ='00'
       global c
       root.after_cancel(c)
       if rjesenjeEnt.get() == konacno:
              dugmeA1.config(state = DISABLED)
              A1.set(podaciA[0].attributes["vrednostA"].value)
              dugmeA2.config(state = DISABLED)
              A2.set(podaciA[1].attributes["vrednostA"].value)
              dugmeA3.config(state = DISABLED)
              A3.set(podaciA[2].attributes["vrednostA"].value)
              dugmeA4.config(state = DISABLED)
              A4.set(podaciA[3].attributes["vrednostA"].value)
              kolonaA.set(rKolonaA)
              kolonaAent.config(state=DISABLED)
              
              dugmeB1.config(state = DISABLED)
              B1.set(podaciB[0].attributes["vrednostB"].value)
              dugmeB2.config(state = DISABLED)
              B2.set(podaciB[1].attributes["vrednostB"].value)
              dugmeB3.config(state = DISABLED)
              B3.set(podaciB[2].attributes["vrednostB"].value)
              dugmeB4.config(state = DISABLED)
              B4.set(podaciB[3].attributes["vrednostB"].value)
              kolonaB.set(rKolonaB)
              kolonaBent.config(state=DISABLED)

              dugmeC1.config(state = DISABLED)
              C1.set(podaciC[0].attributes["vrednostC"].value)
              dugmeC2.config(state = DISABLED)
              C2.set(podaciC[1].attributes["vrednostC"].value)
              dugmeC3.config(state = DISABLED)
              C3.set(podaciC[2].attributes["vrednostC"].value)
              dugmeC4.config(state = DISABLED)
              C4.set(podaciC[3].attributes["vrednostC"].value)
              kolonaC.set(rKolonaC)
              kolonaCent.config(state=DISABLED)

              dugmeD1.config(state = DISABLED)
              D1.set(podaciD[0].attributes["vrednostD"].value)
              dugmeD2.config(state = DISABLED)
              D2.set(podaciD[1].attributes["vrednostD"].value)
              dugmeD3.config(state = DISABLED)
              D3.set(podaciD[2].attributes["vrednostD"].value)
              dugmeD4.config(state = DISABLED)
              D4.set(podaciD[3].attributes["vrednostD"].value)
              kolonaD.set(rKolonaD)
              kolonaDent.config(state=DISABLED)
def odgovor(): # funkcija koja provjeri u kom je entriju kursor a zatim poziva funkciju tacanOdgovor za odredjenu kolonu vezanu za taj entry.. 
       global klik
       if klik == 1:
              klik = 0
              if root.focus_get() == kolonaAent:
                     tacanOdgovorA()
              elif root.focus_get() == kolonaBent:
                     tacanOdgovorB()
              elif root.focus_get() == kolonaCent:
                     tacanOdgovorC()
              elif root.focus_get() == kolonaDent:
                     tacanOdgovorD()
              elif root.focus_get() == rjesenjeEnt:
                     tacanOdgovorR()
              elif root.focus_get() != kolonaAent and root.focus_get() != kolonaBent and root.focus_get() != kolonaCent and root.focus_get() != kolonaDent and root.focus_get() != rjesenjeEnt:
                     return
       else:
              infoPanel('Otvorite polje!!')
              return

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
#sijalica slika
sijalica = PhotoImage(file='sijalica.png')
sijalica = sijalica.subsample(10)
#dugme
potvrdi = tk.Button(root, text="Potvrdi", font = BUTT_FONT, bg='#02A2F2', fg='yellow',  command = odgovor)
potvrdi.grid(column=1, row=5)
potvrdi.place(x=700, y=283)
plavi = tk.Button(root, image = sijalica, bg='blue')
plavi.grid(column=2, row=0)
plavi.place(x=250)
crveni = tk.Button(root, image = sijalica, bg='red')
crveni.grid(column=1, row=0)
crveni.place(x=470)
# brojac
brojac = tk.Label(root, width=5, font=RJ_FONT, relief=SUNKEN)
brojac.place(x=350)
#infoLabel

infolabel=tk.Label(root,textvariable = info, font=BUTT_FONT, fg='yellow', bg='#002240')
infolabel.grid(column=0, row=8,columnspan=1, sticky=(N, S, E, W))
infolabel.place(x=330, y=450)


#root.bind("<Button-1>", setEntry)
root.mainloop()
