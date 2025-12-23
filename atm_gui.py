from tkinter import *
from tkinter import messagebox
import os

BALANCE_FILE = "balance.txt"

def load_balance():
    if not os.path.exists(BALANCE_FILE):
        with open(BALANCE_FILE, "w") as f:
            f.write("1000")
        return 1000

    with open(BALANCE_FILE, "r") as f:
        data = f.read().strip()
        if data == "":
            return 1000
        return float(data)

# Save Balance
def save_balance(amount):
    with open(BALANCE_FILE, "w") as f:
        f.write(str(amount))

balance = load_balance()

# GUI
root = Tk()
root.title("Simple ATM Machine")
root.geometry("400x350")
root.resizable(False, False)

Label(root, text="ATM MACHINE", font=("Arial", 18, "bold")).pack(pady=10)

# Now use Function
def check_balance():
    messagebox.showinfo("Balance", f"Your balance is Rs {balance}")

def deposit():
    global balance
    try:
        amt = float(amount_entry.get())
        if amt <= 0:
            raise ValueError
        balance += amt
        save_balance(balance)
        messagebox.showinfo("Success", "Amount Deposited")
        amount_entry.delete(0, END)
    except:
        messagebox.showerror("Error", "Enter valid amount")

def withdraw():
    global balance
    try:
        amt = float(amount_entry.get())
        if amt <= 0 or amt > balance:
            raise ValueError
        balance -= amt
        save_balance(balance)
        messagebox.showinfo("Success", "Please collect your cash")
        amount_entry.delete(0, END)
    except:
        messagebox.showerror("Error", "Invalid or insufficient balance")

# ye user sai input k liye
Label(root, text="Enter Amount").pack()
amount_entry = Entry(root)
amount_entry.pack(pady=5)

# button
Button(root, text="Check Balance", width=25, command=check_balance).pack(pady=5)
Button(root, text="Deposit", width=25, command=deposit).pack(pady=5)
Button(root, text="Withdraw", width=25, command=withdraw).pack(pady=5)
# run
root.mainloop()
