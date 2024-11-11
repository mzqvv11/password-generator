import random
import tkinter as tk
from tkinter import ttk

def generate_password():
    password = ""
    characters = ""

    if lowercase_var.get():
        characters += "abcdefghijklmnopqrstuvwxyz"
    if numbers_var.get():
        characters += "0123456789"
    if uppercase_var.get():
        characters += "ABCDEFGHIJKLMOPQRSTUVWXYZ"
    if special_var.get():
        characters += "!@#$%"

    password_length = int(lenght_entry.get())
    for _ in range(password_length):
        password += random.choice(characters)

    password_label.config(text=password)

root = tk.Tk()
root.title("генератор паролей")

setiings_frame = tk.Frame(root)
setiings_frame.pack()

lowercase_var = tk.BooleanVar(value=True)
lowercase_checkbox = tk.Checkbutton(setiings_frame, text="добавить алфавит нижнего регистра", variable=lowercase_var)
lowercase_checkbox.pack()

numbers_var = tk.BooleanVar(value=True)
numbers_checkbox = tk.Checkbutton(setiings_frame, text="добавить цифры", variable=numbers_var)
numbers_checkbox.pack()

special_var = tk.BooleanVar(value=True)
special_checkdox = tk.Checkbutton(setiings_frame, text="добавть спецсимволы",variable=special_var)
special_checkdox.pack()

uppercase_var = tk.BooleanVar(value=True)
uppercase_checkbox = tk.Checkbutton(setiings_frame, text="добавить алфавит верхнего регистра", variable=uppercase_var)
uppercase_checkbox.pack()

lenght_label = tk.Label(setiings_frame, text="длина пароля:")
lenght_label.pack()
lenght_entry = tk.Entry(setiings_frame)
lenght_entry.insert(0, "12")
lenght_entry.pack()

generate_button = tk.Button(root, text="сгенерировать", command=generate_password)
generate_button.pack()

password_label = tk.Label(root, text="")
password_label.pack()

root.mainloop()
