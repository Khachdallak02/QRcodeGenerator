import time
import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk
import PIL
from QR import *
buf = simple_qr_code("test")
# Create the main window
window = tk.Tk()
window.geometry("800x400+100+100")
window.title("QR Code Generator")

# Create a label and an input field for the message
message_label = tk.Label(text="Link:")
message_entry = tk.Entry()


def run():
    message = message_entry.get()
    buf = simple_qr_code(message)
    tk.Label(text="QR code saved to qr_code.png").pack()
    image = PIL.Image.open(buf)
    qr_code_image = ImageTk.PhotoImage(image=image)
    image_label = tk.Label(image=qr_code_image)
    image_label.pack()


generate_button = tk.Button(text="Generate QR Code", command=run)

message_label.pack()
message_entry.pack()

generate_button.pack()
image = PIL.Image.open(buf)
qr_code_image = ImageTk.PhotoImage(image=image)
image_label = tk.Label(image=qr_code_image)
image_label.pack()

window.mainloop()
