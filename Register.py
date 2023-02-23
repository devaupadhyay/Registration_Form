from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import re
import mysql.connector
import pyttsx3



class Register():
    def __init__(self,root):
        self.root=root
        self.root.title("Fields Voice Validation Registration Form in Python Using Tkinter")
        self.root.geometry("1600x790+0+0")
        
        #=================Text-To-Speech============
        
        self.engine=pyttsx3.init()
        self.voices=self.engine.getProperty("voices")
        self.engine.setProperty("voice",self.voices[1].id)
        
        #==============Variable===================
        self.name_var=StringVar()
        self.emailid_var=StringVar()
        self.contact_var=StringVar()
        self.gender_var=StringVar()
        self.country_var=StringVar()
        self.id_type_var=StringVar()
        self.id_no_var=StringVar()
        self.password_var=StringVar()
        self.confirm_password_var=StringVar()
        self.check_var=IntVar()
        
        #===========Back Ground Image===============
        
        self.bg=ImageTk.PhotoImage(file="sa.jpg")
        bg_lbl=Label(self.root,image=self.bg,bd=2,relief=RAISED)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)
        
        #===========Logo Image=======================
        
        logo_img=Image.open("icon.png")
        logo_img=logo_img.resize((60,60),Image.ANTIALIAS)
        self.photo_logo=ImageTk.PhotoImage(logo_img)
        
        #===========Title Frame======================
        
        title_frame=Frame(self.root,bd=1,relief=RIDGE)
        title_frame.place(x=450,y=28,width=550,height=82)
        
        #===========Title Lable========================
        
        title_lbl=Label(title_frame,image=self.photo_logo,compound=LEFT,text="USER REGISTER FORM",font=("times new roman",30,"bold"),fg="darkblue")
        title_lbl.place(x=10,y=10)
        
        #=============Information Frame=================
        
        main_frame=Frame(self.root,bd=1,relief=RIDGE)
        main_frame.place(x=450,y=110,width=550,height=620)
        
        #==============Username Label===============================
        
        user_name=Label(main_frame,text="Username :-",font=("times new roman",16,"bold"))
        user_name.grid(row=0,column=0,padx=10,pady=10,sticky=W)
        
        user_entry=ttk.Entry(main_frame,textvariable=self.name_var,font=("times new roman",15),width=25)    
        user_entry.grid(row=0,column=1,padx=10,pady=10,sticky=W)
        
        #==============CallBack and Validation=======================
        
        validate_name=self.root.register(self.checkname)
        user_entry.config(validate="key",validatecommand=(validate_name,"%P"))
        
        #==============Email Id Label===============================
        
        emailid_lbl=Label(main_frame,text="Email ID :-",font=("times new roman",16,"bold"))
        emailid_lbl.grid(row=1,column=0,padx=10,pady=10,sticky=W)
        
        txt_email=ttk.Entry(main_frame,textvariable=self.emailid_var,font=("times new roman",15),width=25)    
        txt_email.grid(row=1,column=1,padx=10,pady=10,sticky=W)
        
        #==============Contact Number Label===============================
        
        contactNo=Label(main_frame,text="Contact Number :-",font=("times new roman",16,"bold"))
        contactNo.grid(row=2,column=0,padx=10,pady=10,sticky=W)
        
        entry_contact=ttk.Entry(main_frame,textvariable=self.contact_var,font=("times new roman",15),width=25)    
        entry_contact.grid(row=2,column=1,padx=10,pady=10,sticky=W)
        
        #==============CallBack and Validation=======================
        
        validate_contact=self.root.register(self.checkcontact)
        entry_contact.config(validate="key",validatecommand=(validate_contact,"%P"))
        
        #==============Gender Lable===============================
        
        gender_lbl=Label(main_frame,text="Select Gender :-",font=("times new roman",16,"bold",))
        gender_lbl.grid(row=3,column=0,padx=10,pady=10,sticky=W)
        
        #==============Gender Frame===============================
        gender_frame=Frame(main_frame)
        gender_frame.place(x=200,y=160,width=280,height=35)
        
        radio_male=Radiobutton(gender_frame,variable=self.gender_var,value="Male",text="Male",font=("times new roman",15))
        radio_male.grid(row=0,column=0,padx=10,pady=0,sticky=W)
        self.gender_var.set("Male")
        
        radio_female=Radiobutton(gender_frame,variable=self.gender_var,value="Female",text="Female",font=("times new roman",15))
        radio_female.grid(row=0,column=1,padx=10,pady=0,sticky=W)
        
        #==============Country Label===============================
        
        select_country=Label(main_frame,text="Select Country :-",font=("times new roman",16,"bold"))
        select_country.grid(row=4,column=0,padx=10,pady=10,sticky=W)
        
        list=["India","UK","Austrila","Newziland","Afganistan","Pakistal","Bangladesh","Nepal"]
        droplist=OptionMenu(main_frame,self.country_var, *list)
        droplist.config(width=21,font=("times new roman",15),bg="white")
        self.country_var.set("Select Your Country")
        droplist.grid(row=4,column=1,padx=10,pady=10,sticky=W)
        
        #==============ID Type Label===============================
        
        id_type=Label(main_frame,text="Select ID Type :-",font=("times new roman",16,"bold",))
        id_type.grid(row=5,column=0,padx=10,pady=10,sticky=W)
        
        self.combo_id_type=ttk.Combobox(main_frame,textvariable=self.id_type_var,font=("times new roman",15),justify="center",state="readonly",width=23)
        self.combo_id_type["values"]=("Select Your ID","Adhar Card","Pan Card","Passport","Driving Licence")
        self.combo_id_type.grid(row=5,column=1,padx=10,pady=10)
        self.combo_id_type.current(0)
        
        #=============ID Number======================================
        
        id_no=Label(main_frame,text="ID Number :-",font=("times new roman",16,"bold"))
        id_no.grid(row=6,column=0,padx=10,pady=10,sticky=W)
        
        entry_id_no=ttk.Entry(main_frame,textvariable=self.id_no_var,font=("times new roman",15),width=25)
        entry_id_no.grid(row=6,column=1,padx=10,pady=10,sticky=W)
        
        #============Password=======================================
        
        s_password=Label(main_frame,text="Password :-",font=("times new roman",16,"bold"))
        s_password.grid(row=7,column=0,padx=10,pady=10,sticky=W)
        
        entry_pass=ttk.Entry(main_frame,textvariable=self.password_var,font=("times new roman",15),width=25)
        entry_pass.grid(row=7,column=1,padx=10,pady=10,sticky=W)
        
        #============Confirm Password=======================================
        
        c_password=Label(main_frame,text="Confirm Password :-",font=("times new roman",16,"bold"))
        c_password.grid(row=8,column=0,padx=10,pady=10,sticky=W)
        
        entry_confirm=ttk.Entry(main_frame,textvariable=self.confirm_password_var,font=("times new roman",15),width=25)
        entry_confirm.grid(row=8,column=1,padx=10,pady=10,sticky=W)
        
        #==============Check Frame===============================
        check_frame=Frame(main_frame)
        check_frame.place(x=130,y=460,width=400,height=70)
        
        check_btn=Checkbutton(check_frame,variable=self.check_var,text="Agree Our Terms & Condition",font=("times new roman",16),onvalue=1,offvalue=0)
        check_btn.grid(row=0,column=0,padx=10,sticky=W)
        
        self.check_lbl=Label(check_frame,text="",font=("arial",16),fg="red")
        self.check_lbl.grid(row=1,column=0,padx=10,sticky=W)
        
        #=======================Button Frame========================
        
        btn_frame=Frame(main_frame)
        btn_frame.place(x=30,y=530,width=480,height=70)
        
        save_data=Button(btn_frame,text="Save Data",command=self.validation,font=("times new roman",16,"bold"),width=12,cursor="hand2",bg="blue",fg="white")
        save_data.grid(row=0,column=0,padx=1,sticky=W)
        
        varify_data=Button(btn_frame,command=self.verify_data,text="Varify Data",font=("times new roman",16,"bold"),width=12,cursor="hand2",bg="blue",fg="white")
        varify_data.grid(row=0,column=1,padx=1,sticky=W)
        
        clear_data=Button(btn_frame,command=self.clear_data,text="Clear Data",font=("times new roman",16,"bold"),width=12,cursor="hand2",bg="blue",fg="white")
        clear_data.grid(row=0,column=2,padx=1,sticky=W)
        
    #===========Call Back Function================================
    #=========Check Name===========================
    
    def checkname(self,name):
        if name.isalnum():
            return True
        if name=="":
            return True
        else:
            self.engine.say("Not Allowed")
            self.engine.runAndWait()
            messagebox.showerror("Invaild","Not Allowed"+name[-1])
            return False
            
    #============Check Contact==============================
    
    def checkcontact(self,contact):
        if contact.isdigit():
            return True
        if len(str(contact))==0:
            return True
        else:
            self.engine.say("Invalid Entry")
            self.engine.runAndWait()
            messagebox.showerror("Invaild","Invalid Entry")
            return False
            
    #============Check Password==============================
    
    def checkpassword(self,password):
        if len(password)<=21:
            if re.match("^(?=.*[0-9])(?=.*[a-z](?=.*[^a-bA-B0-9]))",password):
              return True
            else:
                self.engine.say("Enter Valid Password (Exmale:Deva@123)")
                self.engine.runAndWait()
                messagebox.showinfo("Invaild","Enter Valid Password(Exmale:Deva@123)")
                return False
        else:
            messagebox.showerror("invalid","Lenght Try yo exceed")
            return False
            
            
    #============Check Email Id==============================
    
    def checkemailid(self,emailid):
        if len(emailid)>7:
            if re.match("^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$",emailid):
              return True
            else:
                self.engine.say("Enter Valid User Email ID(Exmale:deva@gmail.com)")
                self.engine.runAndWait()
                messagebox.showinfo("Invaild Email ID","Enter Valid User Email ID(Exmale:deva@gmail.com)")
                return False
        else:
            self.engine.say("Email ID Lenght is Too Small")
            self.engine.runAndWait()
            messagebox.showinfo("invalid","Email ID Lenght is Too Small")
            
            
    #================Validation===========================
    
    def validation(self):
        x=y=0
        if self.name_var.get()=="":
            self.engine.say("Please Enter Your Username")
            self.engine.runAndWait()
            messagebox.showerror("Error","Please Enter Your Username",parent=self.root)
            
        elif self.emailid_var.get()=="":
            self.engine.say("Please Enter Your Email Id")
            self.engine.runAndWait()
            messagebox.showerror("Error","Please Enter Your Email Id",parent=self.root)
            
        elif self.contact_var.get()=="" or len(self.contact_var.get())!=10:
            self.engine.say("Please Enter Your Valid Contact Number")
            self.engine.runAndWait()
            messagebox.showerror("Error","Please Enter Your Valid Contact Number",parent=self.root)
            
        elif self.gender_var.get()=="":
            self.engine.say("Please Select Your Gender")
            self.engine.runAndWait()
            messagebox.showerror("Error","Please Select Your Gender",parent=self.root)
            
        elif self.country_var.get()=="" or self.country_var.get()=="Select Your Country": 
            self.engine.say("Please Select Your Country Name")
            self.engine.runAndWait()
            messagebox.showerror("Error","Please Select Your Country Name",parent=self.root)
            
        elif self.id_type_var.get()=="Select Your ID Type":
            self.engine.say("Please Enter Your ID Type")
            self.engine.runAndWait()
            messagebox.showerror("Error","Please Enter Your ID Type",parent=self.root)
            
        elif self.id_no_var.get()=="":
            self.engine.say("Please Enter Your 14 Digit ID Number")
            self.engine.runAndWait()
            messagebox.showerror("Error","Please Enter Your 14 Digit ID Number",parent=self.root)
        
        elif len(self.id_no_var.get())!=14:
            self.engine.say("Please Enter Your 14 Digit ID Number")
            self.engine.runAndWait()
            messagebox.showerror("Error","Please Enter Your 14 Digit ID Number",parent=self.root)
           
        elif self.password_var.get()=="":
            self.engine.say("Please Enter Your Password")
            self.engine.runAndWait()
            messagebox.showerror("Error","Please Enter Your Password",parent=self.root)
            
        elif self.confirm_password_var.get()=="":
            self.engine.say("Please Enter Your Confirm Password")
            self.engine.runAndWait()
            messagebox.showerror("Error","Please Enter Your Confirm Password",parent=self.root)
            
        elif self.password_var.get()!=self.confirm_password_var.get():
            self.engine.say("Password & Confirm Password Must Be Same")
            self.engine.runAndWait()
            messagebox.showerror("Error","Password & Confirm Password Must Be Same",parent=self.root)
            
        elif self.emailid_var.get()!=None and self.confirm_password_var.get()!=None:
            x=self.checkemailid(self.emailid_var.get())
            y=self.checkpassword(self.password_var.get())
            
        if (x == True) and (y == True):
            if self.check_var.get()==0:
                self.engine.say("Please Agree Our Terms & Condition")
                self.engine.runAndWait()
                self.check_lbl.config(text="Please Agree Our Terms & Condition",fg="red")
            else:
                self.check_lbl.config(text="Checked",fg="green")
                
                
                try:
                    conn=mysql.connector.connect(host='localhost',username='root',password='Test@1234',database='mydata')
                    my_cursor=conn.cursor()
                    my_cursor.execute("insert into Register1 values(%s,%s,%s,%s,%s,%s,%s,%s)",(
                        
                                                                                              self.name_var.get(),
                                                                                              self.emailid_var.get(),
                                                                                              self.contact_var.get(),
                                                                                              self.gender_var.get(),
                                                                                              self.country_var.get(),
                                                                                              self.id_type_var.get(),
                                                                                              self.id_no_var.get(),
                                                                                              self.password_var.get(),
                                                                                               
                                                                                               ))
                    conn.commit()
                    conn.close()
                    self.engine.say("Your Regisration Successfully Completed")
                    self.engine.runAndWait()    
                    messagebox.showinfo("Successfully",f"Your Regisration Successfully Completed Your username:{self.name_var.get()} and password:{self.password_var.get()}")
                
                except Exception as es:
                    messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
                    
    def verify_data(self):
        data=f"Name : {self.name_var.get()}\nEmail ID : {self.emailid_var.get()}\nContact Number : {self.contact_var.get()}\nGender : {self.gender_var.get()}\nCountry : {self.country_var.get()}\nID Type : {self.id_type_var.get()}\nID Number : {self.id_no_var.get()}\nPassword : {self.password_var.get()}"
        messagebox.showinfo("Details",data)
        
    def clear_data(self):
        self.name_var.set(" ")
        self.emailid_var.set(" ")
        self.contact_var.set(" ")
        self.gender_var.set(" ")
        self.country_var.set(" ")
        self.id_type_var.set(" ")
        self.id_no_var.set(" ")
        self.password_var.set(" ")
        self.confirm_password_var.set(" ")
        self.check_var.set(" ")
            
if __name__=="__main__":
    root=Tk()
    object=Register(root)
    root.mainloop()