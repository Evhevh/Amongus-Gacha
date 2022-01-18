from tkinter import *
import random
from PIL import Image, ImageTk


root = Tk()
root.title("AMONGUS GACHAPON")
root.geometry('1150x525')

# menu buttons


def end_game():
    root.destroy()


def show_frame(frame):
    frame.tkraise()


def spend():
    global credit
    if credit > 9:
        credit -= 10
        credit_label.config(text=f' credit: {credit}')
        coin_label.config(text=f' credit: {credit}')


def earn():
    global credit
    chance = random.randrange(0, 10)
    if chance == 1:
        credit += 10
    else:
        credit += 1
    credit_label.config(text=f' credit: {credit}')
    coin_label.config(text=f' credit: {credit}')


def bckground():
    rng = random.choice(prev_list)
    money_button.config(image=rng)


# sprites and assets
imagestart = Image.open("D:/Pictures/MS/maple.png")
imagered = Image.open("D:/!Pycharmprojects/pics/red-among-us-png.png")
imagecyan = Image.open("D:/!Pycharmprojects/pics/cyan-among-us-character.png")
imageyellow = Image.open("D:/!Pycharmprojects/pics/yellow-among-us.png")
imagegreen = Image.open("D:/!Pycharmprojects/pics/among-us-green-png.png")

photostart = ImageTk.PhotoImage(imagestart.resize((300, 300)))
photor = ImageTk.PhotoImage(imagered.resize((300, 300)))
photoc = ImageTk.PhotoImage(imagecyan.resize((300, 300)))
photoy = ImageTk.PhotoImage(imageyellow.resize((300, 300)))
photog = ImageTk.PhotoImage(imagegreen.resize((300, 300)))

photostartr = ImageTk.PhotoImage(imagestart.resize((150, 150)))
photorr = ImageTk.PhotoImage(imagered.resize((150, 150)))
photocr = ImageTk.PhotoImage(imagecyan.resize((150, 150)))
photoyr = ImageTk.PhotoImage(imageyellow.resize((150, 150)))
photogr = ImageTk.PhotoImage(imagegreen.resize((150, 150)))

credit = 100
red_count = 0
cyan_count = 0
yellow_count = 0
green_count = 0


# overlapping frames
start_menu = Frame(root)
game_frame = Frame(root)
coin_frame = Frame(root)
have_frame = Frame(root)

for frame in (start_menu, game_frame, coin_frame, have_frame):
    frame.grid(row=0, column=0, sticky='news')

start_menu.tkraise()

# START MENU GUI
start_label = Label(start_menu, text="AMONG US", font=("Helvetica", 50))
start_label.pack(pady=100)

game_button = Button(start_menu, text='Gacha', font=50, command=lambda: show_frame(game_frame))
game_button.pack(padx=10, pady=10)

coin_button = Button(start_menu, text='Coins', font=50, command=lambda: show_frame(coin_frame))
coin_button.pack(padx=10, pady=10)

have_button = Button(start_menu, text='Inventory', font=50, command=lambda: show_frame(have_frame))
have_button.pack(padx=10, pady=10)

exit_button = Button(start_menu, text="Exit", command=end_game)
exit_button.pack(pady=10, padx=10)


# GACHA GUI frame for gachapon GUI
gacha_frame = LabelFrame(game_frame, text="pull", padx=10, pady=10)
gacha_frame.grid(padx=10, pady=15, column=0, row=0)

pulled = Label(gacha_frame, image=photostart)
pulled.pack()


# GACHA GUI show previous pulls
prev_list = [photostartr, photostartr, photostartr, photostartr, photostartr]
prev_frame = LabelFrame(game_frame, padx=10, pady=10, text='previous rolls')
prev_frame.grid(column=1, row=0)



def display_list():
    for x in range(0, 5):
        prev = Label(prev_frame, image=prev_list[x])
        prev.grid(column=x, row=0)


display_list()

# GACHA GUI credit and pull GUI
spend_frame = LabelFrame(game_frame, padx=10, pady=10)
spend_frame.grid(column=0, row=1, padx=10, pady=10)

credit_label = Label(spend_frame, text=f' credit: {credit}')
credit_label.grid(column=1, row=0)

button_pull = Button(spend_frame, text="10 credits", command=lambda: [gacha_pull(), spend(), display_list()])
button_pull.grid(column=0, row=0)

home = Button(game_frame, text="Menu", command=lambda: show_frame(start_menu))
home.place(relx=0.9, rely=0.85, anchor=CENTER)


# GACHA GUI rolling for amongus
def gacha_pull():
    global red_count
    global cyan_count
    global yellow_count
    global green_count
    pull = round(random.uniform(0, 100), 2)
    if credit > 9:
        if pull <= 5:
            pulled.config(image=photor)
            prev_list.insert(0, photorr)
            prev_list.pop()
            red_count += 1
            red_sus_count.config(text=f' x{red_count}')
        elif 5 < pull <= 25:
            pulled.config(image=photoc)
            prev_list.insert(0, photocr)
            prev_list.pop()
            cyan_count += 1
            cyan_sus_count.config(text=f' x{cyan_count}')
        elif 25 < pull <= 55:
            pulled.config(image=photoy)
            prev_list.insert(0, photoyr)
            prev_list.pop()
            yellow_count += 1
            yellow_sus_count.config(text=f' x{yellow_count}')
        elif 55 < pull <= 100:
            pulled.config(image=photog)
            prev_list.insert(0, photogr)
            prev_list.pop()
            green_count += 1
            green_sus_count.config(text=f' x{green_count}')

    print(pull)

# amongus cookie clicker
# rng chance for +100 coins


rng = random.choice(prev_list)

money_button = Button(coin_frame, image=prev_list[0], command=lambda: [earn(), bckground()])
money_button.place(relx=0.5, rely=0.4, anchor=CENTER)

coin_label = Label(coin_frame, text=f' credit: {credit}', font=50)
coin_label.place(relx=0.5, rely=0.6, anchor=CENTER)

home = Button(coin_frame, text="Menu", command=lambda: show_frame(start_menu))
home.place(relx=0.9, rely=0.85, anchor=CENTER)

# gallery inventory
inventory_frame = LabelFrame(have_frame, text="Inventory", padx=10, pady=10)
inventory_frame.pack(pady=100)

red_sus = Label(inventory_frame, image=photorr)
cyan_sus = Label(inventory_frame, image=photocr)
yellow_sus = Label(inventory_frame, image=photoyr)
green_sus = Label(inventory_frame, image=photogr)

red_sus_count = Label(inventory_frame, text=f' x{red_count}', font=50)
cyan_sus_count = Label(inventory_frame, text=f' x{cyan_count}', font=50)
yellow_sus_count = Label(inventory_frame, text=f' x{yellow_count}', font=50)
green_sus_count = Label(inventory_frame, text=f' x{green_count}', font=50)

red_sus.grid(column=0, row=0, padx=10)
cyan_sus.grid(column=1, row=0, padx=10)
yellow_sus.grid(column=2, row=0, padx=10)
green_sus.grid(column=3, row=0, padx=10)

red_sus_count.grid(column=0, row=1, padx=10)
cyan_sus_count.grid(column=1, row=1, padx=10)
yellow_sus_count.grid(column=2, row=1, padx=10)
green_sus_count.grid(column=3, row=1, padx=10)

home = Button(have_frame, text="Menu", command=lambda: show_frame(start_menu))
home.place(relx=0.9, rely=0.85, anchor=CENTER)

# room to move amongus characters with WASD



root.mainloop()