from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from sqlite3 import *
from datetime import datetime
win=Tk()
win.state('zoomed')
win.configure(bg='powder blue')
win.resizable(width=False,height=False)

lbl_title=Label(win,text="E-Commerce",font=('Algerian',60,'bold'),bg='powder blue')
lbl_title.pack()

def home_screen(pfrm=None):
    if(pfrm!=None):
        pfrm.destroy()
    frm=Frame(win)
    frm.configure(bg='pink')
    frm.place(x=0,y=140,relwidth=1,relheight=1)

    lbl_user=Label(frm,text="Username:",font=('',20,'bold'),bg='pink')
    entry_user=Entry(frm,font=('',20,'bold'),bd=10)

    lbl_user.place(relx=.3,rely=.1)
    entry_user.place(relx=.42,rely=.1)
    entry_user.focus()

    lbl_pass=Label(frm,text="Password:",font=('',20,'bold'),bg='pink')
    entry_pass=Entry(frm,font=('',20,'bold'),bd=10,show="*")

    lbl_pass.place(relx=.3,rely=.2)
    entry_pass.place(relx=.42,rely=.2)

    lbl_type=Label(frm,text="User Type:",font=('',20,'bold'),bg='pink')
    
    lbl_type.place(relx=.3,rely=.3)
    combo_type = ttk.Combobox(frm, 
                            values=[
                                    "---Select user---", 
                                    "Customer",
                                    "Admin",
                                    ],font=('',20,''))
    combo_type.current(0)
    combo_type.place(relx=.42,rely=.3)

    login_btn=Button(frm,command=lambda:welcome_screen(frm,entry_user,entry_pass,combo_type),width=10,text="login",font=('',20,'bold'),bg='powder blue',bd=10)
    login_btn.place(relx=.35,rely=.45)

    reset_btn=Button(frm,command=lambda:reset_home(entry_user,entry_pass,combo_type),width=10,text="reset",font=('',20,'bold'),bg='powder blue',bd=10)
    reset_btn.place(relx=.5,rely=.45)

    open_btn=Button(frm,width=14,command=lambda:open_screen(frm),text="open account",font=('',20,'bold'),bg='powder blue',bd=10)
    open_btn.place(relx=.3,rely=.58)

    fp_btn=Button(frm,width=14,command=lambda:fp_screen(frm),text="forgot password",font=('',20,'bold'),bg='powder blue',bd=10)
    fp_btn.place(relx=.5,rely=.58)

def logout(pfrm):
    option=messagebox.askyesno(title='logout', message="Do you really want to logout?")
    if(option==True):
        home_screen(pfrm)
    else:
        pass
def welcome_screen(pfrm,entry_user,entry_pass,combo_typ):
    user=entry_user.get()
    pwd=entry_pass.get()
    tp=combo_type.get()
    if(tp=="---Select user---"):
        messagebox.showwarning("warning","please select type")
        return
    elif(tp=="Customer"):
        con=connect("com.db")
        cur=con.cursor()
        cur.execute("select name,cart,type from useraccount where acn=? and pass=?",(user,pwd))
        tup=cur.fetchone()
        if(tup==None):
            messagebox.showerror("fail","Invalid username/password")
            return
        else:
            pfrm.destroy()
            frm=Frame(win)
            frm.configure(bg='pink')
            frm.place(x=0,y=140,relwidth=1,relheight=1)


            logout_btn=Button(frm,command=lambda:logout(frm),text="logout",font=('',20,'bold'),bg='powder blue',bd=10)
            logout_btn.place(relx=.9,rely=.001)

            left_frm=Frame(frm)
            left_frm.configure(bg='pink')
            left_frm.place(x=5,y=0,relwidth=.2,relheight=1)

            Label(left_frm,text=f"Welcome,{tup[0]}",font=('',15),bg='pink').place(x=2,y=2)
            check_btn=Button(left_frm,width=12,command=lambda:selectitem_frame(),text="select item",font=('',20,'bold'),bg='powder blue',bd=10)
            check_btn.place(relx=.001,rely=.1)

            deposit_btn=Button(left_frm,width=12,command=lambda:subcatogery_frame(),text="sub catogery",font=('',20,'bold'),bg='powder blue',bd=10)
            deposit_btn.place(relx=.001,rely=.25)

            withdraw_btn=Button(left_frm,width=12,command=lambda:addtocart_frame(),text="add to cart",font=('',20,'bold'),bg='powder blue',bd=10)
            withdraw_btn.place(relx=.001,rely=.4)

            transfer_btn=Button(left_frm,width=12,command=lambda:proceedtocheckout_frame(),text="proceed to checkout",font=('',20,'bold'),bg='powder blue',bd=10)
            transfer_btn.place(relx=.001,rely=.55)

            txnhist_btn=Button(left_frm,width=12,command=lambda:txnhistory_frame(),text="txn history",font=('',20,'bold'),bg='powder blue',bd=10)
            txnhist_btn.place(relx=.001,rely=.7)
    else:
        if(user=="admin" and pwd=="admin"):
            pfrm.destroy()
            frm=Frame(win)
            frm.configure(bg='pink')
            frm.place(x=0,y=140,relwidth=1,relheight=1)

            logout_btn=Button(frm,command=lambda:logout(frm),text="logout",font=('',20,'bold'),bg='powder blue',bd=10)
            logout_btn.place(relx=.9,rely=.001)

            Label(frm,text="Welcome,Admin",font=('',15),bg='pink').place(x=2,y=2)
            
            view_btn=Button(frm,width=18,command=lambda:AddCategories_frame(),text="Add Categories",font=('',20,'bold'),bg='powder blue',bd=10)
            view_btn.place(relx=.0,rely=.1)

            view_btn=Button(frm,width=18,command=lambda:AddProduct_frame(),text="Add Product",font=('',20,'bold'),bg='powder blue',bd=10)
            view_btn.place(relx=.10,rely=.2)

            view_btn=Button(frm,width=22,command=lambda:ProductDetailByUser_frame(),text="Product Detail By User",font=('',20,'bold'),bg='powder blue',bd=10)
            view_btn.place(relx=.15,rely=.3)

            view_btn=Button(frm,width=20,command=lambda:UserGeneratedBill_frame(),text="User Generated Bill",font=('',20,'bold'),bg='powder blue',bd=10)
            view_btn.place(relx=.20,rely=.4)
            
        else:
            messagebox.showerror("Invalid","Invalid username/password for admin")
            return

def welcome_user(pfrm,enter_user,enter_pass,combo_type):
    user=enter_user.get()
    pwd=enter_pass.get()
    tp=combo_type.get()
    if(tp=="---Select user---"):
        messagebox.showwarning("warning","please select type")
        return
    elif(tp=="admin"):
        con=connect("com.db")
        tup=cur.fetchone()
        if(tup==None):
            messagebox.showerror("fail","Invalid username/password")
            return
        else:
            pfrm.destroy()
            frm=Frame(win)
            frm.configure(bg='pink')
            frm.place(x=0,y=140,relwidth=1,relheight=1)


            logout_btn=Button(frm,command=lambda:logout(frm),text="logout",font=('',20,'bold'),bg='powder blue',bd=10)
            logout_btn.place(relx=.9,rely=.001)

            left_frm=Frame(frm)
            left_frm.configure(bg='pink')
            left_frm.place(x=5,y=0,relwidth=.2,relheight=1)

            Label(left_frm,text=f"Welcome,{tup[0]}",font=('',15),bg='pink').place(x=2,y=2)
            
            MultipleCatogeries_btn=Button(left_frm,width=12,command=lambda:MultipleCatogeries_frame(),text="Multiple Catogeries",font=('',20,'bold'),bg='powder blue',bd=10)
            MultipleCatogeries_btn.place(relx=.001,rely=.1)

            subcatogery_btn=Button(left_frm,width=12,command=lambda:subcatogery_frame(),text="sub catogery",font=('',20,'bold'),bg='powder blue',bd=10)
            subcatogery_btn.place(relx=.001,rely=.25)

            ProductDetails_btn=Button(left_frm,width=12,command=lambda:ProductDetails_frame(),text="Product Details",font=('',20,'bold'),bg='powder blue',bd=10)
            ProductDetails_btn.place(relx=.001,rely=.4)

            AddToCart_btn=Button(left_frm,width=12,command=lambda:AddToCart_frame(),text="Add To Cart",font=('',20,'bold'),bg='powder blue',bd=10)
            AddToCart_btn.place(relx=.001,rely=.55)

            BuyProduct_btn=Button(left_frm,width=12,command=lambda:BuyProduct_frame(),text="Buy Product",font=('',20,'bold'),bg='powder blue',bd=10)
            BuyProduct_btn.place(relx=.001,rely=.7)

            Removefromcart_btn=Button(left_frm,width=12,command=lambda:Removefromcart_frame(),text="Remove from cart",font=('',20,'bold'),bg='powder blue',bd=10)
            Removefromcart_btn.place(relx=.001,rely=.85)
        
        if(user=="customer" and pwd=="customer"):
            pfrm.destroy()
            frm=Frame(win)
            frm.configure(bg='pink')
            frm.place(x=0,y=140,relwidth=1,relheight=1)

            logout_btn=Button(frm,command=lambda:logout(frm),text="logout",font=('',20,'bold'),bg='powder blue',bd=10)
            logout_btn.place(relx=.9,rely=.001)

            Label(frm,text="Welcome,Customer",font=('',15),bg='pink').place(x=2,y=2)

            view_btn=Button(frm,width=15,command=lambda:MultipleCatogeries_frame(),text="Multiple Catogeries",font=('',20,'bold'),bg='powder blue',bd=10)
            view_btn.place(relx=.4,rely=.0)

            view_btn=Button(frm,width=15,command=lambda:SubCatogries_frame(),text="Sub Catogries",font=('',20,'bold'),bg='powder blue',bd=10)
            view_btn.place(relx=.8,rely=.1)

            view_btn=Button(frm,width=15,command=lambda:ProductDetails_frame(),text="Product Details",font=('',20,'bold'),bg='powder blue',bd=10)
            view_btn.place(relx=.16,rely=.2)

            view_btn=Button(frm,width=15,command=lambda:AddToCart_frame(),text="Add To Cart",font=('',20,'bold'),bg='powder blue',bd=10)
            view_btn.place(relx=.24,rely=.3)

            view_btn=Button(frm,width=15,command=lambda:BuyProduct_frame(),text="Buy Product",font=('',20,'bold'),bg='powder blue',bd=10)
            view_btn.place(relx=.28,rely=.4)

            view_btn=Button(frm,width=15,command=lambda:Removefromcart_frame(),text="Remove from cart",font=('',20,'bold'),bg='powder blue',bd=10)
            view_btn.place(relx=.32,rely=.5)

        else:
            messagebox.showerror("Invalid","Invalid username/password for customer")
            return


amt=int(input('enter the amount:'))
if(amt>=10000):
    amt=amt-500
else:
    print('No Discount')
print("final amount:",amt)
    

home_screen()
win.mainloop()


















    
