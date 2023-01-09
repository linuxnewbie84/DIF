import tkinter as tk

class App:
    def __init__(self):
        self.vent=tk.Tk()
        self.vent.title("Sistema de pago")
        self.label=tk.Label(self.vent, text="Ingresa la Poliza")
        self.label.grid(column=0, row=1)
        self.dato1=tk.StringVar()
        self.entrada=tk.Entry(self.vent, width=15, textvariable=self.dato1)
        self.entrada.grid(column=0, row=2)
        self.vent.mainloop()
app = App()