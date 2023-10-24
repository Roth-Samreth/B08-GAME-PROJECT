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

GAMESTATUS_STAR = 0
GAMESTATUS_LEVEL_1 = 1
GAMESTATUS_MLEVEL_2 = 2
GAMESTATUS_LEVEL_3 = 3
GAMESTATUS_OVER = 4

# Variable
keyPressed = []
x = 20
y = 430
k = 2
speed = 5
direction = 1
# ____________________Create window
root = Tk()
root.geometry(str(SCREENWIDTH)+"x"+str(SCREENHEIGHT))
root.title("Shinobi Run")
canvas = Canvas(root,width= SCREENWIDTH,height=SCREENHEIGHT)
# Load image
bg = Image.open("Image/10.png")
pp = Image.open("Image/Run1.png")
en = Image.open("Image/enemy/e-boy-1.png")
tile = Image.open("Image/Tile_01.png")
coin = Image.open("Image/coin.png")

# Converting Image
back = ImageTk.PhotoImage(bg)
user = ImageTk.PhotoImage(pp)
oppose = ImageTk.PhotoImage(en)
tile_1 = ImageTk.PhotoImage(tile)
coin_1 = ImageTk.PhotoImage(coin)
# ___________________________________________Animation Images
# Player Forward________________________________________________________
img2 = ImageTk.PhotoImage(Image.open("Image/Run2.png"))
img3 = ImageTk.PhotoImage(Image.open("Image/Run3.png"))
img4 = ImageTk.PhotoImage(Image.open("Image/Run4.png"))
img5 = ImageTk.PhotoImage(Image.open("Image/Run5.png"))
img6 = ImageTk.PhotoImage(Image.open("Image/Run6.png"))
img7 = ImageTk.PhotoImage(Image.open("Image/Run7.png"))
img8 = ImageTk.PhotoImage(Image.open("Image/Run8.png"))

# Enemy Forward
img_e2 = ImageTk.PhotoImage(Image.open("Image/enemy/e-boy-2.png"))
img_e3 = ImageTk.PhotoImage(Image.open("Image/enemy/e-boy-3.png"))
img_e4 = ImageTk.PhotoImage(Image.open("Image/enemy/e-boy-4.png"))
img_e5 = ImageTk.PhotoImage(Image.open("Image/enemy/e-boy-5.png"))
img_e6 = ImageTk.PhotoImage(Image.open("Image/enemy/e-boy-6.png"))
img_e7 = ImageTk.PhotoImage(Image.open("Image/enemy/e-boy-7.png"))
img_e8 = ImageTk.PhotoImage(Image.open("Image/enemy/e-boy-8.png"))
# Player Backward________________________________________________________
img_b2 = ImageTk.PhotoImage(Image.open("runback/Run2.png"))
img_b3 = ImageTk.PhotoImage(Image.open("runback/Run3.png"))
img_b4 = ImageTk.PhotoImage(Image.open("runback/Run4.png"))
img_b5 = ImageTk.PhotoImage(Image.open("runback/Run5.png"))
img_b6 = ImageTk.PhotoImage(Image.open("runback/Run6.png"))
img_b7 = ImageTk.PhotoImage(Image.open("runback/Run7.png"))
img_b8 = ImageTk.PhotoImage(Image.open("runback/Run8.png"))
# Enemy Backward_________________________________________________________
img_eb2 = ImageTk.PhotoImage(Image.open("Image/enemy/re/e-boy-re-2.png"))
img_eb3 = ImageTk.PhotoImage(Image.open("Image/enemy/re/e-boy-re-3.png"))
img_eb4 = ImageTk.PhotoImage(Image.open("Image/enemy/re/e-boy-re-4.png"))
img_eb5 = ImageTk.PhotoImage(Image.open("Image/enemy/re/e-boy-re-5.png"))
img_eb6 = ImageTk.PhotoImage(Image.open("Image/enemy/re/e-boy-re-6.png"))
img_eb7 = ImageTk.PhotoImage(Image.open("Image/enemy/re/e-boy-re-7.png"))
img_eb8 = ImageTk.PhotoImage(Image.open("Image/enemy/re/e-boy-re-8.png"))
# Put the Background
backGround = canvas.create_image(0,0,image=back)
backGround = canvas.create_image(1150,0,image=back)
# Functions
# ______________Animation___________
# _______________Player_______________________________________________
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
def changeback():
    global k
    if k == 8:
        k=2
    if k == 2:
        canvas.itemconfig(player,image=img_b2)
    elif k == 3:
        canvas.itemconfig(player,image=img_b3)
    elif k == 4:
        canvas.itemconfig(player,image=img_b4)
    elif k == 5:
        canvas.itemconfig(player,image=img_b5)
    elif k == 6:
        canvas.itemconfig(player,image=img_b6)
    elif k == 7:
        canvas.itemconfig(player,image=img_b7)
    elif k == 8:
        canvas.itemconfig(player,image=img_b8)
    k+=1
# __________________Enemy-1_____________
def enemy_male():
    global k
    if k == 8:
        k=2
    if k == 2:
        canvas.itemconfig(enemy_males,image=img_e2)
    elif k == 3:
        canvas.itemconfig(enemy_males,image=img_e3)
    elif k == 4:
        canvas.itemconfig(enemy_males,image=img_e4)
    elif k == 5:
        canvas.itemconfig(enemy_males,image=img_e5)
    elif k == 6:
        canvas.itemconfig(enemy_males,image=img_e6)
    elif k == 7:
        canvas.itemconfig(enemy_males,image=img_e7)
    elif k == 8:
        canvas.itemconfig(enemy_males,image=img_e8)
    k+=1
def enemy_male_back():
    global k
    if k == 8:
        k=2
    if k == 2:
        canvas.itemconfig(enemy_males,image=img_eb2)
    elif k == 3:
        canvas.itemconfig(enemy_males,image=img_eb3)
    elif k == 4:
        canvas.itemconfig(enemy_males,image=img_eb4)
    elif k == 5:
        canvas.itemconfig(enemy_males,image=img_eb5)
    elif k == 6:
        canvas.itemconfig(enemy_males,image=img_eb6)
    elif k == 7:
        canvas.itemconfig(enemy_males,image=img_eb7)
    elif k == 8:
        canvas.itemconfig(enemy_males,image=img_eb8)
    k+=1

#     Moving enemy
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

# Coins Location
# @Author: Roth Samreth
def place_coint(x,y,row,col):
    X = x
    Y = y
    global coins
    for j in range(row):
        for i in range(col):
            coins = canvas.create_image(X, Y, image=coin_1,)
            X += 35
        X = x
        Y += 30
def check_collision(image1, image2):
    x1, y1, x2, y2 = canvas.bbox(image1)
    x3, y3, x4, y4 = canvas.bbox(image2)

    if (x1 < x4 and x2 > x3) and (y1 < y4 and y2 > y3):
        return True
    else:
        return False
    
def check_collision_loop_coin():
    if check_collision(player, coins):
        canvas.create_text(580, 200, text="You've won", font=("Metal Mania", 50), fill="white")
        winsound.PlaySound("sound/victory.wav", winsound.SND_ASYNC)
        canvas.delete(coins)
    else:
        root.after(10, check_collision_loop_coin)

def lost():
    global restart
    if check_collision(player, enemy_males):
        canvas.create_text(580, 200, text="You Died", font=("Metal Mania", 50), fill="red")
        canvas.move(player,0,500)
    else:
        root.after(10,lost)

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
    winsound.PlaySound("sound/Theme.wav", winsound.SND_ASYNC)

def death():
    global tiles
    canvas.delete('tiles')
    winsound.PlaySound("sound/Hurt.wav", winsound.SND_ASYNC)
    canvas.create_text(580, 200, text="You Died", font=("Metal Mania", 50), fill="red")
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
            changeback()
        if "Right" in keyPressed:
            x += SPEED
            change()
        if "space" in keyPressed and not check_movement(0, GRAVITY_FORCE, True):
            jump(JUMP_FORCE)
            # jumpsound()
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
# Define the animation function
def animate():
    global direction
    x, y = canvas.coords(enemy_males)
    if x + speed * direction > 550 or x + speed * direction < 340:
        direction = -direction
        canvas.move(enemy_males, speed * direction, 0)
        enemy_male_back()
    else:
        enemy_male()
        canvas.move(enemy_males, speed * direction, 0)
    root.after(100, animate)
def animate1():
    global direction
    x, y = canvas.coords(enemy_males)
    if x + speed * direction > 1080 or x + speed * direction < 1150:
        # Reverse the direction
        direction = -direction
        canvas.move(enemy_males, speed * direction, 0)
        enemy_male_back()
    else:
        enemy_male()
        canvas.move(enemy_males, speed * direction, 0)
    root.after(100, animate)
def gravity():
    global tiles
    if check_movement(0, GRAVITY_FORCE, True):
        canvas.move(player, 0, GRAVITY_FORCE)
        if canvas.bbox(player)[3] > 600:
            death()
    root.after(TIMED_LOOP, gravity)
def level_1():
    global backGround,player,coins,enemy_males,hid_rect
    canvas.delete("all")
    btn.destroy()
    exitBtn.destroy()
    level1_btn.destroy()
    level2_btn.destroy()
    level_btn.destroy()
    startGame()
    backGround = canvas.create_image(0,0,image=back)
    backGround = canvas.create_image(1150, 0, image=back)
    backGround = canvas.create_image(2000, 0, image=back)
    player = canvas.create_image(30, 340, image=user)
    create_platform(20, 400, 5, 8)
    # place_coint(80,340,1,5)
    create_platform(440, 150, 2, 2)
    create_platform(340, 300, 4, 8)
    create_platform(650, 400, 1, 4)
    create_platform(900, 560, 2, 7)
    create_platform(1000, 260, 1, 3)
    coins = canvas.create_image(900, 200, image=coin_1)
    enemy_males = canvas.create_image(340, 240, image=oppose, anchor="center")
    gravity()
    animate1()
    check_collision_loop_coin()
    lost()
def level_2():
    global backGround,player,coins,enemy_males
    canvas.delete("all")
    btn.destroy()
    exitBtn.destroy()
    level1_btn.destroy()
    level2_btn.destroy()
    level_btn.destroy()
    startGame()
    backGround = canvas.create_image(0,0,image=back)
    player = canvas.create_image(30, 350, image=user)
    coins = canvas.create_image(1080, 100, image=coin_1)
    enemy_males = canvas.create_image(500, 220, image=oppose, anchor="center")
    create_platform(20,500,5,6)
    create_platform(280,400,5,3)
    create_platform(440,280,2,4)
    create_platform(500,460,2,8)
    create_platform(770,360,4,2)
    create_platform(890,260,4,2)
    create_platform(950,480,2,6)
    create_platform(1020,150,2,5)
    gravity()
    check_collision_loop_coin()
    animate()
    lost()

def levelTable():
    global backGround,player,coins,enemy_males,level1_btn,level2_btn
    canvas.delete("all")
    btn.destroy()
    exitBtn.destroy()
    level_btn.destroy()
    startGame()
    backGround = canvas.create_image(0,0,image=back)
    level1_btn = Button(text="Level1", font=("Metal Mania", 15), command=level_1)
    level2_btn = Button(text="Level2", font=("Metal Mania", 15), command=level_2)
    level1_btn.place(x=530, y=370)
    level2_btn.place(x=630, y=370)
def Start():
    global backGround, player, coins, enemy_males, level1_btn, level2_btn
    canvas.delete("all")
    btn.destroy()
    exitBtn.destroy()
    startGame()
    backGround = canvas.create_image(0, 0, image=back)
    canvas.create_text(580, 200, text="Click To Start", font=("Metal Mania", 50), fill="red",tags="start_game")
# Game Start Screen
def getStatus():
    res = GAMESTATUS_LEVEL_1
    return res
title = canvas.create_text(580, 200, text="Shinobi Run", font=("Metal Mania", 50), fill="white")
winsound.PlaySound("sound/opening.wav", winsound.SND_ASYNC)
# Button
btn = Button(text="Newgame", font=("Metal Mania", 15), command=Start)
level_btn = Button(text="Level", font=("Metal Mania", 15), command=levelTable)
exitBtn = Button(text="Exit", font=("Metal Mania", 15), command=root.destroy)
btn.place(x=530, y=300)
level_btn.place(x=530, y=370)
exitBtn.place(x=530, y=440)
canvas.pack(expand=True, fill='both')
root.bind("<Key>", start_move)
root.bind("<KeyRelease>", stop_move)
root.mainloop()