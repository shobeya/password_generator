import tkinter as tk
import random
import string
import pyperclip

def generate_password():
    try:
        length = int(entry_length.get())  
        if length <= 0:
            password_var.set("Invalid length")
            return
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        password_var.set(password)
        check_strength(password)
    except ValueError:
        password_var.set("Enter a number")

def check_strength(password):
    length = len(password)
    if length < 6:
        strength_var.set("Weak 🔴")
    elif length < 10:
        strength_var.set("Medium 🟡")
    else:
        strength_var.set("Strong 🟢")

def copy_to_clipboard():
    pyperclip.copy(password_var.get())

# Create GUI
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")

tk.Label(root, text="Enter Password Length:", font=("Arial", 12)).pack(pady=5)
entry_length = tk.Entry(root)
entry_length.pack(pady=5)

password_var = tk.StringVar()
entry_password = tk.Entry(root, textvariable=password_var, font=("Arial", 14), width=24)
entry_password.pack(pady=5)

strength_var = tk.StringVar()
strength_label = tk.Label(root, textvariable=strength_var, font=("Arial", 12))
strength_label.pack(pady=5)

tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)
tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).pack(pady=5)

root.mainloop()
