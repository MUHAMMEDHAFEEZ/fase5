
from pathlib import Path

from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage , messagebox
import sqlite3
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\guiproject\fase5\build\assets\frame0")



def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

bo = 0
def trupass():
    conn = sqlite3.connect('data_user_password.db')
    c = conn.cursor()
    c.execute("SELECT * FROM user")
    r = c.fetchall()
    for i in r :
        if i[0]==entry_1.get() and entry_2.get():
            bo=0
            return bo
        else:
            bo=1
            return bo
    
def get_input():
    if trupass():
        print("sdf")


              
            
        
    
window = Tk()

window.geometry("900x900")
window.configure(bg = "#302F3D")


canvas = Canvas(
    window,
    bg = "#302F3D",
    height = 900,
    width = 900,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)


canvas.place(x = 0, y = 0)
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: get_input(),
    relief="sunken"
)
button_1.place(
    x=377.0,
    y=652.0,
    width=132.73077392578125,
    height=51.5640869140625
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    443.0,
    558.0,
    image=image_image_1
)

canvas.create_text(
    343.0,
    475.0,
    anchor="nw",
    text="username ",
    fill="#666666",
    font=("Poppins Regular", 16 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    443.5,
    520.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=290.0,
    y=503.0,
    width=307.0,
    height=33.0
)

canvas.create_text(
    295.0,
    559.0,
    anchor="nw",
    text="Password",
    fill="#666666",
    font=("Poppins Regular", 16 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    443.5,
    601.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=290.0,
    y=584.0,
    width=307.0,
    height=32.0
)

canvas.create_text(
    383.0,
    424.0,
    anchor="nw",
    text="LOGIN",
    fill="#333333",
    font=("Poppins Medium", 32 * -1)
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    449.0,
    183.0,
    image=image_image_2
)

window.iconphoto(False, image_image_2)

window.resizable(False, False)
window.mainloop()
