#Marcus Krutto 08.02.25 ; 11.02.25
#Tkinter yl 08

#Import
import os
import tkinter as tk
from tkinter import filedialog
from pathlib import Path
from PIL import Image, ImageOps

selected_files = []

#Avamine
def open_directory():
    directory = filedialog.askdirectory()
    dir_label.config(text=f"Valitud kaust: {directory}")
    kausta_sisu = os.listdir(directory)
    for fail in kausta_sisu:
        file_name, file_extension = os.path.splitext(fail)
        if file_extension == ".jpg":
            inputtxt.insert(tk.INSERT, fail+"\n")
            selected_files.append(os.path.join(directory, fail))
        if file_extension == ".jpeg":
            inputtxt.insert(tk.INSERT, fail+"\n")  
            selected_files.append(os.path.join(directory, fail))
        print(selected_files)

#Salvestamine
def save_image():
    save_directory = filedialog.askdirectory()
    for file in selected_files:
        img = Image.open(file)
        img = img.resize((200,200))
        filename = os.path.basename(file)
        img.save(os.path.join(save_directory, filename))


aken = tk.Tk()
aken.title("pildi suuruse muutmine")
aken.geometry("450x400")
aken.resizable(False, False)

label = tk.Label(aken, text="Pildi suurus 200x200", font=("Arial", 24, "bold"))
label.pack(pady=10)

inputtxt = tk.Text(aken, height=10, width=50)
inputtxt.pack(pady=10)

open_button = tk.Button(aken, text="Ava kaust", command=open_directory)
open_button.pack(pady=10)

save_button = tk.Button(aken, text="Salvesta pilt", command=save_image)
save_button.pack(pady=10)

dir_label = tk.Label(aken, text="")
dir_label.pack(pady=10)


aken.mainloop()