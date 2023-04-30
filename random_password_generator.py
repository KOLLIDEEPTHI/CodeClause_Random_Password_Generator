import tkinter as tk
from tkinter import * 
import random

def calculate():
    generated_pwd=''
    Upper_Case = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    Lower_Case = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    special_chars = ['!','@','#','$','%','^','&','*','(',')','_']
    numbers = ['0','1','2','3','4','5','6','7','8','9']

    characters= Upper_Case+Lower_Case+special_chars+numbers
    password=""
    password+=(random.choice(Upper_Case)+random.choice(special_chars)+str(random.choice(numbers)))
    
 
    for i in range(password_len.get()-3):
        password+=random.choice(characters)
        
    generated_pwd=''.join(random.sample(password,len(password)))
    C.set(generated_pwd)


generator = tk.Tk()
generator.title("Password Generator")
generator.geometry("600x600")
Label(generator,text = "Random Password Generator",fg="blue",font=20).pack(pady=5)
addlength = Label(generator,text = "Select the Length of the password: ",font=40).pack(pady=7)
password_len =IntVar()
len_password = Spinbox(generator,from_=8,to_=32,textvariable = password_len,bg = "white",width = 20,font=40).pack()


C=StringVar()
submit = Button(generator,text = "Create the password",font=40,fg="purple",width = 20,command = calculate).pack(pady=10)
Label(generator,text = "The Generated Password is as follows:  ",font=40,).pack(pady=7)
Entry(generator, textvariable=C,width=20,font=60,fg="green").pack()
generator.mainloop()