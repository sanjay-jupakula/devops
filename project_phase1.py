
from tkinter import *
from tkinter import messagebox
import os
    
def login():
    user=username.get()
    pas=password.get()
    if(user=="SUGSS" and pas=="123"):
        #calling scanning tab
        root.destroy()
        scan()
        
    elif user=="" or pas=="":
        messagebox.showinfo("Invalid","Username and Password can't be empty!")
    elif user!="SUGSS":
        messagebox.showinfo("Invalid","Please enter a valid username!")
    elif pas!="123":
        messagebox.showinfo("Username Error","Please enter the correct password!")
    else:
        messagebox.showinfo("Password Error","Please enter correct details!")
          
#Scanning tab
def scan():

    global tab
    
    tab=Tk()
    tab.title("Attendance")
    tab.geometry("500x500")
    tab.state('zoomed')

    sc1=Frame(tab,bg="#e1f0db",width=550,height=370,bd=5).place(relx=0.5,rely=0.45,anchor=CENTER)
       
#Main() funtion  
def main():
    
    global root
    global username
    global password
    
    root=Tk()
    root.title("Attendance Drive Ready+ (AWS DevOps)")
    root.geometry("500x500")
    root.configure(bg="#ffffff")
    root.state('zoomed')

    bc1=Frame(root,bg="#fad311",width=550,height=370).place(relx=0.5,rely=0.45,anchor=CENTER)
    bc2=Frame(root,bg="#72bd20",width=500,height=300).place(relx=0.5,rely=0.45,anchor=CENTER)

    ltitle=Label(text="Hello Trainer!!",height=0,font=("Gabriola",50,'bold'),bg="#72bd20").place(relx=0.5,rely=0.3,anchor=CENTER)
    bg=PhotoImage(file = "logo_header.png")
    img=Label(root,image=bg)
    img.place(x=0,y=0)

    Label(root,text="Username: ",font=("Sitka Small Semibold",15),bg="#72bd20").place(relx=0.45,rely=0.4,anchor=CENTER)
    Label(root,text="Password: ",font=("Sitka Small Semibold",15),bg="#72bd20").place(relx=0.45,rely=0.5,anchor=CENTER)

    username=StringVar()
    password=StringVar() 

    eun=Entry(root,textvariable=username,width=22,bd=2,font=("Californian FB",10)).place(relx=0.55,rely=0.4,anchor=CENTER)
    eps=Entry(root,textvariable=password,width=22,bd=2,font=("Californian FB",10)).place(relx=0.55,rely=0.5,anchor=CENTER)

    Button(root,text="Exit",height="1",width=10,bd=1,command=root.destroy).place(relx=0.45,rely=0.6,anchor=CENTER)
    Button(root,text="Login",height="1",width=10,bd=1,command=login).place(relx=0.55,rely=0.6,anchor=CENTER)           
    
    root.mainloop()

#main
main()

