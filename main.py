import math
import time

try:
    import tkinter as tk
    from tkinter import messagebox
    from tkinter.constants import *
except ModuleNotFoundError:
    print("Tkinter is not installed/corrupt in your device!")
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
def haver_calc():
    global pos1x, pos2x, pos1y, pos2y, result_text
    haver = tk.Toplevel()
    haver.title("Geography Calculator :: Distance Calculator")
    haver.geometry("800x300")
    haver.resizable(0, 0)
    haver.configure(background=config.menu_bg)
    Frame = tk.Frame(haver, bg=config.menu_button, bd="5")
    Frame.pack(pady=45)
    tell_loc1 = tk.Label(Frame, text="จุดที่ 1:  ", font=config.fonts_menu, fg="#fff", bg=config.menu_button).grid(
        column=0, row=0, padx=8)
    tell_loc2 = tk.Label(Frame, text="จุดที่ 2:  ", font=config.fonts_menu, fg="#fff", bg=config.menu_button).grid(
        column=0, row=1)
    pos1x = tk.StringVar()  # First point (x)
    pos1y = tk.StringVar()  # First point (y)
    pos2x = tk.StringVar()  # Second point (x)
    pos2y = tk.StringVar()  # Second point (y)
    loc1x = tk.Entry(Frame, font=config.fonts_menu, width=15, textvariable=pos1x)
    loc1y = tk.Entry(Frame, font=config.fonts_menu, width=15, textvariable=pos1y)
    loc2x = tk.Entry(Frame, font=config.fonts_menu, width=15, textvariable=pos2x)
    loc2y = tk.Entry(Frame, font=config.fonts_menu, width=15, textvariable=pos2y)
    loc1x.grid(column=1, row=0)
    loc1y.grid(column=2, row=0, padx=8)
    loc2x.grid(column=1, row=1)
    loc2y.grid(column=2, row=1)
    confirm_btn = tk.Button(Frame, text="คำนวณ",
                            command=lambda: returnHs(pos1x.get(), pos1y.get(), pos2x.get(), pos2y.get()),
                            bg=config.confirm_btn, fg="#000", font=config.fonts_menu).grid(row=3, column=1, sticky=SE,
                                                                                           pady=3)
    result_text = tk.Label(haver, text="", bg=config.menu_bg, font=(config.fonts_menu[0],"26"), fg="#fff")
    result_text.pack(side=BOTTOM, pady=20)


########################################################################
def gd_calc():
    global md_data, gd_data, md_input, gd_input, submit, reset_btn
    gd_cal = tk.Toplevel()
    gd_cal.title("Geography Calculator :: Geography Map")
    gd_cal.geometry("800x300")
    gd_cal.resizable(0, 0)
    gd_cal.configure(background=config.menu_bg)
    md_data = tk.StringVar()
    gd_data = tk.StringVar()
    Frame = tk.Frame(gd_cal, bg=config.menu_button)
    Frame.pack(pady=35)
    tell_MD = tk.Label(Frame, text="MD :  ", font=config.fonts_menu, fg="#fff", bg=config.menu_button).grid(column=0,
                                                                                                            row=0)
    md_input = tk.Entry(Frame, textvariable=md_data, font=config.fonts_menu)
    md_input.grid(column=1, row=0)
    tell_GD = tk.Label(Frame, text="GD :  ", font=config.fonts_menu, fg="#fff", bg=config.menu_button).grid(column=0,
                                                                                                            row=1)
    gd_input = tk.Entry(Frame, textvariable=gd_data, font=config.fonts_menu)
    gd_input.grid(column=1, row=1, pady=5)
    tell_cm = tk.Label(Frame, text=" CM", font=config.fonts_menu, fg="#fff", bg=config.menu_button).grid(column=2,
                                                                                                         row=0)
    tell_km = tk.Label(Frame, text=" KM", font=config.fonts_menu, fg="#fff", bg=config.menu_button).grid(column=2,
                                                                                                         row=1)
    submit = tk.Button(gd_cal, text="แปลงค่าระยะทาง", font=config.fonts_menu, bg=config.confirm_btn,command=submit_gd,width=15)
    submit.pack()
    reset_btn = tk.Button(gd_cal, text="ล้างค่า", font=config.fonts_menu, bg="#B91646",command=reset_gd, fg="#fff", width=15,state=DISABLED)
    reset_btn.pack(pady=3)

######################################################################

def credit():
    credits = tk.Toplevel()
    credits.title("Credits :: คณะผู้จัดทำ")
    credits.geometry("800x500")
    credits.resizable(0, 0)
    credits.configure(background=config.menu_bg)

    title1 = tk.Label(credits,
                      text="จัดทำโดย....",
                      font=config.fonts_menu,
                      bg="#343A40",
                      fg="white"
                      ).pack(side=TOP, pady=30)

    name_cre_st = tk.Label(
        credits,
        text=f"{config.credit_st[1]} เลขที่ {config.credit_st[0]}",
        font=config.fonts_menu,
        bg=config.menu_bg,
        fg="white"
    ).pack(side=TOP, pady=1)

    name_cre_nd = tk.Label(
        credits,
        text=f"{config.credit_nd[1]} เลขที่ {config.credit_nd[0]}",
        font=config.fonts_menu,
        bg=config.menu_bg,
        fg="white"
    ).pack(side=TOP, pady=1)

    class_tell = tk.Label(
        credits,
        text=config.class_credit,
        font=config.fonts_menu,
        bg=config.menu_bg,
        fg="white"
    ).pack(side=TOP, pady=10)

    title2 = tk.Label(
        credits,
        text="นำเสนอ",
        font=config.fonts_menu,
        bg="#343A40",
        fg="white"
    ).place(anchor=CENTER, x=400, y=300)

    teach = tk.Label(
        credits,
        text=f"{config.teach_pre[0]}\n{config.teach_pre[1]}\n{config.teach_pre[2]}\n{config.teach_pre[3]}",
        font=config.fonts_menu,
        bg=config.menu_bg,
        fg="white"
    ).place(anchor=CENTER, x=400, y=400)

def howtouse():
    htu_sc = tk.Toplevel()
    htu_sc.geometry("800x500")
    htu_sc.configure(bg=config.menu_bg)
    htu_sc.resizable(0,0)

#########################################################################

def returnHs(x1, y1, x2, y2):
    if (pos1x.get() == "") or (pos1y.get() == "") or (pos2x.get() == "") or (pos2y.get() == ""):
        messagebox.showwarning("Error!", "ไม่สามารถปล่อยให้ค่าใดหนึ่งว่าง")
        result_text.configure(text=f"ไม่สามารถแปลงหน่วยได้! [ERR-01]",bg="#343A40")
    else:
        try:
            result = assets.calc.havershow(x1, y1, x2, y2)
            result_text.configure(text=f"{result:.4f} km",bg="#343A40")
        except:
            result_text.configure(text=f"ไม่สามารถแปลงหน่วยได้! [ERR-02]",bg="#343A40")

def reset_gd():
    reset_btn.configure(state=DISABLED)
    md_input.configure(state=NORMAL)
    gd_input.configure(state=NORMAL)
    submit.configure(state=NORMAL)
    gd_input.delete(0,END)
    md_input.delete(0,END)
def submit_gd():
    if (md_data.get() == "") and (gd_data.get() == ""):
        messagebox.showerror("Error!", "ไม่สามารถเว้นค่า")
    elif (md_data.get() != "") and (gd_data.get() != ""):
        md_input.delete(0, END)
        gd_input.delete(0, END)
        messagebox.showinfo("Nofcations", "กรุณาใส่เพียงค่าใดค่าหนึ่ง")
    elif md_data.get() != "":
        try:
            md_cal = float(md_data.get())
            result = (md_cal*50000)/100000
            # GD Replace data.
            gd_input.delete(0,END)
            gd_input.insert(0,str(result))
            gd_input.configure(state=DISABLED)
            submit.configure(state=DISABLED)
            reset_btn.configure(state=NORMAL)
        except ValueError:
            md_input.delete(0, END)
            messagebox.showerror("Error", "โปรดกรอกค่าเป็นตัวเลขเท่านั้น")
    elif gd_data.get() != "":
        try:
            gd_cal = float(gd_data.get())
            result = (gd_cal/50000)*100000
            md_input.delete(0,END)
            md_input.insert(0,str(result))
            md_input.configure(state=DISABLED)
            submit.configure(state=DISABLED)
            reset_btn.configure(state=NORMAL)
        except ValueError:
            gd_input.delete(0, END)
            messagebox.showerror("Error", "โปรดกรอกค่าเป็นตัวเลขเท่านั้น")


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
                   bg="#343A40").pack(side=TOP, pady=25)
btn = tk.Button(root, text="คำนวณระยะทางจุด 2 จุด", command=haver_calc, font=config.fonts_menu, fg="#ffffff",
                bg=config.menu_button, width=50).pack(pady=3)
btn2 = tk.Button(root, text="คำนวณมาตราส่วนแผนที่ GD", command=gd_calc, font=config.fonts_menu, fg="#ffffff",
                 bg=config.menu_button, width=50).pack(pady=3)
btn3 = tk.Button(root, text="วิธีใช้โปรแกรม", command=howtouse, font=config.fonts_menu, fg="#ffffff", bg=config.menu_button,
                 width=50).pack(pady=3)
btn4 = tk.Button(root, text="ผู้จัดทำ", command=credit, font=config.fonts_menu, fg="#ffffff", bg=config.menu_button,
                 width=50).pack(pady=3)
vers = tk.Label(root, text=f"Version 1.0.2 {config.status()} ; Made from Python", font=(config.fonts_menu[0], 18),
                fg="#ffffff", bg="#343A40").pack(side=BOTTOM, pady=10)
root.mainloop()