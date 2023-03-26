from tkinter import *
#for sending dialogue message box
from tkinter import messagebox
import os
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
    
    cdf=pd.read_csv('clg_mail_data.csv')
    c1emailrow=cdf[cdf['clg_name']=='AEC']
    c1email=c1emailrow['clg_mail']
    sample=str(c1email)
    sample=sample[5:]
    s=""
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
    sample=sample[5:]
    s=""
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
    sample=sample[5:]
    s=""
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
    logintab()
    
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
def logintab():
    
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

    Button(root,text="Exit",height="1",width=10,bd=1,command=exitfun).place(relx=0.45,rely=0.6,anchor=CENTER)
    Button(root,text="Login",height="1",width=10,bd=1,command=login).place(relx=0.55,rely=0.6,anchor=CENTER)           
    
    root.mainloop()

############ main()


logintab()
