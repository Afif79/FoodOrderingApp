from tkinter import *
from tkinter import Toplevel
from tkinter import messagebox
from tkinter.font import Font
import pymysql
import time

# Main Window
master = Tk()
master.state('zoomed')
master.configure(background="#FFFFFF")
master.title("BurgerKing")
master.iconbitmap('bkLogo.ico')

# File
global f
f = open("fh.txt", "w+")

# Title
TitleFont = Font(family="Insaniburger", size=35)
title = Label(master, text="Burger King", fg="red", bg="white", font=TitleFont)
title.place(x=635, y=1)

# Title Logo
burgerking = PhotoImage(file="bkLogo.png")
burgerking_logo = Label(master, image=burgerking, bg="white")
burgerking_logo.place(x=10, y=10)

# Fonts
EntryFont = Font(family="Roboto", size='12')
LabelFont = Font(family="Insaniburger", size='14')

# Variable Declaration
global total, total_coke, total_burger1, total_burger2, total_burger3, total_burger4, total_fries, total_cfries, \
    total_floats, order, orderid
total = 0
total_coke, total_burger1, total_burger2, total_burger3, total_burger4, total_fries, total_cfries, total_floats = \
    0, 0, 0, 0, 0, 0, 0, 0
orderid = 0
global burger1_input
# Clock
time1 = ''
clock = Label(master, fg="red", bg="white", font=('Roboto', 15), anchor="center")
clock.place(x=670, y=50)


# Total Function
def total_price(price):
    global total
    total = total + price
    total_label2.config(text=total)
    print(total)


def burger1Fun():
    global burger1_input
    burger1_input = int(burger1_entry.get())
    burger1_input_a = burger1_input + 1
    burger1_entry.delete(0, 'end')
    burger1_entry.insert(0, burger1_input_a)


def burger1Fun2():
    global total_burger1, burger1_input, f
    burger1_input = int(burger1_entry.get())
    total_burger1 = total_burger1 + burger1_input
    f = open("fh.txt", "a+")
    # for line in f:
    #     if line.startswith("Veg Burger"):
    f.write("Veg Burger" + "\t\t\t\t        " + str(total_burger1) + "x\t\t\t\t  " + str((total_burger1 * 50)) + "\n")
    f.close()
    total_price(burger1_input * 50)
    # with open("yourfile.txt", "r") as f:
    #     lines = f.readlines()
    # with open("yourfile.txt", "w") as f:
    #     for line in lines:
    #         if line.strip("\n") != "Veg Burger:
    #             f.write(line)


def burger2Fun():
    burger2_input = int(burger2_entry.get())
    burger2_input_a = burger2_input + 1
    burger2_entry.delete(0, 'end')
    burger2_entry.insert(0, burger2_input_a)


def burger2Fun2():
    global total_burger2, f
    burger2_input = int(burger2_entry.get())
    total_burger2 = total_burger2 + burger2_input
    f = open("fh.txt", "a+")
    f.write(
        "Chicken Burger" + "\t\t\t\t        " + str(total_burger2) + "x\t\t\t\t  " + str((total_burger2 * 70)) + "\n")
    f.close()
    total_price(burger2_input * 70)


def burger3Fun():
    burger3_input = int(burger3_entry.get())
    burger3_input_a = burger3_input + 1
    burger3_entry.delete(0, 'end')
    burger3_entry.insert(0, burger3_input_a)


def burger3Fun2():
    global total_burger3, f
    burger3_input = int(burger3_entry.get())
    total_burger3 = total_burger3 + burger3_input
    f = open("fh.txt", "a+")
    f.write("Boss Whooper" + "\t\t\t\t        " + str(total_burger3) + "x\t\t\t\t " + str((total_burger3 * 150)) + "\n")
    f.close()
    total_price(burger3_input * 150)


def burger4Fun():
    burger4_input = int(burger4_entry.get())
    burger4_input_a = burger4_input + 1
    burger4_entry.delete(0, 'end')
    burger4_entry.insert(0, burger4_input_a)


def burger4Fun2():
    global total_burger4, f
    burger4_input = int(burger4_entry.get())
    total_burger4 = total_burger4 + burger4_input
    f = open("fh.txt", "a+")
    f.write("Chicken Chilly Whooper" + "\t\t\t\t        " + str(total_burger4) + "x\t\t\t\t " + str(
        (total_burger4 * 200)) + "\n")
    f.close()
    total_price(burger4_input * 200)


def friesFun():
    fries_input = int(fries_entry.get())
    fries_input_a = fries_input + 1
    fries_entry.delete(0, 'end')
    fries_entry.insert(0, fries_input_a)


def friesFun2():
    global total_fries, f
    fries_input = int(fries_entry.get())
    total_fries = total_fries + fries_input
    f = open("fh.txt", "a+")
    f.write("Fries" + "\t\t\t\t        " + str(total_fries) + "x\t\t\t\t  " + str((total_fries * 30)) + "\n")
    f.close()
    total_price(fries_input * 30)


def cfriesFun():
    cfries_input = int(cfries_entry.get())
    cfries_input_a = cfries_input + 1
    cfries_entry.delete(0, 'end')
    cfries_entry.insert(0, cfries_input_a)


def cfriesFun2():
    global total_cfries
    cfries_input = int(cfries_entry.get())
    total_cfries = total_cfries + cfries_input
    f = open("fh.txt", "a+")
    f.write("Cheese Fries" + "\t\t\t\t        " + str(total_cfries) + "x\t\t\t\t  " + str((total_cfries * 70)) + "\n")
    f.close()
    total_price(cfries_input * 70)


def cokeFun():
    coke_input = int(coke_qty.get())
    coke_input_a = coke_input + 1
    coke_qty.delete(0, 'end')
    coke_qty.insert(0, coke_input_a)


def cokeFun2():
    global total_coke, f
    coke_input = int(coke_qty.get())
    total_coke = total_coke + coke_input
    f = open("fh.txt", "a+")
    f.write("Coke" + "\t\t\t\t        " + str(total_coke) + "x\t\t\t\t  " + str((total_coke * 40)) + "\n")
    f.close()
    total_price(coke_input * 40)


def cokeFloatFun():
    floats_input = int(floats_entry.get())
    floats_input_a = floats_input + 1
    floats_entry.delete(0, 'end')
    floats_entry.insert(0, floats_input_a)


def cokeFloatFun2():
    global total_floats
    floats_input = int(floats_entry.get())
    total_floats = total_floats + floats_input
    f = open("fh.txt", "a+")
    f.write("Coke Float" + "\t\t\t\t        " + str(total_coke) + "x\t\t\t\t  " + str((total_coke * 60)) + "\n")
    f.close()
    total_price(floats_input * 60)


def bill():  # new window definition
    global f, total, order
    master.withdraw()
    bill = Toplevel(master)
    bill.configure(background="#FFFFFF")
    bill.title("BurgerKing")
    bill.iconbitmap('bkLogo.ico')
    width_of_window = 1200
    height_of_window = 790
    screen_width = master.winfo_screenwidth()
    screen_height = master.winfo_screenheight()
    x_coordinate = (screen_width / 2) - (width_of_window / 2)
    y_coordinate = (screen_height / 2) - (height_of_window / 2)
    bill.geometry("%dx%d+%d+%d" % (width_of_window, height_of_window, x_coordinate, y_coordinate))
    # Title Logo
    burgerking_logo1 = Label(bill, image=burgerking, bg="white")
    burgerking_logo1.place(x=10, y=10)
    # Title
    title2 = Label(bill, text="Burger King", fg="red", bg="white", font=TitleFont)
    title2.place(x=460, y=1)
    # Clock
    bill_time = time.strftime("%m/%d/%Y, %I:%M:%S")
    clock2 = Label(bill, fg="red", text=bill_time, bg="white", font=('Roboto', 15), anchor="center")
    clock2.place(x=490, y=50)
    # Items
    food_font = Font(family="Insaniburger", size='20')
    food_item = Label(bill, fg="red", bg="white", font=food_font, text="Food Item", anchor="center")
    food_item.place(x=50, y=150)
    food_qty = Label(bill, fg="red", bg="white", font=food_font, text="Quantity", anchor="center")
    food_qty.place(x=530, y=150)
    food_price = Label(bill, fg="red", bg="white", font=food_font, text="Price", anchor="center")
    food_price.place(x=1000, y=150)
    food_item1 = Text(bill, fg="red", bg="white", font=food_font, relief=FLAT)
    food_item1.place(x=40, y=200)
    f = open("fh.txt", "r")
    t = f.read()
    # food_item1.config(text=t)
    food_item1.insert(END, t)
    tt = "\n\nTotal\t\t\t\t\t\t\t\t  " + str(total)
    food_item1.insert(END, tt)
    f.close()
    confirm_button = Button(bill, image=order, borderwidth=0, bg="white", relief=FLAT, command=msg)
    confirm_button.place(x=450, y=600)
    print_username = Label(bill, text="Username", font=("InsaniBurger", "22"), fg="red", bg="white")
    print_username.place(x=50, y=105)
    print_ph_no = Label(bill, text="Phone No", font=("InsaniBurger", "22"), fg="red", bg="white")
    print_ph_no.place(x=1000, y=105)
    print_oi = Label(bill, text="Orderid", font=("InsaniBurger", "22"), fg="red", bg="white")
    print_oi.place(x=530, y=105)
    print_username.config(text=username_entry.get())
    print_ph_no.config(text=ph_no_entry.get())
    print_oi.config(text="ODD53618"+str(orderid))


def msg():
    messagebox.showinfo("Confirmed", "Your Order Will be Delivered Shortly")


def check():
    global orderid
    if total == 0:
        messagebox.showinfo("Alert", "Please Select Some Food first!")
    elif username_entry.get() == "":
        messagebox.showinfo("Alert", "Please Enter Username!")
    elif ph_no_entry.get() == "":
        messagebox.showinfo("Alert", "Please Enter Phone Number!")
    else:
        connection = pymysql.connect(host='localhost', user='root', password='', db='foodapp')
        cursor = connection.cursor()
        try:
            sql = "INSERT INTO userdata(username,phoneNo,TotalPrice)VALUES( '%s','%s','%s')" % (username_entry.get(), ph_no_entry.get(), total)
            cursor.execute(sql)
            orderid = cursor.lastrowid
            connection.commit()
        finally:
            connection.close()
        bill()


# Username
username_bg = PhotoImage(file="username.png")
username = Label(master, text="Username", font=LabelFont, fg="red", bg="white")
username.place(x=70, y=105)
username1 = Label(master, image=username_bg, borderwidth=0, bg="white", relief=SUNKEN)
username1.place(x=180, y=102)
username_entry = Entry(master, bd=2, font=EntryFont, width=26, fg="red", relief=FLAT)
username_entry.place(x=195, y=106)

# Phone No
ph_no = Label(master, text="Phone No", font=LabelFont, fg="red", bg="white")
ph_no.place(x=670, y=105)
ph_no1 = Label(master, image=username_bg, borderwidth=0, bg="white", relief=SUNKEN)
ph_no1.place(x=780, y=102)
ph_no_entry = Entry(master, bd=2, font=EntryFont, width=26, fg="red", relief=FLAT)
ph_no_entry.place(x=795, y=106)

# Burger 1 ImageButton
burger = PhotoImage(file="b.png")
burger_button1 = Button(master, image=burger, borderwidth=0, bg="white", command=burger1Fun)
burger_button1.place(x=10, y=150)
# Burger 1 Name And Price
vegBurger = Label(master, text="Veg Burger", fg="red", bg="white", font=LabelFont)
vegBurger.place(x=22, y=280)
vegBurgerPrice = Label(master, text="50₹", fg="red", bg="white", font=LabelFont)
vegBurgerPrice.place(x=200, y=280)
# Burger 1 Entry Fields
burger_qty = PhotoImage(file="qty_button3.png")
burger_qty_button1 = Button(master, image=burger_qty, borderwidth=0, bg="white", command=burger1Fun2)
burger_qty_button1.place(x=180, y=202)
burger1DefaultValue = IntVar(master, value=0)
burger1_entry = Entry(master, bd=2, font=EntryFont, width=3, textvariable=burger1DefaultValue, fg="red", relief=FLAT)
burger1_entry.place(x=185, y=207)

# Burger 2 ImageButton
burger2 = PhotoImage(file="b2.png")
burger_button2 = Button(master, image=burger2, borderwidth=0, bg="white", command=burger2Fun)
burger_button2.place(x=10, y=320)
# Burger 2 Name And Price
cBurger = Label(master, text="Chicken Burger", fg="red", bg="white", font=LabelFont)
cBurger.place(x=8, y=450)
cBurgerPrice = Label(master, text="70₹", fg="red", bg="white", font=LabelFont)
cBurgerPrice.place(x=200, y=450)
# Burger 2 Entry Fields
burger_qty_button2 = Button(master, image=burger_qty, borderwidth=0, bg="white", height=32, command=burger2Fun2)
burger_qty_button2.place(x=180, y=374)
burger2DefaultValue = IntVar(master, value=0)
burger2_entry = Entry(master, bd=2, font=EntryFont, width=3, textvariable=burger2DefaultValue, fg="red", relief=FLAT)
burger2_entry.place(x=185, y=379)

# Burger 3 ImageButton
burger3 = PhotoImage(file="b3.png")
burger_button3 = Button(master, image=burger3, borderwidth=0, bg="white", command=burger3Fun)
burger_button3.place(x=10, y=480)
# Burger 2 Name And Price
BossBurger = Label(master, text="Boss Whooper", fg="red", bg="white", font=LabelFont)
BossBurger.place(x=10, y=610)
BossBurgerPrice = Label(master, text="150₹", fg="red", bg="white", font=LabelFont)
BossBurgerPrice.place(x=195, y=610)
# Burger 3 Entry Fields
burger_qty_button3 = Button(master, image=burger_qty, borderwidth=0, bg="white", height=32, command=burger3Fun2)
burger_qty_button3.place(x=180, y=537)
burger3DefaultValue = IntVar(master, value=0)
burger3_entry = Entry(master, bd=2, font=EntryFont, width=3, textvariable=burger3DefaultValue, fg="red", relief=FLAT)
burger3_entry.place(x=185, y=542)

# Burger 4 ImageButton
burger4 = PhotoImage(file="b4.png")
burger_button4 = Button(master, image=burger4, borderwidth=0, bg="white", command=burger4Fun)
burger_button4.place(x=1, y=650)
# Burger 2 Name And Price
cBossBurger = Label(master, text="Chilly Cheese \nWhooper", fg="red", bg="white", font=LabelFont)
cBossBurger.place(x=13, y=770)
cBossBurgerPrice = Label(master, text="200₹", fg="red", bg="white", font=LabelFont)
cBossBurgerPrice.place(x=190, y=770)
# Burger 4 Entry Fields
burger_qty_button4 = Button(master, image=burger_qty, borderwidth=0, bg="white", height=32, command=burger4Fun2)
burger_qty_button4.place(x=180, y=692)
burger4DefaultValue = IntVar(master, value=0)
burger4_entry = Entry(master, bd=2, font=EntryFont, width=3, textvariable=burger4DefaultValue, fg="red", relief=FLAT)
burger4_entry.place(x=185, y=697)

# Fries ImageButton
fries = PhotoImage(file="fries.png")
fries_button = Button(master, image=fries, borderwidth=0, bg="white", command=friesFun)
fries_button.place(x=540, y=150)
# Fries Name And Price
sfries = Label(master, text="Reg Fries", fg="red", bg="white", font=LabelFont)
sfries.place(x=555, y=280)
sfriesPrice = Label(master, text="30₹", fg="red", bg="white", font=LabelFont)
sfriesPrice.place(x=695, y=280)
# Fries Entry Fields
fries_qty_button = Button(master, image=burger_qty, borderwidth=0, bg="white", height=32, command=friesFun2)
fries_qty_button.place(x=680, y=202)
friesDefaultValue = IntVar(master, value=0)
fries_entry = Entry(master, bd=2, font=EntryFont, width=3, textvariable=friesDefaultValue, fg="red", relief=FLAT)
fries_entry.place(x=685, y=207)

# Fries 2 ImageButton
fries2 = PhotoImage(file="fries2.png")
fries_button2 = Button(master, image=fries2, borderwidth=0, bg="white", command=cfriesFun)
fries_button2.place(x=530, y=340)
# Fries 2 Name And Price
cfries = Label(master, text="Cheese fries", fg="red", bg="white", font=LabelFont)
cfries.place(x=535, y=450)
cfriesPrice = Label(master, text="70₹", fg="red", bg="white", font=LabelFont)
cfriesPrice.place(x=695, y=450)
# Fries 2 Entry Fields
cfries_qty_button = Button(master, image=burger_qty, borderwidth=0, bg="white", height=32, command=cfriesFun2)
cfries_qty_button.place(x=680, y=372)
cfriesDefaultValue = IntVar(master, value=0)
cfries_entry = Entry(master, bd=2, font=EntryFont, width=3, textvariable=cfriesDefaultValue, fg="red", relief=FLAT)
cfries_entry.place(x=685, y=377)

# Coke ImageButton
coke = PhotoImage(file="coke.png")
coke_button = Button(master, image=coke, borderwidth=0, bg="white", command=cokeFun)
coke_button.place(x=1040, y=150)
# Coke Name And Price
coke_name = Label(master, text="Reg Coke", fg="red", bg="white", font=LabelFont)
coke_name.place(x=1055, y=280)
coke_price = Label(master, text="40₹", fg="red", bg="white", font=LabelFont)
coke_price.place(x=1200, y=280)
# Coke Entry Fields
coke_qty_button = Button(master, image=burger_qty, borderwidth=0, bg="white", height=32, command=cokeFun2)
coke_qty_button.place(x=1180, y=202)
cokeDefaultValue = IntVar(master, value=0)
coke_qty = Entry(master, bd=2, font=EntryFont, width=3, fg="red", textvariable=cokeDefaultValue, relief=FLAT)
coke_qty.place(x=1185, y=207)

# Floats ImageButton
floats = PhotoImage(file="floats.png")
floats_button = Button(master, image=floats, borderwidth=0, bg="white", command=cokeFloatFun)
floats_button.place(x=1040, y=320)
# Floats Name And Price
floats_name = Label(master, text="Coke Float", fg="red", bg="white", font=LabelFont)
floats_name.place(x=1045, y=450)
floats_Price = Label(master, text="60₹", fg="red", bg="white", font=LabelFont)
floats_Price.place(x=1200, y=450)
# Floats Entry Fields
floats_qty_button = Button(master, image=burger_qty, borderwidth=0, bg="white", height=32, command=cokeFloatFun2)
floats_qty_button.place(x=1180, y=372)
coke2DefaultValue = IntVar(master, value=0)
floats_entry = Entry(master, bd=2, font=EntryFont, width=3, textvariable=coke2DefaultValue, fg="red", relief=FLAT)
floats_entry.place(x=1185, y=377)

# Total
total_label = Label(master, text="Total :", fg="red", bg="white", font=("Insaniburger", 23))
total_label.place(x=810, y=550)
total_label2 = Label(master, text=total, fg="red", bg="white", font=("Insaniburger", 23))
total_label2.place(x=950, y=551)
total_label3 = Label(master, text='₹', fg="red", bg="white", font=("Insaniburger", 23))
total_label3.place(x=930, y=551)
order = PhotoImage(file="order.png")
order_button = Button(master, image=order, borderwidth=0, bg="white", relief=FLAT, command=check)
order_button.place(x=730, y=600)


# Clock Function
def tick():
    global time1
    # get the current local time from the PC
    time2 = time.strftime("%m/%d/%Y, %I:%M:%S")
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
    # calls itself every 200 milliseconds
    clock.after(200, tick)


tick()
mainloop()
