from tkinter import END, Button, Canvas, Label, PhotoImage, Tk, Entry, messagebox
from password_generator import generate
import json


#BACKEND

# Searching data
def search_data():
    with open("./day29/passwords.json", mode="r") as passw:
        data = json.load(passw)
        if web_ent.get() in data:
            messagebox.showinfo(title=web_ent.get(), message=f'Email: {data[web_ent.get()]["email"]}\n Password: {data[web_ent.get()]["Password"]}')
        else:
            messagebox.showwarning(title="Error", message="The website is not saved")    



# Saving inputs to a .txt file
def add_data():
    
    # Check if any field is empty or not
    if (len(web_ent.get()) == 0) or (len(em_user_ent.get()) == 0) or (len(password_ent.get()) == 0):
        messagebox.showwarning(message="Please don't leave any fields empty") 
    
    else:
        is_ok = messagebox.askokcancel(title="Confirmation Box", message=f"Please confirm the details.\nWebsite:{web_ent.get()} \nEmail/Username:{em_user_ent.get()} \nPassword:{password_ent.get()}")
        with open("./day29/passwords.json", mode="r") as passw:
            data = json.load(passw)
            if web_ent.get() in data:
                messagebox.showinfo(title=web_ent.get(), message=f'This Website has already been saved\nEmail: {data[web_ent.get()]["email"]}\n Password: {data[web_ent.get()]["Password"]}')
                is_ok = False           
        
        if is_ok:
            new_data = {
                    web_ent.get() : {
                        "email": em_user_ent.get(),
                        "Password" : password_ent.get()
                    }
                }   
            
            # Save the entries
            try:

                with open("./day29/passwords.json", mode="r") as passw:    
                    data = json.load(passw)
                    data.update(new_data)
                with open("./day29/passwords.json", mode="w") as passw:
        
                    json.dump(data, passw, indent=4)
                
            except:
                with open("./day29/passwords.json", mode="w") as passw:
                    json.dump(new_data, passw, indent=4)
            
            # Delete all the entries
            password_ent.delete(0, END)
            web_ent.delete(0, END)
            em_user_ent.delete(0, END)


# Generate random password
def generate_pwd():
    password_ent.insert(0, string=generate())


# GUI

# Setting up the canvas and window
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, height=400, width=400)

canvas = Canvas(width=200, height=200)
lock = PhotoImage(file="./day29/logo.png")
canvas.create_image(100, 100, image=lock)
canvas.grid(column=1, row=1)


# Setting up the labels and buttons
title_lab = Label(font=("Courier", 20, "bold"), text="Password Manager")
title_lab.grid(column=1, row=0)

webs_lab = Label(font=("Courier", 10, "normal"), text="Website:")
webs_lab.grid(column=0, row=2)

email_user = Label(font=("Courier", 10, "normal"), text="Email/Username:")
email_user.grid(column=0, row=3)

pwd_lab = Label(font=("Courier", 10, "normal"), text="Password:")
pwd_lab.grid(column=0, row=4)

search = Button(text="Search", command=search_data)
search.grid(column=2, row=2)

generate_pass = Button(text="Generate Password", command=generate_pwd)
generate_pass.grid(column=2, row=4)

add = Button(text="Add", width=35, command=add_data)
add.grid(column=1, row=5, columnspan=2)

password_ent = Entry(width=21)
password_ent.grid(column=1, row=4)

web_ent = Entry(width=21)
web_ent.grid(column=1, row=2)
web_ent.focus()

em_user_ent = Entry(width=35)
em_user_ent.grid(column=1, row=3, columnspan=2)


window.mainloop()
