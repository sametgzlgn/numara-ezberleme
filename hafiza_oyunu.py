import tkinter as tk
import threading
import time
import random

seviye = 4
can = 3
sekans = ""
dogru = 0

def kaybetme_kosullari():
    global can,canlbl
    canlbl["text"] = "Can:" +str(can)
    if can < 1:
        exit()

def yeni_sekans():
    global sayilbl,sekans,seviye,gonderbtn,cevap
    cevap["state"] = tk.DISABLED
    gonderbtn["state"] = tk.DISABLED
    sekans = str(random.randint(10**seviye,10**(seviye + 1) - 1))
    for i in sekans:
        sayilbl["text"] = i
        time.sleep(1)
        sayilbl["text"] = ""
        time.sleep(0.5)
    
    gonderbtn["state"] = tk.ACTIVE
    cevap["state"] = tk.NORMAL

def gonder():
    global sekans,cevap,dogru,dogrulbl,can,seviye
    thr2 = threading.Thread(target=yeni_sekans)
    if cevap.get() == sekans:
        dogru += 1
        dogrulbl["text"] = "Doğru: "+str(dogru)
        seviye += 1
        cevap.delete(0,len(cevap.get()))
        thr2.start()
    else:
        can -= 1
        seviye -= 1
        cevap.delete(0,len(cevap.get()))
        thr2.start()
    kaybetme_kosullari()

pencere = tk.Tk()
pencere.title("Hafıza Oyunu")
pencere.geometry(("400x300"))
pencere.resizable(False,False)
sayilbl = tk.Label(text="",font=("Ariel",70))
sayilbl.pack()
cevap = tk.Entry()
cevap.place(x=120,y=200)
gonderbtn = tk.Button(text="Gönder",command=gonder)
gonderbtn.place(x=165,y=230)
canlbl = tk.Label(text="Can: {}".format(can))
canlbl.place(x=20,y=280)
dogrulbl = tk.Label(text="Doğru: {}".format(dogru))
dogrulbl.place(x=320,y=280)
thr = threading.Thread(target=yeni_sekans)
thr.start()

pencere.mainloop()
