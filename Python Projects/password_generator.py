import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

def generate_password():
    length = length_var.get()
    use_letters = letters_var.get()
    use_numbers = numbers_var.get()
    use_symbols = symbols_var.get()

    chars = ""
    if use_letters:
        chars += string.ascii_letters
    if use_numbers:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation

    if not chars:
        messagebox.showwarning("Error", "Please select at least one option!")
        return

    password = ''.join(random.choice(chars) for _ in range(length))
    password_var.set(password)

def copy_to_clipboard():
    pwd = password_var.get()
    if pwd:
        pyperclip.copy(pwd)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Error", "No password to copy!")

# Main window
root = tk.Tk()
root.title("🔐 Password Generator")
root.geometry("400x300")
root.config(bg="#1e1e2e")

# Variables
length_var = tk.IntVar(value=12)
letters_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)
password_var = tk.StringVar()

# UI Elements
tk.Label(root, text="Password Generator", font=("Arial", 16, "bold"), fg="white", bg="#1e1e2e").pack(pady=10)

frame = tk.Frame(root, bg="#1e1e2e")
frame.pack(pady=10)

tk.Label(frame, text="Length:", fg="white", bg="#1e1e2e").grid(row=0, column=0, sticky="w")
tk.Scale(frame, from_=6, to=32, orient="horizontal", variable=length_var, bg="#1e1e2e", fg="white").grid(row=0, column=1)

tk.Checkbutton(frame, text="Letters", variable=letters_var, fg="white", bg="#1e1e2e").grid(row=1, column=0, sticky="w")
tk.Checkbutton(frame, text="Numbers", variable=numbers_var, fg="white", bg="#1e1e2e").grid(row=2, column=0, sticky="w")
tk.Checkbutton(frame, text="Symbols", variable=symbols_var, fg="white", bg="#1e1e2e").grid(row=3, column=0, sticky="w")

tk.Entry(root, textvariable=password_var, font=("Arial", 14), width=25, justify="center").pack(pady=10)

btn_frame = tk.Frame(root, bg="#1e1e2e")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Generate", command=generate_password, bg="#4CAF50", fg="white", width=10).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Copy", command=copy_to_clipboard, bg="#2196F3", fg="white", width=10).grid(row=0, column=1, padx=5)

root.mainloop()
