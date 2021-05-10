from tkinter import *
from tkinter import ttk, messagebox
import tkinter as tk
import mysql.connector
from PIL import ImageTk
from PIL import Image
import tkinter.font as font


# validation
def Error():
    messagebox.showinfo("information", "All field required")

def Error2():
    messagebox.showinfo("information", "Product already exist")

def Error3():
    messagebox.showinfo("information", "Staff already exist")

def Error4():
    messagebox.showinfo("information", "Customer already exist")

def Error5():
    messagebox.showinfo("information", "Ingredient already exist")

def Error6():
    messagebox.showinfo("information", "We dont have that product")

def Error7():
    messagebox.showinfo("information", "We killed that staff")

def Error8():
    messagebox.showinfo("information", "We killed that customer")

def Error9():
    messagebox.showinfo("information", "We dont have that ingredient")


def ADDING():


    name = ingname.get()
    quantity = ingquantity.get()
    price = ingprice.get()

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="coffee management")
    mycursor = mysqldb.cursor()

    try:
        sql = "insert into ingredient (name,quantity,price) values (%s,%s,%s) "
        value = (name, quantity, price)
        mycursor.execute(sql, value)
        mysqldb.commit()
        messagebox.showinfo("information", "Add ingredient successfully")

        ingname.delete(0, END)
        ingquantity.delete(0, END)
        ingprice.delete(0, END)
        ingname.focus_set()
    except EXCEPTION as e:
        print(e)
        mysqldb.rollback()
    mysqldb.close()


def EDITING():

    name = ingname.get()
    quantity = ingquantity.get()
    price = ingprice.get()

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="coffee management")
    mycursor = mysqldb.cursor()

    try:
        sql = "Update ingredient set  price = %s , quantity = %s where name = %s"
        value = (price, quantity, name)
        mycursor.execute(sql, value)
        mysqldb.commit()
        messagebox.showinfo("information", "Update ingredient successfully")

        ingname.delete(0, END)
        ingquantity.delete(0, END)
        ingprice.delete(0, END)
        ingname.focus_set()

    except EXCEPTION as e:
        print(e)
        mysqldb.rollback()
    mysqldb.close()

def DELETEING():

    name = ingname.get()

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="coffee management")
    mycursor = mysqldb.cursor()

    try:
        sql = "Delete from ingredient where name = %s"
        value = (name,)
        mycursor.execute(sql, value)
        mysqldb.commit()
        messagebox.showinfo("information", "Delete ingredient successfully")

        ingname.delete(0, END)
        ingquantity.delete(0, END)
        ingprice.delete(0, END)
        ingname.focus_set()
    except EXCEPTION as e:
        print(e)
        mysqldb.rollback()
    mysqldb.close()


def Validate_ADDING():
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="coffee management")
    mycursor = mysqldb.cursor()
    name = ingname.get()
    value = (name,)
    sql = "SELECT COUNT(*) FROM ingredient where name = %s"
    result = mycursor.execute(sql, value)
    result = mycursor.fetchone()


    name = ingname.get()
    quantity = ingquantity.get()
    price = ingprice.get()
    count = (0,)

    if name == "":
        Error()
    elif price == "":
        Error()
    elif quantity == "":
        Error()
    elif result == count:
        return ADDING()
    elif result > count:
        Error5()

        proname.delete(0, END)
        proprice.delete(0, END)
        procont.delete(0, END)
        proname.focus_set()
def Validate_EDITING():

    name = ingname.get()
    quantity = ingquantity.get()
    price = ingprice.get()
    count = (0,)

    if name == "":
        Error()
    elif price == "":
        Error()
    elif quantity == "":
        Error()
    else:
        return EDITING()


        ingname.delete(0, END)
        ingquantity.delete(0, END)
        ingprice.delete(0, END)
        ingname.focus_set()



def ingwindow():

    ingredient = tk.Toplevel()
    ingredient.title("Ingredient")
    ingredient.geometry("900x900")



    global ingid
    global ingname
    global ingquantity
    global ingprice

    Label(ingredient, text="Ingredient name", bg="#FFFFCC").place(x=160, y=20)
    Label(ingredient, text="Ingredient quantity", bg="#FFFFCC").place(x=160, y=71)
    Label(ingredient, text="Ingredient price", bg="#FFFFCC").place(x=160, y=120)

    ingname = Entry(ingredient)
    ingname.place(x=280, y=20)

    ingquantity = Entry(ingredient)
    ingquantity.place(x=280, y=71)

    ingprice = Entry(ingredient)
    ingprice.place(x=280, y=120)

    Button(ingredient, text="Add Ingredient", command=Validate_ADDING, bg="#7FFF00", height=4, width=14).place(x=160, y=200)
    Button(ingredient, text="Delete Ingredient", command=DELETEING, bg="#FF6347", height=4, width=14).place(x=320, y=200)
    Button(ingredient, text="Edit Ingredient", command=Validate_EDITING, bg="#87CEFA", height=4, width=14).place(x=480, y=200)


    ## show table
    tree_frame = Frame(ingredient)
    tree_frame.pack(pady=20)
    tree_scroll = Scrollbar(tree_frame)
    tree_scroll.pack(side=RIGHT, fill=Y)
    Table_ing = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, height="6")
    Table_ing['show'] = 'headings'
    Table_ing['columns'] = ("ID", "Name", "Quantity", "Price")
    Table_ing.column("ID", anchor=CENTER, width=80)
    Table_ing.column("Name", anchor=W, width=140)
    Table_ing.column("Quantity", anchor=CENTER, width=140)
    Table_ing.column("Price", anchor=W, width=140)
    Table_ing.heading("ID", text="ID", anchor=CENTER)
    Table_ing.heading("Name", text="Name", anchor=CENTER)
    Table_ing.heading("Quantity", text="Quantity", anchor=CENTER)
    Table_ing.heading("Price", text="Price", anchor=CENTER)
    Table_ing.pack()
    tree_scroll.config(command=Table_ing.yview)
    tree_frame.place(x=155,y=350)
    ##end show


    ## search ing
    tree_frame = Frame(ingredient)
    tree_frame.pack(pady=20)
    tree_scroll = Scrollbar(tree_frame)
    tree_scroll.pack(side=RIGHT, fill=Y)
    Table_ingsearch = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, height="3")
    Table_ingsearch['show'] = 'headings'
    Table_ingsearch['columns'] = ("ID", "Name", "Quantity", "Price")
    Table_ingsearch.column("ID", anchor=CENTER, width=80)
    Table_ingsearch.column("Name", anchor=W, width=140)
    Table_ingsearch.column("Quantity", anchor=CENTER, width=140)
    Table_ingsearch.column("Price", anchor=W, width=140)
    Table_ingsearch.heading("ID", text="ID", anchor=CENTER)
    Table_ingsearch.heading("Name", text="Name", anchor=CENTER)
    Table_ingsearch.heading("Quantity", text="Quantity", anchor=CENTER)
    Table_ingsearch.heading("Price", text="Price", anchor=CENTER)
    Table_ingsearch.pack()
    tree_scroll.config(command=Table_ingsearch.yview)
    tree_frame.place(x=155, y=610)

    def searching():
        mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="coffee management")
        mycursor = mysqldb.cursor()

        selected = drop.get()
        sql = ""
        if selected == "Search By ...":
            test = Label(ingredient, text="Please choose a selection !!")
            test.place(x=155,y=580)
        if selected == "ID":
            sql = "Select * from ingredient where id = %s"

        if selected == "Name":
            sql = "Select * from ingredient where name = %s"

        if selected == "Price":
            sql = "Select * from ingredient where price = %s"

        if selected == "Quantity":
            sql = "Select * from ingredient where quantity = %s"

        searched = search_box.get()

        name = (searched,)
        result = mycursor.execute(sql, name)
        result = mycursor.fetchall()

        x = Table_ingsearch.get_children()
        for item in x:
            Table_ingsearch.delete(item)

        for i, (id, name, quantity, price) in enumerate(result, start=1):
            Table_ingsearch.insert("", "end", values=(id, name, quantity, price))
        mysqldb.close()

        if searched == "":
            test2 = Label(ingredient, text="Please enter the value in search box !!")
            test2.place(x=155, y=580)
        elif not result:
            Error9()


    # entrybox
    search_box = Entry(ingredient)
    search_box.place(x=290,y=550)
    search_box_label = Label(ingredient, text="Search ingredient")
    search_box_label.place(x=155,y=550)
    search_button = Button(ingredient, text="Search ingredient", command=searching)
    search_button.place(x=600,y=550)





    # dropmenuiproduct
    drop = ttk.Combobox(ingredient, value=["Search By ...", "ID", "Name", "Quantity", "Price"])
    drop.current(0)
    drop.place(x=430,y=550)
    ## end search product



##table product
    def TABLEINGREDIENT():

        mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="coffee management")
        mycursor = mysqldb.cursor()
        mycursor.execute("select id,name,quantity,price from ingredient ")
        result = mycursor.fetchall()


        for i, (id, name, quantity, price) in enumerate(result, start=1):
            Table_ing.insert("", "end", values=(id, name, quantity, price))
        mysqldb.close()


    def TAKEVALUE4(event):

        ingname.delete(0, END)
        ingquantity.delete(0, END)
        ingprice.delete(0, END)
        row_ingname = Table_ing.selection()[0]
        select = Table_ing.set(row_ingname)
        ingname.insert(0, select['Name'])
        ingquantity.insert(0, select['Quantity'])
        ingprice.insert(0, select['Price'])

    ##end table product

    TABLEINGREDIENT()
    Table_ing.bind('<Double-Button-1>', TAKEVALUE4)


##validate add product
def Validate_ADD():
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="coffee management")
    mycursor = mysqldb.cursor()
    name = proname.get()
    value = (name,)
    sql = "SELECT COUNT(*) FROM product where name = %s"
    result = mycursor.execute(sql, value)
    result = mycursor.fetchone()


    name = proname.get()
    price = proprice.get()
    content = procont.get()
    count = (0,)

    if name == "":
        Error()
    elif price == "":
        Error()
    elif content == "":
        Error()
    elif result == count:
        return ADDPRODUCT()
    elif result > count:
        Error2()

        proname.delete(0, END)  
        proprice.delete(0, END) 
        procont.delete(0, END)  
        proname.focus_set()


##validate edit product
def Validate_EDIT():

    name = proname.get()
    price = proprice.get()
    content = procont.get()
    count = (0,)

    if name == "":
        Error()
    elif price == "":
        Error()
    elif content == "":
        Error()
    else:
        return EDITPRODUCT()


        proname.delete(0, END)
        proprice.delete(0, END)
        procont.delete(0, END)
        proname.focus_set()


##validate add staff
def Validate_ADDST():
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="coffee management")
    mycursor = mysqldb.cursor()
    name = stname.get()
    value = (name,)
    sql = "SELECT COUNT(*) FROM staff where name = %s"
    result = mycursor.execute(sql, value)
    result = mycursor.fetchone()


    name = stname.get()
    phone = stphone.get()
    address = stadd.get()
    count = (0,)


    if name == "":
        Error()
    elif phone == "":
        Error()
    elif address == "":
        Error()
    elif result == count:
        return ADDSTAFF()
    elif result > count:
        Error3()

        stname.delete(0, END)
        stphone.delete(0, END)
        stadd.delete(0, END)
        stname.focus_set()



##validate edit staff
def Validate_EDITST():

    name = stname.get()
    phone = stphone.get()
    address = stadd.get()
    count = (0,)

    if name == "":
        Error()
    elif phone == "":
        Error()
    elif address == "":
        Error()
    else:
        return EDITSTAFF()

        stname.delete(0, END)
        stphone.delete(0, END)
        stadd.delete(0, END)
        stname.focus_set()

##validate add cus
def Validate_ADDCS():
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="coffee management")
    mycursor = mysqldb.cursor()


    name = csname.get()
    value = (name,)
    sql = "SELECT COUNT(*) FROM customer where name = %s"
    result = mycursor.execute(sql, value)
    result = mycursor.fetchone()

    name = csname.get()
    phone = csphone.get()
    product_buy = cspro.get()
    date_buy = csdate.get()
    count = (0,)

    if name =="":
        Error()
    elif phone =="":
        Error()
    elif product_buy =="":
        Error()
    elif csdate =="":
        date_buy()
    elif result == count:
        return ADDCUSTOMER()
    elif result > count:
        Error4()
        csname.delete(0, END)
        csphone.delete(0, END)
        cspro.delete(0, END)
        csdate.delete(0, END)
        csname.focus_set()



##validate edit cus
def Validate_EDITCS():

    name = csname.get()
    phone = csphone.get()
    product_buy = cspro.get()
    date_buy = csdate.get()

    if name =="":
        Error()
    elif phone =="":
        Error()
    elif product_buy =="":
        Error()
    elif date_buy =="":
        Error()
    else:
        return EDITCUSTOMER()



## CRUD product
def ADDPRODUCT():


    name = proname.get()
    price = proprice.get()
    content = procont.get()

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="coffee management")
    mycursor = mysqldb.cursor()

    try:
        sql = "insert into product (name,price,content) values (%s,%s,%s) "
        value = (name, price, content)
        mycursor.execute(sql, value)
        mysqldb.commit()
        messagebox.showinfo("information", "Add product successfully")

        proname.delete(0, END)
        proprice.delete(0, END)
        procont.delete(0, END)
        proname.focus_set()
    except EXCEPTION as e:
        print(e)
        mysqldb.rollback()
    mysqldb.close()


def EDITPRODUCT():

    name = proname.get()
    price = proprice.get()
    content = procont.get()

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="coffee management")
    mycursor = mysqldb.cursor()

    try:
        sql = "Update product set  price = %s , content = %s where name = %s"
        value = (price, content, name)
        mycursor.execute(sql, value)
        mysqldb.commit()
        messagebox.showinfo("information", "Update product successfully")

        proname.delete(0, END)
        proprice.delete(0, END)
        procont.delete(0, END)
        proname.focus_set()
    except EXCEPTION as e:
        print(e)
        mysqldb.rollback()
    mysqldb.close()


def DELETEPRODUCT():

    name = proname.get()

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="coffee management")
    mycursor = mysqldb.cursor()

    try:
        sql = "Delete from product where name = %s"
        value = (name,)
        mycursor.execute(sql, value)
        mysqldb.commit()
        messagebox.showinfo("information", "Delete product successfully")

        proname.delete(0, END)
        proprice.delete(0, END)
        procont.delete(0, END)
        proname.focus_set()
    except EXCEPTION as e:
        print(e)
        mysqldb.rollback()
    mysqldb.close()
##end crud product


def search_product():

    search_products = Tk()
    search_products.title("Search Product")
    search_products.geometry("750x250")


    tree_frame = Frame(search_products)
    tree_frame.pack(pady=20)
    tree_scroll = Scrollbar(tree_frame)
    tree_scroll.pack(side=RIGHT, fill=Y)
    Table_product = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, height="3")
    Table_product['show'] = 'headings'
    Table_product['columns'] = ("ID", "Name", "Price", "Content")
    Table_product.column("ID", anchor=CENTER, width=80)
    Table_product.column("Name", anchor=W, width=140)
    Table_product.column("Price", anchor=CENTER, width=140)
    Table_product.column("Content", anchor=W, width=140)
    Table_product.heading("ID", text="ID", anchor=CENTER)
    Table_product.heading("Name", text="Name", anchor=CENTER)
    Table_product.heading("Price", text="Price", anchor=CENTER)
    Table_product.heading("Content", text="Content", anchor=CENTER)
    Table_product.pack()
    tree_scroll.config(command=Table_product.yview)
    tree_frame.place(x=20,y=70)


    def search():
        mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="coffee management")
        mycursor = mysqldb.cursor()

        selected = drop.get()
        sql = ""
        if selected == "Search By ...":
            test = Label(search_products, text="Please choose a selection !!")
            test.grid(row=3, column=0)
        if selected == "ID":
            sql = "Select * from product where id = %s"

        if selected == "Name":
            sql = "Select * from product where name = %s"

        if selected == "Price":
            sql = "Select * from product where price = %s"

        if selected == "Content":
            sql = "Select * from product where content = %s"

        searched = search_box.get()

        name = (searched,)
        result = mycursor.execute(sql, name)
        result = mycursor.fetchall()

        x = Table_product.get_children()
        for item in x:
            Table_product.delete(item)

        for i, (id, name, price, content) in enumerate(result, start=1):
            Table_product.insert("", "end", values=(id, name, price, content))
        mysqldb.close()

        if searched == "":
            test2 = Label(search_products, text="Please enter value in search box !!")
            test2.grid(row=3, column=0)
        elif not result:
            Error6()



    # entrybox
    search_box = Entry(search_products)
    search_box.grid(row=0, column=1, padx=10, pady=10)
    search_box_label = Label(search_products, text="Search product  ")
    search_box_label.grid(row=0, column=0, padx=10, pady=10)
    search_button = Button(search_products, text="Search product", command=search)
    search_button.grid(row=0, column=4, padx=10)

    # dropmenuiproduct
    drop = ttk.Combobox(search_products, value=["Search By ...", "ID", "Name", "Price", "Content"])
    drop.current(0)
    drop.grid(row=0, column=2)
## end search product


##table product
def TABLEPRODUCT():

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="coffee management")
    mycursor = mysqldb.cursor()
    mycursor.execute("select id,name,price,content from product ")
    product = mycursor.fetchall()


    for i, (id, name, price, content) in enumerate(product, start=1):
        Table_product.insert("", "end", values=(id, name, price, content))
    mysqldb.close()


def TAKEVALUE(event):

    proname.delete(0, END)
    proprice.delete(0, END)
    procont.delete(0, END)
    row_name = Table_product.selection()[0]
    select = Table_product.set(row_name)

    proname.insert(0, select['Name'])
    proprice.insert(0, select['Price'])
    procont.insert(0, select['Content'])

##end table product

## crud staff
def ADDSTAFF():

    name = stname.get()
    phone = stphone.get()
    address = stadd.get()

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="coffee management")
    mycursor = mysqldb.cursor()

    try:
        sql = "insert into staff (name,phone,address) values (%s,%s,%s) "
        value = (name, phone, address)
        mycursor.execute(sql, value)
        mysqldb.commit()
        messagebox.showinfo("information", "Add staff successfully")

        stname.delete(0, END)
        stphone.delete(0, END)
        stadd.delete(0, END)
        stname.focus_set()
    except EXCEPTION as e:
        print(e)
        mysqldb.rollback()
    mysqldb.close()


def EDITSTAFF():

    name = stname.get()
    phone = stphone.get()
    address = stadd.get()

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="coffee management")
    mycursor = mysqldb.cursor()

    try:
        sql = "Update staff set  phone = %s , address = %s where name = %s"
        value = (phone, address, name)
        mycursor.execute(sql, value)
        mysqldb.commit()
        messagebox.showinfo("information", "Update staff successfully")

        stname.delete(0, END)
        stphone.delete(0, END)
        stadd.delete(0, END)
        stname.focus_set()
    except EXCEPTION as e:
        print(e)
        mysqldb.rollback()
    mysqldb.close()


def DELETESTAFF():

    name = stname.get()

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="coffee management")
    mycursor = mysqldb.cursor()

    try:
        sql = "Delete from staff where id = %s"
        value = (id,)
        mycursor.execute(sql, value)
        mysqldb.commit()
        messagebox.showinfo("information", "Delete staff successfully")

        stname.delete(0, END)
        stphone.delete(0, END)
        stadd.delete(0, END)
        stname.focus_set()
    except EXCEPTION as e:
        print(e)
        mysqldb.rollback()
    mysqldb.close()
##end crud staff



# search staff
def search_staff():

    search_staffs = Tk()
    search_staffs.title("Search Staff")
    search_staffs.geometry("750x250")


    tree_frame = Frame(search_staffs)
    tree_frame.pack(pady=20)
    tree_scroll = Scrollbar(tree_frame)
    tree_scroll.pack(side=RIGHT, fill=Y)
    Table_staff = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, height="3")
    Table_staff['columns'] = ("ID", "Name", "Phone", "Address")
    Table_staff['show'] = 'headings'
    Table_staff.column("ID", anchor=CENTER, width=80)
    Table_staff.column("Name", anchor=W, width=140)
    Table_staff.column("Phone", anchor=CENTER, width=140)
    Table_staff.column("Address", anchor=W, width=140)
    Table_staff.heading("ID", text="ID", anchor=CENTER)
    Table_staff.heading("Name", text="Name", anchor=CENTER)
    Table_staff.heading("Phone", text="Phone", anchor=CENTER)
    Table_staff.heading("Address", text="Address", anchor=CENTER)
    Table_staff.pack()
    tree_scroll.config(command=Table_staff.yview)
    tree_frame.place(x=20,y=80)

    def searchstaff():
        mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="coffee management")
        mycursor = mysqldb.cursor()

        selected = drop.get()
        sql = ""
        if selected == "Search By ...":
            test = Label(search_staffs, text="Please choose a selection !!")
            test.grid(row=3, column=0)

        if selected == "ID":
            sql = "Select * from staff where id = %s"

        if selected == "Name":
            sql = f"Select * from staff where name = %s"

        if selected == "Phone":
            sql = "Select * from staff where phone = %s"

        if selected == "Address":
            sql = "Select * from staff where address = %s"

        searched = search_box.get()

        name = (searched,)

        result = mycursor.execute(sql, name)
        result = mycursor.fetchall()

        x = Table_staff.get_children()
        for item in x:
            Table_staff.delete(item)

        for i, (id, name, phone, address) in enumerate(result, start=1):
            Table_staff.insert("", "end", values=(id, name, phone, address))
        mysqldb.close()

        if searched == "":
            test2 = Label(search_staffs, text="Please enter value in search box !!")
            test2.grid(row=3, column=0)
        elif not result:
            Error7()


    # entrybox
    search_box = Entry(search_staffs)
    search_box.grid(row=0, column=1, padx=10, pady=10)
    search_box_label = Label(search_staffs, text="Search staff  ")
    search_box_label.grid(row=0, column=0, padx=10, pady=10)
    search_button = Button(search_staffs, text="Search staff", command=searchstaff)
    search_button.grid(row=0, column=4, padx=10)

    # dropmenuistaff
    drop = ttk.Combobox(search_staffs, value=["Search By ...", "ID", "Name", "Phone","Address"])
    drop.current(0)
    drop.grid(row=0, column=2)
##end search staff



## table staff
def TABLESTAFF():
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="coffee management")
    mycursor = mysqldb.cursor()
    mycursor.execute("select id,name,phone,address from staff ")
    staff = mycursor.fetchall()



    for i, (id, name, phone, address) in enumerate(staff, start=1):
        Table_staff.insert("", "end", values=(id, name, phone, address))
    mysqldb.close()


def TAKEVALUE2(event):

    stname.delete(0, END)
    stphone.delete(0, END)
    stadd.delete(0, END)
    row_name = Table_staff.selection()[0]
    select = Table_staff.set(row_name)
    stname.insert(0, select['Name'])
    stphone.insert(0, select['Phone'])
    stadd.insert(0, select['Address'])

##end table staff


## crud cs
def ADDCUSTOMER():

    name = csname.get()
    phone = csphone.get()
    product_buy = cspro.get()
    date_buy = csdate.get()

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="coffee management")
    mycursor = mysqldb.cursor()

    try:
        sql = "insert into customer (name,phone,product_buy,date_buy) values (%s,%s,%s,%s) "
        value = (name, phone, product_buy, date_buy)
        mycursor.execute(sql, value)
        mysqldb.commit()
        messagebox.showinfo("information", "Add customer successfully")
        csname.delete(0, END)
        csphone.delete(0, END)
        cspro.delete(0, END)
        csdate.delete(0, END)
        csname.focus_set()
    except EXCEPTION as e:
        print(e)
        mysqldb.rollback()
    mysqldb.close()



def EDITCUSTOMER():

    name = csname.get()
    phone = csphone.get()
    product_buy = cspro.get()
    date_buy = csdate.get()

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="coffee management")
    mycursor = mysqldb.cursor()

    try:
        sql = "Update customer set phone = %s, product_buy = %s , date_buy = %s where name = %s"
        value = (phone, product_buy, date_buy, name)
        mycursor.execute(sql, value)
        mysqldb.commit()
        messagebox.showinfo("information", "Update customer successfully")
        csname.delete(0, END)
        csphone.delete(0, END)
        cspro.delete(0, END)
        csdate.delete(0, END)
        csname.focus_set()
    except EXCEPTION as e:
        print(e)
        mysqldb.rollback()
    mysqldb.close()

def DELETECS():
    name = csname.get()

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="coffee management")
    mycursor = mysqldb.cursor()

    try:
        sql = "Delete from customer where name = %s"
        value = (name,)
        mycursor.execute(sql, value)
        mysqldb.commit()
        messagebox.showinfo("information", "Delete customer successfully")
        csname.delete(0, END)
        csphone.delete(0, END)
        cspro.delete(0, END)
        csdate.delete(0, END)
        csname.focus_set()
    except EXCEPTION as e:
        print(e)
        mysqldb.rollback()
    mysqldb.close()
##end crud cus


##table cus
def TABLECUSTOMER():

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="coffee management")
    mycursor = mysqldb.cursor()
    mycursor.execute("select name,phone,product_buy,date_buy from customer ")
    customer = mycursor.fetchall()


    for i, (name, phone, product_buy,date_buy) in enumerate(customer, start=1):
        Table_customer.insert("", "end", values=(name, phone, product_buy,date_buy))
    mysqldb.close()


def TAKEVALUE3(event):
    csname.delete(0, END)
    csphone.delete(0, END)
    cspro.delete(0, END)
    csdate.delete(0, END)
    row_name = Table_customer.selection()[0]
    select = Table_customer.set(row_name)
    csname.insert(0, select['Name'])
    csphone.insert(0, select['Phone'])
    cspro.insert(0, select['ProductBuy'])
    csdate.insert(0, select['DateBuy'])
##end table cus


##search customer
def search_customer():

    search_customers = Tk()
    search_customers.title("Search Customer")
    search_customers.geometry("750x250")

    tree_frame = Frame(search_customers)
    tree_frame.pack(pady=20)
    tree_scroll = Scrollbar(tree_frame)
    tree_scroll.pack(side=RIGHT, fill=Y)
    Table_customer = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, height="3")
    Table_customer['columns'] = ("Name", "Phone", "ProductBuy", "DateBuy")
    Table_customer['show'] = 'headings'
    Table_customer.column("Name", anchor=CENTER, width=80)
    Table_customer.column("Phone", anchor=W, width=140)
    Table_customer.column("ProductBuy", anchor=CENTER, width=140)
    Table_customer.column("DateBuy", anchor=W, width=140)
    Table_customer.heading("Name", text="Name", anchor=CENTER)
    Table_customer.heading("Phone", text="Phone", anchor=CENTER)
    Table_customer.heading("ProductBuy", text="ProductBuy", anchor=CENTER)
    Table_customer.heading("DateBuy", text="DateBuy", anchor=CENTER)
    Table_customer.pack()
    tree_scroll.config(command=Table_customer.yview)
    tree_frame.place(x=20,y=80)


    def searchcustomer():
        mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="coffee management")
        mycursor = mysqldb.cursor()

        selected = drop.get()
        sql = ""
        if selected == "Search By ...":
            test = Label(search_customers, text="Please choose a selection !!")
            test.grid(row=3, column=0)
        if selected == "Name":
            sql = "Select * from customer where name = %s"

        if selected == "Phone":
            sql = f"Select * from customer where phone = %s"

        if selected == "ProductBuy":
            sql = "Select * from customer where product_buy = %s"

        if selected == "DateBuy":
            sql = "Select * from customer where date_buy = %s"

        searched = search_box.get()

        name = (searched,)


        result = mycursor.execute(sql, name)
        result = mycursor.fetchall()

        x = Table_customer.get_children()
        for item in x:
            Table_customer.delete(item)

        for i, (name, phone, ProductBuy, DateBuy) in enumerate(result, start=1):
            Table_customer.insert("", "end", values=(name, phone, ProductBuy, DateBuy))
        mysqldb.close()

        if searched == "":
            test2 = Label(search_customers, text="Please enter the value in search box !!")
            test2.grid(row=3, column=0)
        elif not result:
            Error8()


    # entrybox
    search_box = Entry(search_customers)
    search_box.grid(row=0, column=1, padx=10, pady=10)
    search_box_label = Label(search_customers, text="Search customer  ")
    search_box_label.grid(row=0, column=0, padx=10, pady=10)
    search_button = Button(search_customers, text="Search customer", command=searchcustomer)
    search_button.grid(row=0, column=4, padx=10)

    # dropmenuistaff
    drop = ttk.Combobox(search_customers, value=["Search By ...", "Name", "Phone", "ProductBuy","DateBuy"])
    drop.current(0)
    drop.grid(row=0, column=2)
##end search customer




##create window root
root = Tk()
root.title("Coffee Management")
root.geometry("1500x1000")



## background image
Load_img = Image.open('image\\w6.jpg')
bg = ImageTk.PhotoImage(Load_img)
img = Label(root, image = bg)
img.place(x=0,y=0,relwidth=1,relheight=1)


## styke treeview
style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview", background="#D3D3D3",foreground="black", rowheight="20", fieldbackground="#D3D3D3")
style.map('Treeview', background=[('selected', '#8B4513')])



## vertical scrollbar
## tree scroll product
tree_frame = Frame(root)
tree_frame.pack(pady=20)
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT,fill=Y)

## tree scroll staff
tree_framest = Frame(root)
tree_framest.pack(pady=20)
tree_scrollst = Scrollbar(tree_framest)
tree_scrollst.pack(side=RIGHT,fill=Y)

## tree scroll customer
tree_framecs = Frame(root)
tree_framecs.pack(pady=20)
tree_scrollcs = Scrollbar(tree_framecs)
tree_scrollcs.pack(side=RIGHT,fill=Y)




##declare variables product
global proid
global proname
global proprice
global procont



Label(root, text="Product name",bg="#FFFFCC").place(x=160, y=20)
Label(root, text="Product price",bg="#FFFFCC").place(x=160, y=71)
Label(root, text="Product content",bg="#FFFFCC").place(x=160, y=120)



proname = Entry(root)
proname.place(x=280, y=20)

proprice = Entry(root)
proprice.place(x=280, y=71)

procont = Entry(root)
procont.place(x=280, y=120)

Button(root, text="Add Product", command=Validate_ADD,bg="#7FFF00", height=4, width=14).place(x=20, y=200)
Button(root, text="Delete Product", command=DELETEPRODUCT,bg="#FF6347", height=4, width=14).place(x=140, y=200)
Button(root, text="Edit Product", command=Validate_EDIT,bg="#87CEFA", height=4, width=14).place(x=260, y=200)



## show table product
Table_product = ttk.Treeview(tree_frame,yscrollcommand=tree_scroll.set,height="6")
Table_product['columns'] = ("ID","Name","Price","Content")
Table_product['show'] = 'headings'

Table_product.column("ID", anchor=CENTER,width=80)
Table_product.column("Name",anchor=W,width=140)
Table_product.column("Price",anchor=CENTER,width=140)
Table_product.column("Content",anchor=W,width=140)

Table_product.heading("ID",text="ID",anchor=CENTER)
Table_product.heading("Name",text="Name",anchor=CENTER)
Table_product.heading("Price",text="Price",anchor=CENTER)
Table_product.heading("Content",text="Content",anchor=CENTER)
Table_product.pack()
tree_scroll.config(command=Table_product.yview)
tree_frame.place(x=20,y=300)



##declare variable staff
global stid
global stname
global stphone
global stadd


Label(root, text="Staff name",bg="#FFFFCC").place(x=620, y=20)
Label(root, text="Staff phone",bg="#FFFFCC").place(x=620, y=71)
Label(root, text="Staff address",bg="#FFFFCC").place(x=620, y=120)



stname = Entry(root)
stname.place(x=740, y=20)

stphone = Entry(root)
stphone.place(x=740, y=71)

stadd = Entry(root)
stadd.place(x=740, y=120)

Button(root, text="Add Staff", command=Validate_ADDST,bg="#7FFF00", height=4, width=14).place(x=520, y=200)
Button(root, text="Delete Staff", command=DELETESTAFF,bg="#FF6347", height=4, width=14).place(x=640, y=200)
Button(root, text="Edit Staff", command=Validate_EDITST,bg="#87CEFA", height=4, width=14).place(x=760, y=200)

## show table staff
Table_staff = ttk.Treeview(tree_framest,yscrollcommand=tree_scrollst.set,height="6")
Table_staff['columns'] = ("ID","Name","Phone","Address")
Table_staff['show'] = 'headings'
Table_staff.column("ID", anchor=CENTER,width=80)
Table_staff.column("Name",anchor=W,width=140)
Table_staff.column("Phone",anchor=CENTER,width=140)
Table_staff.column("Address",anchor=W,width=140)

Table_staff.heading("ID",text="ID",anchor=CENTER)
Table_staff.heading("Name",text="Name",anchor=CENTER)
Table_staff.heading("Phone",text="Phone",anchor=CENTER)
Table_staff.heading("Address",text="Address",anchor=CENTER)
Table_staff.pack()
tree_scrollst.config(command=Table_staff.yview)
tree_framest.place(x=20,y=460)



##declare variable customer
global csname
global csphone
global cspro
global csdate

Label(root, text="Customer name",bg="#FFFFCC").place(x=1100, y=10)
Label(root, text="Customer phone",bg="#FFFFCC").place(x=1100, y=45)
Label(root, text="Product buy",bg="#FFFFCC").place(x=1100, y=80)
Label(root, text="Date buy",bg="#FFFFCC").place(x=1100, y=120)

csname = Entry(root)
csname.place(x=1250, y=10)

csphone = Entry(root)
csphone.place(x=1250, y=45)

cspro = Entry(root)
cspro.place(x=1250, y=80)

csdate = Entry(root)
csdate.place(x=1250, y=120)

Button(root, text="Add Customer", command=Validate_ADDCS,bg="#7FFF00", height=4, width=14).place(x=1020, y=200)
Button(root, text="Delete Customer", command=DELETECS,bg="#FF6347", height=4, width=14).place(x=1140, y=200)
Button(root, text="Edit Customer", command=Validate_EDITCS,bg="#87CEFA", height=4, width=14).place(x=1260, y=200)



##show table customer
Table_customer = ttk.Treeview(tree_framecs,yscrollcommand=tree_scrollcs.set,height="6")
Table_customer['columns'] = ("Name","Phone","ProductBuy","DateBuy")
Table_customer['show'] = 'headings'
Table_customer.column("Name", anchor=W,width=80)
Table_customer.column("Phone",anchor=CENTER,width=140)
Table_customer.column("ProductBuy",anchor=W,width=140)
Table_customer.column("DateBuy",anchor=CENTER,width=140)

Table_customer.heading("Name",text="Name",anchor=CENTER)
Table_customer.heading("Phone",text="Phone",anchor=CENTER)
Table_customer.heading("ProductBuy",text="ProductBuy",anchor=CENTER)
Table_customer.heading("DateBuy",text="DateBuy",anchor=CENTER)
Table_customer.pack()
tree_scrollcs.config(command=Table_customer.yview)
tree_framecs.place(x=20,y=620)


##search button
seacrch_product_button = Button(root, text='Search Product', command=search_product,bg="white", height=4, width=14).place(x=380,y=200)
seacrch_staff_button = Button(root, text="Search Staff", command=search_staff,bg="white", height=4, width=14).place(x=880, y=200)
seacrch_customer_button = Button(root, text="Search Customer", command=search_customer,bg="white", height=4, width=14).place(x=1380, y=200)


#exit btn
exitButton = Button(root, text="Exit", command=root.destroy,bg="red", height=2, width=8).place(x=1420, y=10)
Ingbutton = Button(root, text="Ingredients", command=ingwindow,bg="#90EE90", height=3, width=9).place(x=1420, y=80)



TABLEPRODUCT()
Table_product.bind('<Double-Button-1>', TAKEVALUE)

TABLESTAFF()
Table_staff.bind('<Double-Button-1>', TAKEVALUE2)

TABLECUSTOMER()
Table_customer.bind('<Double-Button-1>', TAKEVALUE3)





root.mainloop()
