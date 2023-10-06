from tkinter import *
from time import sleep
from PIL import Image, ImageTk
from random import randint
from tkinter import messagebox

img = [0, 0, 0]
y = -20
x = randint(10, 690)
game = Tk()
ManHinh = game.title("Hứng hạt")
ManHinh = Canvas(master=game, width=700, height=525, background="black")
ManHinh.pack()
lives_remaining = 5
missed_apples = 0  # Thêm biến để theo dõi số trái táo đã bỏ qua
img[0] = ImageTk.PhotoImage(Image.open("C:\\Users\\Admin\\Downloads\\Ngoc\\Ngoc\\backgr.png"))
img[1] = ImageTk.PhotoImage(Image.open("C:\\Users\\Admin\\Downloads\\Ngoc\\Ngoc\\bowl.png"))
img[2] = ImageTk.PhotoImage(Image.open("C:\\Users\\Admin\\Downloads\\Ngoc\\Ngoc\\seeds.png"))
backgr = ManHinh.create_image(0, 0, anchor=NW, image=img[0])
bowl = ManHinh.create_image(0, 420, anchor=NW, image=img[1])
apple = ManHinh.create_image(x, y, anchor=NW, image=img[2])
ManHinh.update()
score = 0
text_score = ManHinh.create_text(620, 30, text="SCORE: " + str(score), fill="black", font=("Times", 20,))


def AppleFall():
    global apple, score, missed_apples  # Thêm biến missed_apples
    ManHinh.move(apple, 0, 10)
    if ManHinh.coords(apple)[1] > 550:
        ManHinh.delete(apple)
        y = -20
        x = randint(10, 690)
        apple = ManHinh.create_image(x, y, anchor=NW, image=img[2])
        missed_apples += 1  # Tăng số trái táo đã bỏ qua
        if missed_apples >= 3:  # Kiểm tra nếu số trái táo bỏ qua đạt đến 3
            game_over()

    if (ManHinh.coords(apple)[0] >= ManHinh.coords(bowl)[0] and ManHinh.coords(apple)[0] + 50 <= ManHinh.coords(bowl)[0] + 120) and (
            ManHinh.coords(apple)[1] + 50 >= ManHinh.coords(bowl)[1] and ManHinh.coords(apple)[1] + 50 <= ManHinh.coords(bowl)[1] + 37.5):
        ManHinh.delete(apple)
        y = -20
        x = randint(10, 690)
        apple = ManHinh.create_image(x, y, anchor=NW, image=img[2])
        score = score + 1
        ManHinh.itemconfig(text_score, text="SCORE: " + str(score))
    ManHinh.update()


def game_over():
    global gameOver
    gameOver = True
    messagebox.showinfo("Game Over!", "Final Score: " + str(score))
    game.destroy()


# Hàm di chuyển bowl
def right():
    global bowl
    if ManHinh.coords(bowl)[0] < 650:
        ManHinh.move(bowl, 20, 0)
    ManHinh.update()


def left():
    global bowl
    if ManHinh.coords(bowl)[0] > 0:
        ManHinh.move(bowl, -20, 0)
    ManHinh.update()


def keyPress(event):
    if event.keysym == "Right":
        right()
    if event.keysym == "Left":
        left()


ManHinh.bind_all("<KeyPress>", keyPress)
gameOver = False

while not gameOver:
    AppleFall()
    sleep(0.05)

game.mainloop()