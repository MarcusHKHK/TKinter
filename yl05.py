#Marcus Krutto 05.02.25
#Tkinter yl 3

import tkinter as tk

def main():
    aken = tk.Tk()
    aken.geometry("300x150")
    aken.resizable(False, False)

    def igakuine_makse():
        laensum = int(sisestus1.get())
        kuuineintress = float(sisestus2.get())/12/100
        maksete_arv = int(sisestus3.get())*12
        laenvastus = tk.Label(aken, text=f"Igakuinemakse:  {laensum * kuuineintress / (1 - (1 + kuuineintress) ** -maksete_arv):.2f}")
        laenvastus.pack()
        
    #Raamid
    frame = tk.Frame(aken)
    frame.pack(pady=5, padx=5, fill="x")
    frame2 = tk.Frame(aken)
    frame2.pack(pady=5, padx=5, fill="x")
    frame3 = tk.Frame(aken)
    frame3.pack(pady=5, padx=5, fill="x")

    # Esimene sisestusväli
    label1 = tk.Label(frame, text="Laenusumma (€): ", font=("Arial", 10, "bold"), fg="black").pack(side="left")
    sisestus1 = tk.Entry(frame)
    sisestus1.pack(side='left', fill="x", expand="true")
    # Teine sisestusväli
    label2 = tk.Label(frame2, text="Aastane intressimäär (%)", font=("Arial", 10, "bold"), fg="black").pack(side="left")
    sisestus2 = tk.Entry(frame2)
    sisestus2.pack(side='left', fill="x", expand="true")
    # Kolmas sisestusväli
    label3 = tk.Label(frame3, text="Laenuperiood (aastates)", font=("Arial", 10, "bold"), fg="black").pack(side="left")
    sisestus3 = tk.Entry(frame3)
    sisestus3.pack(side='left', fill="x", expand="true")
    # Nupp, mis käivitab funktsiooni kuva_sisestus
    nupp = tk.Button(aken, text="Arvuta", command=igakuine_makse)
    nupp.pack()

    aken.mainloop()

if __name__ == "__main__":
    main()