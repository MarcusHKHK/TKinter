#Marcus Krutto 06.02.25
#Yl 06

import tkinter as tk

aken = tk.Tk()
aken.geometry("400x300")
font = "Arial 10"
padx = 5
pady = 5

nupp_00 = tk.Button(aken, text="wanna be pilt", font=font, bg="silver")
nupp_00.grid(row=1, column=0, rowspan=5, columnspan=2, padx=padx, pady=pady, sticky="nsew")

nupp_02 = tk.Label(aken, text="Palun sisestage oma andmed:", font=font)
nupp_02.grid(row=0, column=2, columnspan=3, padx=padx, pady=pady, sticky="nsew")

nupp_12 = tk.Button(aken, text="Nupp 1,2", font=font)
nupp_12.grid(row=1, column=2, padx=padx, pady=pady, sticky="nsew")

salvesta = tk.Button(aken, text="Salvesta", font=font)
salvesta.grid(row=5, column=2, padx=padx, pady=pady, sticky="nsew")

#Sildid
label = tk.Label(aken, text="Palun sisestage oma andmed:", font=font)
label.grid(row=0, column=2, columnspan=3, padx=padx, pady=pady, sticky="nsew")

nimi = tk.Label(aken, text="Nimi", font=font)
nimi.grid(row=1, column=2, padx=padx, pady=pady, sticky="nsew")

silmad = tk.Label(aken, text="Silmade värv", font=font)
silmad.grid(row=2, column=2, padx=padx, pady=pady, sticky="nsew")

pikkus = tk.Label(aken, text="Pikkus", font=font)
pikkus.grid(row=3, column=2, padx=padx, pady=pady, sticky="nsew")

kaal = tk.Label(aken, text="Kaal", font=font)
kaal.grid(row=4, column=2, padx=padx, pady=pady, sticky="nsew")

pikkuscm = tk.Label(aken, text="cm", font=font)
pikkuscm.grid(row=3, column=4, padx=padx, pady=pady, sticky="nsew")

kaalkg = tk.Label(aken, text="kg", font=font)
kaalkg.grid(row=4, column=4, padx=padx, pady=pady, sticky="nsew")

#Sisestus
sisestus1 = tk.Entry(aken)
sisestus1.grid(row=4, column=3, padx=padx, pady=pady, sticky="nsew")

sisestus1 = tk.Entry(aken)
sisestus1.grid(row=3, column=3, padx=padx, pady=pady, sticky="nsew")

sisestus1 = tk.Entry(aken)
sisestus1.grid(row=2, column=3, padx=padx, pady=pady, sticky="nsew")

sisestus1 = tk.Entry(aken)
sisestus1.grid(row=1, column=3, padx=padx, pady=pady, sticky="nsew")


# Nuppude seadistamine
# aken.grid_rowconfigure(0, weight=1)
# aken.grid_rowconfigure(1, weight=1)
# aken.grid_rowconfigure(2, weight=1)
# aken.grid_rowconfigure(3, weight=1)
# aken.grid_rowconfigure(4, weight=1)
# aken.grid_rowconfigure(6, weight=1)
aken.grid_columnconfigure(0, weight=1)
# aken.grid_columnconfigure(1, weight=1)
# aken.grid_columnconfigure(2, weight=1)
# aken.grid_columnconfigure(3, weight=1)
# aken.grid_columnconfigure(4, weight=1)

aken.mainloop()