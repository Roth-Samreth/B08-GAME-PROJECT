from tkinter import *
# constant
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


def gamescreen():
    root = Toplevel(window)
    canvas = Canvas(root, width=1150, height=600, scrollregion=(0, 0, 4000, 5000))
    back = PhotoImage(file="Image/10.png")
    pp = PhotoImage(file="Image/Run1.png")
    bg = canvas.create_image(20, 20, image=back)
    player = canvas.create_image(45, 300, image=pp)
    # _______________________________________________Enemy__________________________________________
    pf1 = PhotoImage(file="Image/Fighter.png")

    # Create platform
    tile1 = PhotoImage(file="Image/Tile_01.png")

    def create_platform(x, y, row, col):
        X = x
        Y = y
        for j in range(row):
            for i in range(col):
                tiles = canvas.create_image(X, Y, image=tile1, tag='PLATFORM')
                X += 30
            X = x
            Y += 30

    create_platform(20, 400, 5, 8)
    create_platform(340, 300, 4, 8)
    create_platform(650, 400, 1, 4)
    create_platform(800, 560, 2, 8)

    # Funtions
    def check_movement(dx=0, dy=0, checkGround=False):
        coord = canvas.bbox(player)
        platforms = canvas.find_withtag("PLATFORM")

        if coord[0] + dx < 0 or coord[2] + dx > SCREENWIDTH:
            return False

        if checkGround:
            overlap = canvas.find_overlapping(coord[0], coord[1], coord[2], coord[3] + dy)
        else:
            overlap = canvas.find_overlapping(coord[0] + dx, coord[1] + dy, coord[2] + dx, coord[3])

        for platform in platforms:
            if platform in overlap:
                return False

        return True

    def jump(force):
        if force > 0:
            if check_movement(0, -force):
                canvas.move(player, 0, -force)
                root.after(TIMED_LOOP, jump, force - 1)

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

    def gravity():
        if check_movement(0, GRAVITY_FORCE, True):
            canvas.move(player, 0, GRAVITY_FORCE)
        root.after(TIMED_LOOP, gravity)

    canvas.pack()
    gravity()
    canvas.bind_all("<Key>", start_move)
    canvas.bind_all("<KeyRelease>", stop_move)
    root.mainloop()
def startscreen():
    global window
    window = Tk()
    window.geometry("400x400")
    btn = Button(window, text="Play Game", command=gamescreen,font=("Metal Mania",15))
    btn.place(x=150,y=150)
    window.mainloop()
startscreen()