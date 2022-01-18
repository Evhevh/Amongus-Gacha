from tkinter import *
import random
from PIL import Image, ImageTk

root=Tk()
root.title("imposter game")


#SUSSY IMPOSTER COLORS
imagered = Image.open("D:/!Pycharmprojects/pics/red-among-us-png.png")
imagecyan = Image.open("D:/!Pycharmprojects/pics/cyan-among-us-character.png")
imageyellow = Image.open("D:/!Pycharmprojects/pics/yellow-among-us.png")
imagegreen = Image.open("D:/!Pycharmprojects/pics/among-us-green-png.png")

imagesusr = imagered.resize((300,300))
imagesusc = imagecyan.resize((300,300))
imagesusy = imageyellow.resize((300,300))
imagesusg = imagegreen.resize((300,300))

photor = ImageTk.PhotoImage(imagesusr)
photoc = ImageTk.PhotoImage(imagesusc)
photoy = ImageTk.PhotoImage(imagesusy)
photog = ImageTk.PhotoImage(imagesusg)

#background
#bg = PhotoImage(file="d:/!PycharmProjects/pics/The_Skeld_Cafeteria.png")
#my_label = Label(root, image=bg)
#my_label.place(x=0, y=0, relwidth=1, relheight=1)

#starts the game
rng = random.randint(1,4)

#commands for guessing game
#check if button is right or wrong
def check(x):
    if x == rng:
        wrongbutton.forget()
        retrybutton.pack(pady=10, padx=10)

    else:
        wrongbutton.pack(pady=10, padx=10)

#disables a used button
def disable(x):
    if x==1:
        redsus.config(state='disable')
    elif x==2:
        cyansus.config(state='disable')
    elif x==3:
        yellowsus.config(state='disable')
    elif x==4:
        greensus.config(state='disable')

#restarts the game
def retry():
    global rng
    sus=random.randint(1,4)
    rng=sus
    redsus.config(state='active')
    cyansus.config(state='active')
    yellowsus.config(state='active')
    greensus.config(state='active')
    wrongbutton.forget()
    retrybutton.forget()

#closes the game
def end_game():
    root.destroy()


#frame for pictures
susframe = LabelFrame(root, text="SKELD", padx=10,pady=10)
susframe.pack(padx=10,pady=10)


#imposter buttons
redsus = Button(susframe, image=photor, command=lambda: [check(1), disable(1)])
redsus.grid(row=0,column=0)

cyansus = Button(susframe, image=photoc, command=lambda: [check(2), disable(2)])
cyansus.grid(row=0,column=1)

yellowsus = Button(susframe, image=photoy, command=lambda: [check(3), disable(3)])
yellowsus.grid(row=0,column=2)

greensus = Button(susframe, image=photog, command=lambda: [check(4), disable(4)])
greensus.grid(row=0,column=3)


#menu buttons
exitbutton = Button(root, text="Exit", command=end_game)
exitbutton.pack(pady=10, padx=10, side=RIGHT)

retrybutton= Button(root, text="Congrats, Click to Retry", command=lambda:retry())

wrongbutton= Label(root, text="WRONG, Try Again")

#looping
root.mainloop()