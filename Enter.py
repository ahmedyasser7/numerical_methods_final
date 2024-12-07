import sympy as sp  # type: ignore
import numpy as np  # type: ignore
import customtkinter as ctk  # type: ignore
from PIL import Image

main = ctk.CTk()
main.title("Lazy GUI")
Font = ('Helvetica', 20, 'bold')
main.configure(bg="#03045e")

main.geometry("600x600")

welcome_label = ctk.CTkLabel(main, text="Hmmm, A Lazy Project!", font=("Helvetica", 24))

welcome_label.pack(pady=20)

my_image = ctk.CTkImage(dark_image=Image.open("coala.jpg"), size=(350, 250))

image_label = ctk.CTkLabel(main, image=my_image, text="")
def Go():
    print(r"Let's Go!")
    main.destroy()
    import Lazy_GUI
    


TheLabel = ctk.CTkLabel(
    main, text= "Hello, and welcome to our Numerical Methods Lazy GUI!\nLet's explore and see what's inside!\n may be, we can get the full mark!")


button1 = ctk.CTkButton(main, text="Let's GO", command=Go)
image_label.pack()
TheLabel.pack(pady=12, padx=10)
button1.pack(pady=10, padx=10)

main.mainloop()