#Marcus Krutto 06.02.25
#Tkinter yl 07

import tkinter as tk



def valideeriTeksti(*args):
    text = entry_var.get()
    if len(text) == 11:
        sugunr = int(text[0])
        if sugunr %2==0:
            sugu = "naine"
        else:
            sugu = "mees"
        synna = f"{text[5]}{text[6]}.{text[3]}{text[4]}.{text[1]}{text[2]}"
        validation_label.config(text=f"Sugu: {sugu}\nSünnipäev: {synna}", fg="green")
    else:
        validation_label.config(text="Sisesta isikukood vähemalt 11 tähemärki!", fg="red")

aken = tk.Tk()
aken.title("Validaator")
aken.geometry("300x200")

label = tk.Label(aken, text="Isikukood", font=("Arial", 16, "bold"), fg="black").pack()


entry_var = tk.StringVar()
entry_var.trace_add("write", valideeriTeksti)

entry = tk.Entry(aken, textvariable=entry_var)
entry.pack()

validation_label = tk.Label(aken, text="Sisesta isikukood vähemalt 11 tähemärki!", fg="red")
validation_label.pack()

aken.mainloop()