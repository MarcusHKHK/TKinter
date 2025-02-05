#Marcus Krutto 05.02.25
#Tkinter yl 3

import tkinter as tk

def main():
    aken = tk.Tk()
    aken.geometry("400x350")
    aken.resizable(False, False)

    def igakuine_makse():
        laensum = int(sisestus1.get())
        kuuineintress = float(sisestus2.get())/12/100
        maksete_arv = int(sisestus3.get())*12
        laenvastus = tk.Label(aken, text=f"Igakuinemakse:  {laensum * kuuineintress / (1 - (1 + kuuineintress) ** -maksete_arv):.2f}")
        laenvastus.pack()
        
    #Raamid
    frame = tk.Frame(aken)
    frame.pack(pady=5, padx=5)
    frame2 = tk.Frame(aken)
    frame2.pack(pady=5, padx=5)
    frame3 = tk.Frame(aken)
    frame3.pack(pady=5, padx=5)

    # Esimene sisestusväli
    label = tk.Label(aken, text="Laenu summa (€)", font=("Arial", 10, "bold"), fg="black").pack()
    sisestus1 = tk.Entry(frame)
    sisestus1.pack(pady=20)
    # Teine sisestusväli
    label = tk.Label(aken, text="Aastane intressimäär (%)", font=("Arial", 10, "bold"), fg="black").pack()
    sisestus2 = tk.Entry(aken)
    sisestus2.pack(pady=20)
    # Kolmas sisestusväli
    label = tk.Label(aken, text="Laenuperiood (aastates)", font=("Arial", 10, "bold"), fg="black").pack()
    sisestus3 = tk.Entry(aken)
    sisestus3.pack(pady=20)
    # Nupp, mis käivitab funktsiooni kuva_sisestus
    nupp = tk.Button(aken, text="Arvuta", command=igakuine_makse)
    nupp.pack()

    aken.mainloop()

if __name__ == "__main__":
    main()