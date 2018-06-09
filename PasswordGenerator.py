import string
import random
import tkinter


kirjaimet_pienet = list(string.ascii_lowercase)
kirjaimet_pienet.pop(kirjaimet_pienet.index("l"))
kirjaimet_isot = list(string.ascii_uppercase)
kirjaimet_isot.pop(kirjaimet_isot.index("I"))
numerot = list(string.digits)
merkit = []
merkit.append(kirjaimet_pienet)
merkit.append(kirjaimet_isot)
merkit.append(numerot)

def Tee_Salasana(pituus=8):
    salasana = ""
    for x in range(pituus):
        joukko = random.randint(0, 2)
        salasana += merkit[joukko][random.randint(0, len(merkit[joukko])-1)]
    return salasana

def Salasana_Listaus(maara=5, pituus=8):
    kaikki_salasanat = ""
    #print("Tulostetaan lista salasanoja:")
    for each in range(maara):
        salasana = Tee_Salasana(pituus)
        #print(salasana)
        kaikki_salasanat += salasana + '\r\n'
    #print("Lista on valmis")
    print(kaikki_salasanat)
    #teksti.insert('end', kaikki_salasanat)
    return kaikki_salasanat
    #tkinter.messagebox.showinfo(Tee_Salasana)

def MakeEntry(parent, caption, width=None, DefValue="", **options):
    tkinter.Label(parent, text=caption).pack()
    entry = tkinter.Entry(parent, **options)
    entry.insert(tkinter.INSERT, DefValue)
    if width:
        entry.config(width=width)
    entry.pack()
    return entry

def NapinPainallus(event=None):
    try:
        pituusVar = int(pituus.get())
        maaraVar =int(maara.get())
    except ValueError:
        teksti.config(state='normal')
        teksti.delete('1.0', tkinter.END)
        teksti.insert(tkinter.INSERT, "Syötä kelvollinen numero")
        teksti.config(state='disabled')
    salasanat = Salasana_Listaus(maara=maaraVar, pituus=pituusVar)
    teksti.config(state='normal')
    teksti.delete('1.0', tkinter.END)
    teksti.insert(tkinter.INSERT, salasanat)
    teksti.config(state='disabled')


def TextField(parent, **options):
    tkinter.Label(parent, text="Salasanat:").pack()
    text = tkinter.Text(parent)
    text.config(width=30)
    text.config(height=5)
    text.insert(tkinter.INSERT, "salasanat")
    text.config(state='disabled')
    text.pack()
    return text

top = tkinter.Tk()
top.geometry("500x200")

pituus = MakeEntry(top, "Salasanan pituus: ", 3, DefValue="10")
pituus.bind("<Return>", NapinPainallus)
maara = MakeEntry(top, "Salasanojen maara: ", 3, DefValue="5")
maara.bind("<Return>", NapinPainallus)




#nappi = tkinter.Button( top, text="paina nappia", command = NapinPainallus )
#nappi.bind("<Return>", NapinPainallus)
#teksti = tkinter.Message( top, width=200, text=Salasana_Listaus())


#teksti.pack()
#teksti.place(x=10, y=20)
#nappi.place(x=20, y=150)
teksti = TextField(top)
#nappi.pack()
top.mainloop()
