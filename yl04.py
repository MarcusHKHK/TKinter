#Marcus Krutto 05.02.25
#Tkinter yl 4

import tkinter as tk



def main():
    aken = tk.Tk()
    aken.geometry("400x100")

    def kuva_varv(v):
        vastus.config(text=v)


    #Värvid
    nupp1 = tk.Button(bg="red", fg="red", font=("Arial", 16), command=lambda:kuva_varv("Punane"))
    nupp2 = tk.Button(bg="orange", fg="orange", font=("Arial", 16), command=lambda:kuva_varv("Oranž"))
    nupp3 = tk.Button(bg="yellow", fg="yellow", font=("Arial", 16), command=lambda:kuva_varv("Kollane"))
    nupp4 = tk.Button(bg="green", fg="green", font=("Arial", 16), command=lambda:kuva_varv("Roheline"))
    nupp5 = tk.Button(bg="blue", fg="blue", font=("Arial", 16), command=lambda:kuva_varv("Sinine"))
    vastus = tk.Label(aken, text="", justify="center", font=("Arial", 16))
    vastus.pack(side="bottom",padx=10, pady= 10)
    nupp1.pack(side="left", expand=True, fill="x")
    nupp2.pack(side="left", expand=True, fill="x")
    nupp3.pack(side="left", expand=True, fill="x")
    nupp4.pack(side="left", expand=True, fill="x")
    nupp5.pack(side="left", expand=True, fill="x")


    aken.mainloop()

if __name__ == "__main__":
    main()