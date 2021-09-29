import tkinter as tk
from tkinter.constants import LEFT   

window = tk.Tk()

lbl_Nome = tk.Label(
    master=window,
    text = "Nome:"
)

lbl_Cognome = tk.Label(
    master=window,
    text = "Cognome:"
)
lbl_Indirizzo1 = tk.Label(
    master=window,
    text = "Indirizzo 1:"
)
lbl_Indirizzo2 = tk.Label(
    master=window,
    text = "Indirizzo 2"
)
lbl_city = tk.Label(
    master=window,
    text = "Città:"
)
lbl_Stato_Provincia = tk.Label(
    master=window,
    text = "Regione/Provincia:"
)
lbl_Numero_Postale = tk.Label(
    master=window,
    text = "Numero Postale:"
)
lbl_Country = tk.Label(
    master=window,
    text = "Stato:"
)

lbl_Nome.pack(side="left")
lbl_Cognome.pack(side="bottom")
lbl_Indirizzo1.pack(side="bottom", side="left")
lbl_Indirizzo2.pack(side="left")
lbl_city.pack(side="left")
lbl_Stato_Provincia.pack(side="left")
lbl_Country.pack(side="left")


window.mainloop()
