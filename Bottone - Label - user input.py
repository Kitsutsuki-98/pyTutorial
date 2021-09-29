import tkinter as tk

finestra = tk.Tk()

greeting = tk.Label(
    text="Ciao Cazzoni",
    fg="white", #foreground
    bg="black", #background
    width=10,
    height=10
)

button = tk.Button(
    text="Premi il Bottone",
    width=25,
    height=5,
    bg="yellow",
    fg="black",
)

UserInput = tk.Entry(
	fg="yellow",
	bg="blue",
	width=50,	
)


UserInput.pack()
button.pack()
greeting.pack()

finestra.mainloop()


