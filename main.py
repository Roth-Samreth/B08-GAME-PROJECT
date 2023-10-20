# library
from tkinter import *
from PIL import Image,ImageTk

# constant

SCREEN_WIDTH = 1536
SCREEN_HEIGHT = 864
HEALTH = 100
health = ""
TIMELOOP = 10
GRAVITY_FORCE = 9
JUMP_FORCE = 30
SPEED = 7

TIMED_LOOP = 10
# Variable
keyPressed = []

# functions
def check_movement(dx=0, dy=0, checkGround=False):
    coord = canvas.coords(player)
    platforms = canvas.find_withtag("PLATFORM")

    if coord[0] + dx < 0 or coord[0] + dx > SCREEN_WIDTH:
        return False

    if checkGround:
        overlap = canvas.find_overlapping(coord[0], coord[1], coord[0], coord[1] + dy)
    else:
        overlap = canvas.find_overlapping(coord[0]+dx, coord[1], coord[0], coord[1]+dy)

    for platform in platforms:
        if platform in overlap:
            return False

    return True
def jump(force):
    if force > 0:
        if check_movement(0, -force):
            canvas.move(player, 0, -force)
            root.after(TIMED_LOOP, jump, force-1)

def gravity():
    if check_movement(0, GRAVITY_FORCE, True):
        canvas.move(player, 0, GRAVITY_FORCE)
    root.after(TIMED_LOOP, gravity)

def move():
    if not keyPressed == []:
        x = 0
        if "Left" in keyPressed:
            x -= SPEED
        if "Right" in keyPressed:
            x += SPEED
        if "space" in keyPressed and not check_movement(0, GRAVITY_FORCE, True):
            jump(JUMP_FORCE)
        if check_movement(x):
            canvas.move(player, x, 0)
        root.after(TIMED_LOOP, move)
def start_move(event):
    if event.keysym not in keyPressed:
        keyPressed.append(event.keysym)
        if len(keyPressed) == 1:
            move()

def stop_move(event):
    global keyPressed
    if event.keysym in keyPressed:
        keyPressed.remove(event.keysym)
# window

root = Tk()
root.title("Shinobi Run")
root.geometry(str(SCREEN_WIDTH) +"x"+ str(SCREEN_HEIGHT))
# create canvas
canvas = Canvas(root,width=SCREEN_WIDTH,height=SCREEN_HEIGHT)
# background
background = Image.open('./Image/10.png')
bg = ImageTk.PhotoImage(background)
Background = canvas.create_image(0,0,image=bg,anchor="nw")
# player
player_pho = Image.open('Image/Run1.png')
player_image = ImageTk.PhotoImage(player_pho)
player=canvas.create_image(100,700,image=player_image)
canvas.create_text(50,10,text= "HEALTH "+str(HEALTH))

# platform

canvas.create_rectangle(0, 800, SCREEN_WIDTH, SCREEN_HEIGHT, fill="black", tags="PLATFORM")
canvas.create_rectangle(200, 600, 500, 650, fill="black", tags="PLATFORM")
canvas.create_rectangle(600, 700, 650, 850, fill="black", tags="PLATFORM")
canvas.create_rectangle(800, 450, 1100, 500, fill="black", tags="PLATFORM")

canvas.pack(expand=True, fill='both')
gravity()
root.bind("<Key>", start_move)
root.bind("<KeyRelease>", stop_move)
root.mainloop()



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