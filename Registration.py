from tkinter import *
from tkinter.ttk import Combobox

root = Tk()
root.geometry("600x400")
root.configure(bg='grey')


def store():
    Data = [NameEntryWidget.get(), EmailEntryWidget.get(), ContactEntryWidget.get(), cb.get(),
            PasswordEntryWidget.get()]
    print(Data)


NameLabel = Label(root, text="Enter Name ", bg='grey')
NameLabel.grid(row=0, column=0, padx=10, pady=10, sticky=W)
NameEntryWidget = Entry(root, width=25, borderwidth=2)
NameEntryWidget.grid(row=0, column=1, padx=100, pady=10, columnspan=3)

EmailLabel = Label(root, text="Enter Email ", bg='grey')
EmailLabel.grid(row=2, column=0, padx=10, pady=10, sticky=W)
EmailEntryWidget = Entry(root, width=25, borderwidth=2)
EmailEntryWidget.grid(row=2, column=1, padx=100, pady=10, columnspan=3)

ContactLabel = Label(root, text="Contact Number ", bg='grey')
ContactLabel.grid(row=4, column=0, padx=10, pady=10, sticky=W)
ContactEntryWidget = Entry(root, width=25, borderwidth=2)
ContactEntryWidget.grid(row=4, column=1, padx=100, pady=10, columnspan=3)

GenderLabel = Label(root, text="Select Gender", bg='grey')
GenderLabel.grid(row=6, column=0, padx=10, pady=10, sticky=W)
v0 = IntVar()
v0.set(1)
r1 = Radiobutton(root, text="male", variable=v0, value=1)
r2 = Radiobutton(root, text="female", variable=v0, value=2)
r3 = Radiobutton(root, text="Others", variable=v0, value=3)
r1.place(x=235, y=155)
r2.place(x=290, y=155)
r3.place(x=355, y=155)

CountryLabel = Label(root, text="Select Country", bg='grey')
CountryLabel.grid(row=8, column=0, sticky=W, padx=10, pady=10)
var = StringVar()
var.set("India")
data = ("India", "USA", "Canada", "Russia")
cb = Combobox(root, values=data)
cb.grid(row=8, column=1, columnspan=3, padx=100, pady=10)

PasswordLabel = Label(root, text="Enter Password : ", font=("Times", 14), bg='grey', padx=10, pady=10)
PasswordLabel.grid(row=10, column=0, sticky=W, pady=10)
PasswordEntryWidget = Entry(root, font=("Times", 14), show="*")
PasswordEntryWidget.grid(row=10, column=1, sticky=W, padx=100, pady=10, columnspan=3)

RePasswordLabel = Label(root, text="Re-Enter Password : ", font=("Times", 14), bg='grey', padx=10, pady=10)
RePasswordLabel.grid(row=12, column=0, sticky=W, pady=10)
RePasswordEntryWidget = Entry(root, font=("Times", 14), show="*")
RePasswordEntryWidget.grid(row=12, column=1, sticky=W, padx=100, pady=10, columnspan=3)

submit = Button(root, font=("Times", 14), text="Submit", command=store, bg='grey').grid(row=14, column=1, sticky=W,
                                                                                        padx=100, pady=10)
root.mainloop()
