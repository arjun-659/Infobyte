import random
import string as str
import tkinter as tk
from tkinter import messagebox
import pyperclip

# Define character sets
ascii = str.ascii_letters
digits = str.digits
symbols = str.punctuation

# Function to generate a password
def generate_password(length, use_letters=True, use_digits=True, use_symbols=True):
    # Initialize character set
    characters = ''
    if use_letters:
        characters += ascii
    if use_digits:
        characters += digits
    if use_symbols:
        characters += symbols
    
    # Check if character set is empty or length is less than 8
    if not characters or length < 8:
        return None
    
    # Generate password by random sampling and shuffling
    merge = random.sample(characters, length)
    random.shuffle(merge)
    return ''.join(merge)

# Function to copy the password to clipboard
def copy_to_clipboard(password):
    pyperclip.copy(password)
    messagebox.showinfo("Success", "Password copied to clipboard!")

# Create the main GUI window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x250")

# Define variables for user input
length_var = tk.StringVar(value="12")
use_letters = tk.BooleanVar(value=True)
use_digits = tk.BooleanVar(value=True)
use_symbols = tk.BooleanVar(value=True)
result_var = tk.StringVar()

# GUI Layout
tk.Label(root, text="Password Length:").pack()
tk.Entry(root, textvariable=length_var).pack()

tk.Checkbutton(root, text="Include Letters", variable=use_letters).pack()
tk.Checkbutton(root, text="Include Digits", variable=use_digits).pack()
tk.Checkbutton(root, text="Include Symbols", variable=use_symbols).pack()

# Function to handle GUI events
def password_generation():
    try:
        # Get the user input from GUI
        length = int(length_var.get())
    except ValueError:
        messagebox.showerror("Error", "Password length must be an integer.")
        return
    
    # Generate password
    password = generate_password(length, use_letters.get(), use_digits.get(), use_symbols.get())
    if password:
        result_var.set(password)
    else:
        result_var.set("Error in generating password.")

tk.Button(root, text="Generate Password", command=password_generation).pack()

tk.Label(root, text="Generated Password:").pack()
tk.Entry(root, textvariable=result_var, state="readonly").pack()

tk.Button(root, text="Copy to Clipboard", command=lambda: copy_to_clipboard(result_var.get())).pack()

# Run the Tkinter GUI event loop
root.mainloop()