from tkinter import* 
from PIL import Image, ImageTk
from tkinter import filedialog
import PIL
from help import *
from users import  EMOTIONS , get_age
import numpy as np
import database as db
import random
import cv2

import re
import os
import tkinter as tk
from tkinter import messagebox

# Create a dictionary to store user data (In a real application, you'd use a database)
user_data = {}
pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

my_list = [f"{ordinal}" for ordinal in ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]]
agee =0

def close_win(root):
   root.destroy()

def back(root):
    close_win(root)
    wellcome()

def wellcome():
    well=Tk()
    well.configure(bg='#D9D9D9')
    well.geometry('600x500')
    well.title("Wellcome")

    Button(well, text='login',width=20,bg='#FFFFFF',fg='black',borderwidth=0,command= lambda:Login(well)).place(x=230,y=210)  
    Button(well, text='Register',width=20,bg='#FFFFFF',fg='black',borderwidth=0,command= lambda:Register(well)).place(x=230,y=250) 
    well.mainloop()

def loginLogic(email,password,win):
    if email and password:
        if re.match(pattern,email):
            if (is_valid_email(email)):
                
                res= db.check_exist(email,password)
                if res is not None:
                    agee=res[-1]
                    main_function(win,agee)
                else :
                    Label(win, text="Password or Email is not correct",bg='#D9D9D9',borderwidth=0).place(x=200, y=270)
            else:
                messagebox.showerror("Error", "Invalid email format!")
        else:
            Label(win, text="Password or Email is not correct",bg='#D9D9D9',borderwidth=0).place(x=200, y=270)
    else:
         Label(win, text="Username and password are required fields",bg='#D9D9D9',borderwidth=0).place(x=200, y=270)

def Login(win):
    close_win(win)
    login=Tk()
    login.configure(bg='#D9D9D9')
    login.geometry('600x500')  
    login.title("Sign In")

    
    Label(login, text="Email", bg="#D9D9D9").place(x=200, y=190)
    email=Entry(login,borderwidth=0)
    email.place(x=280,y=190)


    Label(login, text="Password",borderwidth=0, bg="#D9D9D9").place(x=200, y=220)
    password=Entry(login,borderwidth=0,show="*")
    password.place(x=280,y=220)
    Button(login, text='Sign In',width=20,bg='#FFFFFF',fg='black',borderwidth=0,command=lambda:loginLogic(email.get(),password.get(),login)).place(x=230,y=250) 
    Button(login, text='Back to Home',width=20,bg='#D9D9D9',fg='black',borderwidth=0,command=lambda :back(login)).place(x=230,y=350) 
    login.mainloop()

def registerLogic(email,password,repass,age,win):
    
    if (password==repass) and password!="" and (password.count!=0):
        if re.match(pattern,email):
            if (is_valid_email(email)):
                agee=age
                db.add_elemet(email,password,int(age))
                main_function(win,age)
            else:
                messagebox.showerror("Error", "Invalid email format!")
        else:
            Label(win, text="Password or Email is not correct",bg='#D9D9D9',borderwidth=0).place(x=200, y=270)
    else:
         Label(win, text="Username and password are required fields",bg='#D9D9D9',borderwidth=0).place(x=200, y=270)

def cam(root,age):

    cp = cv2.VideoCapture(0)
    
    while True:
        ret, frame = cp.read()
        # while it is true it will save the values into temporary variable called camera
        cv2.imshow("Camera ", frame)
        k = cv2.waitKey(1)

        # if k % 256 == 27:
        #     break
        
        if k % 256 == 32:
            imagepath = 'images/opencv_frame.png'
            image = cv2.imwrite(imagepath, cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
            #image=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            image = cv2.resize(image, (256, 500))
            #frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            
            im = PIL.Image.open(imagepath)
            im = im.resize((300, 300))
            tkimage = ImageTk.PhotoImage(im)
            myvar=Label(root,image = tkimage)
            myvar. config(width=300, height=300)
            myvar.image = tkimage
            myvar.pack()
            
            

        if k & 0xFF==ord(' '):
            cv2.waitKey(1000)  # Wait for 1 second
            cv2.destroyAllWindows()
            break

    res= predict_image(imagepath)
    
    L=Label(root, text="The Emothon is  {}".format(res),bg='#D9D9D9',borderwidth=0)
    L.place(x=200, y=400)
    L.config(font=("Arial", 14))

    labels = []
    for i,x in enumerate(EMOTIONS[res][get_age(int(age))]):
        label = Label(root, bg='#D9D9D9',text="suggestions {} is {}".format(my_list[i],x),padx=5, pady=5)
        label.pack()
        labels.append(label)
        
def is_valid_email(email):
    # Basic regex pattern for email validation
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email)


def Register(win):
    close_win(win)
    register=Tk()
    register.configure(bg='#D9D9D9')
    register.geometry('600x500')  


    register.title("Sign Up")
    Label(register, text="Email", bg="#D9D9D9").place(x=200, y=190)
    email=Entry(register,borderwidth=0)
    email.place(x=280,y=190)
    
    Label(register, text="age", bg="#D9D9D9").place(x=200, y=215)
    ageE=Entry(register,borderwidth=0)
    ageE.place(x=280,y=215)


    Label(register, text="Password",borderwidth=0, bg="#D9D9D9").place(x=200, y=240)
    password=Entry(register,borderwidth=0,show="*")
    password.place(x=280,y=240)

    Label(register, text="Re Password",borderwidth=0, bg="#D9D9D9").place(x=200, y=265)
    repassword=Entry(register,borderwidth=0,show="*")
    repassword.place(x=280,y=265)

    Button(register, text='Sign Up',width=20,bg='#FFFFFF',fg='black',borderwidth=0,command= lambda:registerLogic(email.get(),password.get(),repassword.get(),ageE.get(),register)).place(x=230,y=290) 
    Button(register, text='Back to Home',width=20,bg='#D9D9D9',fg='black',borderwidth=0,command=lambda :back(register)).place(x=230,y=350) 

    register.mainloop()


from tkinter import Tk, Label, Button, filedialog, Canvas, Scrollbar, Frame
from PIL import Image, ImageTk

def main_function(win,age):
    close_win(win)
    path=''
    root = Tk()
    root.title('Face Emotions')

    root.geometry("640x530")
    root.configure(bg='#D9D9D9')

    frame = Frame(root, bg='#D9D9D9')
    frame.place(relx=0.5, rely=0.5, anchor='center')

    canvas = Canvas(frame, bg='#D9D9D9', width=640, height=530)
    canvas.pack(side='left', fill='both', expand=True)

    scrollbar = Scrollbar(frame, command=canvas.yview)
    scrollbar.pack(side='right', fill='y')

    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))

    #################################################################
    def select_image():
        nonlocal path
        for widget in canvas.winfo_children():
            widget.destroy()
        path = filedialog.askopenfilename(filetypes=[("Image File",'.*')])
        im = Image.open(path)
        im = im.resize((300, 300))
        tkimage = ImageTk.PhotoImage(im)
        myvar = Label(canvas, image=tkimage)
        myvar.config(width=300, height=300)
        myvar.image = tkimage
        canvas.create_window(150, 0, anchor='nw', window=myvar)
        res = predict_image(path)

        result_label = Label(canvas, text="The Emotion is  {}".format(res), bg='#D9D9D9', borderwidth=0)
        result_label.config(font=("Arial", 14))
        canvas.create_window(200, 410, anchor='nw', window=result_label)

        labels = []
        for i, x in enumerate(EMOTIONS[res][get_age(int(age))]):
            label = Label(canvas, bg='#D9D9D9', text="the {} Suggestion is {}".format(my_list[i], x), padx=5, pady=5)
            canvas.create_window(150, 300 + i * 20, anchor='nw', window=label)
            labels.append(label)

    b = Button(root, text="Predict", width=15, bg='#FFFFFF', fg='black', borderwidth=0, command=lambda: select_image())
    canvas.create_window(180, 490, anchor='nw', window=b)

    b2 = Button(root, text="Cam", width=15, bg='#FFFFFF', fg='black', borderwidth=0, command=lambda: cam(root,age))
    canvas.create_window(350, 490, anchor='nw', window=b2)

    b3 = Button(root, text="Log out", width=15, bg='#D9D9D9', fg='black', borderwidth=0, command=lambda: back(root))
    canvas.create_window(0, 0, anchor='nw', window=b3)

    root.mainloop()

wellcome()