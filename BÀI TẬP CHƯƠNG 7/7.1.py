import tkinter as tk
window = tk.Tk()
window.geometry("350x80")
window.title("Good Morning")

label = tk.Label(window,text="Hello")
label.pack()
window.mainloop()