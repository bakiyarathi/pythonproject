from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from db import Database

db=Database("employee.db")
root=Tk()
root.title("Employee Management System")
root.geometry("1366x768+0+0")
root.config(bg="#2c3e50")
root.state("zoomed")

name=StringVar()
age=StringVar()
doj=StringVar()
gender=StringVar()
email=StringVar()
contact=StringVar()

#Entries Frame
entries_frame=Frame(root,bg="#535c68")
entries_frame.pack(side=TOP,fill=X)
title=Label(entries_frame,text="Employee Management System",font=("calibri",18,"bold"),bg="#535c68",fg="white")
title.grid(row=0,columnspan=2,padx=10,pady=20)

lblName=Label(entries_frame,text="Name",font=("Calibri",16),bg="#535c68",fg="white")
lblName.grid(row=1,column=0,padx=10,pady=10,sticky="w")
txtName=Entry(entries_frame,textvariable=name,font=("Calibri",16),width=30)
txtName.grid(row=1,column=1,padx=10,pady=10,sticky="w")

lblage=Label(entries_frame,text="Age",font=("calibri",16),bg="#535c68",fg="white")
lblage.grid(row=1,column=2,padx=10,pady=10,sticky="w")
txtage=Entry(entries_frame,textvariable=age,font=("Calibri",16),width=30)
txtage.grid(row=1,column=3,padx=10,pady=10,sticky="w")

lbldoj=Label(entries_frame,text="D.O.J",font=("Calibri",16),bg="#535c68",fg="white")
lbldoj.grid(row=2,column=0,padx=10,pady=10,sticky="w")
txtdoj=Entry(entries_frame,textvariable=doj,font=("Calibri",16),width=30)
txtdoj.grid(row=2,column=1,padx=10,pady=10,sticky="w")

lblemail=Label(entries_frame,text="Email",font=("Calibri",16),bg="#535c68",fg="white")
lblemail.grid(row=2,column=2,padx=10,pady=10,sticky="w")
txtemail=Entry(entries_frame,textvariable=email,font=("Calibri",16),width=30)
txtemail.grid(row=2,column=3,padx=10,pady=10,sticky="w")

lblgender=Label(entries_frame,text="Gender",font=("Calibri",16),bg="#535c68",fg="white")
lblgender.grid(row=3,column=0,padx=10,pady=10,sticky="w")
combogender=ttk.Combobox(entries_frame,font=("Calibri",16),width=28,textvariable=gender,state="readonly")
combogender['values']=("Male","Female")
combogender.grid(row=3,column=1,padx=10,sticky="w")

lblcontact=Label(entries_frame,text="Contact",font=("Calibri",16),bg="#535c68",fg="white")
lblcontact.grid(row=3,column=2,padx=10,pady=10,sticky="w")
txtcontact=Entry(entries_frame,textvariable=contact,font=("Calibri",16),width=30)
txtcontact.grid(row=3,column=3,padx=10,pady=10,sticky="w")

lbladdress=Label(entries_frame,text="Address",font=("Calibri",16),bg="#535c68",fg="white")
lbladdress.grid(row=4,column=0,padx=10,pady=10,sticky="w")
txtaddress=Text(entries_frame,width=85,height=5,font=("calibri",16))
txtaddress.grid(row=5,column=0,columnspan=4,padx=10,sticky="w")

btn_frame=Frame(entries_frame,bg="#535c68")
btn_frame.grid(row=6,column=0,columnspan=4,padx=10,pady=10,sticky="w")

def getData(event):
    selected_row=tv.focus()
    data=tv.item(selected_row)
    global row
    row=data["values"]
    name.set(row[1])
    age.set(row[2])
    doj.set(row[3])
    email.set(row[4])
    gender.set(row[5])
    contact.set(row[6])
    txtaddress.delete(1.0,END)
    txtaddress.insert(END, row[7])

def displayall():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("",END,values=row)

def add_employee():
    if txtName.get()=="" or txtage.get()=="" or txtdoj.get()=="" or txtemail.get()=="" or combogender.get()==""or txtcontact.get()=="" or txtaddress.get(1.0,END)=="":
        messagebox.showerror("Error: Please fill all details")
        return
    db.insert(txtName.get(),txtage.get() , txtdoj.get(), txtemail.get(), combogender.get(), txtcontact.get(), txtaddress.get(1.0,END)=="")
    messagebox.showinfo("Sucess","Record Inserted")
    clear()
    displayall()
'''
def update_employee():
    if txtName.get()=="" or txtage.get()=="" or txtdoj.get()=="" or txtemail.get()=="" or combogender.get()==""or txtcontact.get()=="" or txtaddress.get(1.0,END)=="":
        messagebox.showerror("Error: Please fill all details")
        return
    db.update(row[0], txtName.get(),txtage.get() , txtdoj.get(), txtemail.get(), combogender.get(), txtcontact.get(), txtaddress.get(1.0,END)=="")
    messagebox.showinfo("Sucess","Record updated")
    clear()
    displayall()'''

def update_employee():
    # Check if any field is empty
    if (txtName.get() == "" or txtage.get() == "" or txtdoj.get() == "" or
            txtemail.get() == "" or combogender.get() == "" or txtcontact.get() == "" or
            txtaddress.get(1.0, END).strip() == ""):
        messagebox.showerror("Error", "Please fill all details")
        return

    # Update the employee record
    db.update(row[0], txtName.get(), txtage.get(), txtdoj.get(), txtemail.get(),
              combogender.get(), txtcontact.get(), txtaddress.get(1.0, END).strip())

    # Show success message
    messagebox.showinfo("Success", "Record updated")

    # Clear the form and display all records
    clear()
    displayall()


def delete_employee():
    db.remove(row[0])
    clear()
    displayall()

def clear():
    name.set("")
    age.set("")
    doj.set("")
    gender.set("")
    email.set("")
    contact.set("")
    txtaddress.delete(1.0,END)


btnadd=Button(btn_frame,command=add_employee,text="Add Detail",width=15,font=("Calibri",16),bg="#2980b9",fg="white",bd=0).grid(row=0,column=0,padx=10)
btnedit=Button(btn_frame,command=update_employee,text="Update Detail",width=15,font=("Calibri",16),bg="#2980b9",fg="white",bd=0).grid(row=0,column=1,padx=10)
btndelete=Button(btn_frame,command=delete_employee,text="Delete Detail",width=15,font=("Calibri",16),bg="#2980b9",fg="white",bd=0).grid(row=0,column=2,padx=10)
btnclear=Button(btn_frame,command=clear,text="Clear Detail",width=15,font=("Calibri",16),bg="#2980b9",fg="white",bd=0).grid(row=0,column=3,padx=10)

tree_frame=Frame(root,bg="#ecf0f1")
tree_frame.place(x=0,y=455,width=1390,heigh=700)
style=ttk.Style()
style.configure("mystyle.Treeview",font=('Calibri',18),rowheight=50) #modify the font of body
style.configure("mystyle.Treeview.Heading",font=('Calibri',18),rowheight=50)
tv=ttk.Treeview(tree_frame,columns=(1,2,3,4,5,6,7,8),style="mystyle.Treeview")
tv.heading("1", text="Id")
tv.column("1",width=3)
tv.heading("2", text="Name")
tv.heading("3", text="Age")
tv.column("3",width=8)
tv.heading("4", text="D.O.J")
tv.column("4",width=10)
tv.heading("5", text="Email")
tv.heading("6", text="Gender")
tv.heading("7", text="Contact")
tv.heading("8", text="Address")
tv['show']='headings'
tv.bind("<ButtonRelease-1>",getData)
tv.pack(fill=X)


displayall()
root.mainloop()