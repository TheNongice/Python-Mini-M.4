import haversine as hs
import tkinter as tk
from tkinter import messagebox
from tkinter.constants import *
import config
def havershow(x1,y1,x2,y2):
    try:
        loc1 = (float(x1),float(y1))
        loc2 = (float(x2),float(y2))
        #messagebox.showinfo("Notficatons",hs.haversine(loc1,loc2))
        return hs.haversine(loc1,loc2)
    except ValueError:
        messagebox.showerror("Error!","โปรดกรอกข้อมูลเป็นตัวเลขเท่านั้น!")
def gd_ca():
    pass