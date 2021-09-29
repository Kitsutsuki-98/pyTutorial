import tkinter as tk   

window = tk.Tk()

UserInput = tk.Entry(
	fg="black",
	bg="white",
    width=40
)

UserInput.pack()
UserInput.insert("0", "What is your name?")

window.mainloop()


