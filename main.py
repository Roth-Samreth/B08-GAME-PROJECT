# library
import tkinter as tk
from PIL import Image,ImageTk

# constant

SCREEN_WIDTH = 600
SCREEN_HIEGHT = 900
HEALTH = 100
health = ""
# functions
def healthcheck():
    global health
    health = str(HEALTH)
# window

root =  tk.Tk()
root.title("Shinobi Run")
root.geometry(str(SCREEN_WIDTH) +"x"+ str(SCREEN_HIEGHT))
frame = tk.Frame(root,width=SCREEN_WIDTH,height=SCREEN_HIEGHT)
# background
background = Image.open('Image/10.png')
bg = ImageTk.PhotoImage(background)
canvas = tk.Canvas(frame,width=SCREEN_WIDTH,height=SCREEN_HIEGHT)
canvas.create_image(0,200,image=bg)
canvas.create_text(100,10,text= "HEALTH "+str(HEALTH))
frame.pack(expand=True, fill='both')
canvas.pack(expand=True, fill='both')
root.mainloop()