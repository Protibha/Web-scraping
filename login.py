from tkinter import *
from PIL import ImageTk
class Login:
    def __init__(self,root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("780x510+100+50")
        self.root.resizable(False, False)
    
        #Background image
        self.bg=ImageTk.PhotoImage(file="image/College.jpg")
        self.bg_image=Label(self.root, image=self.bg).place(x=0,y=0, relwidth=1, relheight=1)
        
        # Login Frame
        Frame_login = Frame(self.root, bg="white")
        Frame_login.place(x=220, y=100, width=420, height=340)
        
        #Title & Subtitle
        title=Label(Frame_login, text="Login Here", font=("Impact", 30, "bold"), fg="#6162FF", bg="white").place(x=90, y=30)
        subtitle=Label(Frame_login, text="Members Login Area", font=("Goudy old style", 14, "bold"), fg="#1d1d1d", bg="white").place(x=90, y=85)
        
        #Username
        lbl_user=Label(Frame_login, text="Username", font=("Goudy old style", 14, "bold"), fg="grey", bg="white").place(x=90, y=120)
        self.username = Entry(Frame_login, font=("Goudy old style", 14), bg="#E7E6E6")
        self.username.place(x=90, y=145, width=200, height=35)
        
        #Password
        lbl_password=Label(Frame_login, text="Password", font=("Goudy old style", 14, "bold"), fg="grey", bg="white").place(x=90, y=180)
        self.password = Entry(Frame_login, font=("Goudy old style", 14), bg="#E7E6E6")
        self.password.place(x=90, y=205, width=200, height=35)
        
        #Button
        button =Button(Frame_login, text="forgot Password?", bd=0,font=("Goudy old style", 13), fg="grey", bg="white").place(x=90, y=240)
        submit =Button(Frame_login, text="Login?", font=("Goudy old style", 14), fg="white", bg="#6162FF").place(x=90, y=270, width=180, height=35)
        
        
root = Tk()
obj = Login(root)
root.mainloop()
        