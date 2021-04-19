from tkinter import *
from tkinter import ttk , messagebox
import tkinter as tk
import mysql.connector



def ADDPRODUCT():
    id = a.get()
    name = x.get()
    price = y.get()
    content = z.get()

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="coffee management")
    mycursor = mysqldb.cursor()


    try:
        sql = "insert into product (id,name,price,content) values (%s,%s,%s,%s) "
        value = (id, name, price, content)
        mycursor.execute(sql, value)
        mysqldb.commit()
        messagebox.showinfo("information", "Add product successfully")
        a.delete(0, END)
        x.delete(0, END)
        y.delete(0, END)
        z.delete(0, END)
        a.focus_set()
    except EXCEPTION as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()


def EDITPRODUCT():
    id = a.get()
    name = x.get()
    price = y.get()
    content = z.get()

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="coffee management")
    mycursor = mysqldb.cursor()


    try:
        sql = "Update product set name = %s, price = %s , content = %s where id = %s"
        value = (name, price, content, id)
        mycursor.execute(sql, value)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("information", "Update product successfully")
        a.delete(0, END)
        x.delete(0, END)
        y.delete(0, END)
        z.delete(0, END)
        a.focus_set()
    except EXCEPTION as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()




def DELETEPRODUCT():
    id = a.get()

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="coffee management")
    mycursor = mysqldb.cursor()


    try:
        sql = "Delete from product where id = %s"
        value = (id,)
        mycursor.execute(sql, value)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("information", "Delete product successfully")
        a.delete(0, END)
        x.delete(0, END)
        y.delete(0, END)
        z.delete(0, END)
        a.focus_set()
    except EXCEPTION as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()

def SHOWTABLE():
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="coffee management")
    mycursor = mysqldb.cursor()
    mycursor.execute("select id,name,price,content from product ")
    product = mycursor.fetchall()
    print(product)

    for i, (id, name, price, content) in enumerate(product, start=1):
        Listbox.insert("", "end", values=(id, name, price, content))
        mysqldb.close()





def TAKEVALUE(event):
    a.delete(0, END)
    x.delete(0, END)
    y.delete(0, END)
    z.delete(0, END)
    row_id = Listbox.selection()[0]
    select = Listbox.set(row_id)
    a.insert(0, select['ID'])
    x.insert(0, select['NAME'])
    y.insert(0, select['PRICE'])
    z.insert(0, select['CONTENT'])



def ADDSTAFF():
    id = t.get()
    name = u.get()
    age = i.get()
    phone = o.get()
    address = p.get()

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="coffee management")
    mycursor = mysqldb.cursor()


    try:
        sql = "insert into staff (id,name,age,phone,address) values (%s,%s,%s,%s,%s) "
        value = (id, name, age, phone,address)
        mycursor.execute(sql, value)
        mysqldb.commit()
        messagebox.showinfo("information", "Add staff successfully")
        t.delete(0, END)
        u.delete(0, END)
        i.delete(0, END)
        o.delete(0, END)
        p.delete(0, END)
        t.focus_set()
    except EXCEPTION as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()


def EDITSTAFF():
    id = t.get()
    name = u.get()
    age = i.get()
    phone = o.get()
    address = p.get()

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="coffee management")
    mycursor = mysqldb.cursor()


    try:
        sql = "Update staff set name = %s, age = %s , phone = %s , address = %s where id = %s"
        value = (name, age, phone, address, id)
        mycursor.execute(sql, value)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("information", "Update staff successfully")
        t.delete(0, END)
        u.delete(0, END)
        i.delete(0, END)
        o.delete(0, END)
        p.delete(0, END)
        t.focus_set()
    except EXCEPTION as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()




def DELETESTAFF():
    id = t.get()

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="coffee management")
    mycursor = mysqldb.cursor()


    try:
        sql = "Delete from product where id = %s"
        value = (id,)
        mycursor.execute(sql, value)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("information", "Delete staff successfully")
        t.delete(0, END)
        u.delete(0, END)
        i.delete(0, END)
        o.delete(0, END)
        p.delete(0, END)
        t.focus_set()
    except EXCEPTION as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()

def SHOWTABLE2():
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="coffee management")
    mycursor = mysqldb.cursor()
    mycursor.execute("select id,name,age,phone,address from staff ")
    staff = mycursor.fetchall()
    print(staff)

    for i, (id, name, age , phone, address) in enumerate(staff, start=1):
        Listbox.insert("", "end", values=(id, name, age, phone, address ))
        mysqldb.close()


def TAKEVALUE2(event):
    t.delete(0, END)
    u.delete(0, END)
    i.delete(0, END)
    o.delete(0, END)
    p.delete(0, END)
    row_id = Listbox.selection()[0]
    select = Listbox.set(row_id)
    t.insert(0, select['ID'])
    u.insert(0, select['NAME'])
    i.insert(0, select['AGE'])
    o.insert(0, select['PHONE'])
    p.insert(0, select['ADDRESS'])


root = Tk()
root.title("Coffee Management")
root.geometry("500x500")

global a
global x
global y
global z

tk.Label(root, text="Product id").place(x=20,y=10)
Label(root, text="Product name").place(x=20,y=40)
Label(root, text="Product price").place(x=20,y=80)
Label(root, text="Product content").place(x=20,y=120)

a = Entry(root)
a.place(x=170, y=10)

x = Entry(root)
x.place(x=170, y=40)

y = Entry(root)
y.place(x=170, y=80)

z = Entry(root)
z.place(x=170, y=120)

Button(root,text="Add Product", command=ADDPRODUCT, height=4, width=14).place(x=20,y=200)
Button(root,text="Delete Product", command=DELETEPRODUCT, height=4, width=14).place(x=140,y=200)
Button(root,text="Edit Product", command=EDITPRODUCT, height=4, width=14).place(x=260,y=200)

cols=('ID', 'NAME', 'PRICE', 'CONTENT')
Listbox = ttk.Treeview(root, columns=cols, show='headings')

for col in cols:
    Listbox.heading(col, text=col)
    Listbox.grid(row=1, column=0, columnspan=2)
    Listbox.place(x=20, y=300)


global t
global u
global i
global o
global p

tk.Label(root, text="Staff id").place(x=420,y=10)
Label(root, text="Staff name").place(x=420,y=40)
Label(root, text="Staff age").place(x=420,y=80)
Label(root, text="Staff phone").place(x=420,y=120)
Label(root, text="Staff address").place(x=420,y=160)

t = Entry(root)
t.place(x=520, y=10)

u = Entry(root)
u.place(x=520, y=40)

i = Entry(root)
i.place(x=520, y=80)

o = Entry(root)
o.place(x=520, y=120)

p = Entry(root)
p.place(x=520, y=160)

Button(root,text="Add Staff", command=ADDSTAFF, height=4, width=14).place(x=420,y=200)
Button(root,text="Delete Staff", command=DELETESTAFF, height=4, width=14).place(x=540,y=200)
Button(root,text="Edit Staff", command=EDITSTAFF, height=4, width=14).place(x=660,y=200)

cols=('ID', 'NAME', 'AGE', 'PHONE', 'ADDRESS')
Listbox = ttk.Treeview(root, columns=cols, show='headings')

for col in cols:
    Listbox.heading(col, text=col)
    Listbox.grid(row=1, column=0, columnspan=2)
    Listbox.place(x=20, y=500)

SHOWTABLE2()
Listbox.bind('<Double-Button-1>', TAKEVALUE2)
SHOWTABLE()
Listbox.bind('<Double-Button-1>', TAKEVALUE)




















































root.mainloop()




