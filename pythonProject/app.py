from tkinter import *
from PIL import Image, ImageTk
import os
from pathlib import Path
from tkinter import ttk

root = Tk()
root.title('Pokemon Shiny Dex')
root.geometry("900x900")
icon_dir = Path("D:/shinydex")


e = Entry(root, width=50, bg="white", fg="black")
e.insert(0, "Search")
e.pack()


main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)

my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)

my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e:my_canvas.configure(scrollregion = my_canvas.bbox("all")))

second_frame = Frame(my_canvas)
my_canvas.create_window((0,0), window=second_frame, anchor="nw")

frm_grid = Frame(second_frame)
frm_grid.rowconfigure([0, 1, 2, 3, 4, 5], weight=1, minsize=2)
frm_grid.columnconfigure([0, 1, 2, 3, 4, 5], weight=1, minsize=2)
frm_grid.pack(fill=BOTH, expand=YES)
buttons = []
for row in range(0, 99):
    for column in range(0, 7):
        btn = Button(frm_grid)
        btn.grid(row=row, column=column, sticky='news')
        buttons.append(btn)


def switchButtonState():
    if (btn.cget('bg')=="yellow"):
        btn.config(bg='white')
    else:
        btn.config(bg='yellow')

for file in icon_dir.iterdir():
    path = os.path.join("D:/shinydex", file)
    icon = PhotoImage(file=str(file))
    btn = buttons[0]
    namewa = Path(path).stem
    my_label = Label(second_frame, text=namewa)
    btn.config(image=icon, text=namewa, compound=BOTTOM, command=lambda: switchButtonState())
    btn.image = icon
    buttons.remove(btn)




root.mainloop()
