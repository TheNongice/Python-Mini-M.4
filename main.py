import tkinter as tk
from tkinter.constants import *
from PIL import Image,ImageTk
import haversine
import math
import assets.calc
import config

root = tk.Tk()
root.title("Geography Calculator")
root.geometry("800x500")
root.resizable(0,0)
icon_app = tk.PhotoImage(file = "assets/icon.png")
root.iconphoto(True,icon_app)

##############
#  Calc - 1  #
##############
def calc1():
    calcs1 = tk.Tk()
    calcs1.title("Geography Calculator || Distance Calculator")
    calcs1.geometry("800x300")
    calcs1.resizable(0,0)
def gd_calc():
    gd_cal = tk.Tk()
    gd_cal.title("Geography Calculator || Geography Map")
    gd_cal.geometry("800x300")
    gd_cal.resizable(0,0)
def credit():
    credits = tk.Tk()
    credits.title("Credits || คณะผู้จัดทำ")
    credits.resizable(0,0)

#####################
#   Root screen     #
#####################
btn = tk.Button(root,text="คำนวณระยะทางจุด 2 จุด",command=calc1,font=config.fonts_menu,fg="red",bg="black")
btn2 = tk.Button(root,text="คำนวณมาตราส่วนแผนที่ GD",command=gd_calc,font=config.fonts_menu,fg="red",bg="black")
btn3 = tk.Button(root,text="ผู้จัดทำ",command=credit,font=config.fonts_menu,fg="red",bg="black")
btn.pack(side=TOP)
btn2.pack(side=TOP)
btn3.pack(side=TOP)


root.mainloop()