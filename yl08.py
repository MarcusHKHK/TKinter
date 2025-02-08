#Marcus Krutto 08.02.25
#Tkinter yl 08

import tkinter as tk
from tkinter import filedialog
from pathlib import Path

# Kasutajaliides sisaldab järgnevaid elemente:
# Silt (label), mis annab teavet programmi funktsionaalsuse kohta
# Tekstiväli (text field), mis kuvab teavet selle kohta, mida programmiga teha saab
# Nupp “Vali failid”
# Nupule vajutades avaneb failivaliku dialoog, mis lubab valida ainult JPG ja JPEG failitüüpe.
# Valitud failide nimed kuvatakse tekstiväljal eraldi ridadel.
# Taga, et kasutajal pole võimalik valida sama faili uuesti, et vältida topelttöötlust.
# Nupp “Salvesta pildid”
# Nupule vajutades avaneb kausta valiku dialoog, kuhu saab salvestada töödeldud pildid
# Töödeldakse tekstiväljale lisatud failide alusel ja iga pildi suurus muudetakse 200×200 piksliks enne salvestamist
# Valitud pildid salvestatakse määratud kausta pärast nende suuruse muutmist image.save(path/filename)


def open_directory():
    directory = filedialog.askdirectory()
    if directory:
        dir_label.config(text=f"Valitud kaust: {directory}")
    else:
        dir_label.config(text="Kausta ei valitud.")

aken = tk.Tk()
aken.title("Peamine aken")
aken.geometry("450x400")
aken.resizable(False, False)

open_button = tk.Button(aken, text="Ava pilt", command=open_directory)
open_button.pack(pady=10)

dir_label = tk.Label(aken, text="tere")
dir_label.pack(pady=10)

aken.mainloop()