from tkinter import *
from tkinter import messagebox
import os

files = {
    "1111": "nahyhan-user1.txt",   
    "2222": "kazim-user2.txt"
}

balance = 0
current_file = ""


def load(file):
    if not os.path.exists(file):
        open(file, "w").write("1000")
    return float(open(file).read())

def save(file, amt):
    open(file, "w").write(str(amt))

# gui
root = Tk()
root.title("ATM (2 Users)")
root.geometry("350x400")

Label(root, text="ATM MACHINE", font=("Arial", 16, "bold")).pack(pady=10)

# login k liye
def login():
    global balance, current_file
    pin = pin_entry.get()

    if pin in files:
        current_file = files[pin]
        balance = load(current_file)
        messagebox.showinfo("Login", "Login Successful")
    else:
        messagebox.showerror("Error", "Wrong PIN")

Label(root, text="Enter PIN").pack()
pin_entry = Entry(root, show="*")
pin_entry.pack()

Button(root, text="Login", command=login).pack(pady=10)

# functions
def show_balance():
    messagebox.showinfo("Balance", f"Rs {balance}")

def deposit():
    global balance
    amt = float(amount.get())
    balance += amt
    save(current_file, balance)
    messagebox.showinfo("Done", "Amount Deposited")

def withdraw():
    global balance
    amt = float(amount.get())
    if amt > balance:
        messagebox.showerror("Error", "Insufficient Balance")
    else:
        balance -= amt
        save(current_file, balance)
        messagebox.showinfo("Done", "Collect Cash")

# user sai input k liye
Label(root, text="Enter Amount").pack()
amount = Entry(root)
amount.pack()

# BUTTONS
Button(root, text="Check Balance", width=20, command=show_balance).pack(pady=5)
Button(root, text="Deposit", width=20, command=deposit).pack(pady=5)
Button(root, text="Withdraw", width=20, command=withdraw).pack(pady=5)

root.mainloop()
