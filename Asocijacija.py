from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
import tkinter as tk
import os
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
IN_FONT = ('Consolas', 22)

klik = 0   # klik sluzi za sprjecavanje otvaranja vise polja odjednom i unosenja odgovora prije nego se otvori polje
c = None
def vrijeme(count): # tajmer koji prebacuje zutu boju sa igraca na igraca
       global c
       global listaFunkcija
       global klik
       brojac['text'] = count
       if count >= 0:
              if count == 0:
                     if plavi['bg']=='yellow':
                            plavi['bg']='blue'
                            crveni['bg']='yellow'
                            
                     else:
                            crveni['bg']='red'
                            plavi['bg']='yellow'
                            
                     if klik == 0:
                            random.choice(listaFunkcija)()
                     else: klik = 0
                     count = 21
                     
              c=root.after(1000, vrijeme, count-1)

def start(): # start se poziva iz prozorcica koji sluzi da startuje tajmer i pokrene igru
       vrijeme(21)
       plavi['bg']= 'yellow'
       popUp.destroy()
       root.attributes("-topmost", True)

rijeseneKolone = []
listaOtvPolja = []
def reRun():
       popUp.destroy()
       root.destroy()
       os.system('Asocijacija.py')
       
def newGame():
       popUp = Toplevel()
       popUp.geometry('300x200+440+100')
       popUp.attributes("-topmost", True)
       popUp.title('Igra Asocijacije')
       popUp.configure(background='#002240')
       obavjestenje = tk.Label(popUp, text='--Igra asocijacije--',
                               font=TOP_FONT, bg='#002240', fg='yellow')
       obavjestenje.place(x=60)
       pocni = tk.Button(popUp, text='Nova Igra', width=15, font=ENT_FONT, bg="#02A2F2", fg="yellow", command=reRun)
       pocni.place(x=50, y=80)
       zatvori = tk.Button(popUp, text='Zatvori', width=15, font=ENT_FONT, bg="#02A2F2", fg="yellow", command= lambda: root.destroy())
       zatvori.place(x=50, y=140)



root = Tk()
#toplevel se pokrece pri pokretanu programa.
popUp = Toplevel()
popUp.geometry('300x200+440+260')
popUp.attributes("-topmost", True)
popUp.title('Igra Asocijacije')
popUp.configure(background='#002240')
obavjestenje = tk.Label(popUp, text='"Dobro vece!"\n-Milka Canic-',
                        font=TOP_FONT, bg='#002240', fg='yellow')
obavjestenje.place(x=80)
pocni = tk.Button(popUp, text='Pocni igru', width=15, font=ENT_FONT, bg="#02A2F2", fg="yellow", command=start)
pocni.place(x=50, y=80)

root.configure(background='#002240')
#root.geometry('800x800+200+50')
root.minsize(1000,600)
root.title('Igra Asocijacije')

ttk.Style().configure("blue.TFrame", background="#002240")
ram=ttk.Frame(root, style="blue.TFrame")
ram.grid(row=0,column=0)


info = StringVar()
rjesenje = StringVar()

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
       ram.after(2500, clear)
def clear():
       info.set("")


def state(dugme):
       global listaOtvPolja
       global klik
       if dugme == dugmeA1:
              if klik == 0:
                     dugme.config(state = DISABLED)
                     A1.set(podaciA[0].attributes["vrednostA"].value)
                     klik += 1
                     listaOtvPolja.append('A1')
              else:
                     infoPanel('Ponudite odgovor!!')
                     return
       elif dugme == dugmeA2:
              if klik == 0:
                     dugme.config(state = DISABLED)
                     A2.set(podaciA[1].attributes["vrednostA"].value)
                     klik += 1
                     listaOtvPolja.append('A2')
              else:
                     infoPanel('Ponudite odgovor!!')
                     return
       elif dugme == dugmeA3:
              if klik == 0:
                     dugme.config(state = DISABLED)
                     A3.set(podaciA[2].attributes["vrednostA"].value)
                     klik += 1
                     listaOtvPolja.append('A3')
              else:
                     infoPanel('Ponudite odgovor!!')
                     return
       elif dugme == dugmeA4:
              if klik == 0:
                     dugme.config(state = DISABLED)
                     A4.set(podaciA[3].attributes["vrednostA"].value)
                     klik += 1
                     listaOtvPolja.append('A4')
              else:
                     infoPanel('Ponudite odgovor!!')
                     return
       elif dugme == dugmeB1:
              if klik == 0:
                     dugme.config(state = DISABLED)
                     B1.set(podaciB[0].attributes["vrednostB"].value)
                     klik += 1
                     listaOtvPolja.append('B1')
              else:
                     infoPanel('Ponudite odgovor!!')
                     return
       elif dugme == dugmeB2:
              if klik == 0:
                     dugme.config(state = DISABLED)
                     B2.set(podaciB[1].attributes["vrednostB"].value)
                     klik += 1
                     listaOtvPolja.append('B2')
              else:
                     infoPanel('Ponudite odgovor!!')
                     return
       elif dugme == dugmeB3:
              if klik == 0:
                     dugme.config(state = DISABLED)
                     B3.set(podaciB[2].attributes["vrednostB"].value)
                     klik += 1
                     listaOtvPolja.append('B3')
              else:
                     infoPanel('Ponudite odgovor!!')
                     return
       elif dugme == dugmeB4:
              if klik == 0:
                     dugme.config(state = DISABLED)
                     B4.set(podaciB[3].attributes["vrednostB"].value)
                     klik += 1
                     listaOtvPolja.append('B4')
              else:
                     infoPanel('Ponudite odgovor!!')
                     return
       elif dugme == dugmeC1:
              if klik == 0:
                     dugme.config(state = DISABLED)
                     C1.set(podaciC[0].attributes["vrednostC"].value)
                     klik += 1
                     listaOtvPolja.append('C1')
              else:
                     infoPanel('Ponudite odgovor!!')
                     return
       elif dugme == dugmeC2:
              if klik == 0:
                     dugme.config(state = DISABLED)
                     C2.set(podaciC[1].attributes["vrednostC"].value)
                     klik += 1
                     listaOtvPolja.append('C2')
              else:
                     infoPanel('Ponudite odgovor!!')
                     return
       elif dugme == dugmeC3:
              if klik == 0:
                     dugme.config(state = DISABLED)
                     C3.set(podaciC[2].attributes["vrednostC"].value)
                     klik += 1
                     listaOtvPolja.append('C3')
              else:
                     infoPanel('Ponudite odgovor!!')
                     return
       elif dugme == dugmeC4:
              if klik == 0:
                     dugme.config(state = DISABLED)
                     C4.set(podaciC[3].attributes["vrednostC"].value)
                     klik += 1
                     listaOtvPolja.append('C4')
              else:
                     infoPanel('Ponudite odgovor!!')
                     return
       elif dugme == dugmeD1:
              if klik == 0:
                     dugme.config(state = DISABLED)
                     D1.set(podaciD[0].attributes["vrednostD"].value)
                     klik += 1
                     listaOtvPolja.append('D1')
              else:
                     infoPanel('Ponudite odgovor!!')
                     return
       elif dugme == dugmeD2:
              if klik == 0:
                     dugme.config(state = DISABLED)
                     D2.set(podaciD[1].attributes["vrednostD"].value)
                     klik += 1
                     listaOtvPolja.append('D2')
              else:
                     infoPanel('Ponudite odgovor!!')
                     return
       elif dugme == dugmeD3:
              if klik == 0:
                     dugme.config(state = DISABLED)
                     D3.set(podaciD[2].attributes["vrednostD"].value)
                     klik += 1
                     listaOtvPolja.append('D3')
              else:
                     infoPanel('Ponudite odgovor!!')
                     return
       elif dugme == dugmeD4:
              if klik == 0:
                     dugme.config(state = DISABLED)
                     D4.set(podaciD[3].attributes["vrednostD"].value)
                     klik += 1
                     listaOtvPolja.append('D4')
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
       vrijeme(21)
       if kolonaA.get().lower() == rKolonaA.lower():
              klik=1
              rijeseneKolone.append("A")
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
                     kolonaA.set("{}".format(rKolonaA))
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
                     vrijeme(21)
                     kolonaA.set("")
                     root.focus_set()
              elif crveni['bg'] == 'yellow':
                     plavi['bg'] = 'yellow'
                     crveni['bg'] = 'red'
                     root.after_cancel(c)
                     vrijeme(21)
                     kolonaA.set("")
                     root.focus_set()
def tacanOdgovorB():
       brojac['text'] =''
       global c
       global klik
       root.after_cancel(c)
       vrijeme(21)                     
       if kolonaB.get().lower() == rKolonaB.lower():
              klik=1
              rijeseneKolone.append("B")
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
                     kolonaB.set("{}".format(rKolonaB))
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
                     kolonaB.set("{}".format(rKolonaB))
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
                     vrijeme(21)
                     kolonaB.set("")
                     root.focus_set()
              else:
                     plavi['bg'] = 'yellow'
                     crveni['bg'] = 'red'
                     root.after_cancel(c)
                     vrijeme(21)
                     kolonaB.set("")
                     root.focus_set()
def tacanOdgovorC():
       brojac['text'] =''
       global c
       global klik
       root.after_cancel(c)
       vrijeme(21)                     
       if kolonaC.get().lower() == rKolonaC.lower():
              klik=1
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
                     kolonaC.set("{}".format(rKolonaC))
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
                     kolonaC.set("{}".format(rKolonaC))
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
                     vrijeme(21)
                     kolonaC.set("")
                     root.focus_set()
              else:
                     plavi['bg'] = 'yellow'
                     crveni['bg'] = 'red'
                     root.after_cancel(c)
                     vrijeme(21)
                     kolonaC.set("")
                     root.focus_set()                     
def tacanOdgovorD():
       brojac['text'] =''
       global c
       global klik
       root.after_cancel(c)
       vrijeme(21)                     
       if kolonaD.get().lower() == rKolonaD.lower():
              klik=1
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
                     kolonaD.set("{}".format(rKolonaD))
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
                     kolonaD.set("{}".format(rKolonaB))
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
                     vrijeme(21)
                     kolonaD.set("")
                     root.focus_set()
              else:
                     plavi['bg'] = 'yellow'
                     crveni['bg'] = 'red'
                     root.after_cancel(c)
                     vrijeme(21)
                     kolonaD.set("")
                     root.focus_set()
       
def tacanOdgovorR():
       brojac['text'] ='00'
       global c
       root.after_cancel(c)
       if rjesenjeEnt.get().lower() == konacno.lower():
              if plavi['bg'] == 'yellow':
                     if 'A' in rijeseneKolone:
                            pass
                     else:
                            dugmeA1.config(state = DISABLED)
                            A1.set(podaciA[0].attributes["vrednostA"].value)
                            dugmeA1['bg'] = 'blue'
                            dugmeA2.config(state = DISABLED)
                            A2.set(podaciA[1].attributes["vrednostA"].value)
                            dugmeA2['bg'] = 'blue'
                            dugmeA3.config(state = DISABLED)
                            A3.set(podaciA[2].attributes["vrednostA"].value)
                            dugmeA3['bg'] = 'blue'
                            dugmeA4.config(state = DISABLED)
                            A4.set(podaciA[3].attributes["vrednostA"].value)
                            dugmeA4['bg'] = 'blue'
                            kolonaA.set(rKolonaA)
                            kolonaAent.config(state=DISABLED)
              
                     if 'B' in rijeseneKolone:
                            pass
                     else:
                            dugmeB1.config(state = DISABLED)
                            B1.set(podaciB[0].attributes["vrednostB"].value)
                            dugmeB1['bg'] = 'blue'
                            dugmeB2.config(state = DISABLED)
                            B2.set(podaciB[1].attributes["vrednostB"].value)
                            dugmeB2['bg'] = 'blue'
                            dugmeB3.config(state = DISABLED)
                            B3.set(podaciB[2].attributes["vrednostB"].value)
                            dugmeB3['bg'] = 'blue'
                            dugmeB4.config(state = DISABLED)
                            B4.set(podaciB[3].attributes["vrednostB"].value)
                            dugmeB4['bg'] = 'blue'
                            kolonaB.set(rKolonaB)
                            kolonaBent.config(state=DISABLED)

                     if 'C' in rijeseneKolone:
                            pass
                     else:
                            dugmeC1.config(state = DISABLED)
                            C1.set(podaciC[0].attributes["vrednostC"].value)
                            dugmeC1['bg'] = 'blue'
                            dugmeC2.config(state = DISABLED)
                            C2.set(podaciC[1].attributes["vrednostC"].value)
                            dugmeC2['bg'] = 'blue'
                            dugmeC3.config(state = DISABLED)
                            C3.set(podaciC[2].attributes["vrednostC"].value)
                            dugmeC3['bg'] = 'blue'
                            dugmeC4.config(state = DISABLED)
                            C4.set(podaciC[3].attributes["vrednostC"].value)
                            dugmeC4['bg'] = 'blue'
                            kolonaC.set(rKolonaC)
                            kolonaCent.config(state=DISABLED)

                     if 'D' in rijeseneKolone:
                            pass
                     else:
                            dugmeD1.config(state = DISABLED)
                            D1.set(podaciD[0].attributes["vrednostD"].value)
                            dugmeD1['bg'] = 'blue'
                            dugmeD2.config(state = DISABLED)
                            D2.set(podaciD[1].attributes["vrednostD"].value)
                            dugmeD2['bg'] = 'blue'
                            dugmeD3.config(state = DISABLED)
                            D3.set(podaciD[2].attributes["vrednostD"].value)
                            dugmeD3['bg'] = 'blue'
                            dugmeD4.config(state = DISABLED)
                            D4.set(podaciD[3].attributes["vrednostD"].value)
                            dugmeD4['bg'] = 'blue'
                            kolonaD.set(rKolonaD)
                            kolonaDent.config(state=DISABLED)
                            infoPanel("Pobjednik je PLAVI!")
                            newGame()
              if crveni['bg'] == 'yellow':
                     if 'A' in rijeseneKolone:
                            pass
                     else:
                            dugmeA1.config(state = DISABLED)
                            A1.set(podaciA[0].attributes["vrednostA"].value)
                            dugmeA1['bg'] = 'red'
                            dugmeA2.config(state = DISABLED)
                            A2.set(podaciA[1].attributes["vrednostA"].value)
                            dugmeA2['bg'] = 'red'
                            dugmeA3.config(state = DISABLED)
                            A3.set(podaciA[2].attributes["vrednostA"].value)
                            dugmeA3['bg'] = 'red'
                            dugmeA4.config(state = DISABLED)
                            A4.set(podaciA[3].attributes["vrednostA"].value)
                            dugmeA4['bg'] = 'red'
                            kolonaA.set(rKolonaA)
                            kolonaAent.config(state=DISABLED)
              
                     if 'B' in rijeseneKolone:
                            pass
                     else:
                            dugmeB1.config(state = DISABLED)
                            B1.set(podaciB[0].attributes["vrednostB"].value)
                            dugmeB1['bg'] = 'red'
                            dugmeB2.config(state = DISABLED)
                            B2.set(podaciB[1].attributes["vrednostB"].value)
                            dugmeB2['bg'] = 'red'
                            dugmeB3.config(state = DISABLED)
                            B3.set(podaciB[2].attributes["vrednostB"].value)
                            dugmeB3['bg'] = 'red'
                            dugmeB4.config(state = DISABLED)
                            B4.set(podaciB[3].attributes["vrednostB"].value)
                            dugmeB4['bg'] = 'red'
                            kolonaB.set(rKolonaB)
                            kolonaBent.config(state=DISABLED)

                     if 'C' in rijeseneKolone:
                            pass
                     else:
                            dugmeC1.config(state = DISABLED)
                            C1.set(podaciC[0].attributes["vrednostC"].value)
                            dugmeC1['bg'] = 'red'
                            dugmeC2.config(state = DISABLED)
                            C2.set(podaciC[1].attributes["vrednostC"].value)
                            dugmeC2['bg'] = 'red'
                            dugmeC3.config(state = DISABLED)
                            C3.set(podaciC[2].attributes["vrednostC"].value)
                            dugmeC3['bg'] = 'red'
                            dugmeC4.config(state = DISABLED)
                            C4.set(podaciC[3].attributes["vrednostC"].value)
                            dugmeC4['bg'] = 'red'
                            kolonaC.set(rKolonaC)
                            kolonaCent.config(state=DISABLED)

                     if 'D' in rijeseneKolone:
                            pass
                     else:
                            dugmeD1.config(state = DISABLED)
                            D1.set(podaciD[0].attributes["vrednostD"].value)
                            dugmeD1['bg'] = 'red'
                            dugmeD2.config(state = DISABLED)
                            D2.set(podaciD[1].attributes["vrednostD"].value)
                            dugmeD2['bg'] = 'red'
                            dugmeD3.config(state = DISABLED)
                            D3.set(podaciD[2].attributes["vrednostD"].value)
                            dugmeD3['bg'] = 'red'
                            dugmeD4.config(state = DISABLED)
                            D4.set(podaciD[3].attributes["vrednostD"].value)
                            dugmeD4['bg'] = 'red'
                            kolonaD.set(rKolonaD)
                            kolonaDent.config(state=DISABLED)
                            infoPanel("Pobjednik je CRVENI!")
                            newGame()
              rjesenjeEnt.config(state = DISABLED)
       elif rjesenjeEnt.get() != konacno:
               
               infoPanel('Odgovor netacan!')
               if plavi['bg'] == 'yellow':
                      crveni['bg'] = 'yellow'
                      plavi['bg'] = 'blue'
                      root.after_cancel(c)
                      vrijeme(21)
                      kolonaD.set("")
                      root.focus_set()
               else:
                      plavi['bg'] = 'yellow'
                      crveni['bg'] = 'red'
                      root.after_cancel(c)
                      vrijeme(21)
                      kolonaD.set("")
                      root.focus_set()      
def odgovor(*args): # funkcija koja provjeri u kom je entriju kursor a zatim poziva funkciju tacanOdgovor za odredjenu kolonu vezanu za taj entry.. 
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
def dalje():
       global klik
       if klik == 0:
              infoPanel('Otvorite polje!!')
              return
       if plavi['bg'] == 'yellow':
              crveni['bg'] = 'yellow'
              plavi['bg'] = 'blue'
              root.after_cancel(c)
              vrijeme(21)
              kolonaD.set("")
              root.focus_set()
       else:
              plavi['bg'] = 'yellow'
              crveni['bg'] = 'red'
              root.after_cancel(c)
              vrijeme(21)
              kolonaD.set("")
              root.focus_set()
       klik = 0
#kolone A

dugmeA1 = tk.Button(ram, textvariable = A1, command = lambda: state(dugmeA1),
                  bg='#02A2F2', fg='white', width = 16, font = BUTT_FONT, state = NORMAL) #ovo je postavljanje buttona i entryija
dugmeA1.grid(column=1, row=0, padx=(0,0), pady=(0,0), sticky='w')                                                  #klasicni fizicki posao :) 
dugmeA2 = tk.Button(ram, textvariable = A2, command = lambda: state(dugmeA2),
                  bg='#02A2F2', fg='white', width = 16, font = BUTT_FONT, state = NORMAL)
dugmeA2.grid(column=1, row=1, padx=(40,0),pady=(0,0), sticky='w')
dugmeA3 = tk.Button(ram, textvariable = A3, command = lambda: state(dugmeA3),
                  bg='#02A2F2', fg='white', width = 16, font = BUTT_FONT, state = NORMAL)
dugmeA3.grid(column=1, row=2,  padx=(80,0),pady=(0,0),sticky='w')
dugmeA4 = tk.Button(ram, textvariable = A4, command = lambda: state(dugmeA4),
                bg='#02A2F2', fg='white', width = 16, font = BUTT_FONT, state = NORMAL)
dugmeA4.grid(column=1, row=3, padx= (120,0), pady=(0,0),sticky='w')

kolonaAent = tk.Entry(ram, textvariable = kolonaA, fg='#02A2F2', justify='center', font = ENT_FONT, width=18)
kolonaAent.grid(column=1,row=4, padx=(120,0),pady=(0,0),sticky='w')
kolonaAent.bind("<Button-1>", brisiEntry)

#kolone B
dugmeB1 = tk.Button(ram, textvariable = B1, command = lambda: state(dugmeB1),
                  bg='#02A2F2', fg='white', width = 16, font = BUTT_FONT, state = NORMAL)
dugmeB1.grid(column=3, row=0, padx=(190,0), pady=(0,0),sticky='w')

dugmeB2 = tk.Button(ram, textvariable = B2, command = lambda: state(dugmeB2),
                  bg='#02A2F2', fg='white', width = 16, font = BUTT_FONT, state = NORMAL)
dugmeB2.grid(column=3, row=1, padx=(150,0), pady=(0,0), sticky='w')

dugmeB3 = tk.Button(ram, textvariable = B3, command = lambda: state(dugmeB3),
                  bg='#02A2F2', fg='white', width = 16, font = BUTT_FONT, state = NORMAL)
dugmeB3.grid(column=3, row=2, padx=(110,0), pady=(0,0), sticky='w')

dugmeB4 = tk.Button(ram, textvariable = B4, command = lambda: state(dugmeB4),
                  bg='#02A2F2', fg='white', width = 16, font = BUTT_FONT, state = NORMAL)
dugmeB4.grid(column=3, row=3, padx=(70,0), pady=(0,0), sticky='w')

kolonaBent = tk.Entry(ram, textvariable = kolonaB, fg='#02A2F2', justify='center', font = ENT_FONT, width=18)
kolonaBent.grid(column=3, row=4, padx=(0,0), pady=(0,0),sticky='w')

kolonaBent.bind("<Button-1>", brisiEntry)

#RJSENJE
rjesenjeEnt = tk.Entry(ram, textvariable=rjesenje, fg='#02A2F2', justify='center', width = 35, font = RJ_FONT)
rjesenjeEnt.grid(column=1, row=5, padx=(2,0), pady=(20,0), ipady=(2),columnspan=3)
rjesenjeEnt.bind("<Button-1>", brisiEntry)

#kolone C

dugmeC1 = tk.Button(ram, textvariable = C1, command = lambda: state(dugmeC1),
                  bg='#02A2F2', fg='white', width = 16, font = BUTT_FONT, state = NORMAL)
dugmeC1.grid(column=1, row=7, padx=(120,0), pady=(0,0), sticky='w')

dugmeC2 = tk.Button(ram, textvariable = C2, command = lambda: state(dugmeC2),
                  bg='#02A2F2', fg='white', width = 16, font = BUTT_FONT, state = NORMAL)
dugmeC2.grid(column=1, row=8, padx=(80,0), pady=(0,0), sticky='w')

dugmeC3 = tk.Button(ram, textvariable = C3, command = lambda: state(dugmeC3),
                  bg='#02A2F2', fg='white', width = 16, font = BUTT_FONT, state = NORMAL)
dugmeC3.grid(column=1, row=9, padx=(40,0), pady=(0,0), sticky='w')

dugmeC4 = tk.Button(ram, textvariable = C4, command = lambda: state(dugmeC4),
                  bg='#02A2F2', fg='white', width = 16, font = BUTT_FONT, state = NORMAL)
dugmeC4.grid(column=1, row=10, padx=(0,0), pady=(0,0), sticky='w')

kolonaCent = tk.Entry(ram, textvariable = kolonaC, fg='#02A2F2', justify='center', font = ENT_FONT, width=18)
kolonaCent.grid(column=1,row=6, padx=(120,0), pady=(0,0),sticky='w')

kolonaCent.bind("<Button-1>", brisiEntry)


#kolone D

dugmeD1 = tk.Button(ram, textvariable = D1, command = lambda: state(dugmeD1),
                  bg='#02A2F2', fg='white', width = 16, font = BUTT_FONT, state = NORMAL)
dugmeD1.grid(column=3, row=7,  padx=(70,0), sticky='w')

dugmeD2 = tk.Button(ram, textvariable = D2, command = lambda: state(dugmeD2),
                  bg='#02A2F2', fg='white', width = 16, font = BUTT_FONT, state = NORMAL)
dugmeD2.grid(column=3, row=8, padx=(120,0),sticky='w')

dugmeD3 = tk.Button(ram, textvariable = D3, command = lambda: state(dugmeD3),
                  bg='#02A2F2', fg='white', width = 16, font = BUTT_FONT, state = NORMAL)
dugmeD3.grid(column=3, row=9, padx=(150,0),sticky='w')

dugmeD4 = tk.Button(ram, textvariable = D4, command = lambda: state(dugmeD4),
                  bg='#02A2F2', fg='white', width = 16, font = BUTT_FONT, state = NORMAL)
dugmeD4.grid(column=3, row=10, padx=(190,0),sticky='w')

kolonaDent = tk.Entry(ram, textvariable = kolonaD, fg='#02A2F2', justify='center', font = ENT_FONT, width=18)
kolonaDent.grid(column=3,row=6,padx=(0,0),sticky='w')

kolonaDent.bind("<Button-1>", brisiEntry)

def pop(*args):
    tk.messagebox.showinfo("PROČITAJ", "Prilikom upsivanja rešenja Koristite slova sa kvačicama(š,đ,č,ć,ž).")

up = tk.Button(ram, text = "Uputsvto", command= pop,bg='#02A2F2', fg='yellow', justify="center", width = 10, font = BUTT_FONT, state = NORMAL)
up.grid(column=2, row=8, sticky='w')



#sijalica slika
sijalica = PhotoImage(file='sijalica.png')
sijalica = sijalica.subsample(10)
#dugme
potvrdi = tk.Button(ram, text="Potvrdi", font = BUTT_FONT, bg='#02A2F2', fg='yellow', width=8, command = odgovor)
potvrdi.grid(column=4, row=5, padx=(0,30))
kontis= ttk.Frame(ram, style="blue.TFrame" )
kontis.grid(row=0, column=1, columnspan=3, rowspan=2, padx=(190,190), pady=(0,0), sticky=(N,S,E,W))
plavi = tk.Button(kontis, image = sijalica, bg='blue')
plavi.grid(column=2, row=0)
crveni = tk.Button(kontis, image = sijalica, bg='red')
crveni.grid(column=0, row=0)
dalje = tk.Button(ram, text="Dalje",  font=BUTT_FONT, bg='#02A2F2', fg='yellow', width=8, command = dalje)
dalje.grid(column=0, padx=(30,0),row=5)

# brojac
brojac = tk.Label(kontis,font=RJ_FONT, relief=SUNKEN)
brojac.grid(column=1, row=0, sticky=(N,S,E,W))
#infoLabel
infolabel=tk.Label(ram,textvariable = info, font=IN_FONT, fg='yellow', bg='#002240')
infolabel.grid(column=1, columnspan=3, row=11,sticky=(N, S, E, W))

####################Pojedinacne funkcije za otvaranje random polja####################
def otvA1():
       if 'A1' in listaOtvPolja:
              random.choice(listaFunkcija)()
       else:
              dugmeA1.config(state = DISABLED)
              A1.set(podaciA[0].attributes["vrednostA"].value)
              listaOtvPolja.append('A1')
              klik = 1
def otvA2():
       if 'A2' in listaOtvPolja:
              random.choice(listaFunkcija)()
       else:
              dugmeA2.config(state = DISABLED)
              A2.set(podaciA[1].attributes["vrednostA"].value)
              listaOtvPolja.append('A2')
              klik = 1
def otvA3():
       if 'A3' in listaOtvPolja:
              random.choice(listaFunkcija)()
       else:
              dugmeA3.config(state = DISABLED)
              A3.set(podaciA[2].attributes["vrednostA"].value)
              listaOtvPolja.append('A3')
              klik = 1
def otvA4():
       if 'A4' in listaOtvPolja:
              random.choice(listaFunkcija)()
       else:
              dugmeA4.config(state = DISABLED)
              A4.set(podaciA[3].attributes["vrednostA"].value)
              listaOtvPolja.append('A4')
              klik = 1
       


def otvB1():
       if 'B1' in listaOtvPolja:
              random.choice(listaFunkcija)()
       else:
              dugmeB1.config(state = DISABLED)
              B1.set(podaciB[0].attributes["vrednostB"].value)
              listaOtvPolja.append('B1')
              klik = 1
def otvB2():
       if 'B2' in listaOtvPolja:
              random.choice(listaFunkcija)()
       else:
              dugmeB2.config(state = DISABLED)
              B2.set(podaciB[1].attributes["vrednostB"].value)
              listaOtvPolja.append('B2')
              klik = 1
def otvB3():
       if 'B3' in listaOtvPolja:
              random.choice(listaFunkcija)()
       else:
              dugmeB3.config(state = DISABLED)
              B3.set(podaciB[2].attributes["vrednostB"].value)
              listaOtvPolja.append('B3')
              klik = 1
def otvB4():
       if 'B4' in listaOtvPolja:
              random.choice(listaFunkcija)()
       else:
              dugmeB4.config(state = DISABLED)
              B4.set(podaciB[3].attributes["vrednostB"].value)
              listaOtvPolja.append('B4')
              klik = 1

def otvC1():
       if 'C1' in listaOtvPolja:
              random.choice(listaFunkcija)()
       else:
              dugmeC1.config(state = DISABLED)
              C1.set(podaciC[0].attributes["vrednostC"].value)
              listaOtvPolja.append('C1')

              klik = 1

def otvC2():

       if 'C2' in listaOtvPolja:
              random.choice(listaFunkcija)()
       else:
              dugmeC2.config(state = DISABLED)
              C2.set(podaciC[1].attributes["vrednostC"].value)
              listaOtvPolja.append('C2')
              klik = 1
def otvC3():
       if 'C3' in listaOtvPolja:
              random.choice(listaFunkcija)()
       else:
              dugmeC3.config(state = DISABLED)
              C3.set(podaciC[2].attributes["vrednostC"].value)
              listaOtvPolja.append('C3')
              klik = 1
def otvC4():
       if 'C4' in listaOtvPolja:
              random.choice(listaFunkcija)()
       else:
              dugmeC4.config(state = DISABLED)
              C4.set(podaciC[3].attributes["vrednostC"].value)
              listaOtvPolja.append('C4')
              klik = 1

def otvD1():
       if 'D1' in listaOtvPolja:
              random.choice(listaFunkcija)()
       else:
              dugmeD1.config(state = DISABLED)
              D1.set(podaciD[0].attributes["vrednostD"].value)
              listaOtvPolja.append('D1')
              klik = 1
def otvD2():
       if 'D2' in listaOtvPolja:
              random.choice(listaFunkcija)()
       else:
              dugmeD2.config(state = DISABLED)
              D2.set(podaciD[1].attributes["vrednostD"].value)
              listaOtvPolja.append('D2')
              klik = 1
def otvD3():
       if 'D3' in listaOtvPolja:
              random.choice(listaFunkcija)()
       else:
              dugmeD3.config(state = DISABLED)
              D3.set(podaciD[2].attributes["vrednostD"].value)
              listaOtvPolja.append('D3')
              klik = 1
def otvD4():
       if 'D4' in listaOtvPolja:
              random.choice(listaFunkcija)()
       else:
              dugmeD4.config(state = DISABLED)
              D4.set(podaciD[3].attributes["vrednostD"].value)
              listaOtvPolja.append('D4')
              klik = 1
global listaFunkcija
listaFunkcija = [otvA1, otvA2, otvA3, otvA4, otvB1, otvB2, otvB3, otvB4, otvC1, otvC2, otvC3, otvC4, otvD1, otvD2, otvD3, otvD4]


root.columnconfigure(0,weight=1)
root.rowconfigure(0,weight=1)

for i in range(5):
	ram.columnconfigure(i,weight=1)
for i in range(12):
	ram.rowconfigure(i,weight=1)

kontis.columnconfigure(0, weight=1)
kontis.columnconfigure(1, weight=1)
kontis.columnconfigure(2, weight=1)
kontis.rowconfigure(0, weight=1)

for a in ram.winfo_children(): a.grid_configure(pady=5)
rjesenjeEnt.grid_configure(pady=15)


root.bind("<Return>", odgovor)


root.mainloop()
