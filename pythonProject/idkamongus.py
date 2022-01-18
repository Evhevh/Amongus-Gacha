from tkinter import *
from PIL import Image, ImageTk
import random

root = Tk()
root.title('amongus piano')
root.geometry("500x700")
root.config(background='black')


#SUSSY IMPOSTER COLORS
imagered = Image.open("D:/!Pycharmprojects/pics/red-among-us-png.png")
imagecyan = Image.open("D:/!Pycharmprojects/pics/cyan-among-us-character.png")
imageyellow = Image.open("D:/!Pycharmprojects/pics/yellow-among-us.png")
imagegreen = Image.open("D:/!Pycharmprojects/pics/among-us-green-png.png")

imagesusr = imagered.resize((500,500))
imagesusc = imagecyan.resize((500,500))
imagesusy = imageyellow.resize((500,500))
imagesusg = imagegreen.resize((500,500))

photor = ImageTk.PhotoImage(imagesusr)
photoc = ImageTk.PhotoImage(imagesusc)
photoy = ImageTk.PhotoImage(imagesusy)
photog = ImageTk.PhotoImage(imagesusg)

image_list = [photor, photoc, photoy, photog]
rng = random.choice(image_list)

#makes me super sussy
def amongus():                                                            #imposter
    sussy = Label(root, text="IMPOSTER IS SUS", bg='BLACK', fg='WHITE')
    sussy.pack()  #imposter

# crab dance
def bckground():   #imposter
    rng = file = random.choice(image_list)
    button1.config(image=rng)



button1 = Button(root, image=photor, command=lambda:[amongus(), bckground()])
button1.pack()


root.mainloop()

