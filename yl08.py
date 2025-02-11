#Marcus Krutto 08.02.25 ; 11.02.25
#Tkinter yl 08

#Import
import os
import tkinter as tk
from tkinter import filedialog
from pathlib import Path
from PIL import Image, ImageOps

#Avamine
def open_directory():
    directory = filedialog.askopenfile()
    if directory:
        dir_label.config(text=f"Valitud kaust: {directory}")
    else:
        dir_label.config(text="Kausta ei valitud.")


#Salvestamine
def save_image():
    pass


aken = tk.Tk()
aken.title("pildi suuruse muutmine")
aken.geometry("450x400")
aken.resizable(False, False)

label = tk.Label(aken, text="Pildi suurus 200x200", font=("Arial", 16, "bold"))
label.pack(pady=10)

inputtxt = tk.Text(aken, height=10, width=50)
inputtxt.pack(pady=10)

open_button = tk.Button(aken, text="Ava pilt", command=open_directory)
open_button.pack(pady=10)

save_button = tk.Button(aken, text="Salvesta pilt", command=save_image)
save_button.pack(pady=10)

dir_label = tk.Label(aken, text="")
dir_label.pack(pady=10)


aken.mainloop()