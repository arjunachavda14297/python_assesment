from tkinter import *
from tkinter import messagebox
import mysql.connector

def connection():
    return mysql.connector.connect(host='localhost',user='root',passwd='',database='product')

bg1="lightgreen"
bg2="lightblue"
fg1="blue"
fg2="brown"
fg3="green"

font1=("cooper 15 bold ")
font2=('arial 20 bold underline')
font3=("cooper 15 bold")
font4=('arial 20 bold')
font5=("cooper 15")

ob=Tk()
ob.title('Product Data')
ob.geometry('525x500')
ob.resizable(False,False)
ob.configure(bg=bg2)


def insert_data():
    db=connection()
    cur=db.cursor()
    qry=" insert product(pname,prise) values(%s,%s) "
    argument=(e_pname.get(),e_prise.get())
    if e_pname.get()=="" or e_prise.get()=="":
        messagebox.showerror('Insert Status','Fill product name and product prise.')
    else:
        try:
            cur.execute(qry,argument)
            clear_data()
            db.commit()
            db.close()
            messagebox.showinfo('insert status','your record is inserted successfully.')
            e_pname.focus()
        except:
            db.rollback()

def update_data():
    db=connection()
    cur=db.cursor()
    qry=" update product set pname=%s, prise=%s where pid=%s "
    argument=(e_pname.get(),e_prise.get(),e_pid.get())
    if e_pid.get()=="":
        messagebox.showerror('Update status','Please insert Product id.')
    else:
        msg=messagebox.askyesno('Update status','Are you sure to Update record?')
        if msg==0:
            clear_data()
        else:
            try:
                cur.execute(qry,argument)
                clear_data()
                db.commit()
                db.close()
                messagebox.showinfo('update status','your record is updated successfully.')
                e_pname.focus()
            except:
                db.rollback()

def delete_data():
    db=connection()
    cur=db.cursor()
    qry=" delete from product where pid=%s "
    argument=(e_pid.get(),)
    if e_pid.get()=="":
        messagebox.showerror('Delete status','Please insert Product id.')
    else:
        msg=messagebox.askyesno('Delete status','Are you sure to delete record?')
        if msg==0:
            clear_data()
        else:
            try:
                cur.execute(qry,argument)
                clear_data()
                db.commit()
                db.close()
                messagebox.showinfo('Delete status','your record is deleted successfully.')
                e_pname.focus()
            except:
                db.rollback()

def select_data():
    db=connection()
    cur=db.cursor()
    qry=" select * from product where pid=%s "
    argument=(e_pid.get(),)
    if e_pid.get()=="":
        messagebox.showerror('Select status','Please insert Product id.')
    else:
        try:
            cur.execute(qry,argument)
            res=cur.fetchall()
            clear_data()
            e_pid.insert(0,res[0][0])
            e_pname.insert(0,res[0][1])
            e_prise.insert(0,res[0][2])
            db.close()
        except:
            return

def clear_data():
    e_pid.delete(0,END)
    e_pname.delete(0,END)
    e_prise.delete(0,END)
    e_pname.focus()


top=Label(ob,text='Product Detail',bg=bg2,font=font2,fg=fg1)
top.pack(pady=50)

l_pid=Label(ob,text='Product ID',bg=bg2,fg=fg2,font=font1)
l_pid.place(x=50,y=120)

l_pname=Label(ob,text='Product Name',bg=bg2,fg=fg2,font=font1)
l_pname.place(x=50,y=170)

l_prise=Label(ob,text='Product Prise',bg=bg2,fg=fg2,font=font1)
l_prise.place(x=50,y=220)

e_pid=Entry(ob,font=font5,width='25')
e_pid.place(x=200,y=120)

e_pname=Entry(ob,font=font5,width='25')
e_pname.focus()
e_pname.place(x=200,y=170)

e_prise=Entry(ob,font=font5,width='25')
e_prise.place(x=200,y=220)

insert=Button(ob,text='INSERT',width='7',font=font3,bg='gray',fg='yellow',activebackground='silver',activeforeground='red',command=insert_data)
insert.place(x=65,y=300)

update=Button(ob,text='UPDATE',width='7',font=font3,bg='gray',fg='yellow',activebackground='silver',activeforeground='red',command=update_data)
update.place(x=165,y=300)

delete=Button(ob,text='DELETE',width='7',font=font3,bg='gray',fg='yellow',activebackground='silver',activeforeground='red',command=delete_data)
delete.place(x=265,y=300)

select=Button(ob,text='SELECT',width='7',font=font3,bg='gray',fg='yellow',activebackground='silver',activeforeground='red',command=select_data)
select.place(x=365,y=300)

clear=Button(ob,text='CLEAR',width='7',font=font3,bg='gray',fg='yellow',activebackground='silver',activeforeground='red',command=clear_data)
clear.place(x=220,y=360)

header=Label(ob,text=('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^'),font=font4,fg=fg3,bg=bg2)
header.place(x=0,y=5)

footer=Label(ob,text=('* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *'),font=font2,fg=fg3,bg=bg2)
footer.place(x=0,y=440)

ob.mainloop()




















