# library
import tkinter as tk
from PIL import Image,ImageTk
from tkinter import messagebox
# constant

SCREEN_WIDTH = 1536
SCREEN_HEIGHT = 864
root =  tk.Tk()
root.title("Shinobi Run")
root.geometry(str(SCREEN_WIDTH) +"x"+ str(SCREEN_HEIGHT))
frame = tk.Frame(root,width=SCREEN_WIDTH,height=SCREEN_HEIGHT)
# create canvas
canvas = tk.Canvas(frame,width=SCREEN_WIDTH,height=SCREEN_HEIGHT)
# Background
img = Image.open("Image/10.png")
bg = ImageTk.PhotoImage(img)
Background = canvas.create_image(0,0,image=bg,anchor="nw")
canvas.create_text(750,250,text="Shinobi Run",font=('Metal Mania',80))
btn1 = tk.Button(canvas, text = 'New game',font=('Metal Mania',20),command = root.destroy)
btn1.place(x=700,y=300)
btn = tk.Button(canvas, text = 'Exit',font=('Metal Mania',20),)
btn.place(x=725,y=400)
frame.pack(expand=True, fill='both')
canvas.pack(expand=True, fill='both')
root.mainloop()