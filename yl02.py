#Marcus Krutto 04.02.25
#Tkinter


#import

import tkinter as tk
from PIL import Image, ImageTk

#pilt

def kuva_pilt(aken, failinimi, laius, korgus):
    pilt = Image.open(failinimi)
    pilt = pilt.crop((0, 0, laius, korgus))
    foto = ImageTk.PhotoImage(pilt)
    label = tk.Label(aken, image=foto)
    label.image = foto
    label.pack()

#Tekst

def loe_fail(failinimi):
    with open(failinimi, 'r', encoding='utf-8') as file:
        return file.read()
#Window

def main():
    # DPI teadlikkuse seadistamine kõrge DPI ekraanide jaoks
    
    aken = tk.Tk()
    aken.title("Marcus")
    aken.geometry("500x700")
    aken.resizable(False, False)
   
    #Silt 
    label = tk.Label(aken, text="Chuck Norris", font=("Arial", 16, "bold"), fg="blue").pack()
    #Pilt
    kuva_pilt(aken,  "norris.png", 200, 200)
    #Tekst
    tekst = tk.Text(aken, wrap=tk.WORD, font=("Arial", 12), fg="black")
    scrollbar = tk.Scrollbar(aken, command=tekst.yview)
    tekst.config(yscrollcommand=scrollbar.set)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    tekst.pack(expand=True, fill=tk.BOTH)

    failisisu = loe_fail("DefNotJokes.txt")
    tekst.insert(tk.INSERT, failisisu)
   
    aken.mainloop()

if __name__ == "__main__":
    main()