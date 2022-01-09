import tkinter as tk
import haversine
import math
import assets.calc

root = tk.Tk()
root.title("Geography Calculator")
root.geometry("800x500")
icon_app = tk.PhotoImage(file = "assets/icon.png")
root.iconphoto(True,icon_app)

##############s
#  Calc - 1  #
##############
def calc1():
    calcs1 = tk.Tk()
    calcs1.title("Geography Calculator - Distance Calculator")
    calcs1.geometry("800x300")
    tk.Tk.messagebox.showerror("พ่อมึงตาย","ไอเย็ดแม่")

##############
#   Main     #
##############
btn = tk.Button(text="คำนวณระยะทางจุด 2 จุด",command=calc1,font=20,foreground="red")
btn.pack()


root.mainloop()