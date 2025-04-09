
# create a user login usinf tkinter takes input userid and password and display it on the screen
# // no comment  simple form
from tkinter import *
from tkinter import messagebox


root = Tk()
root.geometry("500x500")
root.title("User Login")

# label
label = Label(root, text="User Login", font=("Arial", 20))
label.pack()

# userid
userid_label = Label(root, text="User ID:")
userid_label.pack()
userid_entry = Entry(root)
userid_entry.pack()

# password
password_label = Label(root, text="Password:")
password_label.pack()
password_entry = Entry(root)
password_entry.pack()

def login():
    print("User ID:", userid_entry.get())
    print("Password:", password_entry.get())
    messagebox.showinfo("Login Successful", "Login Successful")
    
login_button = Button(root, text="Login", command=login)
login_button.pack()

root.mainloop()
