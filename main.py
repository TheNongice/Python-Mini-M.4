import math
import time
try:
    import tkinter as tk
    from tkinter import messagebox
    from tkinter.constants import *
except ModuleNotFoundError:
    print("Tkinter is not installed in your device!")
    input("Please reinstall!")

try:
    import assets.calc
    import config  # config.py
except ModuleNotFoundError:
    messagebox.showerror("Geography Calculator :: Error",
                         "ไฟล์ Modules ที่จำเป็นในการเปิดเสียหาย โปรดถอนการติดตั้งโปรแกรมและติดตั้งใหม่อีกครั้ง")
    exit()

#################################
#   Import Outsource Modules    #
#################################
try:
    from PIL import Image, ImageTk
    import haversine as hs
except ModuleNotFoundError:
    messagebox.showerror("Geography Calculator :: Error",
                         "ไม่พบโมดูล PIL (Pillow) หรือ haversine กรุณาตรวจสอบ/ติดตั้งใหม่อีกครั้ง")
    exit()

################
#  All screen  #
################
def calc1():
    global pos1x,pos2x,pos1y,pos2y
    calcs1 = tk.Toplevel()
    calcs1.title("Geography Calculator :: Distance Calculator")
    calcs1.geometry("800x300")
    calcs1.resizable(0, 0)
    calcs1.configure(background=config.menu_bg)
    tell_loc1 = tk.Label(calcs1, text="จุดที่ 1:  ", font=config.fonts_menu, fg="#fff", bg=config.menu_button).place(
        x=125, y=50)
    tell_loc2 = tk.Label(calcs1, text="จุดที่ 2:  ", font=config.fonts_menu, fg="#fff", bg=config.menu_button).place(
        x=125, y=100)
    pos1x = tk.StringVar() ; pos1y = tk.StringVar()
    pos2x = tk.StringVar() ; pos2y = tk.StringVar()
    loc1x = tk.Entry(calcs1, font=config.fonts_menu, width=15,textvariable=pos1x).place(x=200, y=50)
    loc1y = tk.Entry(calcs1, font=config.fonts_menu, width=15,textvariable=pos1y).place(x=365, y=50)
    loc2x = tk.Entry(calcs1, font=config.fonts_menu, width=15,textvariable=pos2x).place(x=200, y=100)
    loc2y = tk.Entry(calcs1, font=config.fonts_menu, width=15,textvariable=pos2y).place(x=365, y=100)
    confirm_btn = tk.Button(calcs1,text="คำนวณ",command=lambda: assets.calc.havershow(pos1x.get(),pos1y.get(),pos2x.get(),pos2y.get()),bg=config.confirm_btn, fg="#000", font=config.fonts_menu).place(x=560,
                                                                                                                 y=70)

def gd_calc():
    gd_cal = tk.Tk()
    gd_cal.title("Geography Calculator :: Geography Map")
    gd_cal.geometry("800x300")
    gd_cal.resizable(0, 0)
    gd_cal.configure(background=config.menu_bg)

def credit():
    credits = tk.Toplevel()
    credits.title("Credits :: คณะผู้จัดทำ")
    credits.geometry("800x500")
    credits.resizable(0, 0)
    credits.configure(background="#000")  # BG this dialogs
    messagebox.showinfo("Note", "อย่าลืมแก้หน้า Credit ต่อ")

    title1 = tk.Label(credits,
                      text="จัดทำโดย....",
                      font=config.fonts_menu,
                      bg=config.menu_button,
                      fg="white"
                      ).pack(side=TOP, pady=30)

    name_cre_st = tk.Label(
        credits,
        text=f"{config.credit_st[1]} เลขที่ {config.credit_st[0]}",
        font=config.fonts_menu,
        bg="black",
        fg="white"
    ).pack(side=TOP, pady=1)

    name_cre_nd = tk.Label(
        credits,
        text=f"{config.credit_nd[1]} เลขที่ {config.credit_nd[0]}",
        font=config.fonts_menu,
        bg="black",
        fg="white"
    ).pack(side=TOP, pady=1)

    class_tell = tk.Label(
        credits,
        text=config.class_credit,
        font=config.fonts_menu,
        bg=config.menu_button,
        fg="white"
    ).pack(side=TOP, pady=10)

    title2 = tk.Label(
        credits,
        text="นำเสนอ",
        font=config.fonts_menu,
        bg=config.menu_button,
        fg="white"
    ).place(anchor=CENTER, x=400, y=300)

    teach = tk.Label(
        credits,
        text=f"{config.teach_pre[0]}\n{config.teach_pre[1]}\n{config.teach_pre[2]}\n{config.teach_pre[3]}",
        font=config.fonts_menu,
        bg="black",
        fg="white"
    ).place(anchor=CENTER, x=400, y=400)

#####################
#   Root screen     #
#####################

root = tk.Tk()
root.title("Geography Calculator")
root.geometry("800x500")
root.configure(background=config.menu_bg)
root.resizable(0, 0)
icon_app = tk.PhotoImage(file="assets/icon.png")
root.iconphoto(True, icon_app)
pg_name = tk.Label(root, text="โปรแกรมคำนวณทางภูมิศาสตร์", font=(config.fonts_menu[0], 45), fg="#ffffff",
                   bg="#2D2926").pack(side=TOP, pady=25)
btn = tk.Button(root, text="คำนวณระยะทางจุด 2 จุด", command=calc1, font=config.fonts_menu, fg="#ffffff",
                bg=config.menu_button, width=50).pack(pady=3)
btn2 = tk.Button(root, text="คำนวณมาตราส่วนแผนที่ GD", command=gd_calc, font=config.fonts_menu, fg="#ffffff",
                 bg=config.menu_button, width=50).pack(pady=3)
btn3 = tk.Button(root, text="ผู้จัดทำ", command=credit, font=config.fonts_menu, fg="#ffffff", bg=config.menu_button,
                 width=50).pack(pady=3)
vers = tk.Label(root, text=f"Version 1.0.0 {config.status()} ; Made from Python", font=(config.fonts_menu[0], 18),
                fg="#ffffff", bg="#2D2926").pack(side=BOTTOM, pady=10)
root.mainloop()
