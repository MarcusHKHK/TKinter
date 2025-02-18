#Marcus Krutto 12.2.25 ; Tkinter harjutus 9

# Import
import tkinter as tk

# Window conf
aken = tk.Tk()
aken.geometry("250x400")
aken.title("Pitsa")



# Funktsiooid
def show_selection():
    # print("hind", selected_size.get())
    # print(var1.get(), float(var2.get()), var3.get())
    # print(selected_option.get())
    if selected_option.get()=="Kuller":
        trans = 3
    else:
        trans = 0
    summa = selected_size.get() + var1.get() + float(var2.get()) + var3.get() + trans
    print(summa)

#Kasutaja ID
label = tk.Label(aken, text="Kasutaja ID:").pack(pady=(10, 0))
tk.Entry(aken).pack()

# StringVar, mis hoiab valitud värvi nime
selected_size = tk.StringVar(value=5)

label = tk.Label(aken, text="Vali suurus (hind):").pack()


# Suuruse valikud
pitsa_v = tk.Radiobutton(aken, text="Väike (5€)", variable=selected_size, value=5)
pitsa_s = tk.Radiobutton(aken, text="Suur (8€)", variable=selected_size, value=8)
pitsa_p = tk.Radiobutton(aken, text="Pere (12€)", variable=selected_size, value=12)
pitsa_v.pack()
pitsa_s.pack()
pitsa_p.pack()

var1 = tk.IntVar(value=0)
var2 = tk.StringVar(value=0)
var3 = tk.IntVar(value=0)
tk.Label(aken, text="Vali lisandid", font="Arial 16").pack(pady=(10, 0))
# Checkboxes
checkbox1 = tk.Checkbutton(aken, text="Juust (+1€)", variable=var1, onvalue=1, offvalue=0)
checkbox2 = tk.Checkbutton(aken, text="Pepperoni (+1.5€)", variable=var2, onvalue="1.5", offvalue=0)
checkbox3 = tk.Checkbutton(aken, text="Seen (+1€)", variable=var3, onvalue=1, offvalue=0)
checkbox1.pack()
checkbox2.pack()
checkbox3.pack()

#Kättetoimetamine
label = tk.Label(aken, text="Vali kättetoimetamine (hind):").pack()
#Dropdown
valikud = ["Kuller", "Kohapeal"]
selected_option = tk.StringVar()
selected_option.set("Vali teenus")

dropdown = tk.OptionMenu(aken, selected_option, *valikud)
dropdown.pack()

btn_confirm = tk.Button(aken, text="Arvuta hind", command=show_selection)
btn_confirm.pack()

aken.mainloop()
