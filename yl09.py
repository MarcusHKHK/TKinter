#Marcus Krutto 12.2.25 ; Tkinter harjutus 9

# Import
import tkinter as tk

# Window conf
aken = tk.Tk()
aken.geometry("250x400")
aken.title("Pitsa")

# Funktsiooid
def show_selection():
    print("Valitud suurus:", selected_size.get())

# StringVar, mis hoiab valitud värvi nime
selected_size = tk.StringVar(value=5)

# Suuruse valikud
pitsa_v = tk.Radiobutton(aken, text="Väike (5€)", variable=selected_size, value=5)
pitsa_s = tk.Radiobutton(aken, text="Suur (8€)", variable=selected_size, value=8)
pitsa_p = tk.Radiobutton(aken, text="Pere (12€)", variable=selected_size, value=12)
pitsa_v.pack()
pitsa_s.pack()
pitsa_p.pack()

btn_confirm = tk.Button(aken, text="Kinnita valik", command=show_selection)
btn_confirm.pack()

var1 = tk.IntVar(value=0)
var2 = tk.IntVar(value=0)
var3 = tk.IntVar(value=0)

# Lisandite valikud
checkbox1 = tk.Checkbutton(aken, text="+ 1€", variable=var1, onvalue=1, offvalue=0)
checkbox2 = tk.Checkbutton(aken, text="+ 1.50€", variable=var2, onvalue=15, offvalue=0)
checkbox3 = tk.Checkbutton(aken, text="+ 1€", variable=var3, onvalue=1, offvalue=0)
checkbox1.pack()
checkbox2.pack()
checkbox3.pack()

btn_show = tk.Button(aken, text="Näita valikut", command=show_selection)
btn_show.pack()

aken.mainloop()
