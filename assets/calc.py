import haversine as hs
from tkinter import messagebox
def havershow(x1,y1,x2,y2):
    try:
        loc1 = (float(x1),float(y1))
        loc2 = (float(x2),float(y2))
        #print(hs.haversine(loc1,loc2))
        messagebox.showinfo("Notficatons",hs.haversine(loc1,loc2))
    except ValueError:
        messagebox.showerror("Error!","โปรดกรอกข้อมูลเป็นตัวเลขเท่านั้น!")