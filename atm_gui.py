from tkinter import *
from tkinter import messagebox
import os
from datetime import datetime

# ---------------- FILE NAMES ----------------
BALANCE_FILE = "balance.txt"
PIN_FILE = "pin.txt"
TRANS_FILE = "transactions.txt"

# ---------------- LOAD / SAVE FUNCTIONS ----------------
def load_balance():
    if not os.path.exists(BALANCE_FILE):
        with open(BALANCE_FILE, "w") as f:
            f.write("1000")
        return 1000.0
    with open(BALANCE_FILE, "r") as f:
        data = f.read().strip()
        if data == "":
            with open(BALANCE_FILE, "w") as fw:
                fw.write("1000")
            return 1000.0
        return float(data)

def save_balance(amount):
    with open(BALANCE_FILE, "w") as f:
        f.write(str(amount))

def load_pin():
    if not os.path.exists(PIN_FILE):
        with open(PIN_FILE, "w") as f:
            f.write("1234")
        return "1234"
    with open(PIN_FILE, "r") as f:
        return f.read().strip()

def save_pin(new_pin):
    with open(PIN_FILE, "w") as f:
        f.write(new_pin)

def save_transaction(text):
    with open(TRANS_FILE, "a") as f:
        f.write(text + "\n")

# ---------------- INITIAL DATA ----------------
balance = load_balance()
current_pin = load_pin()

# ---------------- MAIN WINDOW ----------------
root = Tk()
root.title("ATM Machine System")
root.state("zoomed")
root.resizable(False, False)

# ---------------- LOGIN FRAME ----------------
def login():
    if pin_entry.get() == current_pin:
        login_frame.pack_forget()
        menu_frame.pack()
    else:
        messagebox.showerror("Error", "Invalid PIN")

login_frame = Frame(root)
login_frame.pack(pady=90)

Label(login_frame, text="ATM MACHINE", font=("Arial", 18, "bold")).pack(pady=10)
Label(login_frame, text="Enter PIN").pack()
pin_entry = Entry(login_frame, show="*")
pin_entry.pack(pady=5)

Button(login_frame, text="Login", width=18, command=login).pack(pady=10)

# ---------------- MENU FRAME ----------------
menu_frame = Frame(root)

def show_balance():
    messagebox.showinfo("Balance", f"Current Balance: Rs {balance}")

def deposit():
    global balance
    try:
        amt = float(amount_entry.get())
        if amt <= 0:
            raise ValueError
        balance += amt
        save_balance(balance)
        save_transaction(f"{datetime.now()} | Deposit | Rs {amt}")
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
        save_transaction(f"{datetime.now()} | Withdraw | Rs {amt}")
        messagebox.showinfo("Success", "Please collect cash")
        amount_entry.delete(0, END)
    except:
        messagebox.showerror("Error", "Invalid or insufficient balance")

def show_transactions():
    if not os.path.exists(TRANS_FILE):
        messagebox.showinfo("Transactions", "No transactions yet")
        return
    with open(TRANS_FILE, "r") as f:
        data = f.read()
    messagebox.showinfo("Transaction History", data if data else "No transactions")

def change_pin():
    def save_new_pin():
        global current_pin
        if new_pin.get().isdigit() and len(new_pin.get()) == 4:
            save_pin(new_pin.get())
            current_pin = new_pin.get()
            messagebox.showinfo("Success", "PIN changed successfully")
            pin_win.destroy()
        else:
            messagebox.showerror("Error", "PIN must be 4 digits")

    pin_win = Toplevel(root)
    pin_win.title("Change PIN")
    pin_win.geometry("250x150")

    Label(pin_win, text="Enter New PIN").pack(pady=10)
    new_pin = Entry(pin_win, show="*")
    new_pin.pack()

    Button(pin_win, text="Save PIN", command=save_new_pin).pack(pady=10)

def logout():
    menu_frame.pack_forget()
    login_frame.pack()

Label(menu_frame, text="Welcome to ATM", font=("Arial", 16, "bold")).pack(pady=10)

Button(menu_frame, text="Check Balance", width=25, command=show_balance).pack(pady=5)

Label(menu_frame, text="Enter Amount").pack()
amount_entry = Entry(menu_frame)
amount_entry.pack(pady=5)

Button(menu_frame, text="Deposit", width=25, command=deposit).pack(pady=4)
Button(menu_frame, text="Withdraw", width=25, command=withdraw).pack(pady=4)
Button(menu_frame, text="Transaction History", width=25, command=show_transactions).pack(pady=4)
Button(menu_frame, text="Change PIN", width=25, command=change_pin).pack(pady=4)
Button(menu_frame, text="Logout", width=25, command=logout).pack(pady=8)

# ---------------- RUN APP ----------------
root.mainloop()
