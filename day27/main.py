from tkinter import Button, Entry, Tk, Label

window = Tk()
window.title("Miles to Km")
window.minsize(width=500, height=300)
window.config(pady=20)

def convert():
    result = float(input.get())*1.6
    label3.config(text=f"Km: {round(result, 3)}")

label0 = Label()
label0.grid(column=0, row=0)

label1 = Label(text= "Convert miles to km", font=("Courier", 20, "bold"))
label1.grid(column=2, row=0)

input = Entry()
input.grid(column=2, row=1)

label2 = Label(text="Miles", font=("Courier", 15, "normal"))
label2.grid(column=3, row=1)

label3 = Label(text=f"Km: 0", font=("Courier", 15, "normal"))
label3.grid(column=3, row=3)

buttons1 = Button(text="Convert", command=convert)
buttons1.grid(column=2, row=4)



window.mainloop()
    