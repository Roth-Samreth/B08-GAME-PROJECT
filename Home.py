# ____________________Import library
from tkinter import *
from PIL import Image,ImageTk
import winsound

# ___________________Constant
SCREENWIDTH = 1150
SCREENHEIGHT = 600
GRAVITY_FORCE = 30
SPEED = 7
TIMED_LOOP = 10
JUMP_FORCE = 30

# Variable
keyPressed = []
x = 20
y = 430
k = 2
result =  0
# ____________________Create window
root = Tk()
root.geometry(str(SCREENWIDTH)+"x"+str(SCREENHEIGHT))
root.title("Shinobi Run")
canvas = Canvas(root,width= SCREENWIDTH,height=SCREENHEIGHT)
# Load image
bg = Image.open("Image/10.png")
pp = Image.open("Image/Run1.png")
en = Image.open("Image/Fighter.png")
tile = Image.open("Image/Tile_01.png")

# Converting Image
back = ImageTk.PhotoImage(bg)
user = ImageTk.PhotoImage(pp)
oppose = ImageTk.PhotoImage(en)
tile_1 = ImageTk.PhotoImage(tile)
img2 = ImageTk.PhotoImage(Image.open("Image/Run2.png"))
img3 = ImageTk.PhotoImage(Image.open("Image/Run3.png"))
img4 = ImageTk.PhotoImage(Image.open("Image/Run4.png"))
img5 = ImageTk.PhotoImage(Image.open("Image/Run5.png"))
img6 = ImageTk.PhotoImage(Image.open("Image/Run6.png"))
img7 = ImageTk.PhotoImage(Image.open("Image/Run7.png"))
img8 = ImageTk.PhotoImage(Image.open("Image/Run8.png"))
# Put the Background
backGround = canvas.create_image(0,0,image=back)
# Functions
def create_platform(x,y,row,col):
    X = x
    Y = y
    global tiles
    for j in range(row):
        for i in range(col):
            tiles = canvas.create_image(X, Y, image=tile_1, tag='PLATFORM')
            X += 30
        X = x
        Y += 30
def check_movement(dx=0, dy=0, checkGround=False):
    global player
    coord = canvas.bbox(player)
    platforms = canvas.find_withtag("PLATFORM")

    if coord[0] + dx < 0 or coord[2] + dx > SCREENWIDTH:
        return False

    if checkGround:
        overlap = canvas.find_overlapping(coord[0], coord[1], coord[2], coord[3] + dy)
    else:
        overlap = canvas.find_overlapping(coord[0]+dx, coord[1]+dy, coord[2]+dx, coord[3])

    for platform in platforms:
        if platform in overlap:
            return False

    return True
def jumpsound():
    winsound.PlaySound("sound/Jump.wav", winsound.SND_ASYNC)
def startGame():
    winsound.PlaySound("sound/yo.wav", winsound.SND_ASYNC)
def death():
    global tiles
    canvas.delete('tiles')
    winsound.PlaySound("sound/Hurt.wav", winsound.SND_PURGE)
    canvas.create_text(580, 200, text="You Died", font=("Metal Mania", 50), fill="red")
def change():
    global k
    if k == 8:
        k=2
    if k == 2:
        canvas.itemconfig(player,image=img2)
    elif k == 3:
        canvas.itemconfig(player,image=img3)
    elif k == 4:
        canvas.itemconfig(player,image=img4)
    elif k == 5:
        canvas.itemconfig(player,image=img5)
    elif k == 6:
        canvas.itemconfig(player,image=img6)
    elif k == 7:
        canvas.itemconfig(player,image=img7)
    elif k == 8:
        canvas.itemconfig(player,image=img8)
    k+=1
    root.after(200,change)
def jump(force):
    if force > 0:
        if check_movement(0, -force):
            canvas.move(player, 0, -force)
        root.after(TIMED_LOOP, jump, force-1)
def move():
    global player
    if not keyPressed == []:
        x = 0
        if "Left" in keyPressed:
            x -= SPEED
        if "Right" in keyPressed:
            x += SPEED
            change()
        if "space" in keyPressed and not check_movement(0, GRAVITY_FORCE, True):
            jump(JUMP_FORCE)
            jumpsound()
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

def gravity():
    global tiles
    if check_movement(0, GRAVITY_FORCE, True):
        canvas.move(player, 0, GRAVITY_FORCE)
        if canvas.bbox(player)[3] > 600:
            checkGround = False
            if checkGround == False:
                death()
    root.after(TIMED_LOOP, gravity)
def level_1():
    global backGround,player
    canvas.delete("all")
    btn.destroy()
    exitBtn.destroy()
    startGame()
    backGround = canvas.create_image(0,0,image=back)
    player = canvas.create_image(30, 340, image=user)
    create_platform(20, 400, 5, 8)
    create_platform(340, 300, 4, 8)
    create_platform(650, 400, 1, 4)
    create_platform(800, 560, 2, 8)
    gravity()

# Game Start Screen
title = canvas.create_text(580,200,text="Shinobi Run",font=("Metal Mania",50),fill="white")
# Button
btn = Button(text="Newgame",font=("Metal Mania",15),command=level_1)
exitBtn = Button(text="Exit",font=("Metal Mania",15),command=root.destroy)
btn.place(x=530,y=300)
exitBtn.place(x=550,y=380)
canvas.pack(expand = True,fill='both')
root.bind("<Key>", start_move)
root.bind("<KeyRelease>", stop_move)
root.mainloop()