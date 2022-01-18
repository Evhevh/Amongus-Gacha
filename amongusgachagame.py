from tkinter import *
import random
from PIL import Image, ImageTk
# 1/14/22 avh - Import game_data_ds module
import modules.data_service.game_data_ds as game_data_ds

root = Tk()
root.title("AMONGUS GACHAPON")
root.geometry('1150x525')

# menu buttons


def end_game():
    # 1/14/22 avh - Uses game_data_ds module to update the user's credit in the database
    # 1/14/22 evh - updates inventory into the database
    game_data_ds.update_credit(username, credit)
    game_data_ds.update_inventory(username, red_count, cyan_count, yellow_count, green_count)
    print("*** Updates user's Credit in the db to " + str(credit))
    print("*** Updates Inventory Count")
    print("*** Red:" + str(red_count) + " Cyan:" + str(cyan_count) +
          " Yellow:" + str(yellow_count) + " Green:" + str(green_count))

    root.destroy()


def show_frame(frame):
    frame.tkraise()


# 1/14/22 evh - resets the state of pictures for gacha pulls
def reset_state():
    global prev_list
    prev_list = [photostartr, photostartr, photostartr, photostartr, photostartr]
    display_list()
    pulled.config(image=photostart)
    money_button.config(image=photostartr)


# 1/14/22 evh - logout function that updates the database without closing the program
def logout_function():
    game_data_ds.update_credit(username, credit)
    game_data_ds.update_inventory(username, red_count, cyan_count, yellow_count, green_count)
    print("*** Updates user's Credit in the db to " + str(credit))
    print("*** Updates Inventory Count")
    print("*** Red:" + str(red_count) + " Cyan:" + str(cyan_count) +
          " Yellow:" + str(yellow_count) + " Green:" + str(green_count))
    login_frame.tkraise()
    login_warning.place_forget()


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


# 1/14/22 avh - Uses game_data_ds module to get the user's credit from the database
# credit = 100
# 1/14/22 evh - login feature
def login():
    global username
    global red_count
    global cyan_count
    global yellow_count
    global green_count
    global credit
    answer = login_info.get().strip().lower()
    if answer == "1" or answer == "2":
        username = int(login_info.get())
        row = game_data_ds.get_row_by_user(username)
        credit = row['credit']
        print("*** Credit stores in db is " + str(credit))
        red_count = row['inventory_r']
        cyan_count = row['inventory_c']
        yellow_count = row['inventory_y']
        green_count = row['inventory_g']
        credit_label.config(text=f' credit: {credit}')
        coin_label.config(text=f' credit: {credit}')
        red_sus_count.config(text=f' x{red_count}')
        cyan_sus_count.config(text=f' x{cyan_count}')
        yellow_sus_count.config(text=f' x{yellow_count}')
        green_sus_count.config(text=f' x{green_count}')
        start_menu.tkraise()
    else:
        login_warning.place(relx=0.51, rely=0.6, anchor=CENTER)


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

credit = 0
red_count = 0
cyan_count = 0
yellow_count = 0
green_count = 0
username = 0

# 1/14/22 evh - added a login frame
# overlapping frames
login_frame = Frame(root)
start_menu = Frame(root)
game_frame = Frame(root)
coin_frame = Frame(root)
have_frame = Frame(root)

for frame in (login_frame, start_menu, game_frame, coin_frame, have_frame):
    frame.grid(row=0, column=0, sticky='news')

login_frame.tkraise()


# 1/14/22 evh - login GUI
login_label = Label(login_frame, text="Welcome", font=("Helvetica", 30))
login_label.place(relx=0.51, rely=0.4, anchor=CENTER)

login_warning = Label(login_frame, text="Invalid login")

login_info = Entry(login_frame)
login_info.place(relx=0.49, rely=0.5, anchor=CENTER)

login_button = Button(login_frame, text='Login', command=lambda: login())
login_button.place(relx=0.57, rely=0.5, anchor=CENTER)

exit_game = Button(login_frame, text="Exit", command=end_game)
exit_game.place(relx=0.9, rely=0.85, anchor=CENTER)


# START MENU GUI
start_label = Label(start_menu, text="AMONG US", font=("Helvetica", 50))
start_label.pack(pady=70)

game_button = Button(start_menu, text='Gacha', font=50, command=lambda: show_frame(game_frame))
game_button.pack(padx=10, pady=10)

coin_button = Button(start_menu, text='Coins', font=50, command=lambda: show_frame(coin_frame))
coin_button.pack(padx=10, pady=10)

have_button = Button(start_menu, text='Inventory', font=50, command=lambda: show_frame(have_frame))
have_button.pack(padx=10, pady=10)

# 1/14/22 evh - added a logout button
logout_button = Button(start_menu, text='Logout', font=50, command=lambda: [logout_function(), reset_state()])
logout_button.pack(padx=10, pady=10)

exit_button = Button(start_menu, text="Exit", font=50, command=end_game)
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


root.mainloop()
