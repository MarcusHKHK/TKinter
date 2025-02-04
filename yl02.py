#Marcus Krutto 04.02.25
#Tkinter


#import

import tkinter as tk

#Window
def main():
    # DPI teadlikkuse seadistamine kõrge DPI ekraanide jaoks
    
    aken = tk.Tk()
    aken.title("Marcus")
    aken.geometry("400x400")
    aken.resizable(True, False)
   
    label = tk.Label(aken, text="Chuck Norris", font=("Arial", 16, "bold"), fg="blue").pack()
    
   
    aken.mainloop()

if __name__ == "__main__":
    main()