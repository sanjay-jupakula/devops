from tkinter import *
#for sending dialogue message box
from tkinter import messagebox

import os
import sys 
import pandas as pd
#for mailing
import smtplib
from email.message import EmailMessage
import ssl
#for sending attachments
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

###################################################################################################

                                    #MAILING
    
####################################################################################################
    
#data segregation
def seggregation():
    global remail
    
    rdf=pd.read_csv('Original data.csv')
    remailrow=rdf[rdf['Roll_No']==rdata]
    remail=remailrow['Email']
    print(remail)
    
#data collegewise segration
def segdata():

    global sedata
    
    sedata=pd.read_csv('attendance.csv')
    c1=sedata[sedata['Roll_No'].str.contains('A9')]
    c1=c1['Roll_No']
    c2=sedata[sedata['Roll_No'].str.contains('P3')]
    c2=c2['Roll_No']
    c3=sedata[sedata['Roll_No'].str.contains('MH')]
    c3=c3['Roll_No']
    c1.to_csv('AEC.csv',index=False)
    c2.to_csv('ACET.csv',index=False)
    c3.to_csv('ACOE.csv',index=False)
    
#sending Email
def sendemail():
    e_sender='drplusdevops@gmail.com'
    seggregation()
    e_pass='gfyjnhyyodpqutvy'
    
    e_receiver=remail

    sub="Attendance report."
    body="Attendance captured for today."

    em=EmailMessage()
    em['From']=e_sender
    em['To']=e_receiver
    em['Subject']=sub
    em.set_content(body)

    context=ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smt:
        smt.login(e_sender,e_pass)
        smt.sendmail(e_sender,e_receiver,em.as_string())

#college mail Seggregation
def clgemail():
    global c1email
    segdata()
    
    cdf=pd.read_csv('clg_mail_data.csv')
    c1emailrow=cdf[cdf['clg_name']=='AEC']
    c1email=c1emailrow['clg_mail']
    sample=str(c1email)
    s=""
    flag=0
    startind=0
    for i in range(0,len(sample)):
        if(flag==0):
            if((sample[i]>='0' and sample[i]<='9') and (sample[i+1]!=' ')):
                startind=i
                flag=1
                
            elif((sample[i]>='a' and sample[i]<='z') and (sample[i+1]!=' ')):
                startind=i
                flag=1
                
            elif((sample[i]>='A' and sample[i]<='Z') and (sample[i+1]!=' ')):
                startind=i
                flag=1
        else:
            break
    sample=sample[i-1:]
    for i in sample:
        if(i=="\n" or i==' '):
            break
        s+=i
            
    print(s)
    sendemailclg(s,"AEC.csv")
    print("AEC",s)

    c2emailrow=cdf[cdf['clg_name']=='ACET']
    c2email=c2emailrow['clg_mail']
    sample=str(c2email)
    s=""
    flag=0
    startind=0
    for i in range(0,len(sample)):
        if(flag==0):
            if((sample[i]>='0' and sample[i]<='9') and (sample[i+1]!=' ')):
                startind=i
                flag=1
                
            elif((sample[i]>='a' and sample[i]<='z') and (sample[i+1]!=' ')):
                startind=i
                flag=1
                
            elif((sample[i]>='A' and sample[i]<='Z') and (sample[i+1]!=' ')):
                startind=i
                flag=1
        else:
            break
    sample=sample[i-1:]
    for i in sample:
        if(i=="\n" or i==' '):
            break
        s+=i
        
    print(s)
    sendemailclg(s,"ACET.csv")
    print("ACET",s)

    c3emailrow=cdf[cdf['clg_name']=='ACOE']
    c3email=c3emailrow['clg_mail']
    sample=str(c3email)
    s=""
    flag=0
    startind=0
    for i in range(0,len(sample)):
        if(flag==0):
            if((sample[i]>='0' and sample[i]<='9') and (sample[i+1]!=' ')):
                startind=i
                flag=1
                
            elif((sample[i]>='a' and sample[i]<='z') and (sample[i+1]!=' ')):
                startind=i
                flag=1
                
            elif((sample[i]>='A' and sample[i]<='Z') and (sample[i+1]!=' ')):
                startind=i
                flag=1
        else:
            break
    sample=sample[i-1:]
    for i in sample:
        if(i=="\n" or i==' '):
            break
        s+=i
        
    print(s)
    sendemailclg(s,"ACOE.csv")
    print("ACOE",s)

#sending mail to colleges
def sendemailclg(cmail,file):
    port=465
    smtp_server='smtp.gmail.com'
    
    e_sender='drplusdevops@gmail.com'
    e_pass='gfyjnhyyodpqutvy'
    e_receiver=cmail
          
    sub="Attendance report."
    body="Thub Attendance for today."

    aem=MIMEMultipart()
    aem['From']=e_sender
    aem['To']=e_receiver
    aem['Subject']=sub

    aem.attach(MIMEText(body,'plain'))

    filename=file

    attachment=open(filename,'rb')
    attachment_package=MIMEBase('application','octet-stream')
    attachment_package.set_payload((attachment).read())
    encoders.encode_base64(attachment_package)
    attachment_package.add_header('Content-Disposition',"attachment; filename= "+filename)
    aem.attach(attachment_package)

    context=ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smt:
        smt.login(e_sender,e_pass)
        smt.sendmail(e_sender,e_receiver,aem.as_string())

###################################################################################################

                                    #Mailing END
    
####################################################################################################
    
#***************************************************************************************************************************
#***************************************************************************************************************************
        
###################################################################################################

                                    #TRAINER
    
####################################################################################################
    
#scanning into csv file
df=pd.DataFrame(columns=['Roll_No'])
def writecsv():
    global df
    global rdata
    
    rdata=data.get()
    df=df.append({'Roll_No':rdata},ignore_index=True)
    df.index += 1
    #sending email
    sendemail()
    df.to_csv('attendance.csv')
   
#scan() funtion
def scan():
    ldata=data.get()
    lab1.configure(text=ldata+" done!")
    writecsv()
    reset()

#reset()
def reset():
    den.delete(0,END)

#tabdel
def td():
    tab.destroy()
    trainerlogintab()
    
#Scanning tab
def scantab():

    global tab
    global data
    global den
    global lab1
    
    tab=Tk()
    tab.title("Attendance")
    tab.geometry("500x500")
    tab.state('zoomed')

    
    
    sc1=Frame(tab,bg="#e1f0db",width=550,height=300,bd=5).place(relx=0.5,rely=0.4,anchor=CENTER)
    sltitle=Label(text="Drive Ready+(DevOps) Attendance",font=("Gabriola",30,'bold'),bg="#e1f0db",bd=2).place(relx=0.5,rely=0.3,anchor=CENTER)

    Label(tab,text="Scan your ID: ",font=("Sitka Small Semibold",15),bg="#72bd20").place(relx=0.5,rely=0.4,anchor=CENTER)
    
    data=StringVar()
    
    den=Entry(tab,textvariable=data,width=22,bd=2,font=("ariel FB",10))
    den.place(relx=0.5,rely=0.5,anchor=CENTER)

    lab1=Label(tab,font=("Comic Sans MS",12),bg="#e1f0db",fg="#0e6473")
    
    Button(tab,text="Done",font=("Sitka Small Semibold",5),height="2",width=15,bd=1,command=scan).place(relx=0.5,rely=0.6,anchor=CENTER)
    lab1.place(relx=0.5,rely=0.55,anchor=CENTER)

    Button(tab,text="Logout",font=("ariel",10),height=1,width=15,bd=1,command=td).place(relx=0.5,rely=0.75,anchor=CENTER)
    tab.mainloop()

def login():
    user=username.get()
    pas=password.get()
    if(user=="SUGSS" and pas=="123"):
        #calling scanning tab
        root.destroy()
        scantab()
        
    elif user=="" or pas=="":
        messagebox.showinfo("Invalid","Username and Password can't be empty!")
    elif user!="SUGSS":
        messagebox.showinfo("Invalid","Please enter a valid username!")
    elif pas!="123":
        messagebox.showinfo("Username Error","Please enter the correct password!")
    else:
        messagebox.showinfo("Password Error","Please enter correct details!")


#exit()
def exitfun():
    clgemail()
    root.destroy()
    

    
#logintab() funtion  
def trainerlogintab():
    
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

    ltitle=Label(text="Hello Trainer!!",height=0,font=("Gabriola",50,'bold'),bg="#72bd20").place(relx=0.5,rely=0.32,anchor=CENTER)

    bg=PhotoImage(file = "logo_header.png")
    img=Label(root,image=bg)
    img.place(x=0,y=0)

    Label(root,text="Username: ",font=("Sitka Small Semibold",15),bg="#72bd20").place(relx=0.45,rely=0.42,anchor=CENTER)
    Label(root,text="Password: ",font=("Sitka Small Semibold",15),bg="#72bd20").place(relx=0.45,rely=0.5,anchor=CENTER)

    username=StringVar()
    password=StringVar() 

    eun=Entry(root,textvariable=username,width=22,bd=2,font=("Californian FB",10)).place(relx=0.55,rely=0.42,anchor=CENTER)
    eps=Entry(root,textvariable=password,width=22,bd=2,font=("Californian FB",10)).place(relx=0.55,rely=0.5,anchor=CENTER)

    Button(root,text="Exit",height="1",width=10,bd=1,command=exitfun).place(relx=0.45,rely=0.6,anchor=CENTER)
    Button(root,text="Login",height="1",width=10,bd=1,command=login).place(relx=0.55,rely=0.6,anchor=CENTER)           
    
    root.mainloop()

###################################################################################################

                                    #TRAINER END
    
####################################################################################################

#***************************************************************************************************************************
#***************************************************************************************************************************

###################################################################################################

                                    #ADMIN
    
####################################################################################################
##########################################################  ///viewing User
#view Users for Admin
def view_users():
    global ad
    
    ad = Tk()
    ad.geometry('580x250')
    ad.state('zoomed')
    
    dframe=pd.read_csv("Admin_data.csv",index_col=[0])

    txt=Text(ad) 
    txt.pack() 

    class PrintToTXT(object): 
        def write(self, s): 
            txt.insert(END, s)

    sys.stdout = PrintToTXT() 
    print('Technical Hub Users and Passwords') 
    print(dframe)

    Button(ad,text="Return Admin Home",height="1",width=20,bd=1,command=call_adminv).place(relx=0.5,rely=0.7,anchor=CENTER)

    ad.mainloop()

#calling viewer
def call_viewers():
    admin.destroy()
    view_users()

#calling admin from view
def call_adminv():
    ad.destroy()
    Admin()
##########################################################  ///viewing User
    
##########################################################  ///adiing User

#calling add user
def call_adduser():
    admin.destroy()
    add_user()
    
#Add a user for admin
def add_user():

    global a_usertk
    global a_id
    global a_us
    global a_ps
    global aid
    global us
    global ps
    
    a_usertk=Tk()
    a_usertk.geometry("500x500")
    a_usertk.configure(bg="#ffffff")
    a_usertk.state('zoomed')
    
    bc1=Frame(a_usertk,bg="#fad311",width=550,height=370).place(relx=0.5,rely=0.45,anchor=CENTER)
    bc2=Frame(a_usertk,bg="#72bd20",width=500,height=300).place(relx=0.5,rely=0.45,anchor=CENTER)

    Label(text="Please enter new Username and Password",height=0,font=("Gabriola",20,'bold'),bg="#72bd20").place(relx=0.5,rely=0.3,anchor=CENTER)

    Label(a_usertk,text="ID: ",font=("Sitka Small Semibold",12),bg="#72bd20").place(relx=0.48,rely=0.35,anchor=CENTER)
    Label(a_usertk,text="Username: ",font=("Sitka Small Semibold",12),bg="#72bd20").place(relx=0.45,rely=0.4,anchor=CENTER)
    Label(a_usertk,text="Password: ",font=("Sitka Small Semibold",12),bg="#72bd20").place(relx=0.45,rely=0.45,anchor=CENTER)

    a_id=StringVar()
    a_us=StringVar()
    a_ps=StringVar()

    aid=Entry(a_usertk,textvariable=a_id,width=22,bd=2,font=("Californian FB",10))
    aid.place(relx=0.55,rely=0.35,anchor=CENTER)
    us=Entry(a_usertk,textvariable=a_us,width=22,bd=2,font=("Californian FB",10))
    us.place(relx=0.55,rely=0.4,anchor=CENTER)
    ps=Entry(a_usertk,textvariable=a_ps,width=22,bd=2,font=("Californian FB",10))
    ps.place(relx=0.55,rely=0.45,anchor=CENTER)
    
    Button(a_usertk,text="Done",height="1",width=10,bd=1,command=add_d).place(relx=0.5,rely=0.55,anchor=CENTER)
    Button(a_usertk,text="Return Admin Home",height="1",width=20,bd=1,command=close_aduser).place(relx=0.5,rely=0.7,anchor=CENTER)

    a_usertk.mainloop()
    
#closing add_user
def close_aduser():
    a_usertk.destroy()
    Admin()
    
#adding to Admin data
def add_d():
    global Ad_data

    did=a_id.get()
    d1=a_us.get()
    d2=a_ps.get()

    if(did=='' or d1=='' or d2==''):
        messagebox.showinfo("Invalid","password can't be empty!")

    else:
        
        df1=pd.read_csv('Admin_data.csv')
    
        df=pd.DataFrame(columns=['ID','username','password'])
        df=df.append({'ID':did,'username':d1,'password':d2},ignore_index=True)
        df.set_index("ID", inplace = True)
        d=df1.shape[0]

        Label(a_usertk,text=d1+" added",font=("Comic Sans Ms",12),bg="#72bd20").place(relx=0.5,rely=0.5,anchor=CENTER)

        df.to_csv('Admin_data.csv', mode='a', header=False)
    clear_aduser()

#clearig add_user
def clear_aduser():
    us.delete(0,END)
    ps.delete(0,END)
    aid.delete(0,END)
##########################################################  ///adiing User
    
##########################################################   ///DELETING
#calling deleting fun
def call_delete():
    admin.destroy()
    delete_user()
    
#deleting user data for admin
def delete_user():
    global delete_u
    global ind
    global ind_

    delete_u=Tk()
    delete_u.geometry("500x500")
    delete_u.configure(bg="#ffffff")
    delete_u.state('zoomed')

    bc1=Frame(delete_u,bg="#fad311",width=550,height=370).place(relx=0.5,rely=0.45,anchor=CENTER)
    bc2=Frame(delete_u,bg="#72bd20",width=500,height=300).place(relx=0.5,rely=0.45,anchor=CENTER)

    ind=StringVar()

    Label(delete_u,text="Please Enter ID No of Trainer Username:",font=("Sitka Small Semibold",15),bg="#72bd20").place(relx=0.5,rely=0.32,anchor=CENTER)
    
    ind_=Entry(delete_u,textvariable=ind,width=22,bd=2,font=("Californian FB",10))
    ind_.place(relx=0.5,rely=0.42,anchor=CENTER)

    Button(delete_u,text="Delete",height="1",width=10,bd=1,command=deleting).place(relx=0.5,rely=0.55,anchor=CENTER)

    Button(delete_u,text="Return to Admin page",height="1",width=20,bd=1,command=call_admind).place(relx=0.5,rely=0.7,anchor=CENTER)

    delete_u.mainloop()
    
#deleting user name
def deleting():
    x=ind.get()
    if x!='':
        
        x=int(x)
        df=pd.read_csv('Admin_data.csv')
        df.set_index("ID", inplace = True)
        df=df.drop([x])
        df.to_csv('Admin_data.csv')

        Label(delete_u,text="Username with ID: "+str(x)+" deleted",font=("Comic Sans Ms",10),bg="#72bd20").place(relx=0.5,rely=0.47,anchor=CENTER)
    else:
        messagebox.showinfo("Invalid","Input can't be empty!")
    ind_.delete(0,END)

#calling admin
def call_admind():
    delete_u.destroy()
    Admin()
########################################################## ///Deleting

########################################################## /// changing password
#changing password of admin
def call_changepass():
    admin.destroy()
    changepass()

#change password fun
def changepass():
    global cpass_a
    global c_pass1
    global c_pass2
    global a_cpass1
    global a_cpass2

    cpass_a=Tk()
    cpass_a.geometry("500x500")
    cpass_a.configure(bg="#ffffff")
    cpass_a.state('zoomed')
    
    bc1=Frame(cpass_a,bg="#fad311",width=550,height=370).place(relx=0.5,rely=0.45,anchor=CENTER)
    bc2=Frame(cpass_a,bg="#72bd20",width=500,height=300).place(relx=0.5,rely=0.45,anchor=CENTER)

    Label(cpass_a,text="Please enter new Password",height=0,font=("Gabriola",20,'bold'),bg="#72bd20").place(relx=0.5,rely=0.3,anchor=CENTER)

    Label(cpass_a,text="Password: ",font=("Sitka Small Semibold",12),bg="#72bd20").place(relx=0.46,rely=0.42,anchor=CENTER)
    Label(cpass_a,text="Re-enter Password: ",font=("Sitka Small Semibold",12),bg="#72bd20").place(relx=0.43,rely=0.5,anchor=CENTER)

    c_pass1=StringVar()
    c_pass2=StringVar()
    
    a_cpass1=Entry(cpass_a,textvariable=c_pass1,width=22,bd=2,font=("Californian FB",10))
    a_cpass1.place(relx=0.55,rely=0.42,anchor=CENTER)
    a_cpass2=Entry(cpass_a,textvariable=c_pass2,width=22,bd=2,font=("Californian FB",10))
    a_cpass2.place(relx=0.55,rely=0.5,anchor=CENTER)

    img=PhotoImage(file="logo_header.png")
    img_label=Label(cpass_a,image=img)
    img_label.grid(row=0,column=0)
    img_label.image=img

    Button(cpass_a,text="change",height="1",width=10,bd=1,command=call_change).place(relx=0.5,rely=0.6,anchor=CENTER)
    Button(cpass_a,text="Return Home screen",height="1",width=20,bd=1,command=call_adminc).place(relx=0.5,rely=0.7,anchor=CENTER)
    
#verifing and changing the passwords
def call_change():
    p1=c_pass1.get()
    p2=c_pass2.get()


    if p1=="" or p2=="":
        messagebox.showinfo("Invalid","passwordcan't be empty!")
        a_cpass1.delete(0,END)
        a_cpass2.delete(0,END)
        
    elif(p1 == p2):
        df=pd.read_csv('Admin_data.csv')
        df.set_index("ID", inplace=True)
        idx=df.index[df['username']=='ADMIN']
        df.loc[idx,'password']=p1
        df.to_csv('Admin_data.csv')
        
        lab1=Label(cpass_a,text="Password changed",font=("Comic Sans MS",12),bg="#72bd20",fg="#0e6473")
        lab1.place(relx=0.5,rely=0.55,anchor=CENTER)
        a_cpass1.delete(0,END)
        a_cpass2.delete(0,END)
        
    elif p1!=p2:
        messagebox.showinfo("Invalid","passwords didn't matched!")
        a_cpass1.delete(0,END)
        a_cpass2.delete(0,END)

#calling admin from change password
def call_adminc():
    cpass_a.destroy()
    Admin()    
########################################################## /// changing password
#admin login tab
def Adminlogintab():
    
    global adlogin
    global a_username
    global a_password
    
    adlogin=Tk()
    adlogin.title("Attendance Drive Ready+ (AWS DevOps)")
    adlogin.geometry("500x500")
    adlogin.configure(bg="#ffffff")
    adlogin.state('zoomed')

    bc1=Frame(adlogin,bg="#fad311",width=550,height=370).place(relx=0.5,rely=0.45,anchor=CENTER)
    bc2=Frame(adlogin,bg="#72bd20",width=500,height=300).place(relx=0.5,rely=0.45,anchor=CENTER)

    
    bg=PhotoImage(file = "logo_header.png",master=adlogin)
    img=Label(adlogin,image=bg)
    img.place(x=0,y=0)
    
    ltitle=Label(text="Hello ADMIN!!",height=0,font=("Gabriola",50,'bold'),bg="#72bd20").place(relx=0.5,rely=0.32,anchor=CENTER)

    Label(adlogin,text="Username: ",font=("Sitka Small Semibold",15),bg="#72bd20").place(relx=0.45,rely=0.42,anchor=CENTER)
    Label(adlogin,text="Password: ",font=("Sitka Small Semibold",15),bg="#72bd20").place(relx=0.45,rely=0.5,anchor=CENTER)

    a_username=StringVar()
    a_password=StringVar() 

    a_eun=Entry(adlogin,textvariable=a_username,width=22,bd=2,font=("Californian FB",10)).place(relx=0.55,rely=0.42,anchor=CENTER)
    a_eps=Entry(adlogin,textvariable=a_password,width=22,bd=2,font=("Californian FB",10)).place(relx=0.55,rely=0.5,anchor=CENTER)

    Button(adlogin,text="Exit",height="1",width=10,bd=1,command=call_adminh).place(relx=0.45,rely=0.6,anchor=CENTER)
    Button(adlogin,text="Login",height="1",width=10,bd=1,command=admin_login).place(relx=0.55,rely=0.6,anchor=CENTER)           
    
    adlogin.mainloop()

#calling home page from admin
def call_adminh():
    
    adlogin.destroy()
    homepage()
    
#Admin login access
def admin_login():
    user=a_username.get()
    pas=a_password.get()
    ap=pd.read_csv('Admin_data.csv')
    ap=ap[ap['username']=='ADMIN']
    ap=ap['password']
    sample=str(ap)
    s=""
    flag=0
    startind=0
    for i in range(0,len(sample)):
        if(flag==0):
            if((sample[i]>='0' and sample[i]<='9') and (sample[i+1]!=' ')):
                startind=i
                flag=1
                
            elif((sample[i]>='a' and sample[i]<='z') and (sample[i+1]!=' ')):
                startind=i
                flag=1
                
            elif((sample[i]>='A' and sample[i]<='Z') and (sample[i+1]!=' ')):
                startind=i
                flag=1
        else:
            break
    sample=sample[i-1:]
    for i in sample:
        if(i=="\n" or i==' '):
            break
        s+=i
    
    if(user=="ADMIN" and pas==s):
        adlogin.destroy()
        Admin()
        
    elif user=="" or pas=="":
        messagebox.showinfo("Invalid","Username and Password can't be empty!")
    elif user!="ADMIN":
        messagebox.showinfo("Invalid","Please enter a valid username!")
    elif pas!=s:
        messagebox.showinfo("Username Error","Please enter the correct password!")
    else:
        messagebox.showinfo("Password Error","Please enter correct details!")


#Admin Properties
def Admin():

    global admin
    
    admin=Tk()
    admin.title("Technical Attendance Portal")
    admin.geometry("500x500")
    admin.configure(bg="#ffffff")
    admin.state('zoomed')

    bc1=Frame(admin,bg="#fad311",width=550,height=370).place(relx=0.5,rely=0.45,anchor=CENTER)
    bc2=Frame(admin,bg="#72bd20",width=500,height=300).place(relx=0.5,rely=0.45,anchor=CENTER)

    ltitle=Label(text="Hello Admin!!",height=0,font=("Gabriola",50,'bold'),bg="#72bd20").place(relx=0.5,rely=0.32,anchor=CENTER)

    img = PhotoImage(file="logo_header.png",master=admin)
    label = Label(admin,image=img)
    label.place(x=0,y=0)
    
    Button(admin,text="Add User",height="1",width=15,bd=1,command=call_adduser).place(relx=0.5,rely=0.45,anchor=CENTER)
    Button(admin,text="View Users",height="1",width=15,bd=1,command=call_viewers).place(relx=0.5,rely=0.5,anchor=CENTER)
    Button(admin,text="Delete User",height="1",width=15,bd=1,command=call_delete).place(relx=0.5,rely=0.55,anchor=CENTER)
    Button(admin,text="Change Password",height="1",width=15,bd=1,command=call_changepass).place(relx=0.5,rely=0.6,anchor=CENTER)
    Button(admin,text="Return Home",height="1",width=15,bd=1,command=call_homea).place(relx=0.5,rely=0.7,anchor=CENTER)
    
    admin.mainloop()

#calling hom
def call_homea():
    admin.destroy()
    homepage()

####################################################################################################
    
                                    #ADMIN END

####################################################################################################
    
#################################    Calling ADMIN and Trainer   #####################################

#calling logintab from homepage()
def call_trainer():
    home.destroy()
    trainerlogintab()

#calling admin
def call_admin():
    home.destroy()
    Adminlogintab()

#################################    Calling ADMIN and Trainer   #####################################
#Homepage
def homepage():

    global home
    
    home=Tk()
    home.title("Technical Attendance Portal")
    home.geometry("500x500")
    home.configure(bg="#ffffff")
    home.state('zoomed')

    bc1=Frame(home,bg="#fad311",width=550,height=370).place(relx=0.5,rely=0.45,anchor=CENTER)
    bc2=Frame(home,bg="#72bd20",width=500,height=300).place(relx=0.5,rely=0.45,anchor=CENTER)

    ltitle=Label(text="Good Day!!",height=0,font=("Gabriola",50,'bold'),bg="#72bd20").place(relx=0.5,rely=0.35,anchor=CENTER)

    img = PhotoImage(file="logo_header.png",master=home)
    label = Label(home,image=img)
    label.place(x=0,y=0)

    Button(home,text="ADMIN",height="3",width=10,bd=1,command=call_admin).place(relx=0.45,rely=0.5,anchor=CENTER)
    Button(home,text="Trainer",height="3",width=10,bd=1,command=call_trainer).place(relx=0.55,rely=0.5,anchor=CENTER)           

    home.mainloop()
    
#############################   MAIN()  #############################################
homepage()

