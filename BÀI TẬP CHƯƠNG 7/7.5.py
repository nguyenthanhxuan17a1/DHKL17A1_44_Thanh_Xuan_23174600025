import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
window.title("Ảnh")
image = Image.open(r"D:\BÀI TẬP\BÀI TẬP CHƯƠNG 7\oto.jpg")
new_size = (500,500)
image = image.resize(new_size, Image.Resampling.LANCZOS)
img = ImageTk.PhotoImage(image)
label = tk.Label(window, image=img)
label.image = img 
label.pack()

window.mainloop()