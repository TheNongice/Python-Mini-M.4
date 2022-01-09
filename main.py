import tkinter as tk
from tkinter.constants import *
from PIL import Image,ImageTk
import haversine as hs
import math
import assets.calc
import config # config.py

root = tk.Tk()
root.title("Geography Calculator")
root.geometry("800x500")
root.resizable(0,0)
icon_app = tk.PhotoImage(file = "assets/icon.png")
root.iconphoto(True,icon_app)

################
#  All screen  #
################
def calc1():
    calcs1 = tk.Tk()
    calcs1.title("Geography Calculator :: Distance Calculator")
    calcs1.geometry("800x300")
    calcs1.resizable(0,0)
def gd_calc():
    gd_cal = tk.Tk()
    gd_cal.title("Geography Calculator :: Geography Map")
    gd_cal.geometry("800x300")
    gd_cal.resizable(0,0)
def credit():
    credits = tk.Toplevel()
    credits.title("Credits :: คณะผู้จัดทำ")
    credits.geometry("800x500")
    credits.resizable(0,0)
    credits.configure(background="#000") # BG this dialogs

    title1 = tk.Label(credits,
        text="จัดทำโดย....",
        font=config.fonts_menu,
        bg="red",
        fg="white"
    ).pack(side=TOP,pady=30)

    name_cre_st = tk.Label(
        credits,
        text=f"{config.credit_st[1]} เลขที่ {config.credit_st[0]}",
        font=config.fonts_menu,
        bg = "black",
        fg = "white"
    ).pack(side=TOP,pady=1)
    
    name_cre_nd = tk.Label(
        credits,
        text=f"{config.credit_nd[1]} เลขที่ {config.credit_nd[0]}",
        font=config.fonts_menu,       
        bg = "black",
        fg = "white"
    ).pack(side=TOP,pady=1)

    class_tell = tk.Label(
        credits,
        text=config.class_credit,
        font=config.fonts_menu,        
        bg = "red",
        fg = "white"
    ).pack(side=TOP,pady=10)

    title2 = tk.Label(
        credits,
        text="นำเสนอ",
        font=config.fonts_menu,
        bg="red",
        fg="white"
    ).place(anchor=CENTER,x=400,y=300)

    teach = tk.Label(
        credits,
        text=f"{config.teach_pre[0]}\n{config.teach_pre[1]}",
        font=config.fonts_menu,
        bg="black",
        fg="white"
    ).place(anchor=CENTER,x=400,y=365)
    global kuy
    kuy = ImageTk.PhotoImage(Image.open("assets/credit/zuking.png"))
    hi = tk.Label(credits,image=kuy).pack()

#####################
#   Root screen     #
#####################
pg_name = tk.Label(root,text="โปรแกรมคำนวณทางภูมิศาสตร์",font=(config.fonts_menu[0],45)).pack(side=TOP,pady=25)
btn = tk.Button(root,text="คำนวณระยะทางจุด 2 จุด",command=calc1,font=config.fonts_menu,fg="red",bg="black").pack(pady=3)
btn2 = tk.Button(root,text="คำนวณมาตราส่วนแผนที่ GD",command=gd_calc,font=config.fonts_menu,fg="red",bg="black").pack(pady=3)
btn3 = tk.Button(root,text="ผู้จัดทำ",command=credit,font=config.fonts_menu,fg="red",bg="black").pack(pady=3)
vers = tk.Label(root,text=f"Version 1.0.0 {config.status()} ; Made from Python",font=(config.fonts_menu[0],18)).pack(side=BOTTOM,pady=10)


root.mainloop()